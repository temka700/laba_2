#3
import csv
import random

def references(book_csv):
    book_csv.seek(0)  
    reader = csv.DictReader(book_csv, delimiter=';')
    a = list(reader)              
    chose = random.sample(a, 20)  
    res = []
    for x in chose:
        year = x['Дата поступления'][6:10] 
        res.append(f"{x['Автор']}. {x['Название']} - {year}")
    return res

with open('books.csv') as book_csv:
    res = references(book_csv)

with open('task3.txt', 'w', encoding='utf-8') as output:
    for i in range(len(res)):
        if 0<i<9: n = 2
        else: n = 1
        output.write(f'{i+1}' + f'{n*' '}'  + f'{res[i]}' + '\n')