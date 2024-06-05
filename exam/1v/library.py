
from colorama import Fore
from utils import PrintGREEN, PrintRED, PrintYELLOW
from author import Author
from publication import Publication


class Library:
    def __init__(self):
        self.mAuthors = dict()
        self.mPublications = dict()

    def AddAuthor(self, nameAuthor):
        if len(self.mAuthors) == 0:
            idAuthor = 0
        else:
            idAuthor = max(self.mAuthors.keys()) + 1
        newAuthor = Author(idAuthor, nameAuthor)
        self.mAuthors[idAuthor] = newAuthor
        PrintGREEN("Author " + nameAuthor + " successfully added")

    def AddPublication(self, title, idAuthorsList, linksToOtherPublicationsList, keywords):
        if len(self.mPublications) == 0:
            idPublication = 0
        else:
            idPublication = max(self.mPublications.keys()) + 1

        if idAuthorsList and len(self.mAuthors) < max(idAuthorsList):
            PrintRED("Error: Author with id " + str(max(idAuthorsList)) + " does not exist")
            PrintYELLOW("Publication not created, please try again")
            return
        if linksToOtherPublicationsList and len(self.mPublications) < max(linksToOtherPublicationsList):
            PrintRED("Error: A link to a non-existent post has been added")
            PrintYELLOW("Publication not created, please try again")
            return

        newPublication = Publication(idPublication, title, idAuthorsList, linksToOtherPublicationsList, keywords)
        self.mPublications[idPublication] = newPublication
        PrintGREEN("Publication " + title + " successfully added")

    def PrintAllAuthors(self):
        PrintGREEN("All Authors: ")
        for idAuthor in self.mAuthors:
            self.mAuthors[idAuthor].PrintAuthor()

    def PrintAllPublications(self):
        PrintGREEN("All Publications: ")
        for idPublication in self.mPublications:
            self.mPublications[idPublication].PrintPublication()

    def PrintLinksToOtherPublications(self, idPublication):
        if idPublication not in self.mPublications:
            PrintRED("Error: publication " + str(idPublication) + " not found, please try again")
            return

        PrintGREEN("Links To Other Publications in publication: " + str(idPublication))
        for id in self.mPublications[idPublication].linksToOtherPublications:
            self.mPublications[id].PrintPublication()

    def KeywordSearch(self, listOfKeywords):
        PrintGREEN("KeywordSearch: " + str(listOfKeywords))
        for idPublication in self.mPublications:
            if any(keyword in self.mPublications[idPublication].keywords for keyword in listOfKeywords):
                self.mPublications[idPublication].PrintPublication()
                self.mPublications[idPublication].IncreaseRating()

    def SearchByAuthors(self, idAuthorsList):
        PrintGREEN("SearchByAuthors id = : " + str(idAuthorsList))
        for idPublication in self.mPublications:
            if any(author in self.mPublications[idPublication].idAuthors for author in idAuthorsList):
                self.mPublications[idPublication].PrintPublication()
                self.mPublications[idPublication].IncreaseRating()

    def GetSortedPublicationsByRelevance(self):
        sorted_publications = sorted(self.mPublications.values(), key=lambda pub: pub.rating, reverse=True)
        PrintGREEN("Publications sorted by relevance:")
        for pub in sorted_publications:
            pub.PrintPublication()


