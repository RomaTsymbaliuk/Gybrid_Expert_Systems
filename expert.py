from fuzzy_system import *
class Expert_System:
    def __init__(self, args, args_out, values):
        self.args = args
        self.args_out = args_out
        self.values = values
        self.FSІ = FuzzySystemClass(self.args, self.args_out)
        self.FSІ.fuzzy_rules_and_system_create()
    def use_expert_system(self):
        results = self.FSІ.use_fuzzy_system(self.values)
        self.results = results
        return results
