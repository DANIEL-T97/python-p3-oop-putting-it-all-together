class Book:
    pass
    def _init_(self, title, page_count:int):
        assert page_count , "page_count must be an integer"

        self.title = title
        self.page_count = page_count
    def turn_page(self):
        return "Flipping the page...wow,you read fast!"

my_book= Book("fathers of nations", 20)

print(my_book.title)
print(my_book.page_count)
print(my_book.turn_page())