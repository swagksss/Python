from library import Library

if __name__ == '__main__':
    library = Library()

    library.AddAuthor("name1")
    library.AddAuthor("name2")
    library.AddAuthor("name3")
    library.AddAuthor("name4")

    library.AddPublication("publication1", [0, 2], [], ["keyword1", "keyword2"])
    library.AddPublication("publication2", [0, 4], [1], ["keyword3", "keyword4"])
    library.AddPublication("publication3", [2], [], ["keyword1", "keyword4"])
    library.AddPublication("publication4", [3], [1, 2, 3], ["keyword3", "keyword2"])
    library.AddPublication("publication5", [], [1, 2, 3, 4, 5], ["keyword5", "keyword2"])
    library.AddPublication("publication5", [1, 2], [1, 2, 3, 4], ["keyword1"])
    library.AddPublication("publication6", [], [1, 2, 3, 4, 5], ["keyword6", "keyword7"])

    library.PrintAllAuthors()
    library.PrintAllPublications()

    library.PrintLinksToOtherPublications(1)
    library.PrintLinksToOtherPublications(18)
    library.PrintLinksToOtherPublications(5)

    library.SearchByAuthors([2])
    library.KeywordSearch(["keyword1"])
    library.KeywordSearch(["keyword3"])

    library.GetSortedPublicationsByRelevance()