def read_file(filename, method='all'):
   try:
    with open(filename, 'r') as file:
        if method == 'all':
            content = file.read()
            print(content)
        if method == 'line':
            for line in file:
                print(line)
   except FileNotFoundError:
       print(f"Файл '{filename} не обнаружен.")
read_file( "examp.txt", "all")
