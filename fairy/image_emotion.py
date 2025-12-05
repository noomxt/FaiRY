from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import tkinter as tk
from tkinter import filedialog

# FER2013 감정 라벨
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
emotion_korean = {
    'Angry': '분노',
    'Disgust': '혐오',
    'Fear': '두려움',
    'Happy': '기쁨',
    'Sad': '슬픔',
    'Surprise': '놀람',
    'Neutral': '중립'
}

# 파일 탐색기에서 이미지 선택
def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path

# 감정 예측
def predict_emotion(img_path):
    # 모델과 전처리기 불러오기
    model = ViTForImageClassification.from_pretrained("trpakov/vit-face-expression")
    processor = ViTImageProcessor.from_pretrained("trpakov/vit-face-expression")

    # 이미지 열기
    image = Image.open(img_path).convert("RGB")

    # 전처리
    inputs = processor(images=image, return_tensors="pt")

    # 추론
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax(-1).item()

    emotion_eng = emotion_labels[predicted_class]
    emotion_kor = emotion_korean[emotion_eng]

    print("\n=== 감정 분석 결과 ===")
    for i, label in enumerate(emotion_labels):
        print(f"{emotion_korean[label]}: {logits[0][i].item():.2f}")
    print(f"\n최종 감정: {emotion_kor}")

# 실행
if __name__ == "__main__":
    img_path = select_image()
    if img_path:
        predict_emotion(img_path)
    else:
        print("이미지를 선택하지 않았습니다.")
