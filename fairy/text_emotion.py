import re
from difflib import SequenceMatcher

class TextEmotionAnalyzer:
    def __init__(self):
        self.emotion_keywords = {
            "분노": ["빡친다", "돌겟네", "개빡", "킹받네", "열받아", "뚜껑 열린다", "딥빡", "씨", "시발", "짜증", "화나"],
            "슬픔": ["광광", "롬곡", "힝", "시무룩", "흑흑", "ㅠ", "ㅜ", "우울", "눈물"],
            "기쁨": ["굳", "개꿀", "나이스", "쪼아", "아이조아", "굿", "행복", "신나","야르"],
            "무서움": ["무서워", "오싹", "ㄷㄷ", "소름"],
        }

    def preprocess_text(self, text):
        text = re.sub(r'(.)\1{2,}', r'\1\1', text) 
        return "".join(text.split())

    def _calculate_similarity(self, input_text, keyword):
        return SequenceMatcher(None, input_text, keyword).ratio()

    def _check_slang(self, text):
        slang_list = ["시발", "씨발", "개새", "ㅈㄴ", "존나", "미친", "ㅅㅂ","쌰갈","싸갈","사갈","씹","쓰발"]
        for slang in slang_list:
            if slang in text:
                return True
        return False

    def analyze(self, text):
        processed_text = self.preprocess_text(text)
        print(f"[Debug] 전처리된 텍스트: {processed_text}")
        
        scores = {emotion: 0 for emotion in self.emotion_keywords.keys()}
        
        if self._check_slang(processed_text):
            scores["분노"] += 20 

        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                clean_keyword = "".join(keyword.split())
                
                if clean_keyword in processed_text:
                    scores[emotion] += 100
                else:
                    similarity = self._calculate_similarity(processed_text, clean_keyword)
                    if similarity >= 0.6:
                        scores[emotion] += int(similarity * 50)

        max_score = max(scores.values())
        if max_score == 0: 
            return "평온"
        
        top_emotions = [k for k, v in scores.items() if v == max_score]
        return top_emotions[0]