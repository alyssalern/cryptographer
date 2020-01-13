
class CyphertextData:
    def __init__(self, text = ""):
        self.text = text
        self.space_symbol = None
        self.alpha_freq = -1
        self.nonstandard_freq = -1
        self.upper_freq = -1

class PlaintextSolution:
    def __init__(self, text = ""):
        self.text = text
        self.solution_certainty = None
    
    @property
    def solution_found(self):
        return self.solution_certainty is not None