#Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
#В первом столбце указана единица, если пассажир выжил, и ноль в противном случае,
#во втором столбце записано полное имя пассажира, в третьем — пол, в четвертом — возраст:

#survived;name;sex;age
#0;Mr. Owen Harris Braund;male;22
#1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
#...

#Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет,
#каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола,
#а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

#Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.

import csv

with open('titanic.csv', encoding='utf-8') as file:
    titanic = list(csv.reader(file, delimiter=';'))
    del titanic[0]
    titanic = sorted(titanic, key=lambda x: x[2], reverse=True)

    for surv, name, sex, age in titanic:
        if float(age) < 18 and int(surv) == 1:
            print(name)