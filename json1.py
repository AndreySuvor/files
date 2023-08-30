import csv
import json
from datetime import datetime

result = []
my_dict = {}
with open('exam_results.csv', encoding='utf-8') as file, open('best_scores.json', 'w', encoding='utf-8') as new_file:
    data = csv.DictReader(file)

    for row in data:
        x = tuple((row['email'], row['name'], row['surname']))
        if x not in my_dict:
            my_dict[x] = [int(row['score']), datetime.strptime(row['date_and_time'], '%Y-%m-%d %H:%M:%S')]
        else:
            info = [int(row['score']), datetime.strptime(row['date_and_time'], '%Y-%m-%d %H:%M:%S')]
            if my_dict[x][0] < info[0]:
                my_dict[x] = info
            elif my_dict[x][0] == info[0]:
                if my_dict[x][1] < info[1]:
                    my_dict[x] = info

    for k, v in sorted(my_dict.items()):
        res = {"name" : k[1], "surname": k[2], "best_score" : v[0], "date_and_time": v[1].strftime('%Y-%m-%d %H:%M:%S'), "email": k[0]}
        result.append(res)

    json.dump(result, new_file, indent=3)