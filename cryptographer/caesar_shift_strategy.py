from decryption_strategy import DecryptionStrategy
from shared_utils import alphabet
from text_data import PlaintextSolution

class CaesarShiftStrategy(DecryptionStrategy):
    def __init__(self):
        super().__init__("Caeser Shift Decryptor")


    def _preconditions_met(self, cyphertext):
        return super()._preconditions_met(cyphertext)

    def _decrypt(self):
        best_shift = None
        best_certainty = -1.0

        for shift in range(len(alphabet)):
            decryption_attempt = self._decrypt_with_shift(self._cyphertext_sample, shift)
            decryption_certainty = self._get_solution_certainty(decryption_attempt)

            if decryption_certainty > best_certainty:
                best_shift = shift
                best_certainty = decryption_certainty

        if best_shift is not None:
            return self._create_final_solution(best_shift)

        return None
        
    def _decrypt_with_shift(self, text, shift):
        shifted_chars = [self._shift_char(x, shift) for x in list(text)]
        return ''.join(shifted_chars)

    def _shift_char(self, char, shift):
        upper_char = char.upper()
        if upper_char not in alphabet:
            return char
        shifted_index = (alphabet.index(upper_char) + shift) % len(alphabet)

        upper_shifted_char = alphabet[shifted_index]
        if char.islower():
            return upper_shifted_char.lower()
        return upper_shifted_char
    
    def _get_solution_certainty(self, solution):
        words = solution.split(self._cyphertext_data.space_symbol)
        return self._solution_evaluator.evaluate(words)
    
    def _create_final_solution(self, shift):
        solution = PlaintextSolution()
        solution.text = self._decrypt_with_shift(self._cyphertext_data.text, shift)
        solution.solution_certainty = self._get_solution_certainty(solution.text)

        if solution.solution_certainty >= self._MIN_SOLUTION_CERTAINTY:
            return solution

        return None