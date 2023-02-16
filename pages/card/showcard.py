from tkinter.messagebox import askyesno
import customtkinter


class ShowCard(customtkinter.CTkFrame):
    def __init__(self, master, card, **kwargs):
        super().__init__(master, **kwargs)

        self.card = card

        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text="Card details",
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=32
        )

        self.edit_button = customtkinter.CTkButton(
            master=self, 
            text="Edit Card",
            fg_color="#439A97",
            hover_color="#62B6B7",
            command=self.editCard
        )

        self.edit_button.grid(
            row=1,
            column=0,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        self.delete_button = customtkinter.CTkButton(
            master=self, 
            text="Delete Card",
            fg_color="#FF0032",
            hover_color="#CD0404",
            command=self.deleteCard
        )

        self.delete_button.grid(
            row=1,
            column=1,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        # Card Info

        self.card_info_frame = customtkinter.CTkFrame(
            master=self
        )

        self.card_info_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew",
            ipady=8,
            ipadx=8,
            pady=10, 
            padx=10 
        )

        self.card_info_word = customtkinter.CTkLabel(
            master=self.card_info_frame,
            text=self.card.word,
            font=("TkDefaultFont", 40),
        )

        self.card_info_word.pack(
            pady=16
        )

        self.card_info_translation = customtkinter.CTkLabel(
            master=self.card_info_frame,
            text=self.card.translation,
            font=("TkDefaultFont", 28),
        )

        self.card_info_translation.pack(
            pady=10
        )

        self.back_button = customtkinter.CTkButton(
            master=self, 
            text="Back to Home Page",
            command=self.backHome
        )

        self.back_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

    def deleteCard(self):
        answer = askyesno(
            title='confirmation',
            message='Are you sure that you want to delete this?'
        )

        if answer:
            from pages import goTo
            self.card.delete()
            goTo("home")

    def editCard(self):
        from pages import goTo
        goTo("editCard", self.card)

    def backHome(self):
        from pages import goTo
        goTo("home")




        




