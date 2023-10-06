from tkinter import *

from constants import *


class MyLabel(Label):
    def __init__(self, bg="white", pady=5, **kwargs):
        super().__init__(background=bg, pady=pady, **kwargs)


class MyButton(Button):
    def __init__(self, text, width, bg="white", **kwargs):
        super().__init__(background=bg, text=text, width=width, **kwargs)


class MyCanvas(Canvas):
    def __init__(
        self, width=WIDTH, height=HEIGHT, bg="white", highlightthickness=0, **kwargs
    ):
        super().__init__(
            width=width,
            height=height,
            background=bg,
            highlightthickness=highlightthickness,
            **kwargs,
        )
