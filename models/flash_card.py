import models.card as c
import pandas as pd
import shortuuid
import csv

class FlashCard:
    def __init__(self, name, color, id=None):
        self.id = id if id != None else shortuuid.uuid()
        self.name = name
        self.color = color

    @staticmethod
    def all():
        try:
            df = pd.read_csv('db/flashcards.csv')
            flashcards = []
            for _, row in df.iterrows():
                flashcard = FlashCard(
                    name=row['Name'],
                    color=row['Color'],
                    id=row['ID'],
                )
                flashcards.append(flashcard)
            return flashcards
        except FileNotFoundError:
            print('No flashcards found in the database.')
            return []
        
    @staticmethod
    def find(id):
        try:
            df = pd.read_csv('db/flashcards.csv')
            flashcard_df = df[df['ID'] == id]
            if flashcard_df.empty:
                print(f'No flashcard found with ID {id}.')
                return None
            flashcard = FlashCard(
                name=flashcard_df.iloc[0]['Name'],
                color=flashcard_df.iloc[0]['Color'],
                id=flashcard_df.iloc[0]['ID'],
            )
            return flashcard
        except FileNotFoundError:
            print('No flashcard found in the database.')
            return None
        
    @staticmethod
    def count():
        with open('db/flashcards.csv') as f:
            return sum(1 for _ in f) - 1
        
    def save(self):
        with open('db/flashcards.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.name, self.color])

    def update(self, name=None, color=None):
        try:
            df = pd.read_csv('db/flashcards.csv')
            flashcard_df = df[df['ID'] == self.id]

            if flashcard_df.empty:
                print(f'No flashcard found with ID {self.id}.')
                return
            if name:
                df.loc[df['ID'] == self.id, 'Name'] = name
            if color:
                df.loc[df['ID'] == self.id, 'Color'] = color

            df.to_csv('db/flashcards.csv', index=False)

            self.name = name
            self.color = color
        except FileNotFoundError:
            print('No flashcard found in the database.')

    def delete(self):
        try:
            df = pd.read_csv('db/flashcards.csv')
            df = df[df['ID'] != self.id]
            df.to_csv('db/flashcards.csv', index=False)

            # delete related cards
            cards_df = pd.read_csv('db/cards.csv')
            cards_df = cards_df[cards_df['Flashcard_ID'] != self.id]
            cards_df.to_csv('db/cards.csv', index=False)
            
        except FileNotFoundError:
            print('No flashcards found in the database.')
            

    def cards(self):
        try:
            df = pd.read_csv('db/cards.csv')
            df = df[df['Flashcard_ID'] == self.id]
            if df.empty:
                print(f'No card found with Flashcard_ID {self.id}.')
                return None
            cards = []
            for _, row in df.iterrows():
                card = c.Card(
                    word=row['Word'],
                    translation=row['Translation'],
                    id=row['ID'],
                    flashcard_id=row['Flashcard_ID']
                )
                cards.append(card)
            return cards
        except FileNotFoundError:
            print('No cards found in the database.')
            return []

    def create_card(self, word, translation):
        card = c.Card(word, translation, flashcard_id=self.id)
        card.save()
        return card

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, color: {self.color}"