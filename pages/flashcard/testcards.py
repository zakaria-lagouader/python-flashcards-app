from models import LearnedWords
import customtkinter


class TestCards(customtkinter.CTkFrame):
    def __init__(self, master, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard
        self.cards = self.flashcard.cards()
        self.card_index = 0
        self.current_card = self.cards[self.card_index]


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

        self.card_info_language = customtkinter.CTkLabel(
            master=self.card_info_frame,
            text="Français:",
            font=("TkDefaultFont", 28),
        )

        self.card_info_language.pack(
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
            text="Non",
            command=self.onNoClick
        )

        self.yes_button = customtkinter.CTkButton(
            fg_color="#66bb6a",
            hover_color="#43a047",
            master=self,
            text="Oui",
            command=self.onYesClick
        )

        self.animate_progress()

    def animate_progress(self, current = 0):
        from pages import app
        next = current + 0.2
        if next >= 1 :
            self.progressbar.set(1)
            self.toggle_translation(show=True)
        else:
            self.progressbar.set(next)
            app.after(1000, self.animate_progress, next)

    def next_card(self):
        if self.card_index < len(self.cards) - 1:
            self.card_index += 1
            self.current_card = self.cards[self.card_index]
            self.toggle_translation(show=False)
            self.animate_progress()
        else:
            self.finish()

    def toggle_buttons(self, hide: bool):
        if hide:
            self.yes_button.grid_forget()
            self.no_button.grid_forget()
        else:
            self.no_button.grid(
                row=2,
                column=0,
                sticky="ew",
                ipady=8,
                ipadx=8,
                pady=10, 
                padx=10
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

    def toggle_translation(self, show: bool):
        if show:
            self.card_info_language.configure(text="English:")
            self.card_info_word.configure(text=self.current_card.translation)
            self.toggle_buttons(hide=False)
        else:
            self.card_info_language.configure(text="Français:")
            self.card_info_word.configure(text=self.current_card.word)
            self.toggle_buttons(hide=True)

    def onNoClick(self):
        LearnedWords.add(self.current_card.id, False)
        self.next_card()

    def onYesClick(self):
        LearnedWords.add(self.current_card.id, True)
        self.next_card()

    def finish(self):
        self.card_info_frame.grid_forget()
        self.yes_button.grid_forget()
        self.no_button.grid_forget()

        self.message_label = customtkinter.CTkLabel(
            master=self,
            text="Vous avez Terminé",
            font=("TkDefaultFont", 40),
        )

        self.message_label.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            ipady=8,
            ipadx=8,
            pady=(175, 10), 
            padx=10 
        )

        self.back_button = customtkinter.CTkButton(
            master=self,
            text="Retour",
            command=self.back
        )

        self.back_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew",
            ipady=8,
            ipadx=8,
            pady=10, 
            padx=10 
        )

    def back(self):
        from pages import goTo
        goTo("showflashCard", self.flashcard)


