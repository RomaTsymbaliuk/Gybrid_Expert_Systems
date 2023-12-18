
from fuzzy_system import *
from ui import *
from alg import *

printer_age_interval = [0, 10]
printer_chew_interval = [0, 30]
printer_speed_interval = [0, 200]
printer_sound_interval = [30, 100]
printer_temperature_interval = [22, 50]


args = ["Age", "Temperature", "Chewing", "Sound", "Speed"]
args_out = ["Paper_Mis_Defects", "Cartridge_Defects", "Software_Defects", "Cabel_Defects"]
win = UI(len(args), args, args_out)
win.window.mainloop()

