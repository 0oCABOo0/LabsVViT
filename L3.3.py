def write_to_file(filename, content):
    with open(filename, 'a', encoding="UTF-8") as file:
        file.write(content)
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
user_input = input("Введите текст (для написания с новой строки - ничего не пишите):")
write_to_file('user_input.txt', user_input)
print("Текст записан")
add_more = input("Хотите дополнить текст (да/нет): ").strip().lower()
if add_more == 'да':
    additional_input = input("Введите текст для дополнения: ")
    append_to_file('user_input.txt', '\n' + additional_input)
    print("Текст дополнен")
if add_more == 'нет':
    print("Готово")
