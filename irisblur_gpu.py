import csv
import torch
import numpy as np
import cv2
import argparse
from utils import SizeOfImage, HelpDetect, ImageBlur

class IrisSecurity:
    def __init__(self, model_path, class_list):
        with open(class_list, 'r') as f:
            self.classes = self.load_classes(csv.reader(f, delimiter=','))

        self.labels = {}
        for key, value in self.classes.items():
            self.labels[value] = key

        self.model = torch.load(model_path)

        if torch.cuda.is_available():
            self.model = self.model.cuda()

        self.model = self.model.module if isinstance(self.model, torch.nn.DataParallel) else self.model
        self.model.training = False
        self.model.eval()

    @staticmethod
    def load_classes(csv_reader):
        result = {}
        for line, row in enumerate(csv_reader):
            line += 1
            try:
                class_name, class_id = row
            except ValueError:
                raise ValueError('line {}: format should be \'class_name,class_id\''.format(line))
            class_id = int(class_id)
            if class_name in result:
                raise ValueError('line {}: duplicate class name: \'{}\''.format(line, class_name))
            result[class_name] = class_id
        return result

    def detect_objects(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Unable to read the image at '{image_path}'.")
            return

        image_orig = image.copy()
        rows, cols, cns = image.shape

        smallest_side = min(rows, cols)
        min_side = 608
        max_side = 1024
        scale = min_side / smallest_side

        largest_side = max(rows, cols)

        if largest_side * scale > max_side:
            scale = max_side / largest_side

        image = cv2.resize(image, (int(round(cols * scale)), int(round((rows * scale)))))
        rows, cols, cns = image.shape

        pad_w = 32 - rows % 32
        pad_h = 32 - cols % 32

        new_image = np.zeros((rows + pad_w, cols + pad_h, cns)).astype(np.float32)
        new_image[:rows, :cols, :] = image.astype(np.float32)
        image = new_image.astype(np.float32)
        image /= 255
        image -= [0.485, 0.456, 0.406]
        image /= [0.229, 0.224, 0.225]
        image = np.expand_dims(image, 0)
        image = np.transpose(image, (0, 3, 1, 2))

        with torch.no_grad():
            with torch.no_grad():
                if torch.cuda.is_available():
                    image = image.cuda()

                scores, classification, transformed_anchors = self.model(image)
            ids = torch.where(scores > 0.3)[0].numpy()

            image_result = image_orig.copy()
            image_orig_height, image_orig_width = SizeOfImage.image_size(image_result)

            for j in range(len(ids)):
                bbox = transformed_anchors[ids[j], :]
                x1 = int(bbox[0] / scale)
                y1 = int(bbox[1] / scale)
                x2 = int(bbox[2] / scale)
                y2 = int(bbox[3] / scale)
                label_name = self.labels[int(classification[ids[j]])]
                print(bbox, classification.shape)
                score = scores[ids[j]]
                caption = '{} {:.3f}'.format(label_name, score)

                bbox_top_left = (x1, y1)  # replace with actual values
                bbox_bottom_right = (x2, y2)  # replace with actual values

                # Crop the original image using bounding box coordinates
                cropped_img = image_orig[bbox_top_left[1]:bbox_bottom_right[1],
                              bbox_top_left[0]:bbox_bottom_right[0]]

                mask_img = HelpDetect.make_mask_image(cropped_img)

                contours, _ = cv2.findContours(mask_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                max_area, max_contour = HelpDetect.find_max_area(contours)

                if max_area != -1:
                    max_contour = max_contour.squeeze()
                    max_contour[:, 0] += x1
                    max_contour[:, 1] += y1

                    image_result = ImageBlur.apply_gaussian_blur_to_max_contour(image_result, max_contour, x1, y1)
                    height, width = SizeOfImage.image_size(image_result)

            cv2.namedWindow('img_org', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('img_org', image_orig_width, image_orig_height)
            cv2.imshow('img_org', image_orig)

            cv2.namedWindow('img_result', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('img_result', width, height)
            cv2.imshow('img_result', image_result)
            cv2.waitKey(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Object Detection Script')
    parser.add_argument('--image_path', required=True, help='Path to image file for object detection')
    parser.add_argument('--model_path', required=True, help='Path to model')
    parser.add_argument('--class_list', help='Path to CSV file listing class names (see README)')
    args = parser.parse_args()

    iris_security = IrisSecurity(args.model_path, args.class_list)
    iris_security.detect_objects(args.image_path)
