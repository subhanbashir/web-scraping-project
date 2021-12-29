import unittest
import web_scr_local as ijc

class Test(unittest.TestCase):
    def test_counter_valid(self):
        test_url = "http://localhost/it_indeed_test.html"
        actual_val = 15
        expected_val = ijc.counter(test_url)
        self.assertEqual(actual_val, expected_val)
    def test_counter_invalid(self):
        test_url = "http://localhost/it_indeed_test.html"
        actual_val = 12
        expected_val = ijc.counter(test_url)
        self.assertNotEqual(actual_val, expected_val)  
    def test_multiple_urls(self):
        test_url = "http://localhost/it_indeed_test.html"
        actual_val = ['https://de.indeed.comhttps://de.indeed.com/jobs?q=IT&l=deutschland&start=10', 'https://de.indeed.comhttps://de.indeed.com/jobs?q=IT&l=deutschland&start=20', 'https://de.indeed.comhttps://de.indeed.com/jobs?q=IT&l=deutschland&start=30', 'https://de.indeed.comhttps://de.indeed.com/jobs?q=IT&l=deutschland&start=40', 'https://de.indeed.comhttps://de.indeed.com/jobs?q=IT&l=deutschland&start=10']
        expected_val = ijc.multiple_url(test_url)
        self.assertNotEqual(actual_val, expected_val)      


if __name__ == '__main__':
    unittest.main()