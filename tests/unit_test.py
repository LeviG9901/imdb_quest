import unittest
import scraper
import rating_adj


class TestFunctions(unittest.TestCase):
    # Testing scraper function
    # Length of the returned list must be 20, and type must be list
    def test_scraper(self):
        og_top20 = scraper.scrape()
        self.assertEqual(len(og_top20), 20)
        self.assertEqual(type(og_top20), list)


if __name__ == '__main__':
    unittest.main()
