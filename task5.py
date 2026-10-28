#5
import csv

def tags(book_csv):
    book_csv.seek(0)   
    reader = csv.DictReader(book_csv, delimiter=';')
    t = set()   
    for x in reader:
        for tag in x['Жанр книги'].split('#'):   
            if tag.strip() != '':   
                t.add(tag.strip())   
    return t   

with open('books.csv') as book_csv:
    for i in tags(book_csv):
        print(i)