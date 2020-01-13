from text_data import CyphertextData
from abc import ABC, abstractmethod
from shared_utils import SolutionEvaluator

class DecryptionStrategy(ABC):
    _MIN_LEN = 50
    _MIN_ALPHA_FREQ = 0.8
    _MAX_NONSTANDARD_FREQ = 0.2
    _SAMPLE_LEN = 1000
    _MIN_SOLUTION_CERTAINTY = 0.9

    def __init__(self, strategy_name):
        self.strategy_name = strategy_name
        self._cyphertext_data = None
        self._cyphertext_sample = None
        self._solution_evaluator = SolutionEvaluator()

    def decrypt(self, cyphertext_data):
        print("{} - Beginning analysis.".format(self.strategy_name))
        if self._preconditions_met(cyphertext_data) is False:
            print("The preconditions for this decryption strategy have not been met.")
            return None
        self._cyphertext_data = cyphertext_data
        self._cyphertext_sample = cyphertext_data.text[:self._SAMPLE_LEN]
        return self._decrypt()

    @abstractmethod
    def _preconditions_met(self, cyphertext):
        preconds_met = True

        if len(cyphertext.text) < self._MIN_LEN:
            print("Precondition failed - not enough text")
            preconds_met = False

        if cyphertext.space_symbol is None:
            print("Precondition failed - indeterminate space symbol")
            preconds_met = False

        if cyphertext.alpha_freq < self._MIN_ALPHA_FREQ:
            print("Precondition failed - not enough alphabetic characters")
            preconds_met = False

        if cyphertext.nonstandard_freq > self._MAX_NONSTANDARD_FREQ:
            print("Precondition failed - too many unexpected characters ({})".format(cyphertext.nonstandard_freq))
            preconds_met = False
            
        return preconds_met
    
    @abstractmethod
    def _decrypt(self):
        pass
    
