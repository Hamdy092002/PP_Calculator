#############################################################################
#
#
#
#
#
#
#
#
#################################################################################
import tkinter as tk

LARGE_FONT_STYLE = ("Ariel", 40, "bold")
SMALL_FONT_STYLE = ("Ariel", 16)
DIGITS_FONT_STYLE = ("Ariel", 24)
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.total_label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            3: (3, 1), 2: (3, 2), 1: (3, 3),
            ".": (4,1), 0: (4, 2)
        }
        self.button_frame = self.create_buttons_frame()
        self.create_digits_buttons()
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                                     bg=LIGHT_GRAY, fg=LABEL_COLOR, padx =24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                                     bg=LIGHT_GRAY, fg=LABEL_COLOR, padx =24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_digits_buttons(self):
        for digits, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digits), bg=WHITE, fg =LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    Calc = Calculator()
    Calc.run()