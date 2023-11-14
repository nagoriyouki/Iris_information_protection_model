# <div align="center">Iris_information_protection_model</div>
<div align="center"> <strong>눈동자를 검출한 뒤 원본을 거의 훼손하지 않고 블러 처리하는 프로그램</strong>
    
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
</div><br>

 <br/>
 
# 🧠사용 모델: Retinanet🧠

모델 출처: https://github.com/yhenon/pytorch-retinanet.git

 <br/>
 
# ✂️학습 이미지 데이터 세트 다운로드 방법✂️

⬇️https://universe.roboflow.com/tosiken/eye_hand 접속 후 V8 다운로드

 <br/>
 
# 👁️홍채 보안 (블러) 적용 예시👁️</div>

<strong>&nbsp;&nbsp;&nbsp;안경 안 낀 여자 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/94c84e12-36fb-41a1-b387-7f2638f44be9">
</p>

<strong>&nbsp;&nbsp;&nbsp;안경 안 낀 여자 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/a61d3fb8-03ee-41b8-ba5e-f0bf2d3aadc9">
</p>

<strong>&nbsp;&nbsp;&nbsp;어린 남자 아이 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/4f94999b-7e4b-45de-9c31-8495b34c94c6">
</p>

<strong>&nbsp;&nbsp;&nbsp;어린 남자 아이 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/151d6183-5175-4698-8c23-2ff3252bff0f">
</p>

<strong>&nbsp;&nbsp;&nbsp;안경 낀 남자 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/e3ca4231-50e4-4f38-9184-42cddba4f2ed">
</p>

<strong>&nbsp;&nbsp;&nbsp;안경 낀 남자 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/56d09011-298d-4e0b-a47c-814b7587de7c">
</p>
<div align="center">
    
 <br/>
    
# 실행방법
💻<strong>cpu 사용 모델</strong>💻<br>
▶️python irisblur.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로<br><br>
🚀<strong>gpu 사용 모델</strong>🚀<br>
▶️python irisblur_gpu.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로
</div>
