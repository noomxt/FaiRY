from setuptools import setup, find_packages

setup(
    name="FaiRY",
    version="1.0.0",
    description="Multi-modal Emotion Analysis & Recommendation Library",
    author="AIF5 Team",
    author_email="baesohyun04@hanyang.ac.kr",
    url="https://github.com/noomxt/FaiRY",
    
    packages=find_packages(),
    
    install_requires=[
        "flask",            # 웹 서버 (app.py)
        "werkzeug",         # 파일 업로드 보안 (app.py)
        "pillow",           # 이미지 처리 (image_emotion.py)
        "torch",            # 딥러닝 프레임워크 (image_emotion.py)
        "transformers",     # ViT 모델 로드 (image_emotion.py)
        "numpy",            # (의존성)
        "pandas"            # (데이터 처리 등 일반적 필요)
    ],
    
    python_requires=">=3.8",
)
