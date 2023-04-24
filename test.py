import unittest
from main import ROI_Estimator


def test_make_instance(self):
    self.assertEqual(ROI_Estimator.main_menu('brandon').name, 'brandon')


def test_isupper(self):
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
