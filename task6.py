#6
import csv

def popular(book_csv):
    book_csv.seek(0)  
    reader = csv.DictReader(book_csv, delimiter=';')
    pop = {}
    for x in reader:
        name = x['Название']
        pop[name] = pop.get(name, 0) + int(x['Кол-во выдач'])  
    return dict(sorted(pop.items(), key=lambda x: x[1], reverse=True)[:20])

with open('books.csv') as book_csv:
    for i, j in popular(book_csv).items():
        print(f'{i}' + ' - ' + f'{j}')