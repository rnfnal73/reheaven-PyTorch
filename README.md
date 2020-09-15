# reheaven-PyTorch

- 모델 배포: [깃허브](https://github.com/mario3316/reheaven-PyTorch)

- 모델 가중치 다운로드: [구글 드라이브](https://drive.google.com/drive/folders/1TmNXriWMGAGYrAnEWP7pHL0MmVtwW_eQ?usp=sharing)

- 실행 환경: **Google Colab**




## 1. 모델 실행 준비  

간편한 모델 실행과 가중치 로드를 위해 [**Google Colaboratory**](https://colab.research.google.com/notebooks/intro.ipynb)을 실행 환경으로 사용합니다.

모델 실행을 위해서 모델의 source code와 base model, weight 파일을 준비하고 Google Drive에 업로드 해야 합니다.

![download_model](https://user-images.githubusercontent.com/40377057/93164392-54c91800-f754-11ea-8b80-81b6d377d2d9.png)

[링크](https://github.com/mario3316/reheaven-PyTorch) 를 이용해 프로젝트 파일을 .zip형태로 내려받습니다

![model_weight](https://user-images.githubusercontent.com/40377057/93164367-4ed33700-f754-11ea-98dc-39fdb4b32904.png)

![unzip](https://user-images.githubusercontent.com/40377057/93164372-509cfa80-f754-11ea-8657-2544496dea09.png)

준비가 되면 [구글 드라이브 공유 링크](https://drive.google.com/drive/folders/1TmNXriWMGAGYrAnEWP7pHL0MmVtwW_eQ?usp=sharing)에서 베이스 모델인 **wordpiece_base** 폴더와 가중치 파일인 **pytorch_model.bin**을 내려받습니다


![weight_file](https://user-images.githubusercontent.com/40377057/93164373-509cfa80-f754-11ea-9b46-8f94c146d93b.png)

wordpiece_base 폴더와 pytorch_model.bin 파일을 압축 해제된 프로젝트 폴더 reheaven-PyTorch-master에 붙여넣습니다


![folder_upload](https://user-images.githubusercontent.com/40377057/93164401-5692db80-f754-11ea-99c2-3453150f6103.png)

![folder_upload2](https://user-images.githubusercontent.com/40377057/93164402-5692db80-f754-11ea-9980-19cd4d73ff09.png)

그 후 reheaven-PyTorch-master 폴더 전체를 구글 드라이브에 업로드 합니다


## 2. 구글 드라이브에서 .ipynb 실행하기
구글 드라이브에 업로드한 reheaven-PyTorch-master 내 reheaven.ipynb 파일은 jupyter notebook 파일로 Google Colab 환경에서 실행이 가능합니다
이를 통해 터미널 명령어와 파이썬 스크립트를 손쉽게 실행해볼 수 있습니다

![colab_install](https://user-images.githubusercontent.com/40377057/93164387-5397eb00-f754-11ea-9959-daee6d0d8191.png)

![colab_install_2](https://user-images.githubusercontent.com/40377057/93164389-54308180-f754-11ea-9f7c-69152d638284.png)

![colab_connect](https://user-images.githubusercontent.com/40377057/93164374-51359100-f754-11ea-91ec-4ab223e33fa2.png)


먼저 구글 드라이브에서 reheaven.ipynb 파일을 찾고 오른쪽 버튼을 클릭해 Google Colab을 설치,연결하는 작업을 진행합니다

이로써 모델 실행을 위한 준비가 끝났습니다

## 3. input file 준비하기
reheaven-PyTorch-master 내부에 test_input.txt 파일이 있습니다
![test_input](https://user-images.githubusercontent.com/40377057/93165905-3c5afc80-f758-11ea-86ca-1937fd77d757.png)
위와 같이 test_input.txt 파일을 작성(긍/부정을 평가하고 싶은 문장을 줄바꿈 문자를 기준으로 입력) 하면 모델을 통해test_output.txt를 test_input.txt와 같은 위치에 생성하게 됩니다


## 4. 모델 실행하기
input data와 실행 준비가 완료됐다면, 마지막으로 reheaven.ipynb를 실행하면 됩니다

![colab_connect](https://user-images.githubusercontent.com/40377057/93164374-51359100-f754-11ea-91ec-4ab223e33fa2.png)

위 이미지와 같이 reheavn.ipynb 파일을 Google Colab으로 열고 아래 그림을 따라 실행 절차를 진행합니다

![colab_execute](https://user-images.githubusercontent.com/40377057/93164375-51ce2780-f754-11ea-8e3a-1366802b7208.png)

![colab_execute2](https://user-images.githubusercontent.com/40377057/93164377-51ce2780-f754-11ea-9716-f0ea2fbd2427.png)
![colab_execute3](https://user-images.githubusercontent.com/40377057/93164380-5266be00-f754-11ea-8fe2-afe43a22f2cb.png)

![colab_execute4](https://user-images.githubusercontent.com/40377057/93164382-5266be00-f754-11ea-9180-a363f6716f2e.png)

![colab_execute5](https://user-images.githubusercontent.com/40377057/93166373-5517e200-f759-11ea-955b-977293a9469b.png)

![colab_execute6](https://user-images.githubusercontent.com/40377057/93164385-5397eb00-f754-11ea-9301-4b4d82b1f78f.png)

wordpiece_base 모델이 tensorflow로 작성된 모델이기 때문에 로딩 시간이 조금 걸릴 수 있습니다

아래와 같은 결과 화면(done)이 나온다면 test_output.txt의 작성이 완료된 것으로 결과를 확인하면 됩니다

![done](https://user-images.githubusercontent.com/40377057/93166186-e89ce300-f758-11ea-9d9d-448560a39cef.png)
