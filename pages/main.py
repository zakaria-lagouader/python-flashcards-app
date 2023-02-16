from .home import HomePage
from .flashcard import ShowFlashCard, AddFlashCard, EditFlashCard
from .card import AddCard, ShowCard, EditCard
import customtkinter

customtkinter.set_appearance_mode("system")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Flashcards app")
        self.geometry("500x700")

        # container to stack the pages
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {
            "home": HomePage,
            "showflashCard": ShowFlashCard,
            "addflashCard": AddFlashCard,
            "editflashCard": EditFlashCard,
            "addCard": AddCard,
            "showCard": ShowCard,
            "editCard": EditCard,
        }

        self.goTo("home")

    def goTo(self, page, payload = None):
        # Clear the container
        for widget in self.container.winfo_children():
            widget.destroy()

        F = self.pages[page]

        self.page = F(
            self.container,
            payload
        )

        self.page.grid(
            row=0,
            column=0,
            sticky="nsew",
        )


app = App()

def goTo(page, payload = None):
    global app
    app.goTo(page, payload)