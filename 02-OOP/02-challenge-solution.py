class Person:
    def __init__(self, user_name):
        self.user_name = user_name

    def talk(self):
        print(f'hi i"m {self.user_name}')


nizar = Person("nizar")
nizar.talk()
