import cv2
import numpy as np

class SizeOfImage:
    @staticmethod
    def image_size(image):
        height, width, _ = image.shape
        return height, width

class HelpDetect:
    @staticmethod
    def make_mask_image(img_bgr):
        img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
        # 첫 번째 범위에 대한 마스크 생성
        low1 = (0, 50, 20)
        high1 = (20, 255, 80)
        img_mask1 = cv2.inRange(img_hsv, low1, high1)

        # 두 번째 범위에 대한 마스크 생성
        low2 = (0, 0, 0)
        high2 = (180, 100, 50)
        img_mask2 = cv2.inRange(img_hsv, low2, high2)

        # 두 마스크 이미지 합치기
        img_mask = cv2.bitwise_or(img_mask1, img_mask2)

        return img_mask  # 눈동자를 좀 더 잘 잡기 위함 ∵렌즈, 조명에 따라 조금씩 색이 다를 수도 있음

    @staticmethod
    def find_max_area(contours):
        max_contour = None
        max_area = -1

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > max_area:
                max_area = area
                max_contour = contour

        return max_area, max_contour

class ImageBlur:
    @staticmethod
    def apply_gaussian_blur_to_max_contour(image, max_contour, x, y):
        x, y, w, h = cv2.boundingRect(max_contour)
        roi = image[y:y + h, x:x + w]
        blurred_roi = cv2.GaussianBlur(roi, (5, 5), 2)
        image_copy = image.copy()
        image_copy[y:y + h, x:x + w] = blurred_roi
        return image_copy
