from simpful import *

def fuzzy_rules_and_system_create():
    FS = FuzzySystem()
    S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=25), term="quiet")
    S_2 = FuzzySet(function=Triangular_MF(a=20, b=30, c=70), term="medium")
    S_3 = FuzzySet(function=Triangular_MF(a=65, b=80, c=100), term="loud")
    FS.add_linguistic_variable("Sound", LinguisticVariable([S_1, S_2, S_3], concept="Printer sound",
                                                             universe_of_discourse=[0, 100]))
    S_11 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="low")
    S_22 = FuzzySet(function=Triangular_MF(a=0, b=10, c=20), term="medium")
    S_33 = FuzzySet(function=Triangular_MF(a=10, b=20, c=30), term="high")
    FS.add_linguistic_variable("Chewing", LinguisticVariable([S_11, S_22, S_33], concept="Printer chewing",
                                                             universe_of_discourse=[0, 30]))

    S_111 = FuzzySet(function=Triangular_MF(a=0, b=0, c=2), term="young")
    S_222 = FuzzySet(function=Triangular_MF(a=1, b=5, c=6), term="medium")
    S_333 = FuzzySet(function=Triangular_MF(a=4, b=7, c=10), term="high")
    FS.add_linguistic_variable("Age", LinguisticVariable([S_111, S_222, S_333], concept="Printer Age",
                                                             universe_of_discourse=[0, 10]))

    S_1111 = FuzzySet(function=Triangular_MF(a=22, b=22, c=30), term="low")
    S_2222 = FuzzySet(function=Triangular_MF(a=25, b=30, c=38), term="medium")
    S_3333 = FuzzySet(function=Triangular_MF(a=32, b=40, c=50), term="big")
    FS.add_linguistic_variable("Temperature", LinguisticVariable([S_1111, S_2222, S_3333], concept="Printer temperature",
                                                         universe_of_discourse=[22, 50]))

    #How many papers in hour it prints
    S_11111 = FuzzySet(function=Triangular_MF(a=0, b=20, c=100), term="low")
    S_22222 = FuzzySet(function=Triangular_MF(a=80, b=90, c=120), term="medium")
    S_33333 = FuzzySet(function=Triangular_MF(a=110, b=140, c=200), term="big")
    FS.add_linguistic_variable("Speed",
                               LinguisticVariable([S_11111, S_22222, S_33333], concept="Printer speed",
                                                  universe_of_discourse=[0, 200]))

    T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=20), term="small")
    T_2 = FuzzySet(function=Triangular_MF(a=10, b=30, c=40), term="average")
    T_3 = FuzzySet(function=Trapezoidal_MF(a=30, b=40, c=55, d=100), term="high")
    FS.add_linguistic_variable("Paper_Mis_Defects", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0, 100]))

    T_11 = FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small")
    T_22 = FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average")
    T_33 = FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")
    FS.add_linguistic_variable("Cartridge_Defects", LinguisticVariable([T_11, T_22, T_33], universe_of_discourse=[0, 100]))

    T_111 = FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small")
    T_222 = FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average")
    T_333 = FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")
    FS.add_linguistic_variable("Software_Defects",
                               LinguisticVariable([T_111, T_222, T_333], universe_of_discourse=[0, 100]))

    T_1111 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small")
    T_2222 = FuzzySet(function=Triangular_MF(a=5, b=30, c=80), term="average")
    T_3333 = FuzzySet(function=Trapezoidal_MF(a=70, b=75, c=85, d=100), term="high")
    FS.add_linguistic_variable("Cabel_Defects",
                               LinguisticVariable([T_1111, T_2222, T_3333], universe_of_discourse=[0, 100]))

    R1 = "IF (Sound IS loud) THEN (Paper_Mis_Defects IS high)"
    R2 = "IF (Sound IS quiet) AND (Chewing IS low) THEN (Paper_Mis_Defects IS small)"
    R3 = "IF (Sound IS medium) AND (Chewing IS high) THEN (Paper_Mis_Defects IS high)"
    R4 = "IF (Sound IS medium) AND (Chewing IS low) THEN (Paper_Mis_Defects IS high)"
    R5 = "IF (Sound IS medium) AND (Chewing IS medium) THEN (Paper_Mis_Defects IS small)"
    R6 = "IF (Sound IS quiet) AND (Chewing IS medium) THEN (Paper_Mis_Defects IS small)"
    R7 = "IF (Sound IS quiet) AND (Chewing IS high) THEN (Paper_Mis_Defects IS high)"
    R9 = "IF (Age IS young) THEN (Cartridge_Defects IS small)"
    R10 = "IF (Age IS medium) THEN (Cartridge_Defects IS average)"
    R11 = "IF (Age IS high) THEN (Cartridge_Defects IS high)"
    R12 = "IF (Temperature IS big) THEN (Cabel_Defects IS high)"
    R13 = "IF (Temperature IS medium) THEN (Cabel_Defects IS average)"
    R14 = "IF (Temperature IS low) THEN (Cabel_Defects IS low)"
    R15 = "IF (Speed IS low) THEN (Software_Defects IS high)"
    R16 = "IF (Speed IS medium) THEN (Software_Defects IS average)"
    R17 = "IF (Speed IS big) THEN (Software_Defects IS low)"

    FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R9, R10, R11, R12, R13, R14, R15, R16, R17])
    return FS

def use_fuzzy_system(FS, sound, chewing, age, temperature, speed):
    # Sound - [0, 100]
    FS.set_variable("Sound", sound)
    # Chewing -[0, 20]
    FS.set_variable("Chewing", chewing)
    # Age - [0, 10]
    FS.set_variable("Age", age)
    # Temperature - [22, 50]
    FS.set_variable("Temperature", temperature)
    # Speed - [0, 200]
    FS.set_variable("Speed", speed)
    results = FS.Mamdani_inference(["Paper_Mis_Defects", "Cartridge_Defects", "Software_Defects", "Cabel_Defects"])
    return results