from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(
            self
            ) -> None:
        pass

    def run(self):
        # setup root window
        self.root = Tk()

        # configure parameter and variables
        self.root.title("Window Title")
        # self.root.maxsize(960, 540)
        self.answer = StringVar()

        # create frames
        self.mainframe = ttk.Frame(self.root).pack()
        self.top_frame = ttk.Frame(self.mainframe).pack(expand=True, fill=BOTH)
        self.mid_frame = ttk.Frame(self.mainframe).pack(expand=True, fill=BOTH)
        self.bottom_frame = ttk.Frame(self.mainframe).pack(expand=True, fill=BOTH)

        # create Widgets
        self.question_label = ttk.Label(self.top_frame, text="Here question")
        self.answer_entry = ttk.Entry(self.mid_frame, textvariable=self.answer)
        self.next_btn = ttk.Button(self.bottom_frame, text="Next", command=self._check_answer)
        self.start_btn = ttk.Button(self.bottom_frame, text="Start Timer")

        # configure placement of widgets
        self.question_label.pack()
        self.answer_entry.pack()
        self.next_btn.pack(side=LEFT)
        self.start_btn.pack(side=RIGHT)

        # for child in mainframe.winfo_children(): 
        #     child.grid_configure(padx=5, pady=5)
        
        # configure extras
        self.answer_entry.focus()
        self.root.bind("<Return>", self._check_answer)

        # starts mainloop
        self.root.mainloop()

    def _check_answer(self):
        # dummy function -> implemented by CPLUSKORF
        print(self.answer.get())


if __name__ == "__main__":
    test = GUI()
    test.run()

# start btn, next btn . text feld (stattic field at the end)