import datetime


class PermanentTasks:
    def __init__(self, name, quantity, frequency, exp, virtual_coins, described):
        self.name = name
        self.frequency = frequency
        self.quantity = quantity
        self.exp = exp
        self.virtual_coins = virtual_coins
        self.dat = datetime.datetime.now().date()
        self.done = False
        self.described = described

    def did(self):
        self.done = True

    def edit(self, **kwargs):
        for i, j in kwargs:
            if i == "name":
                self.name = j
            elif i == "frequency":
                self.frequency = j
            elif i == "exp":
                self.exp = j
            elif i == "virtual_coins":
                self.virtual_coins = j
            elif i == "described":
                self.described = j


class OneTimeTasks:
    def __init__(self, name, exp, virtual_coins, term, described):
        self.name = name
        self.exp = exp
        self.virtual_coins = virtual_coins
        self.dat = datetime.datetime.now().date()
        self.done = False
        self.term = term
        self.described = described

    def did(self):
        self.done = True

    def edit(self, **kwargs):
        for i, j in kwargs:
            if i == "name":
                self.name = j
            elif i == "term":
                self.term = j
            elif i == "exp":
                self.exp = j
            elif i == "virtual_coins":
                self.virtual_coins = j
            elif i == "described":
                self.described = j


class Homework:
    def __init__(self, name, exp, virtual_coins, term, lesson, task):
        self.name = name
        self.exp = exp
        self.virtual_coins = virtual_coins
        self.dat = datetime.datetime.now().date()
        self.done = False
        self.term = term
        self.lesson = lesson
        self.task = task

    def did(self):
        self.done = True

    def edit(self, **kwargs):
        for i, j in kwargs:
            if i == "name":
                self.name = j
            elif i == "term":
                self.term = j
            elif i == "exp":
                self.exp = j
            elif i == "virtual_coins":
                self.virtual_coins = j
            elif i == "described":
                self.described = j
            elif i == "lesson":
                self.lesson = j
            elif i == "task":
                self.task = j


class Ideas:
    def __init__(self, name, exp, virtual_coins, described):
        self.name = name
        self.exp = exp
        self.virtual_coins = virtual_coins
        self.dat = datetime.datetime.now().date()
        self.done = False
        self.described = described

    def did(self):
        self.done = True

    def edit(self, **kwargs):
        for i, j in kwargs:
            if i == "name":
                self.name = j
            elif i == "exp":
                self.exp = j
            elif i == "virtual_coins":
                self.virtual_coins = j
            elif i == "described":
                self.described = j


class Rules:
    def __init__(self, name, exp, virtual_coins, described):
        self.name = name
        self.exp = exp
        self.virtual_coins = virtual_coins
        self.dat = datetime.datetime.now().date()
        self.described = described
        self.violated = 0

    def edit(self, **kwargs):
        for i, j in kwargs:
            if i == "name":
                self.name = j
            elif i == "exp":
                self.exp = j
            elif i == "virtual_coins":
                self.virtual_coins = j
            elif i == "described":
                self.described = j
