from .home import HomePage, ShowStats
from .flashcard import ShowFlashCard, AddFlashCard, EditFlashCard, TestCards
from .card import AddCard, ShowCard, EditCard
import customtkinter

customtkinter.set_appearance_mode("system")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window Title and Geometry
        self.title("Flashcards app")
        self.geometry("500x700")

        # Container to stack the pages
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # List of all the pages
        self.pages = {
            "home": HomePage,
            "showStats": ShowStats,
            "showflashCard": ShowFlashCard,
            "addflashCard": AddFlashCard,
            "editflashCard": EditFlashCard,
            "testCards": TestCards,
            "addCard": AddCard,
            "showCard": ShowCard,
            "editCard": EditCard,
        }

        self.goTo("home")

    def goTo(self, page, payload = None):
        # Clear the container
        for widget in self.container.winfo_children():
            widget.destroy()

        # Get page by name
        Page = self.pages[page]

        # Render the page
        self.current_page = Page(
            self.container,
            payload
        )

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew",
        )


# Exports
app = App()

def goTo(page, payload = None):
    global app
    app.goTo(page, payload)