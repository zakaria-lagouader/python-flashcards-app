import customtkinter


class EditCard(customtkinter.CTkFrame):
    def __init__(self, master, card, **kwargs):
        super().__init__(master, **kwargs)

        self.card = card

        # configure grid
        self.columnconfigure((0, 1), weight=1, uniform="fred")

        # Page Title
        self.page_title = customtkinter.CTkLabel(
            master=self,
            text="Edit Card",
            font=("TkDefaultFont", 32),
        )

        self.page_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=32
        )

        # Form Inputs

        self.word_label = customtkinter.CTkLabel(
            master=self, 
            text="Word :",
        )

        self.word_label.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10 
        )

        self.word_input = customtkinter.CTkEntry(
            master=self, 
            placeholder_text="Word"
        )
        self.word_input.insert(0, self.card.word)

        self.word_input.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=(5, 10), 
            padx=10 
        )

        self.translation_label = customtkinter.CTkLabel(
            master=self, 
            text="Translation :",
        )

        self.translation_label.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w",
            padx=10 
        )

        self.translation_input = customtkinter.CTkEntry(
            master=self, 
            placeholder_text="Translation"
        )

        self.translation_input.insert(0, self.card.translation)

        self.translation_input.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8,
            pady=(5, 10), 
            padx=10 
        )


        self.edit_button = customtkinter.CTkButton(
            master=self, 
            text="Edit Card",
            command=self.editCard
        )

        self.edit_button.grid(
            row=5,
            column=0,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )

        self.cancel_button = customtkinter.CTkButton(
            master=self, 
            text="cancel",
            fg_color="#576F72",
            hover_color="#7D9D9C",
            command=self.cancel
        )

        self.cancel_button.grid(
            row=5,
            column=1,
            sticky="ew",
            ipady=8,
            pady=10, 
            padx=10 
        )


    def editCard(self):
        word = self.word_input.get()
        translation = self.translation_input.get()

        if word != "" and translation != "":
            from pages import goTo
            self.card.update(word, translation)
            goTo("showCard", self.card)

    def cancel(self):
        from pages import goTo
        goTo("showCard", self.card)


