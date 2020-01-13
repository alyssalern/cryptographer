
class SolutionEvaluator:
    def __init__(self):
        self.word_searcher = WordSearcher()
    
    def evaluate(self, words):
        english_word_count = 0
        for w in words:
            if self.word_searcher.is_english_word(w):
                english_word_count += 1
        return english_word_count / len(words)

class WordSearcher:
    def __init__(self):
        file = open("../res/english-words.txt", "r")
        self.words = set(file.read().lower().splitlines())

    def is_english_word(self, text):
        text = self._format_for_comparison(text)
        return text in self.words
    
    def _format_for_comparison(self, text):
        return text.lower().strip(''.join(standard_nonalpha_chars))

alphabet = [chr(x) for x in list(range(ord('A'), ord('Z') + 1))]
standard_nonalpha_chars = [' ', ',', '.', ';', ':', '-', '?', '!']