import re

class TextEmotionAnalyzer:
    def __init__(self):
        pass

    def _remove_whitespace(self,text):
        return "".join(text.split())
    
    def _normalize_repeated_chars(self,text):
        return re.sub(r'(.)\1{2,}',r'\1\1',text)