import unittest
import scraper
import rating_adj
import copy

MOVIES = [{'title': 'The Shawshank Redemption', 'rating': 9.2, 'votes': 2552126, 'oscars': 0}, {'title': 'The Godfather', 'rating': 9.2, 'votes': 1756363, 'oscars': 3}]

class TestFunctions(unittest.TestCase):
    # Testing scraper function
    # Length of the returned list must be 20, and type must be list
    def test_scraper(self):
        og_top20 = scraper.scrape()
        self.assertEqual(len(og_top20), 20)
        self.assertEqual(type(og_top20), list)

    # Testing penalizer function with two given movies
    # Length of the list will be 2, and type must be list
    def test_penalizer(self):
        # Get a deep copy of the MOVIES list of dictionaries
        copy_l = []
        for li in MOVIES:
            d2 = copy.deepcopy(li)
            copy_l.append(d2)
        # p_list for storing the returned list
        p_list = rating_adj.penalizer(copy_l)
        self.assertEqual(len(p_list), 2)
        self.assertEqual(type(p_list), list)
        self.assertEqual(p_list[0]['rating'], 9.2)
        self.assertEqual(p_list[1]['rating'], 8.4)


if __name__ == '__main__':
    unittest.main()
