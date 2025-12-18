# 在这里编写代码
class Book:
    def __init__(self, idx, title, author, isbn):
        self.id = idx
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def status(self):
        return "可借阅" if not self.is_borrowed else "已借阅"


class User:
    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.borrowed_books = []

    def show_borrowed(self):
        if self.borrowed_books:
            print(f"\n{self.name}（卡号{self.card_id}）已借书籍：")
            for book in self.borrowed_books:
                print(f"- {book.title}（ISBN：{book.isbn}）")
        else:
            print(f"\n{self.name}（卡号{self.card_id}）暂无借阅书籍")


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book.id] = book
        print(f"已添加书籍：{book.title}（ISBN：{book.isbn}）")

    def add_user(self, user):
        self.users[user.card_id] = user
        print(f"已注册用户：{user.name}（卡号：{user.card_id}）")

    def check_availability(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            status = book.status()
            print(f"书籍《{book.title}》状态：{status}")
            return not book.is_borrowed
        else:
            print("未找到该书籍")
            return False

    def borrow_book(self, user_card, book_id):
        if user_card not in self.users:
            print("未找到该用户")
            return
        if book_id not in self.books:
            print("未找到该书籍")
            return
        
        user = self.users[user_card]
        book = self.books[book_id]

        if book.borrow():
            user.borrowed_books.append(book)
            print(f"用户{user.name}成功借阅《{book.title}》")
        else:
            print(f"《{book.title}》当前无法借阅")

    def return_book(self, user_card, book_id):
        if user_card not in self.users:
            print("未找到该用户")
            return
        if book_id not in self.books:
            print("未找到该书籍")
            return
        
        user = self.users[user_card]
        book = self.books[book_id]

        if book in user.borrowed_books and book.return_book():
            user.borrowed_books.remove(book)
            print(f"用户{user.name}成功归还《{book.title}》")
        else:
            print(f"无法归还《{book.title}》（未借阅或状态异常）")

    def list_books(self):
        print("\n=== 馆藏书籍列表 ===")
        for book in self.books.values():
            print(f"ID:{book.id:4} | 书名:{book.title:20} | 作者:{book.author:15} | ISBN:{book.isbn:15} | 状态:{book.status():10}")


if __name__ == "__main__":
    lib = Library()

    book1 = Book(1, "Python编程", "埃里克·马瑟斯", "9787115428028")
    book2 = Book(2, "算法图解", "Aditya Bhargava", "9787115447630")
    lib.add_book(book1)
    lib.add_book(book2)

    user1 = User("张三", "U001")
    user2 = User("李四", "U002")
    lib.add_user(user1)
    lib.add_user(user2)

    lib.check_availability(1)

    lib.borrow_book("U001", 1)
    lib.borrow_book("U002", 1)

    user1.show_borrowed()

    lib.return_book("U001", 1)

    lib.list_books()
