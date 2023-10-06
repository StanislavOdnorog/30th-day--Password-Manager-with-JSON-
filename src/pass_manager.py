import re
from tkinter import messagebox

import pyperclip

from core.pass_gen import PassGen
from db.pass_manager import PassDBManager
from obj.my_objects import *


class PassManager:
    def __init__(self, title="Program", padding=50, bg="white"):
        self.window = Tk()
        self.window.resizable(False, False)

        self.window.title(title)
        self.window.config(padx=padding, pady=padding)
        self.window.config(bg=bg)
        self.canvas = MyCanvas()
        self.lock_img = PhotoImage(file="./media/lock.png")
        self.canvas.create_image(150, 150, image=self.lock_img)
        self.objects = {}

    def configure_objects(self):
        self.set_object("LockImage", self.canvas, 1, 0, 1)
        self.set_object("WebText", MyLabel(text="Website:"), 0, 1, 1)
        self.set_object("EmailText", MyLabel(text="Email/Username:"), 0, 2, 1)
        self.set_object("PassText", MyLabel(text="Password:"), 0, 3, 1)
        self.set_object("WebEntry", Entry(width=49), 1, 1, 1)
        self.set_object("EmailEntry", Entry(width=70), 1, 2, 2)
        self.set_object("PassEntry", Entry(width=49), 1, 3, 1)
        self.set_object("SearchButton", MyButton("Search", 16), 2, 1, 1)
        self.set_object("GetPassButton", MyButton("Generate Password", 16), 2, 3, 1)
        self.set_object("AddButton", MyButton("Add", 60), 1, 4, 2)
        self.set_object("DeleteButton", MyButton("Delete", 60), 1, 5, 2)

        self.objects["SearchButton"]["elem"].config(command=self.show_pass)
        self.objects["AddButton"]["elem"].config(command=self.save_pass)
        self.objects["GetPassButton"]["elem"].config(command=self.generate_pass)
        self.objects["DeleteButton"]["elem"].config(command=self.delete_pass)

    def set_object(self, index, elem, col, row, colspan):
        self.objects[index] = {"elem": elem, "col": col, "row": row, "colspan": colspan}

    def are_entries_valid(
        self, website, email="IS_NOT_NEEDED", password="IS_NOT_NEEDED"
    ):
        if email != "IS_NOT_NEEDED" and not re.fullmatch(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email
        ):
            messagebox.showerror(title="Error", message="Email Validation Failed")
        elif not website:
            messagebox.showerror(title="Error", message="Website is Empty")
        elif password != "IS_NOT_NEEDED" and not password:
            messagebox.showerror(title="Error", message="Password is Empty")
        else:
            return True

    def save_pass(self):
        email = self.objects["EmailEntry"]["elem"].get()
        website = self.objects["WebEntry"]["elem"].get()
        password = self.objects["PassEntry"]["elem"].get()

        if self.are_entries_valid(website, email, password) != None:
            PassDBManager.save_pass(website=website, email=email, password=password)
            pyperclip.copy(password)
            self.objects["WebEntry"]["elem"].delete(0, END)
            self.objects["PassEntry"]["elem"].delete(0, END)

    def delete_pass(self):
        website = self.objects["WebEntry"]["elem"].get()

        if self.are_entries_valid(website) != None:
            if PassDBManager.get_pass(website) != (None, None):
                is_ok = messagebox.askokcancel(
                    title=website,
                    message=f"The password exist.\nDo you want delete it?",
                )
                if is_ok:
                    PassDBManager.delete_pass(website)
                    messagebox.showinfo(
                        title=website,
                        message=f"The password has been deleted.",
                    )
            else:
                messagebox.showinfo(
                    title=website,
                    message=f"The password doesn't exist.",
                )

    def show_pass(self):
        website = self.objects["WebEntry"]["elem"].get()

        if self.are_entries_valid(website) != None:
            user_email, user_password = PassDBManager.get_pass(website)
            if user_password != None:
                pyperclip.copy(user_password)
                messagebox.showinfo(
                    title=website,
                    message=f"The password exists:\nEmail: {user_email}\nPassword: {user_password}",
                )
            else:
                messagebox.showinfo(
                    title=website,
                    message=f"The password doesn't exist.",
                )

    def generate_pass(self):
        password = PassGen.generate_pass()
        pyperclip.copy(password)
        self.objects["PassEntry"]["elem"].delete(0, END)
        self.objects["PassEntry"]["elem"].insert(0, password)

    def start_loop(self):
        for _, v in self.objects.items():
            v["elem"].grid(column=v["col"], row=v["row"], columnspan=v["colspan"])

        self.objects["WebEntry"]["elem"].focus()
        self.objects["EmailEntry"]["elem"].insert(0, "isodnorog@gmail.com")
        self.window.mainloop()
