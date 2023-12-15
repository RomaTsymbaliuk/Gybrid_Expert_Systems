
from fuzzy_system import *
from ui import *
from alg import *

printer_age_interval = [0, 10]
printer_chew_interval = [0, 30]
printer_speed_interval = [0, 200]
printer_sound_interval = [30, 100]
printer_temperature_interval = [22, 50]
class Expert_System:
    def __init__(self, args):
        self.args = args
        self.FS = None
    def create_expert_system(self):
        self.FS = fuzzy_rules_and_system_create()

    def use_expert_system(self):
        results = use_fuzzy_system(self.FS, self.args)
        self.results = results
        print(results)


win = UI(5)
Expert = Expert_System(win.printer_vars_value)
Expert.create_expert_system()
Expert.use_expert_system()
win.window.mainloop()

