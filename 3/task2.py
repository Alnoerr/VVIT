def write_to_file(text, mode):
    with open('user_input.txt', mode, encoding='UTF-8') as file:
        file.write(text)


# write_to_file("Строка текста", "w")
# write_to_file("Ещё больше текста", "w")

write_to_file("\nОчень много текста", "a")
write_to_file("\nТри строки", "a")
