from main import CurrenciesList

if __name__ == '__main__':

    import unittest

    class TestPrecisionFunc(unittest.TestCase):
        def test_result_type(self):
            
            self.assertIsInstance(CurrenciesList(), CurrenciesList)

        def test_is_singleton(self):
            my_cur_list = CurrenciesList('R01020A')
            my_cur_list2 = CurrenciesList('R01035')

            self.assertEqual(id(my_cur_list), id(my_cur_list2))

    unittest.main(verbosity=1) 
