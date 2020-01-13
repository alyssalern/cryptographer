from text_data import CyphertextData
from shared_utils import alphabet
from shared_utils import standard_nonalpha_chars

class TextPreanalyzer:

    _EXPECTED_WORD_LENGTH = 4.7
    _WORD_LENGTH_TOLERANCES = (3.5, 6.5)
    _MAX_WORD_LENGTH = 45

    def __init__(self):
        pass
    
    def analyze(self, text):
        cyphertext = CyphertextData(text)
        text = text[:10000]
        cyphertext.space_symbol = self._deduce_space_symbol(text)
        cyphertext.alpha_freq = self._get_alpha_char_freq(text)
        cyphertext.nonstandard_freq = self._get_nonstandard_char_freq(text)
        cyphertext.upper_freq = self._get_uppercase_letter_freq(text)
        return cyphertext

    def _deduce_space_symbol(self, text):
        candidate_spaces = set(filter(lambda c : c.upper() not in alphabet, set(text)))
        return self._get_best_space_symbol(text, candidate_spaces)

    def _get_candidate_spaces(self, text):
        candidate_spaces = set(text[:self._MAX_WORD_LENGTH])
        return set(filter(lambda c : c not in alphabet, candidate_spaces))

    def _get_best_space_symbol(self, text, candidate_spaces):
        best_space_symbol = None
        best_avg_word_length = 0.0

        for candidate_space in candidate_spaces:
            if self._word_lengths_feasible(text, candidate_space) is False:
                continue
            avg_word_length = self._get_avg_word_length(text.split(candidate_space))
            if avg_word_length < self._WORD_LENGTH_TOLERANCES[0] or avg_word_length > self._WORD_LENGTH_TOLERANCES[1]:
                continue
            if abs(avg_word_length - self._EXPECTED_WORD_LENGTH) < abs(best_avg_word_length - self._EXPECTED_WORD_LENGTH):
                best_space_symbol = candidate_space
                best_avg_word_length = avg_word_length

        return best_space_symbol
    
    def _get_avg_word_length(self, words):
        get_word_length = lambda word: sum(map(lambda x: x.upper() in alphabet, word))

        avg_word_length = get_word_length(words[0])
        for i in range(1, len(words) - 1):
            word_length = get_word_length(words[i])
            avg_word_length += (word_length - avg_word_length) / (i + 1)

        return avg_word_length

    def _word_lengths_feasible(self, text, space_symbol):
        for word in text.split(space_symbol):
            if len(word) > self._MAX_WORD_LENGTH:
                return False
        return True

    def _get_alpha_char_freq(self, text):
        sum = 0
        for x in text:
            if x.upper() in alphabet:
                sum += 1
        return sum / len(text)
    
    def _get_nonstandard_char_freq(self, text):
        sum = 0
        for x in text:
            if x.upper() not in alphabet and x not in standard_nonalpha_chars:
                sum += 1
        return sum / len(text)
    
    def _get_uppercase_letter_freq(self, text):
        alpha_chars = [x for x in text if x.upper() in alphabet]
        sum = 0
        for x in alpha_chars:
            if x in alphabet:
                sum += 1
        return sum / len(alpha_chars)