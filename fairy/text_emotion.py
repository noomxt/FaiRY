import re
import csv
from config import EMOTION_FILES
import random

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
        recommendations = {
            "기쁨": [
                {"song": "NewJeans - Hype Boy", "todo": "친구들에게 연락해 번개 모임 잡기"},
                {"song": "Pharrell Williams - Happy", "todo": "맛있는 디저트 사먹으며 기분 만끽하기"},
                {"song": "Bruno Mars - Uptown Funk", "todo": "거울 보고 춤 한번 추기"},
                {"song": "Day6 - 한 페이지가 될 수 있게", "todo": "오늘의 기분을 일기장에 기록하기"},
                {"song": "Red Velvet - 빨간 맛", "todo": "시원한 음료수 마시며 산책하기"}
            ],
            "슬픔": [
                {"song": "IU - 밤편지", "todo": "따뜻한 차 한 잔 마시며 멍 때리기"},
                {"song": "박효신 - 야생화", "todo": "슬픈 영화 한 편 보면서 실컷 울기"},
                {"song": "폴킴 - 모든 날, 모든 순간", "todo": "포근한 이불 속에서 푹 쉬기"},
                {"song": "이하이 - 한숨", "todo": "친한 친구에게 전화해서 하소연하기"},
                {"song": "김광석 - 서른 즈음에", "todo": "조용한 카페에서 생각 정리하기"}
            ],
            "분노": [
                {"song": "Imagine Dragons - Believer", "todo": "눈 감고 깊게 심호흡 10번 하기"},
                {"song": "Eminem - Lose Yourself", "todo": "베개에 얼굴 파묻고 소리 지르기"},
                {"song": "Linkin Park - Faint", "todo": "땀 날 때까지 운동하거나 달리기"},
                {"song": "2NE1 - 내가 제일 잘 나가", "todo": "매운 음식 먹으면서 스트레스 풀기"},
                {"song": "G-Dragon - 삐딱하게", "todo": "종이에 화나는 일 적고 구겨서 버리기"}
            ],
            "피곤함": [
                {"song": "Jaurim - 스물다섯, 스물하나", "todo": "따뜻한 물로 반신욕 하기"},
                {"song": "10cm - 스토커", "todo": "핸드폰 끄고 30분만 낮잠 자기"},
                {"song": "Zion.T - 꺼내 먹어요", "todo": "비타민이나 영양제 챙겨 먹기"},
                {"song": "백예린 - Square", "todo": "가벼운 스트레칭으로 몸 풀기"},
                {"song": "성시경 - 두 사람", "todo": "눈 찜질팩 하고 눈 휴식하기"}
            ],
            "무서움": [
                {"song": "Gaho - 시작 (이태원 클라쓰)", "todo": "가족이나 가장 친한 친구에게 전화하기"},
                {"song": "BTS - Dynamite", "todo": "밝고 명랑한 예능 프로그램 보기"},
                {"song": "Twice - Cheer Up", "todo": "방 불 환하게 켜고 따뜻한 우유 마시기"},
                {"song": "Disney OST - Under the Sea", "todo": "귀여운 동물 영상 찾아보기"},
                {"song": "Bolbbalgan4 - 여행", "todo": "좋아하는 담요 덮고 안정을 취하기"}
            ],
            "평온": [
                {"song": "Yiruma - River Flows In You", "todo": "읽다 만 책 마저 읽기"},
                {"song": "Joe Hisaishi - Summer", "todo": "창문 열고 바깥 공기 쐬기"},
                {"song": "Lofi Girl - Hip Hop Radio", "todo": "오늘 해야 할 일 차분히 정리하기"},
                {"song": "Depapepe - Start", "todo": "식물에 물 주거나 정리 정돈하기"},
                {"song": "Maroon 5 - Sunday Morning", "todo": "드립 커피 직접 내려 마시기"}
            ]
        }

        target_list = recommendations.get(sentiment, recommendations["평온"])
        return random.choice(target_list)