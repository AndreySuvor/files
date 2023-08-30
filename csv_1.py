#Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин,
#в котором он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных магазинах.
#В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:

#Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
#Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
#Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
#...

#Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается,
#в следующем формате: <название продукта>: <название магазина>

#Если имеется несколько самых дешевых товаров, то следует вывести тот товар,
#чье название меньше в лексикографическом сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене,
#то следует вывести тот магазин, чье название меньше в лексикографическом сравнении.

#Примечание 1. Разделителем в файле prices.csv является точка с запятой, при этом кавычки не используются.

import csv

with open('prices.csv', encoding='utf-8') as file:
    result = []
    my_dict = {}
    rows = csv.DictReader(file, delimiter=';')

    for r in rows:
        x = r["Магазин"]
        del r['Магазин']
        cheap = min(r.items(), key=lambda x: int(x[1]))
        my_dict[x] = cheap
    min_price = int(min(my_dict.items(), key=lambda x: int(x[1][1]))[1][1])

    for k, v in my_dict.items():
        if int(v[1]) == min_price:
            result.append((k, v[0]))
    result = sorted(result, key=lambda x: (x[1], x[0]))
    res = result[0]
    print(f'{res[1]}: {res[0]}')