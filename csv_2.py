#Вам доступен файл student_counts.csv,
#который содержит данные о количестве учеников в некотором учебном заведении за период 2000 — 2021 г.
#В первом столбце записан год, в последующих столбцах записан класс и количество учеников в данном классе в этом году:

#year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
#2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
#2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
#...

#Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv,
#располагая все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

#Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:
#<номер класса>-<буква класса>

import csv

with open('student_counts.csv', encoding='utf-8') as file, open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as new:

    result = csv.DictReader(file)
    x = result.fieldnames
    result = list(result)
    year = x[0]
    del x[0]
    names = [i.split('-') for i in x]
    names = sorted(names, key=lambda x: (int(x[0]), x[1]))
    names= ['-'.join(i) for i in names]
    names.insert(0, year)
    writer = csv.DictWriter(new, fieldnames=names)
    writer.writeheader()
    writer.writerows(result)