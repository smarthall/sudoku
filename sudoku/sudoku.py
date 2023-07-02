import tkinter as tk
from tkinter import StringVar, font as tkFont

class Sudoku(object):
    def __init__(self, representation=None) -> None:
        self._data = [None for i in range(9 * 9)]

        if representation is not None:
            if len(representation) != 81:
                raise Exception(f'Expected length of 81, got {len(representation)}')

            for i in range(9 * 9):
                self._data[i] = representation[i]

    def _index(self, x, y):
        return (x * 9) + y
    
    def _coords(self, index):
        return ((index / 9), (index % 9))

    def __getitem__(self, key) -> str:
        x, y = key
        return self._data[self._index(x, y)]
    
    def __setitem__(self, key, value) -> None:
        x, y = key
        self._data[self._index(x, y)] = value

    def __str__(self) -> str:
        return ''.join(self._data)

class SudokuWindow(object):
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.font = tkFont.Font(family="sans", size=22)
        self.labels = {}

        # Loop over frames
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(
                    master=self.window,
                    relief=tk.RAISED,
                    borderwidth=2
                )
                frame.grid(row=i, column=j)

                # Loop over items in frames
                for k in range(3):
                    for l in range(3):
                        lframe = tk.Frame(
                            master=frame,
                            relief=tk.GROOVE,
                            borderwidth=1
                        )
                        lframe.grid(row=k, column=l)

                        text = StringVar()
                        label = tk.Label(master=lframe, textvariable=text, font=self.font, width=2, height=1)
                        label.pack()

                        x = (i * 3) + k
                        y = (j * 3) + l

                        self.labels[(x, y)] = text

    def show(self, sudoku):
        for x in range(9):
            for y in range(9):
                val = sudoku[x, y]
                label = self.labels[(x, y)]
                
                if val in '123456789':
                    label.set(val)
                else:
                    label.set('')

    def wait(self):
        self.window.mainloop()
