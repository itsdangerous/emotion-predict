# [Window | Python] Flask를 활용한 표정 예측 API

> **개발 환경
Language : Python |** version : 3.11.4
**Shell : Git Bash**
> 
> 
> 3.11.4버전이 최신 버전이고 안정적인 3.10 버전에 비해 GCC Compile에 대해  최대 약 25%가량 빠르기 때문에 사용했다.
> 
> Python version에 관한 docs link는 [여기](https://docs.python.org/ko/3/whatsnew/3.11.html#summary-release-highlights)에서 확인 가능하다.
> 

## 개발 환경 세팅

### 1. Python 설치

[Get Python 3.11 from the Microsoft Store](https://www.microsoft.com/store/productId/9NRWMJP3717K)

Window를 사용한다면 Store에서 3.11.4 버전을 다운받을 수 있다.
다른 방법으로도 설치할 수 있지만, 환경 변수 세팅까지 알아서 해주기 때문에 이게 젤 편하다.

### 1-1. python pip 설치

pip는 Python 패키지 관리자로, Python 개발 환경에서 필요한 라이브러리를 쉽게 설치하고 관리할 수 있는 프롬프트 명령어이다.

보통 store에서 설치를 하면 system PATH에 추가된다.

```bash
# pip version 확인
pip --version

# 만약 pip 설치되어있지 않으면 프롬프트 창에 아래 실행
python -m ensurepip --upgrade # python 내장 ensurepip 모듈 사용하여 pip 설치

# pip version 재확인
pip --version
```

### 1-2. 가상환경 세팅

프로젝트 단위로 파이썬 프로젝트를 관리할 경우에는 가상 환경 단위로 관리하는 것이 좋다.

그 이유는 위에 언급한 pip 패키지 관리자는 python 버전에 따라 영향을 받는데,
프로젝트별로 python 버전이 다른 경우가 많기 때문에 개발 환경을 독립적으로 관리하기 위해서 이다.

먼저, 작업하고자 하는 디렉토리로 이동 한후 아래 명령 실행한다.

```bash
python -m venv .venv
```

그럼 현재 디렉토리에 .venv라는 파일이 보일 것이다(숨김 파일 보기 옵션 체크)

가상 환경에 진입. 아래 명령줄 실행

```bash
source ./.venv/Scripts/activate 
```

## 2. 프로젝트 clone

[https://github.com/itsdangerous/emotion-predict.git](https://github.com/itsdangerous/emotion-predict.git)

여기 코드를 가져온다

```bash
# git clone
git clone https://github.com/itsdangerous/emotion-predict.git
```

클론 받은 폴더에 가보면 requirements.txt란 파일이 보일텐데 필요한 패키지 목록이다.

한방에 패키지를 받기 위해 아래와 같은 명령줄 실행

```bash
pip install -r requirements.txt
```

## 3. 프로젝트 실행

세팅 완료 됐으니, 아래 명령줄을 실행하여 서버를 가동한다. (아직은 WSGI 서버를 사용하지 않았다.)

```bash
python app.py
```

## 4. API 테스트

swagger를 통해 테스트할 수 있다.

`http://localhost/api-docs`

에 가면 api에 관한 documents를 볼 수 있고 테스트할 수 있다.

POST 형식의 /analyze 엔드포인트는 requestBody를 인자로 받고 form-data 형식이다.

image 값에 얼굴 사진을 등록하면 다음과 같이 표정 예측 결과를 얻을 수 있다.

![screenshot](https://github.com/itsdangerous/emotion-predict/assets/76903093/3c199db6-2480-4f63-a5b6-4a912981d781)
