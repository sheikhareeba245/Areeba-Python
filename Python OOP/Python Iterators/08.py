class BookShelf:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

# Taking input from user
books = []
while True:
    user_input = input("Enter the book you want to add to your Digital Book Shelf (or type 'Done' to finish): ")
    if user_input.lower() == "done":
        break
    books.append(user_input)

# Create bookshelf and display
shelf = BookShelf(books)
print("\nBooks in your Digital Book Shelf:")
for book in shelf:
    print(f"- {book}")
