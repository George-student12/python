
class User:

    def __init__(self, name="Егор", family="Морозов"):
        print("меня зовут")
        self.first_name = name
        self.last_name = family

    def Name(self):
        print(self.first_name)

    def Family(self):
        print(self.last_name)

    def Name_and_Family(self):
        print("Меня зовут", self.first_name, self.last_name)
