from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(self) -> None:
        pass
    

    def run(self):
        root = Tk()
        root.title("Are you awake?")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.answer = StringVar()
        self.answer_entry = ttk.Entry(mainframe, width=7, textvariable=self.answer)
        self.answer_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Button(mainframe, text="Next", command=self._check_answer).grid(column=3, row=3, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
        self.answer_entry.focus()
        root.bind("<Return>", self._check_answer)

        root.mainloop()

    def _check_answer(self):
        # dummy function -> implemented by CPLUSKORF
        print(self.user_input.get())


if __name__ == "__main__":
    test = GUI()
    test.run()

