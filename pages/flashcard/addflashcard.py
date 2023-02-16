from tkinter.colorchooser import askcolor
from models import FlashCard
import customtkinter


class AddFlashCard(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)

        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text="Add flashCard",
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=32
        )

        # Form Inputs

        self.name_label = customtkinter.CTkLabel(
            master=self, 
            text="Name :",
        )

        self.name_label.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10 
        )

        self.name_input = customtkinter.CTkEntry(
            master=self, 
            placeholder_text="Name"
        )

        self.name_input.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=(5, 10), 
            padx=10 
        )

        self.color_input = customtkinter.CTkButton(
            master=self, 
            text="Choose Color",
            fg_color="black",
            hover="black",
            command=self.shooseColor
        )

        self.color_input.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        self.add_button = customtkinter.CTkButton(
            master=self, 
            text="Add Flashcard",
            command=self.addFlashcard
        )

        self.add_button.grid(
            row=4,
            column=0,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        self.cancel_button = customtkinter.CTkButton(
            master=self, 
            text="cancel",
            fg_color="#576F72",
            hover_color="#7D9D9C",
            command=self.cancel
        )

        self.cancel_button.grid(
            row=4,
            column=1,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

    def shooseColor(self):
        colors = askcolor(
            title="Choose flashcard color", 
            initialcolor=self.color_input.cget("fg_color")
        )
        if colors[1] != None:
            self.color_input.configure(fg_color=colors[1], hover_color=colors[1])

    def addFlashcard(self):
        name = self.name_input.get()
        color = self.color_input.cget("fg_color")

        if name != "" and color != "":
            from pages import goTo
            flashcard = FlashCard(name, color)
            flashcard.save()
            goTo("showflashCard", flashcard)

    def cancel(self):
        from pages import goTo
        goTo("home")



