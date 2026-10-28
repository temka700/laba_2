#2
import csv
def find(book_csv, aufter):
    c = 0
    book_csv.seek(0)
    reader = csv.DictReader(book_csv, delimiter=';')
    res = []
    for x in reader:
        if aufter in x['Автор']:
            res.append(x)   
        else: pass
    return res

with open('books.csv') as book_csv:
    aufter = input('название автора (ИФ) с заглавной буквы: ')
    print(find(book_csv, aufter))