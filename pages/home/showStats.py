from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from models import LearnedWords
import customtkinter


class ShowStats(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)


        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text="Your Stats",
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=32
        )

        # Figure
        self.fig = Figure(
            figsize = (5, 5),
            dpi = 100
        )

  
        # adding the subplot
        self.plot = self.fig.add_subplot(111)


        # Plot words
        LearnedWords.plot_words(self.plot)
        
        # For fixing date display
        self.fig.autofmt_xdate()

        self.canvas = FigureCanvasTkAgg(
            figure=self.fig,
            master=self
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=10, 
            padx=10 
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


    def backHome(self):
        from pages import goTo
        goTo("home")




        




