import re
import config

class TextEmotionAnalyzer:
    def __init__(self):
        self.sad_keywords = getattr(config, 'SAD_KEYWORDS', [])
        self.happy_keywords = getattr(config, 'HAPPY_KEYWORDS', [])
        self.slang_map = getattr(config, 'SLANG_MAP', {})

    def _remove_whitespace(self,text):
        return "".join(text.split())
    
    def _normalize_repeated_chars(self,text):
        return re.sub(r'(.)\1{2,}',r'\1\1',text)
    
    def _censor_slang(self, text):
        processed_text = text.lower()
        for slang, replacement in self.slang_map.items():
            processed_text = processed_text.replace(slang, replacement)
        return processed_text
    
    def preprocess_text(self, text):
        text = self._normalize_repeated_chars(text)
        text = self._censor_slang(text)
        text = self._remove_whitespace(text)
        return text
    
    def analyze_text(self, text):
        processed_text = self.preprocess_text(text)

        if any(word in processed_text for word in self.sad_keywords):
            return "sad"
        elif any(word in processed_text for word in self.happy_keywords):
            return "happy"
        else:
            return "neutral"
        
    def get_matching_results(self, sentiment):
        if sentiment == "sad":
            return {"recommendation": "따뜻한 차 마시기"}
        elif sentiment == "happy":
            return {"recommendation": "신나는 노래 듣기"}
        else:
            return {"recommendation": "명상하기"}