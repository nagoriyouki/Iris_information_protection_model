# <div align="center">👁️Iris_information_protection_model👁️</div>

<div align="center"> <strong>이미지에서 눈동자를 식별한 뒤 블러처리하는 프로그램</strong>
    
<div align="center">
    <div style="display: inline-block; text-align: center;">
        <div><br>⌨️Language⌨️</div>
        <br>
        <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />
        <br><br>
        <div>⚙️Tools⚙️</div>
        <br>
        <img src="https://img.shields.io/badge/github-181717?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/pycharm-000000?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/opencv-5C3EE8?style=flat&logo=python&logoColor=white" />
        <br><br>
        <div>📝Portfolio📝</div>
        <br>
        <img src="https://img.shields.io/badge/notion-000000?style=flat&logo=python&logoColor=white" />
    </div>
</div>

# 🧠사용 모델: Retinanet🧠

모델 출처: 

# ✂️학습 이미지 데이터 세트 다운로드 방법✂️

⬇️https://universe.roboflow.com/tosiken/eye_hand 접속 후 V8 다운로드


|class|Images|Instances|P|R|mAP50|
|:---:|:---:|:---:|:---:|:---:|:---:|
|all|1608|2156|0.726|0.796|0.793|
|bollard|1608|731|0.82|0.722|0.803|
|crosswalk|1608|752|0.68|0.856|0.826|
|greenlight|1608|349|0.723|0.83|0.801|
|redlight|1608|324|0.681|0.778|0.745|

# PR curve

<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/397839f0-58a4-47fd-9fef-26ac161f0d5c">
</p>

# P-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/94b55951-26c9-4267-96da-d198724e4de8">
</p>

# Result
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/d80c08fe-e788-4824-869c-b76f4060e158">
</p>

# 실행방법
[detect.py]
▶️pip install -r requirements.txt
▶️python detect.py --source 0 --weights /path/best.pt --data /path/seconddata.yaml


# 📊(.onnx) Prune 후 성능지표📊

mAP50: 0.789

|class|Images|Instances|P|R|mAP50|
|:---:|:---:|:---:|:---:|:---:|:---:|
|all|1608|2156|0.735|0.789|0.789|
|bollard|1608|731|0.857|0.679|0.782|
|crosswalk|1608|752|0.693|0.864|0.83|
|greenlight|1608|349|0.704|0.84|0.8|
|redlight|1608|324|0.687|0.773|0.742|

# PR curve

<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/a90d04b3-bbc9-4737-bdcd-6701e3112221">
</p>

# P-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/38575484-f9d6-4715-8de2-16d136a6032b">
</p>

# R-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/2f315e05-a687-44d4-9f6a-a974b0f1a409">
</p>

# 실행방법
<strong>[detect.py]</strong><br>
▶️ pip install -r requirements.txt<br>
▶️ python detect.py --source 0 --weights /path/best_cpu.onnx --data /path/seconddata.yaml

# 기타
⬇️<strong>데이터셋 다운로드</strong>: kaggle datasets download -d juhyehyeon/crosswalk-bollard-trafficlight<br>
💡<strong>기존 모델 출처</strong>: Jocher, G. (2020). YOLOv5 by Ultralytics (Version 7.0) [Computer software]. https://doi.org/10.5281/zenodo.3908559
</div>


