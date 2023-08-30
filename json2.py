import json

my_dict = {}
my_dict_name = {}

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    for c in data:
        my_dict[c['District']] = my_dict.get(c['District'], 0) + 1
        if c['IsNetObject'] == 'да':
            my_dict_name[c['OperatingCompany']] = my_dict_name.get(c['OperatingCompany'], 0) + 1
    count_area = max(my_dict.items(), key=lambda x: x[1])
    count_name = max(my_dict_name.items(), key=lambda x: x[1])
    print(f'{count_area[0]}: {count_area[1]}')
    print(f'{count_name[0]}: {count_name[1]}')