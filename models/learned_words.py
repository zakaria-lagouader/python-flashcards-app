from datetime import date
import pandas as pd
import csv

class LearnedWords:
    
    @staticmethod
    def add(card_id, learned):
        with open('db/learned_words.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([card_id, learned, date.today()])

    @staticmethod
    def get_correct():
        df = pd.read_csv('db/learned_words.csv')
        return df[df["Correct"] == True].to_dict('records')
    
    @staticmethod
    def get_incorrect():
        df = pd.read_csv('db/learned_words.csv')
        return df[df["Correct"] == False].to_dict('records')
    
    @staticmethod
    def plot_words(plt):
        # Create a list of dates and a list of number of words learned each day
        df = pd.read_csv('db/learned_words.csv')
        # correct_words = df[df["Correct"] == True]

        # Convert the 'date' column to a datetime object
        df['Date'] = pd.to_datetime(df['Date'])

        # Group the DataFrame by date and count the number of words learned on each day
        words_learned = df.groupby('Date')['Card_ID'].count().reset_index(name='num_words')

        # Create a bar chart
        plt.bar(words_learned['Date'], words_learned['num_words'])

        # Create a line plot
        # plt.plot(words_learned['Date'], words_learned['num_words'])

        plt.locator_params(axis="y", integer=True, tight=True)

        # Add labels and title
        plt.set_xlabel('Date')
        plt.set_ylabel('Nombre de mots appris')
        plt.set_title('Mots appris chaque jour')