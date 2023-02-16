from .flashcardslist import FlashCardsList
import customtkinter


class HomePage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, data = None, **kwargs):
        super().__init__(master, **kwargs)

        # configure grid
        self.columnconfigure((0, 1), weight=1)

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text="FlashCards App",
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=32
        )

        # add button 

        self.add_button = customtkinter.CTkButton(
            master=self,
            text="Add a Flashcard",
            font=("TkDefaultFont", 18),
            cursor="hand2",
            command=self.addFlashCard
        )

        self.add_button.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=10 
        )

        # FlashCardsList
        self.flash_card_list = FlashCardsList(
            master=self
        )

        self.flash_card_list.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=16
        )

    def addFlashCard(self):
        from pages import goTo
        goTo("addflashCard")
