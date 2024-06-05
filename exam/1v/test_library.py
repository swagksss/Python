import unittest
from author import Author
from publication import Publication
from library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_author(self):
        self.library.AddAuthor("Test Author")
        self.assertEqual(len(self.library.mAuthors), 1)
        self.assertEqual(self.library.mAuthors[0].name, "Test Author")

    def test_add_publication(self):
        self.library.AddAuthor("Author 1")
        self.library.AddAuthor("Author 2")
        self.library.AddPublication("Test Publication", [0, 1], [], ["keyword1", "keyword2"])
        self.assertEqual(len(self.library.mPublications), 1)
        self.assertEqual(self.library.mPublications[0].title, "Test Publication")
        self.assertEqual(self.library.mPublications[0].idAuthors, [0, 1])
        self.assertEqual(self.library.mPublications[0].keywords, ["keyword1", "keyword2"])

    def test_print_all_authors(self):
        self.library.AddAuthor("Author 1")
        self.library.AddAuthor("Author 2")
        self.library.AddAuthor("Author 3")
        self.library.PrintAllAuthors()

    def test_print_all_publications(self):
        self.library.AddAuthor("Author 1")
        self.library.AddPublication("Publication 1", [0], [], ["keyword1"])
        self.library.AddPublication("Publication 2", [0], [0], ["keyword2"])
        self.library.PrintAllPublications()

    def test_print_links_to_other_publications(self):
        self.library.AddAuthor("Author 1")
        self.library.AddPublication("Publication 1", [0], [], ["keyword1"])
        self.library.AddPublication("Publication 2", [0], [0], ["keyword2"])
        self.library.PrintLinksToOtherPublications(1)

    def test_keyword_search(self):
        self.library.AddAuthor("Author 1")
        self.library.AddPublication("Publication 1", [0], [], ["keyword1"])
        self.library.AddPublication("Publication 2", [0], [0], ["keyword2"])
        self.library.KeywordSearch(["keyword1"])

    def test_search_by_authors(self):
        self.library.AddAuthor("Author 1")
        self.library.AddAuthor("Author 2")
        self.library.AddPublication("Publication 1", [0], [], ["keyword1"])
        self.library.AddPublication("Publication 2", [1], [], ["keyword2"])
        self.library.SearchByAuthors([1])

    def test_get_sorted_publications_by_relevance(self):
        self.library.AddAuthor("Author 1")
        self.library.AddPublication("Publication 1", [0], [], ["keyword1"])
        self.library.AddPublication("Publication 2", [0], [0], ["keyword2"])
        self.library.KeywordSearch(["keyword1"])
        self.library.GetSortedPublicationsByRelevance()

if __name__ == '__main__':
    unittest.main()
