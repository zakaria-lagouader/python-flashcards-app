import models.flash_card as f
import pandas as pd
import shortuuid
import csv

class Card:
    def __init__(self, word, translation, id = None, flashcard_id = None):
        self.id = id if id != None else shortuuid.uuid()
        self.word = word
        self.translation = translation
        self.flashcard_id = flashcard_id

    @staticmethod
    def all():
        try:
            df = pd.read_csv('db/cards.csv')
            cards = []
            for _, row in df.iterrows():
                card = Card(
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
        
    @staticmethod
    def find(id):
        try:
            df = pd.read_csv('db/cards.csv')
            card_df = df[df['ID'] == id]
            if card_df.empty:
                print(f'No card found with ID {id}.')
                return None
            card = Card(
                word=card_df.iloc[0]['Word'],
                translation=card_df.iloc[0]['Translation'],
                id=card_df.iloc[0]['ID'],
                flashcard_id=card_df.iloc[0]['Flashcard_ID']
            )
            return card
        except FileNotFoundError:
            print('No card found in the database.')
            return None
        
    @staticmethod
    def count():
        with open('db/cards.csv') as f:
            return sum(1 for _ in f) - 1
        

    def save(self):
        with open('db/cards.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.word, self.translation, self.flashcard_id])

    def update(self, word=None, translation=None):
        try:
            df = pd.read_csv('db/cards.csv')
            card_df = df[df['ID'] == self.id]

            if card_df.empty:
                print(f'No card found with ID {self.id}.')
                return
            if word:
                df.loc[df['ID'] == self.id, 'Word'] = word
            if translation:
                df.loc[df['ID'] == self.id, 'Translation'] = translation

            df.to_csv('db/cards.csv', index=False)

            self.word = word
            self.translation = translation
        except FileNotFoundError:
            print('No cards found in the database.')
        

    def delete(self):
        try:
            df = pd.read_csv('db/cards.csv')
            df = df[df['ID'] != self.id]
            df.to_csv('db/cards.csv', index=False)
        except FileNotFoundError:
            print('No cards found in the database.')

    def flashcard(self):
        try:
            df = pd.read_csv('db/flashcards.csv')
            flashcard_df = df[df['ID'] == self.flashcard_id]
            if flashcard_df.empty:
                print(f'No flashcard found with ID {self.flashcard_id}.')
                return None
            flashcard = f.FlashCard(
                name=flashcard_df.iloc[0]['Name'],
                color=flashcard_df.iloc[0]['Color'],
                id=flashcard_df.iloc[0]['ID'],
            )
            return flashcard
        except FileNotFoundError:
            print('No flashcard found in the database.')
            return None


    def __str__(self) -> str:
        return f"id: {self.id}, word: {self.word}, translation: {self.translation}"
        