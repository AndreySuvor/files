def control_sum(a, b):
    with open(a, 'rb') as file:
        obj = pickle.load(file)
    if isinstance(obj, list):
        obj = list(filter(lambda x: isinstance(x, int), obj))
        total = 0 if len(obj) == 0 else max(obj) * min(obj)
        print('Контрольные суммы совпадают' if total == int(b) else 'Контрольные суммы не совпадают')
    else:
        total = sum([key for key in obj if isinstance(key, int)])
        print('Контрольные суммы совпадают' if total == int(b) else 'Контрольные суммы не совпадают')

control_sum(input(), input())