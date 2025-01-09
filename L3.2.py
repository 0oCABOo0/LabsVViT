def read_file(filename, method='all'):
    with open(filename, 'r') as file:
        if method == 'all':
            content = file.read()
            print(content)
        if method == 'line':
            for line in file:
                print(line)
read_file( "example.txt", "all")

