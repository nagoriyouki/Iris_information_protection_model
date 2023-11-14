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

# 홍채 보안 (블러) 적용 예시

<strong>안경 안 낀 여자 블러 처리 전</strong>
<p align="center">
  <img src="">
</p>

<strong>안경 안 낀 여자 블러 처리 후</strong>
<p align="center">
  <img src="">
</p>

<strong>어린 남자 아이 블러 처리 전</strong>
<p align="center">
  <img src="">
</p>

<strong>어린 남자 아이 블러 처리 후/strong>
<p align="center">
  <img src="">
</p>

<strong>안경 낀 남자 블러 처리 전</strong>
<p align="center">
  <img src="">
</p>

<strong>안경 낀 남자 블러 처리 후/strong>
<p align="center">
  <img src="">
</p>

# 실행방법
💻<strong>cpu 사용 모델</strong>💻<br>
irisblur.py
▶️python irisblur.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로<br>
🚀<strong>gpu 사용 모델</strong>🚀<br>
▶️python irisblur_gpu.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로
</div>
