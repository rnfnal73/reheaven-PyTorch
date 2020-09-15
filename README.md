# reheaven-PyTorch

- 모델 배포: [깃허브](https://github.com/mario3316/reheaven-PyTorch)

- 모델 가중치 다운로드: [구글 드라이브](https://drive.google.com/drive/folders/13DEquqxwQxWa_zEe78mmpCO9TK2JfYCP)

- 실행 환경: **Google Colab**




## 1. 모델 실행 준비  

간편한 모델 실행과 가중치 로드를 위해 [**Google Colaboratory**](https://colab.research.google.com/notebooks/intro.ipynb)을 실행 환경으로 사용합니다.

모델 실행을 위해서 모델의 source code와 base model, weight 파일을 준비하고 Google Drive에 업로드 해야 합니다.

![download_model](https://user-images.githubusercontent.com/40377057/93164392-54c91800-f754-11ea-8b80-81b6d377d2d9.png)
아래 링크를 이용해 프로젝트 파일을 .zip형태로 내려받습니다
[깃허브](https://github.com/mario3316/reheaven-PyTorch) 

준비가 되면 아래 구글 드라이브 공유 링크에서 베이스 모델인 **wordpiece_base** 폴더와 가중치 파일인 **pytorch_model.bin**을 내려받습니다
[구글 드라이브](https://drive.google.com/drive/folders/13DEquqxwQxWa_zEe78mmpCO9TK2JfYCP)


### **Commit**
파일 및 폴더의 추가/변경 사항을 저장소에 기록하려면 '커밋'이란 버튼을 눌러줘야 합니다.

커밋 버튼을 누르면 이전 커밋 상태부터 현재 상태까지의 변경 이력이 기록된 커밋(혹은 리비전)이 만들어집니다.

커밋은 이렇게 이력을 남기는 중요한 작업이기 때문에 커밋 버튼을 누를땐 커밋 메시지를 필수로 입력해야 합니다. 
메시지가 없으면 커밋이 실행되지 않습니다.

### **Push**
내 PC의 로컬 저장소에서 변경된 이력을 원격 저장소에 공유하려면, 로컬 저장소의 변경 이력을 원격 저장소에 업로드해야 합니다.

웹 상의 원격 저장소로 변경된 파일을 업로드하는 것을 Git에서는 푸시(Push)라고 합니다.
 push 를 실행하면, 원격 저장소에 내 변경 이력이 업로드되어, 원격 저장소와 로컬 저장소가 동일한 상태가 됩니다.

[출처](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)  


##  2. **Local** git 설치하기(window 10 기준)  

[git install](https://git-scm.com/downloads)  
위 링크를 클릭해 자신의 OS에 맞는 버전을 설치해줍니다. 여기서는 window 10을 기준으로 진행하겠습니다.

설치 중 나오는 설정은 기본적으로 체크된 대로 진행하시면 됩니다.

![gitbashopen](./readme_image/gitbashopen.png)  
설치가 완료되면 바탕화면의 아무곳에나 대고 오른쪽 버튼을 클릭해 git bash를 열어줍니다.

![gitconfig](./readme_image/gitconfig.JPG)  
위와 같은 명령어를 통해 local git과 연동할 github의 이메일과 username을 등록해줍니다.  



##  3. **Gitbhub** 저장소에 대해 **Collaborator** 권한 얻기  

다음으로 원본 repository에 대한 commit과 push 권한을 얻기위해 원본 repository의 collaborator가 되는 과정입니다.

해당 권한이 없으면 원본 코드에 수정사항을 반영하기 위해 commit과 push를 진행하고, repository의 소유자에게 pull request를 요청해 승인을 받아야 해당 코드가 반영되게 됩니다.

이번 프로젝트에서는 이 과정을 생략하기 위해 collaborator 권한을 얻어 코드 수정자가 직접 원본 코드에 push하도록 하겠습니다.

Github repository 소유자에게 collaborator invitation을 요청합니다. 소유자가 invitation을 보내면, github에 등록된 이메일로 invitation 메일이 오게됩니다.

![invitation](./readme_image/invitation.JPG)
![accept_invitation](./readme_image/accept_invitation.JPG)  

이메일에서 accept invitation을 누르고 다음 과정을 거치게 되면 해당 repository의 collaborator로서 등록이 되게됩니다.  

##  4. **Remote repository** (github 저장소)에서 **Local git**으로 **repository**를 clone 해오기  

이전 과정에서 repository의 동료 권한을 얻게되면 나의 local desktop 환경으로 repository 프로젝트를 복사해서 가져올 수 있게됩니다. 

![gitbashopen](./readme_image/gitbashopen.png)  
여기서는 바탕화면에 git_test라는 폴더에 local git 저장소를 만들어 저장해보겠습니다.  

![cloning_repo](./readme_image/cloning_repo.JPG)  
git clone <클론하려는 저장소 주소> <복사하려는경로>  
위와 같은 명령어를 통해 바탕화면(Desktop) 경로에 git_test 폴더를 생성함과 동시에 local git 저장소로 만들었습니다.

![cloned_folder](./readme_image/cloned_folder.JPG)  
위와 같이 .git 폴더와 github repository 프로젝트 파일들이 생성되었다면 성공적으로 clone된 것입니다.  

##  5. **Intellij**에서 프로젝트 수정사항 **commit**, **push**하기  

![open_project](./readme_image/open_project.JPG)  
먼저 intellij에서 생성한 clone해온 프로젝트를 열어 줍니다.

![imported_project](./readme_image/imported_project.JPG)  

위 프로젝트에서 src/main 과 src/test에 각각 소스코드와 그 소스코드를 테스트할 테스트코드를 하면됩니다.

![intellij_git](./readme_image/intellij_git.JPG)  

intellij에서 작성한 코드 수정사항을 반영하기 위해서는 intellij에 git.exe 파일의 위치를 인식 시켜줘야 합니다.  
intellij 상단 메뉴에서 File - settings - version control - git에 들어가면 자동으로 git.exe의 위치를 찾아줍니다.  
여기서 test 버튼을 클릭해 git version이 제대로 뜨는지 확인해줍니다.

![intellij_github](./readme_image/intellij_github.JPG)  

같은 위치에서 version control - github에서 우측 상단 +를 클릭해 자신의 github account를 입력해줍니다.  
login에는 이메일 주소 or username을 입력하고 비밀번호를 입력해준 뒤 로그인 해줍니다.

프로젝트에 수정사항(코드수정 등)이 발생했을때 이를 commit 하게되면 이것이 바로 github의 repository(remote repository)에 반영되는 것이 아닙니다.

이는 local repository에 반영되고 이를 remote repo에 push 해줘야 원본 코드에 반영됩니다.

![commit](./readme_image/commit.JPG)  
위 그림에서 초록색 v표시를 누릅니다.

![commit2](./readme_image/commit2.JPG)  
수정사항이 생긴 프로젝트 파일이 목록에 나타나게 되고 commit하고 싶은 파일을 선택해줍니다.  
commit에 대한 설명을 commit message에 남겨주고, commit 버튼을 눌러줍니다.

![commit3](./readme_image/commit3.JPG)  
commit을 확인하는 창이 나타나는데 error 없다면 commit을 진행합니다.

![commit4](./readme_image/commit4.JPG) 
위와 같은 창이 나타나면 local repo에 commit이 완료된것입니다.

이제 remote repo에 반영하기 위해 push를 진행해보겠습니다.

![push](./readme_image/push.png)  
상단 메뉴에서 VCS - Git - push를 차례로 선택합니다.  
push할 저장소를 추가하기 위해 Define remote를 선택합니다.

![push2](./readme_image/push2.JPG)  
Name에 remote repository의 이름, url에 그 주소를 입력합니다.

![push3](./readme_image/push3.JPG)  
저장소가 추가되면 다시 한번 origin을 눌러 해당 저장소로 바꿔줍니다.  
왼쪽 목록에 원본 저장소의 commit history가 나타나는 것을 볼 수 있습니다. 이제 push를 눌러줍니다.

![push4](./readme_image/push4.JPG)  
앞서 등록해둔 github account로 로그인 해줍니다.  
>이때 선택하는 account는 collaborator 권한을 가지고 있어야합니다.

![push5](./readme_image/push5.JPG)  
우측 하단에 위와 같은 메세지가 나온면 remote repo에 수정 사항이 반영된 것입니다.  

