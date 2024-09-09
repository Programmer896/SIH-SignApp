class GujaratiSignInterpreter:
    def __init__(self):
        self.english_to_gujarati_dict = {
            'a': 'અ', 'aa': 'આ', 'i': 'ઇ', 'ee': 'ઈ', 'u': 'ઉ',
            'oo': 'ઊ', 'e': 'એ', 'ai': 'ઐ', 'o': 'ઓ', 'au': 'ઔ',
            'k': 'ક', 'kh': 'ખ', 'g': 'ગ', 'gh': 'ઘ', 'ch': 'ચ',
            'chh': 'છ', 'j': 'જ', 'jh': 'ઝ', 't': 'ટ', 'th': 'ઠ',
            'd': 'ડ', 'dh': 'ઢ', 'n': 'ણ', 'ta': 'ત', 'tha': 'થ',
            'da': 'દ', 'dha': 'ધ', 'na': 'ન', 'p': 'પ', 'ph': 'ફ',
            'b': 'બ', 'bh': 'ભ', 'm': 'મ', 'y': 'ય', 'r': 'ર',
            'l': 'લ', 'v': 'વ', 'sh': 'શ', 's': 'સ', 'h': 'હ',
            'L': 'ળ', 'ksh': 'ક્ષ', 'gn': 'જ્ઞ'
        }
        self.gujarati_to_sign_dict = {
            'અ': '👆', 'આ': '👋', 'ઇ': '✌️', 'ઈ': '🤘', 'ઉ': '👌',
            'ઊ': '🖐️', 'એ': '👍', 'ઐ': '🤙', 'ઓ': '👊', 'ઔ': '🤛',
            'ક': '🤜', 'ખ': '👐', 'ગ': '🙌', 'ઘ': '👏', 'ચ': '🤝',
            'છ': '🤲', 'જ': '🤞', 'ઝ': '🤟', 'ટ': '🤚', 'ઠ': '✋',
            'ડ': '🖖', 'ઢ': '👇', 'ણ': '☝️', 'ત': '👉', 'થ': '👈',
            'દ': '🤏', 'ધ': '🤌', 'ન': '🤘', 'પ': '🤟', 'ફ': '🤙',
            'બ': '👌', 'ભ': '🤞', 'મ': '🖕', 'ય': '☝️', 'ર': '👆',
            'લ': '👇', 'વ': '👉', 'શ': '👈', 'સ': '👋', 'હ': '🤚',
            'ળ': '✋', 'ક્ષ': '🖖', 'જ્ઞ': '🤏'
        }
        self.sign_to_gujarati_dict = {v: k for k, v in self.gujarati_to_sign_dict.items()}

    def english_to_gujarati(self, text):
        gujarati_text = ''
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i:i+2] in self.english_to_gujarati_dict:
                gujarati_text += self.english_to_gujarati_dict[text[i:i+2]]
                i += 2
            elif text[i] in self.english_to_gujarati_dict:
                gujarati_text += self.english_to_gujarati_dict[text[i]]
                i += 1
            else:
                gujarati_text += text[i]
                i += 1
        return gujarati_text

    def to_sign(self, text):
        sign_text = ''
        for char in text:
            if char in self.gujarati_to_sign_dict:
                sign_text += self.gujarati_to_sign_dict[char]
            else:
                sign_text += char
        return sign_text

    def sign_to_gujarati(self, sign):
        return self.sign_to_gujarati_dict.get(sign, sign)

    def is_gujarati(self, text):
        return any('\u0A80' <= char <= '\u0AFF' for char in text)