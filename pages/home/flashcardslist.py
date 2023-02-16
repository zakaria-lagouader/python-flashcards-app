from .flashcardlistitem import FlashCardsListItem
from models import FlashCard
import customtkinter


class FlashCardsList(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        self.configure(
            fg_color="transparent"
        )

        # Get all FlashCards
        flashcards = FlashCard.all()

        i = 2
        j = 2

        for flashcard in flashcards:
            f = FlashCardsListItem(
                master=self,
                flashcard=flashcard
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
