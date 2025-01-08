class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")


if __name__ == '__main__':
    book = Book("1984", "Джордж Оруэлл", 1949)
    book.get_info()