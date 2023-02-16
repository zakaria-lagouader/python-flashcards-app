import customtkinter


class FlashCardsListItem(customtkinter.CTkFrame):
    def __init__(self, master, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard

        # configure grid
        self.columnconfigure((0, 1), weight=1)

        # dynamic flashcard color
        self.configure(
            fg_color=self.flashcard.color, 
            bg_color="transparent",
            cursor="hand2", 
        )

        # flashcard title
        self.title = customtkinter.CTkLabel(
            master=self, 
            text=self.flashcard.name, 
            font=("TkDefaultFont", 20)
        )

        self.title.grid(
            row=0, 
            column=0, 
            columnspan=2, 
            pady=(0, 20), 
            ipady=16, 
            ipadx=16 ,
            sticky="w"
        )

        # cards count
        cards = self.flashcard.cards()
        cards_count = len(cards) if cards != None else 0

        self.count = customtkinter.CTkLabel(
            master=self, 
            text=f"{cards_count} cards", 
            font=("TkDefaultFont", 16)
        )
        
        self.count.grid(
            row=2,
            column=0,
            ipady=2,
            ipadx=16,
            sticky="w"
        )

        self.bind("<Button-1>", self.showFlashCard)

    def showFlashCard(self, event):
        from pages import goTo
        goTo("showflashCard", self.flashcard)