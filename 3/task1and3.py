def read_file(is_line_reading):
    try:
        with open('example.txt', 'r', encoding='UTF-8') as file:
            if is_line_reading:
                for line in file:
                    print(line, end='')
            else:
                content = file.read()
                print(content)
    except FileNotFoundError:
        print("Файл example.txt не найден")


read_file(is_line_reading=False)
print()
read_file(is_line_reading=True)
