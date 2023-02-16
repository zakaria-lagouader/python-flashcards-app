from tkinter.messagebox import askyesno
import customtkinter


class ShowFlashCard(customtkinter.CTkFrame):
    def __init__(self, master, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard

        # configure grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="fred")

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text=self.flashcard.name,
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            pady=32
        )

        self.edit_button = customtkinter.CTkButton(
            master=self, 
            text="Edit FlashCard",
            fg_color="#439A97",
            hover_color="#62B6B7",
            command=self.editFlashCard
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
            text="Delete FlashCard",
            fg_color="#FF0032",
            hover_color="#CD0404",
            command=self.deleteFlashCard
        )

        self.delete_button.grid(
            row=1,
            column=1,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        self.add_button = customtkinter.CTkButton(
            master=self, 
            text="Add a Card",
            command=self.addCard
        )

        self.add_button.grid(
            row=1,
            column=2,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        cards = self.flashcard.cards()

        if cards != None:
            self.cards_list = CardsList(
                master=self,
                cards=cards
            )

            self.cards_list.grid(
                row=2,
                column=0,
                columnspan=3,
                sticky="ew",
                pady=16
            )

        self.back_button = customtkinter.CTkButton(
            master=self, 
            text="Back to Home Page",
            command=self.backHome
        )

        self.back_button.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

    def addCard(self):
        from pages import goTo
        goTo("addCard", self.flashcard)


    def deleteFlashCard(self):
        answer = askyesno(
            title='confirmation',
            message='Are you sure that you want to delete this?'
        )

        if answer:
            from pages import goTo
            self.flashcard.delete()
            goTo("home")

    def editFlashCard(self):
        from pages import goTo
        goTo("editflashCard", self.flashcard)

    def backHome(self):
        from pages import goTo
        goTo("home")



class CardsList(customtkinter.CTkFrame):
    def __init__(self, master, cards, **kwargs):
        super().__init__(master, **kwargs)

        self.cards = cards

        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        self.configure(
            fg_color="transparent"
        )

        i = 2
        j = 2

        for card in cards:
            f = CardsListItem(
                master=self,
                card=card
            )

            f.grid(
                row=j, 
                column=(i % 2), 
                sticky="nsew", 
                padx=5, 
                pady=5, 
                ipadx=5, 
                ipady=5
            )

            i += 1
            j += 1 if i % 2 == 0 else 0


class CardsListItem(customtkinter.CTkFrame):
    def __init__(self, master, card, **kwargs):
        super().__init__(master, **kwargs)

        self.card = card

        # configure grid
        self.columnconfigure((0, 1), weight=1)

        self.configure(
            cursor="hand2", 
        )

        # Card title
        self.word = customtkinter.CTkLabel(
            master=self, 
            text=self.card.word, 
            font=("TkDefaultFont", 20)
        )

        self.word.grid(
            row=0, 
            column=0, 
            columnspan=2, 
            ipady=16, 
            ipadx=16 ,
            sticky="w"
        )


        self.translation = customtkinter.CTkLabel(
            master=self, 
            text=card.translation, 
            font=("TkDefaultFont", 16)
        )
        
        self.translation.grid(
            row=2,
            column=0,
            ipady=2,
            ipadx=16,
            sticky="w"
        )

        self.bind("<Button-1>", self.showCard)

    def showCard(self, event):
        from pages import goTo
        goTo("showCard", self.card)

