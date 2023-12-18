from simpful import *

class FuzzySystemClass:
    def __init__(self, args_in, args_out):
        self.FS = None
        self.args_in = args_in
        self.args_out = args_out

    def fuzzy_rules_and_system_create(self):
        FS = FuzzySystem()

        FS.add_linguistic_variable("Sound", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=25),    term="quiet"),
                                                                FuzzySet(function=Triangular_MF(a=20, b=30, c=70),  term="medium"),
                                                                FuzzySet(function=Triangular_MF(a=65, b=80, c=100), term="loud")], concept="Printer sound",
                                                                universe_of_discourse=[0, 100]))


        FS.add_linguistic_variable("Chewing", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="low"),
                                                                  FuzzySet(function=Triangular_MF(a=0, b=10, c=20), term="medium"),
                                                                  FuzzySet(function=Triangular_MF(a=10, b=20, c=30), term="high")], concept="Printer chewing",
                                                                  universe_of_discourse=[0, 30]))

        FS.add_linguistic_variable("Age", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=2), term="young"),
                                                              FuzzySet(function=Triangular_MF(a=1, b=5, c=6), term="medium"),
                                                              FuzzySet(function=Triangular_MF(a=4, b=7, c=10), term="high")], concept="Printer Age",
                                                              universe_of_discourse=[0, 10]))

        FS.add_linguistic_variable("Temperature", LinguisticVariable([FuzzySet(function=Triangular_MF(a=22, b=22, c=30), term="low"),
                                                                      FuzzySet(function=Triangular_MF(a=25, b=30, c=38),
                                                                               term="medium"),
                                                                      FuzzySet(function=Triangular_MF(a=32, b=40, c=50), term="big")], concept="Printer temperature",
                                                                      universe_of_discourse=[22, 50]))

        FS.add_linguistic_variable("Speed",
                                   LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=20, c=100), term="low"),
                                                       FuzzySet(function=Triangular_MF(a=80, b=90, c=120), term="medium"),
                                                       FuzzySet(function=Triangular_MF(a=110, b=140, c=200), term="big")], concept="Printer speed",
                                                       universe_of_discourse=[0, 200]))

        FS.add_linguistic_variable("Paper_Mis_Defects", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=20), term="small"),
                                                                            FuzzySet(function=Triangular_MF(a=10, b=30, c=40), term="average"),
                                                                            FuzzySet(function=Trapezoidal_MF(a=30, b=40, c=55, d=100), term="high")],
                                                                            universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("Cartridge_Defects", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small"),
                                                                            FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average"),
                                                                            FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")],
                                                                            universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("Software_Defects",
                                   LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small"),
                                                       FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average"),
                                                       FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")],
                                                       universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("Cabel_Defects",
                                   LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small"),
                                                       FuzzySet(function=Triangular_MF(a=5, b=30, c=80), term="average"),
                                                       FuzzySet(function=Trapezoidal_MF(a=70, b=75, c=85, d=100), term="high")],
                                                       universe_of_discourse=[0, 100]))

        RULES = [
            "IF (Sound IS loud) THEN (Paper_Mis_Defects IS high)",
            "IF (Sound IS quiet) AND (Chewing IS low) THEN (Paper_Mis_Defects IS small)",
            "IF (Sound IS medium) AND (Chewing IS high) THEN (Paper_Mis_Defects IS high)",
            "IF (Sound IS medium) AND (Chewing IS low) THEN (Paper_Mis_Defects IS high)",
            "IF (Sound IS medium) AND (Chewing IS medium) THEN (Paper_Mis_Defects IS small)",
            "IF (Sound IS quiet) AND (Chewing IS medium) THEN (Paper_Mis_Defects IS small)",
            "IF (Sound IS quiet) AND (Chewing IS high) THEN (Paper_Mis_Defects IS high)",
            "IF (Age IS young) THEN (Cartridge_Defects IS small)",
            "IF (Age IS medium) THEN (Cartridge_Defects IS average)",
            "IF (Age IS high) THEN (Cartridge_Defects IS high)",
            "IF (Temperature IS big) THEN (Cabel_Defects IS high)",
            "IF (Temperature IS medium) THEN (Cabel_Defects IS average)",
            "IF (Temperature IS low) THEN (Cabel_Defects IS low)",
            "IF (Speed IS low) THEN (Software_Defects IS high)",
            "IF (Speed IS medium) THEN (Software_Defects IS average)",
            "IF (Speed IS big) THEN (Software_Defects IS low)"
        ]

        FS.add_rules(RULES)
        self.FS = FS

    def use_fuzzy_system(self, values):
        for text, arg in zip(self.args_in, values):
            self.FS.set_variable(text, arg)
        results = self.FS.Mamdani_inference(self.args_out)
        return results