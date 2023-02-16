import customtkinter


class TestCards(customtkinter.CTkFrame):
    def __init__(self, master, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard
        cards = self.flashcard.cards()
        self.current_card = cards[0]


        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")


        # Card Info

        self.progressbar = customtkinter.CTkProgressBar(
            master=self
        )

        self.progressbar.set(0)

        self.progressbar.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew",
        )

        self.card_info_frame = customtkinter.CTkFrame(
            master=self
        )

        self.card_info_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            ipady=8,
            ipadx=8,
            pady=(175, 10), 
            padx=10 
        )

        self.card_info_translation = customtkinter.CTkLabel(
            master=self.card_info_frame,
            text="French:",
            font=("TkDefaultFont", 28),
        )

        self.card_info_translation.pack(
            pady=10
        )

        self.card_info_word = customtkinter.CTkLabel(
            master=self.card_info_frame,
            text=self.current_card.word,
            font=("TkDefaultFont", 40),
        )

        self.card_info_word.pack(
            pady=16
        )

        self.no_button = customtkinter.CTkButton(
            master=self,
            fg_color="#FF0032",
            hover_color="#CD0404",
            text="No"
        )

        self.no_button.grid(
            row=2,
            column=0,
            sticky="ew",
            ipady=8,
            ipadx=8,
            pady=10, 
            padx=10
        )

        self.yes_button = customtkinter.CTkButton(
            master=self,
            text="Yes"
        )

        self.yes_button.grid(
            row=2,
            column=1,
            sticky="ew",
            ipady=8,
            ipadx=8,
            pady=10, 
            padx=10
        )

        self.animate_progress()

    def animate_progress(self, current = 0):
        from pages import app
        next = current + 0.2
        if next >= 1 :
            self.progressbar.set(1)
        else:
            self.progressbar.set(next)
            app.after(1000, self.animate_progress, next)







        




