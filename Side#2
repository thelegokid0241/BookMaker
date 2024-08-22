import csv
from Questions.Book import Book
from Login import *
class User():

    def __init__(self,book_file):
        self.book_list = []#this user has a list of books
        self.book_file = book_file#and a file where they are stored
        self.num_count = 1
    def add_book(self,book):
        self.book_list.append(book)
        book.number=self.num_count
        self.num_count = self.num_count+1


    def load_books(self):
        try:
            with open(self.book_file,'r') as f:

                reader = csv.DictReader(f)
                for row in reader:
                    self.add_book(Book(row['title'],row['insides'], row['number'], ))
        except FileNotFoundError:
            pass

    def save_books(self):
        with open(self.book_file, 'w') as csvfile:
            fieldnames = ['title', 'insides', 'number']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.book_list:
                writer.writerow(book.__dict__)
acc=accounts
