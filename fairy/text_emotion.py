import tkinter as tk
from tkinter import messagebox
import csv
import random
import os
import config  # 설정 파일(config.py) 불러오기

class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FaiRY - 감정 분석기")
        self.root.geometry("600x500")
        self.root.configure(bg="#F0F8FF")

        self.brain = {}
        self.recommendations = {}
        
        self.load_data()
        self.setup_ui()

    def load_data(self):
        print("🤖: 데이터 학습 시작...")
        for emotion, file_path in config.EMOTION_FILES.items():
            self.recommendations[emotion] = []
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            content = row['content']
                            if content:
                                # [핵심] 멘트 학습 (이 말을 들으면 -> 이 감정이다!)
                                self.brain[content] = emotion
                                self.recommendations[emotion].append(content)
            except Exception:
                pass
        print(f"✅ 학습 완료! 총 {len(self.brain)}개의 문장을 배웠어요.")

    def analyze_emotion(self, user_text):
        # 1. 정확히 똑같은 말이 있는지 확인
        if user_text in self.brain:
            return self.brain[user_text]
        # 2. 포함된 단어가 있는지 확인
        for known_text, emotion in self.brain.items():
            if known_text in user_text: 
                return emotion
        return "평온"

    def on_click_analyze(self):
        # 👇 [수정됨] 점(.) 뒤에 get()을 추가해서 오타 해결!
        user_input = self.entry.get().strip()
        
        if not user_input:
            messagebox.showwarning("알림", "하고 싶은 말을 적어주세요!")
            return

        detected_emotion = self.analyze_emotion(user_input)
        
        if detected_emotion in self.recommendations and self.recommendations[detected_emotion]:
            rec_text = random.choice(self.recommendations[detected_emotion])
        else:
            rec_text = "추천 데이터가 없네요 😅"

        self.lbl_result_emotion.config(text=f"분석된 감정: {detected_emotion}", fg="blue")
        self.lbl_result_text.config(text=f"💌 추천 멘트:\n{rec_text}")

    def setup_ui(self):
        tk.Label(self.root, text="오늘 어떤 일이 있었나요?", font=("맑은 고딕", 16, "bold"), bg="#F0F8FF").pack(pady=20)
        self.entry = tk.Entry(self.root, font=("맑은 고딕", 12), width=40)
        self.entry.pack(pady=10)
        tk.Button(self.root, text="감정 분석하기 🔍", command=self.on_click_analyze, bg="#4682B4", fg="white").pack(pady=10)
        self.lbl_result_emotion = tk.Label(self.root, text="여기에 감정이 분석됩니다", font=("맑은 고딕", 14), bg="#F0F8FF")
        self.lbl_result_emotion.pack(pady=20)
        self.lbl_result_text = tk.Label(self.root, text="", bg="white", width=50, height=5, wraplength=400)
        self.lbl_result_text.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()