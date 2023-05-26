import os


class Reader():
    def review(name):
        name = name
        new_value = input("Enter file name:\n").lower()
        updated_value = os.fspath(new_value)
        with open(updated_value, encoding='utf-8') as f:
            read_data = f.read()
            print(read_data)
            f.close

bo = Reader()
carlos = Reader()
ceaser = Reader()
christian = Reader()
michael = Reader()
santiago = Reader()
new = Reader()
new.review()
