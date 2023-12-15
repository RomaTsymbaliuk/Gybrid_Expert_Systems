
from fuzzy_system import *
from ui import *
from alg import *

printer_age_interval = [0, 10]
printer_chew_interval = [0, 30]
printer_speed_interval = [0, 200]
printer_sound_interval = [30, 100]
printer_temperature_interval = [22, 50]
class Expert_System:
    def __init__(self, printer_age, printer_chew, printer_sound, printer_speed, printer_temperature):
        self.printer_age = printer_age if printer_age_interval[0] <= printer_age < printer_age_interval[1] else printer_age_interval[1] - 1
        self.printer_chew = printer_chew if printer_chew_interval[0] <= printer_chew < printer_chew_interval[1] else printer_chew_interval[1] - 1
        self.printer_speed = printer_speed if printer_speed_interval[0] <= printer_speed < printer_speed_interval[1] else printer_speed_interval[1] - 1
        self.printer_sound = printer_sound if printer_sound_interval[0] <= printer_sound < printer_sound_interval[1] else printer_sound_interval[1] - 1
        self.printer_temperature = printer_temperature if printer_temperature_interval[0] <= printer_temperature < printer_temperature_interval[1] else printer_temperature_interval[1] - 1
        self.FS = None
    def create_expert_system(self):
        self.FS = fuzzy_rules_and_system_create()

    def use_expert_system(self):
        results = use_fuzzy_system(self.FS, self.printer_sound, self.printer_chew, self.printer_age, self.printer_temperature, self.printer_speed)
        self.results = results
        print(results)
""""
def get_all_values():
    Expert = Expert_System(printer_age, printer_chew, printer_sound, printer_speed, printer_temperature)
    Expert.create_expert_system()
    results = Expert.use_expert_system()
    print(results)
def build_best_path_from_graph():
    #    points = [results['Paper_Mis_Defects'], results['Inc_Defects']]
    points = [0, 1, 2, 3]  # 0 - Paper_Mis_Defects, 1 - Cartridge_Defects, 2 - Software_Defects, 3 - Cabel_Defects, 4 -
    graph = [[math.inf, 7, 8, 2], [7, math.inf, 4, 5], [8, 4, math.inf, 3], [5, 1, 2, math.inf]]
    best_path = ant_colony_optimization(points, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1,
                                        graph=graph)
    print(best_path)
"""

win = UI(5)
win.window.mainloop()

