from colorama import Fore
from utils import PrintYELLOW

class Publication:
    def __init__(self, id, title, idAuthors, linksToOtherPublications, keywords):
        self.id = id
        self.title = title
        self.idAuthors = idAuthors
        self.linksToOtherPublications = linksToOtherPublications
        self.keywords = keywords
        self.rating = 0

    def PrintPublication(self):
        PrintYELLOW(
            "  Publication id: " + str(self.id) + ", title: " + self.title +
            ", idAuthors: " + str(self.idAuthors) + ", linksToOtherPublications: " + str(self.linksToOtherPublications))

    def IncreaseRating(self):
        self.rating += 1