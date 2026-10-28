#1
import csv
def find(book_csv):
    c = 0
    book_csv.seek(0) 
    reader = csv.DictReader(book_csv, delimiter=';')
    for x in reader:
        if len(x['Название']) > 30:
            c += 1
        else: pass
    return c

with open('books.csv') as book_csv:
    print(find(book_csv))