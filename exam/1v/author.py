from colorama import Fore
from utils import PrintYELLOW

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def PrintAuthor(self):
        PrintYELLOW("  Author id: " + str(self.id) + ", name: " + self.name)