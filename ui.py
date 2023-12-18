import math
from tkinter import *
from expert import *
from alg import *
class UI:
    def __init__(self, params_num, args, args_out):
        self.params = params_num
        self.window = Tk()
        self.window.columnconfigure([0, 1, 2], minsize=100)
        self.window.rowconfigure([x for x in range(20)], minsize=20)
        self.printer_vars_value = []
        self.args = args
        self.args_out = args_out
        self.printer_text_lbl = [
                    "Enter printer age min: 0 max: 10",
                    "Enter printer temperature min: 22 max: 50",
                    "How it chews paper (Number of chewed papers in hour [0, 30])?",
                    "How it sounds? In dB (min:0 ; max:100)",
                    "Enter speed (Number of printer papers in hour [0, 200])"
        ]
        self.solutions = [ "reinstall software", "buy new paper", "change cartridge", "change cable"]
        self.printer_vars = [StringVar() for i in range(self.params)]
        self.graph_vars = [[StringVar() if i != j else None for j in range(len(self.solutions))] for i in range(len(self.solutions))]

        expert_solution_quest_text = "How difficult for you to"

        for i in range(len(self.printer_text_lbl)):
            self.build_labels(self.printer_text_lbl[i], i, 0, self.window, self.printer_vars[i])

        row_count = len(self.printer_text_lbl)
        for i,q in enumerate(self.solutions):
            for j,w in enumerate(self.solutions):
                if q != w:
                    text = expert_solution_quest_text + " " + q + " after " + w + " (0 - 10) "
                    self.build_labels(text, row_count, 0, self.window, self.graph_vars[i][j], True)
                    row_count = row_count + 1
        Button(self.window, text="Get result", command=self.get_all_values).grid(row=row_count, column=0)
        self.end_row = row_count
    def build_labels(self, text, row, column, window, var, grade=False, input=True):
        Label(text=text).grid(row=row, column=column)
        if grade:
            var.set(5)
        if input:
            Entry(window, textvariable=var).grid(row=row, column=column + 1)

    def get_all_values(self):
        self.printer_vars_value = [int(self.printer_vars[i].get()) for i in range(self.params)]
        self.graph = [[self.graph_vars[i][j].get() if i != j else math.inf for j in range(len(self.solutions))] for i in range(len(self.solutions))]
        sols = [x for x in range(len(self.solutions))]
        best_order = ant_colony_optimization(points=sols, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1, graph=self.graph)
        print(best_order)
        Expert = Expert_System(self.args, self.args_out, self.printer_vars_value)
        results = Expert.use_expert_system()
        self.display_results(results, best_order)

    def display_results(self, results, best_order):
        row_count = 1
        for key,x in zip(results, range(len(self.solutions))):
            self.build_labels(self.solutions[best_order[x]], self.end_row + row_count, 0, self.window, None, input=False)
            self.build_labels(results[key], self.end_row + row_count, 1, self.window, None, input=False)
            row_count = row_count + 1
