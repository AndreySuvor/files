from zipfile import ZipFile

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for c in info:
        Flag = True
        if not c.is_dir():
            size = convert_bytes(c.file_size)
            Flag = False

        c = c.filename
        if c[-1] == '/':
            c = c[:-1]
        amount = c.count('/') * '  '
        if Flag:
            print(f'{amount}{c.split("/")[-1]}')
        else:
            print(f'{amount}{c.split("/")[-1]} {size}')