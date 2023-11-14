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
<strong>학습 데이터 세트</strong><br>
⬇️https://universe.roboflow.com/tosiken/eye_hand 접속 후 V8 다운로드<br>
<strong>모델 다운로드(.pt)</strong><br>
⬇️https://www.dropbox.com/scl/fo/1cb3qln03kydwfg2gmjxt/h?rlkey=ssv9cnupojwmv0rbx3uf1f15a&dl=0
 <br/>
 
# 👁️홍채 보안 (블러) 적용 예시👁️</div>

<strong>&nbsp;&nbsp;안경 안 낀 여자 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/76019605-a8d9-420d-b217-2fd44ac12553">
</p>

<strong>&nbsp;&nbsp;안경 안 낀 여자 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/cbd8fe7a-64eb-4f81-ad2b-3ab10e03857d">
</p>

<strong>&nbsp;&nbsp;어린 남자 아이 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/be9d819f-cf4c-4dec-bf66-595edb54ed86">
</p>

<strong>&nbsp;&nbsp;어린 남자 아이 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/04d67edf-8e66-4ff7-abd0-892f54901291">
</p>

<strong>&nbsp;&nbsp;안경 낀 남자 블러 처리 전</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/7dc2e193-c6d7-44d7-b0de-594504e7da43">
</p>

<strong>&nbsp;&nbsp;안경 낀 남자 블러 처리 후</strong>
<p align="center">
  <img src="https://github.com/nagoriyouki/Iris_information_protection_model/assets/130470442/8d4ef0f3-e6ba-428b-98aa-be1f15a463a9">
</p>
<div align="center">
    
 <br/>
    
# 실행방법
💻<strong>cpu 사용 모델</strong>💻<br>
▶️python irisblur.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로<br><br>
🚀<strong>gpu 사용 모델</strong>🚀<br>
▶️python irisblur_gpu.py --image_path 이미지 경로 --model_path 모델 경로 --class_list list.csv 파일 경로
</div>
