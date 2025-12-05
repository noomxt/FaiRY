from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image, ImageDraw, ImageFont
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

# 감정별 말풍선 텍스트 (현재는 모두 "할 거 추천")
emotion_bubble_texts = {label: "할 거 추천" for label in emotion_labels}

# 파일 탐색기에서 이미지 선택
def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path

# 말풍선 합성 함수
def add_speech_bubble(img_path, text, output_path="output.png"):
    img = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    # 말풍선 위치와 크기
    bubble_x, bubble_y = 50, 50
    bubble_w, bubble_h = 200, 100

    # 말풍선 그리기 (사각형 + 꼬리)
    draw.rectangle([bubble_x, bubble_y, bubble_x+bubble_w, bubble_y+bubble_h], fill="white", outline="black")
    draw.polygon([(bubble_x+50, bubble_y+bubble_h),
                  (bubble_x+70, bubble_y+bubble_h+30),
                  (bubble_x+90, bubble_y+bubble_h)], fill="white", outline="black")

    # 글꼴 설정
    font = ImageFont.load_default()
    draw.text((bubble_x+10, bubble_y+10), text, font=font, fill="black")

    # 저장
    img.save(output_path)
    print(f"✅ 말풍선 합성 완료: {output_path}")

# 감정 예측 + 말풍선 합성
def predict_and_bubble(img_path):
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

    # 말풍선 텍스트 선택
    bubble_text = emotion_bubble_texts[emotion_eng]

    # 말풍선 합성
    add_speech_bubble(img_path, bubble_text)

# 실행
if __name__ == "__main__":
    img_path = select_image()
    if img_path:
        predict_and_bubble(img_path)
    else:
        print("이미지를 선택하지 않았습니다.")
