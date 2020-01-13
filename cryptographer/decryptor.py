from text_preanalyzer import TextPreanalyzer
from caesar_shift_strategy import CaesarShiftStrategy

class Decryptor:
    def __init__(self):
        self._preanalyzer = TextPreanalyzer()
        self._decryption_strategies = [CaesarShiftStrategy()]

    def decrypt(self, text):
        cyphertext = self._preanalyzer.analyze(text)

        for strategy in self._decryption_strategies:
            result = strategy.decrypt(cyphertext)
            if result is not None:
                return result
                
        print("Decryptor - Failed to decrypt the text")
        return None