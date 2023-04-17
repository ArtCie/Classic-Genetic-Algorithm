from tkinter import *
from tkinter import ttk, messagebox
from algorithm.cross_binary.cross_binary import CrossTypes
from algorithm.mutation.mutation import MutationTypes
from algorithm.selection.selection import SelectionTypes
from algorithm.inversion.inversion import Inversion
from algorithm.genetic_algorithm_calculator import GeneticAlgorithmCalculator
import time

class InterfaceMain:
    def __init__(self):
        self.root = Tk()

    def draw(self):
        self._init_root()
        self._draw_title()
        self._draw_user_input()
        self._draw_options()
        self.root.mainloop()

    def _init_root(self):
        self.root.geometry("800x650")
        self.root.title("Genetic Algorithm")

    def _draw_title(self):
        title = StringVar()
        label = Label(self.root, textvariable=title)
        title.set("Genetic algorithm for finding max/min in eggholder function")
        label.pack(padx=5, pady=20)


    def _draw_user_input(self):
        self.range_a = self._create_input(text="Begin of the range - a", x=25, y=50)
        self.range_b = self._create_input(text="End of the range - b", x=425, y=50)
        self.population_size = self._create_input(text="Population size", x=25, y=120)
        self.number_of_bits = self._create_input(text="Number of bits", x=425, y=120)
        self.epochs_number = self._create_input(text="Epochs amount", x=25, y=190)
        self.best_and_tournament_chromosome_amount = self._create_input(text="Best and tournament chromosome amount",
                                                                        x=425, y=190)
        self.elite_strategy_amount = self._create_input(text="Elite Strategy amount", x=25, y=260)
        self.cross_probability = self._create_input(text="Cross probability", x=425, y=260)
        self.mutation_probability = self._create_input(text="Mutation probability", x=25, y=330)
        self.inversion_probability = self._create_input(text="Inversion probability", x=425, y=330)

        self.pixel = PhotoImage(width=1, height=1)
        search_button = Button(self.root, text="Search", image=self.pixel, width=340, height=60,
                               command=self.process_algorithm, compound="center", state = NORMAL)
        search_button.place(x=225, y=550)

    def _create_input(self, text, x, y):
        function_frame = LabelFrame(self.root, text=text, width=340, height=60)
        function_frame.place(x=x, y=y)
        entry = Entry(self.root, width=30, textvariable=StringVar())
        entry.place(x=x + 15, y=y + 20)
        return entry

    def _draw_options(self):
        self.selection_method = self._generate_combobox(label_text="Choose selection method", label_x=25,
                                                        label_y=400,
                                                        values=SelectionTypes.get_names())

        self.cross_method = self._generate_combobox(label_text="Choose cross_binary method", label_x=425,
                                                    label_y=400,
                                                    values=CrossTypes.get_names())

        self.mutation_method = self._generate_combobox(label_text="Choose mutation method", label_x=25,
                                                       label_y=470,
                                                       values=MutationTypes.get_names())
        self.is_max = self._generate_checkbutton()

    def _generate_combobox(self, label_text, label_x, label_y, values):
        function_frame = LabelFrame(self.root, text=label_text, width=340, height=60)
        function_frame.place(x=label_x, y=label_y)
        combobox_field = ttk.Combobox(self.root, values=values, state="readonly")
        combobox_field.current(0)
        combobox_field.place(x=label_x+15, y=label_y+20)
        return combobox_field

    def _generate_checkbutton(self):
        var = IntVar()
        function_frame = LabelFrame(self.root, text="Minimanization", width=340, height=60)
        function_frame.place(x=425, y=470)
        Checkbutton(self.root, text='Is minimized?', variable=var).place(x=440, y=490)
        return var
    
    def display_time(self,time):
        elapsed_time = time
        time_label = Label(self.root, text=f"time needed: {elapsed_time:.2f} seconds")
        time_label.place(x=50, y=600)

    def process_algorithm(self):
        try:
            genetic_algorithm_calculator = GeneticAlgorithmCalculator(
                range_a=float(self.range_a.get()),
                range_b=float(self.range_b.get()),
                population_size=int(self.population_size.get()),
                number_of_bits=int(self.number_of_bits.get()),
                epoch_number=int(self.epochs_number.get()),
                best_and_tournament_chromosome_amount=int(self.best_and_tournament_chromosome_amount.get()),
                elite_strategy_amount=int(self.elite_strategy_amount.get()),
                cross_probability=float(self.cross_probability.get()),
                mutation_probability=float(self.mutation_probability.get()),
                inversion_probability=float(self.inversion_probability.get()),
                selection_method=self.selection_method.current(),
                cross_method=self.cross_method.current(),
                mutation_method=self.mutation_method.current(),
                is_max=self.is_max.get()
            )
            result = genetic_algorithm_calculator.run()
            time_needed = genetic_algorithm_calculator.elapsed_time
            self.display_time(time_needed)
        except Exception as e:
            messagebox.showwarning("Error!", str(e))
