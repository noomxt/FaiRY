# 🧚 FaiRY 라이브러리 
Face and text Analysis & Intelligent Recommendation for You - 당신을 위한 얼굴, 텍스트 분석 및 지능형 추천 시스템

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Flask-2.0-green)
![Library](https://img.shields.io/badge/PyTorch-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> **"당신의 감정을 지켜주는 요정, FaiRY"**

**FaiRY**는 사용자의 얼굴 표정(Face)과 텍스트(Text)를 분석하여 현재 감정을 파악하고, 

마치 요정처럼 그에 딱 맞는 **활동과 음악을 추천**해주는 **지능형 멀티모달 감정 케어 서비스**입니다.

이 프로젝트는 2025년 2학기 한양대학교 ERICA 인공지능학과

**오픈소스 실전 인공지능(AI Practice OSS)** 강의의 일환으로 개발되었습니다.

---

## 🚀 주요 기능 (Key Features)

### 1. 📸 얼굴 및 텍스트 감정 분석 (Face & Text Analysis)
* **Visual Analysis:** ViT (Vision Transformer) 모델을 사용하여 미세한 얼굴 표정을 정밀하게 분석합니다.
* **Text Analysis:** 사용자가 입력한 일기나 문장에서 핵심 키워드를 추출하여 감정 상태를 판별합니다.
* **Multi-modal:** 시각 정보와 텍스트 정보를 결합하여 5가지 핵심 감정(기쁨, 슬픔, 분노, 공포, 평온)을 도출합니다.

### 2. 🎁 지능형 추천 시스템 (Intelligent Recommendation)
* 분석된 감정 데이터(Emotion)를 기반으로 기분 전환에 도움이 되는 맞춤형 활동(Todo)과 음악(Song)을 추천합니다.
* `data/` 폴더 내의 자체 구축된 감정별 데이터베이스와 매칭 알고리즘을 사용합니다.

### 3. 💻 감성적인 웹 인터페이스 (Web Interface)
* **Flask** 프레임워크 기반의 가볍고 빠른 웹 데모를 제공합니다.
* 프로젝트 컨셉(Fairy)에 맞춘 파스텔 핑크톤 UI와 Pretendard 폰트로 사용자 친화적인 경험을 제공합니다.

---

## 🛠 프로젝트 구조 (Project Structure)

```bash
FaiRY/
├── data/               # 📂 [Assets] 감정 데이터셋(CSV) 및 폰트 파일
│   ├── emotions.csv    # 감정별 추천 목록 DB
│   └── ...
├── fairy/              # 🐍 [Library] 핵심 분석 모듈 (Core Logic)
│   ├── __init__.py
│   ├── config.py       # 경로 및 설정 관리 (Path Management)
│   ├── image_emotion.py # 얼굴 표정 분석 모듈
│   ├── text_emotion.py  # 텍스트 감정 분석 모듈
│   └── ...
├── static/             # 🎨 [Web] CSS 스타일시트, 업로드 파일 저장소
├── templates/          # 📄 [Web] HTML 템플릿 (UI)
├── app.py              # 🚀 [Execution] 웹 애플리케이션 실행 파일
├── setup.py            # 📦 [Deploy] 패키지 배포 및 설치 설정
└── requirements.txt    # 📌 [Env] 의존성 라이브러리 목록
```

---
## 📦 설치 및 실행 (Installation & Usage) 
프로젝트를 로컬 환경에서 실행하는 방법입니다.

### **필수 조건 (Prerequisites)**
#### 1. Python 3.8 이상
#### 2. Git 설치
#### 3. 터미널(Terminal)에서 아래 명령어를 입력하세요.
① 프로젝트 접근
```bash
pip install git+https://github.com/noomxt/FaiRY.git
```
② 필수 라이브러리 설치 (Install Dependencies)
```bash
pip install -r requirements.txt
# 또는
pip install flask werkzeug pillow torch transformers opencv-python pandas
```

#### 4. 실행 (Run Demo)
설치가 완료되면 웹 데모를 실행할 수 있습니다.
```bash
python app.py
```
실행 후 브라우저 주소창에 http://127.0.0.1:5000 을 입력하여 접속하세요.

---
## 👥 Contributors - Team: AIF5
#### FaiRY는 한양대학교 ERICA 인공지능학과 학부생으로 구성된 AIF5 Team이 제작했습니다.
| 이름 (Name) | 역할 (Role) | 담당 업무 (Responsibility) |
|:---:|:---:|:---|
| **배소현** | **Team Leader (PM)** | 프로젝트 총괄, Git 인프라 및 배포 전략 수립, 발표 자료 제작 |
| **박다연** | Image Engineer | ViT 모델 활용 얼굴 감정 인식 알고리즘 구현 및 최적화 |
| **박지수** | Text Engineer | 텍스트 기반 감정 키워드 추출 및 매칭 로직 개발 |
| **김미현** | Data Manager | 감정별 추천 데이터셋(CSV) 구축 및 config 경로 시스템 설계 |
| **신민주** | Web Developer | Flask 웹 서버 구축, UI/UX 디자인 및 프론트엔드 통합 |

---
## 📜 라이선스 (License)
이 프로젝트는 [MIT License](LICENSE)를 따릅니다.
