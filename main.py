
from tkinter import *
from fuzzy_system import *
from alg import *
import math

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
def get_all_values():
    printer_age = int(printer_age_string.get())
    printer_chew = int(printer_chew_string.get())
    printer_sound = int(printer_sound_string.get())
    printer_speed = int(printer_speed_string.get())
    printer_temperature = int(printer_temperature_string.get())


    print('Printer age : ', printer_age, ' printer_chew : ', printer_chew, ' printer_sound : ', printer_sound, ' printer_speed : ', printer_speed, ' printer_temperature : ', printer_temperature)
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

def build_labels(text, row, column, window, var):
    Label(text=text).grid(row=row, column=column)
    Entry(window, textvariable=var).grid(row=row, column=column+1)


window = Tk()
window.columnconfigure([0, 1, 2], minsize=100)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=20)
printer_age_string = StringVar()
printer_temperature_string = StringVar()
printer_age_string = StringVar()
printer_chew_string = StringVar()
printer_sound_string = StringVar()
printer_speed_string = StringVar()

printer_vars = [
    printer_age_string, printer_temperature_string,
    printer_chew_string, printer_sound_string, printer_speed_string
]

printer_text_lbl = [
                    "Enter printer age min: 0 max: 10",
                    "Enter printer temperature min: 22 max: 50",
                    "How it chews paper (Number of chewed papers in hour [0, 30])?",
                    "How it sounds? In dB (min:0 ; max:100)",
                    "Enter speed (Number of printer papers in hour [0, 200])"
]

solutions = [
    "reinstall software",
    "change cable",
    "buy new paper",
    "change cartridge"
]
expert_solution_quest_text = "How difficult for you to change"
expert_solution_questions = []

for q in solutions:
    expert_solution_questions.append(expert_solution_quest_text + " " + q + " after " + q)

print(expert_solution_questions)
for i in range(len(printer_vars)):
    build_labels(printer_text_lbl[i], i, 0, window, printer_vars[i])

get_button = Button(window, text="Get result", command=get_all_values)
get_button.grid(row=6, column=0)
window.mainloop()

