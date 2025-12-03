import re
import csv
from config import EMOTION_FILES

class TextEmotionAnalyzer:
    def __init__(self):
        self.emotion_keywords = self._load_data()

    def _load_data(self):
        data = {}
        for emotion, file_path in EMOTION_FILES.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    keywords = [line.strip() for line in f.readlines() if line.strip()]
                    data[emotion] = keywords
            except FileNotFoundError:
                data[emotion] = []
        return data

    def _remove_whitespace(self,text):
        return "".join(text.split())
    
    def _normalize_repeated_chars(self,text):
        return re.sub(r'(.)\1{2,}',r'\1\1',text)
    
    def _censor_slang(self, text):
        slang_map = {"ㅅㅂ": "비읍", "개새끼": "멍멍이", "존나": "매우"}
        
        processed_text = text.lower()
        for slang, replacement in slang_map.items():
            processed_text = processed_text.replace(slang, replacement)
        return processed_text
    
    def preprocess_text(self, text):
        text = self._normalize_repeated_chars(text)
        text = self._censor_slang(text)
        text = self._remove_whitespace(text)
        return text
    
    def analyze_text(self, text):
        processed_text = self.preprocess_text(text)

        sad_list = self.emotion_keywords.get('슬픔', [])
        if any(word in processed_text for word in sad_list):
            return "슬픔"
        for emotion, keywords in self.emotion_keywords.items():
            if emotion == '슬픔': continue
            if any(word in processed_text for word in keywords):
                return emotion
        return "평온"
        
    def get_matching_results(self, sentiment):
        if sentiment == "슬픔":
            return {"song": "IU - 밤편지", "todo": "따뜻한 차 마시기"}
        elif sentiment == "기쁨":
            return {"song": "NewJeans - Hype Boy", "todo": "친구와 약속 잡기"}
        elif sentiment == "분노":
            return {"song": "Imagine Dragons - Believer", "todo": "심호흡 10번 하기"}
        else:
            return {"song": "Classic Piano", "todo": "휴식 취하기"}