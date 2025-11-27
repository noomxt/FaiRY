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