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
    # Length of the returned list must be equal to the length of the MOVIES
    # Returned type must be a list
    # Checking the change in the movie ratings
    def test_penalizer(self):
        # Get a deep copy of the MOVIES list of dictionaries
        copy_l = []
        for li in MOVIES:
            d2 = copy.deepcopy(li)
            copy_l.append(d2)
        # p_list for storing the returned list
        p_list = rating_adj.penalizer(copy_l)
        self.assertEqual(len(p_list), len(MOVIES))
        self.assertEqual(type(p_list), list)
        self.assertEqual(p_list[0]['rating'], 9.2)
        self.assertEqual(p_list[1]['rating'], 8.4)

    # Testing oscar calculator function with two given movies
    # Length of the returned list must be equal to the length of the MOVIES
    # Returned type must be a list
    # Checking the change in the movie ratings
    def test_oscar_calculator(self):
        # Get a deep copy of the MOVIES list of dictionaries
        copy_l = []
        for li in MOVIES:
            d2 = copy.deepcopy(li)
            copy_l.append(d2)
        # o_list for storing the returned list
        o_list = rating_adj.oscar_calculator(copy_l)
        self.assertEqual(len(o_list), len(MOVIES))
        self.assertEqual(type(o_list), list)
        self.assertEqual(o_list[0]['rating'], 9.2)
        self.assertEqual(o_list[1]['rating'], 9.7)

if __name__ == '__main__':
    unittest.main()
