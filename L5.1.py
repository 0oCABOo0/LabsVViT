class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

my_book = Book("Судьба человека","Михаил Александрович Шолохов", 1956)

print(my_book.get_info())