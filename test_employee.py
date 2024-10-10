import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def  tearDownClass(cls):
        print('tearDownClass')
    
    def setUp(self):
        self.emp_1 = Employee('Araceli', 'Rojas', 50000)
        self.emp_2 = Employee('Kevin', 'Bort', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        #print('test_email')
        self.assertEqual(self.emp_1.email, 'Araceli.Rojas@gmail.com')
        self.assertEqual(self.emp_2.email, 'Kevin.Bort@gmail.com')

        self.emp_1.first = 'Daniela'
        self.emp_2.first = 'Alexis'

        self.assertEqual(self.emp_1.email, 'Daniela.Rojas@gmail.com')
        self.assertEqual(self.emp_2.email, 'Alexis.Bort@gmail.com')

    def test_fullname(self):
        #print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Araceli Rojas')
        self.assertEqual(self.emp_2.fullname, 'Kevin Bort')

        self.emp_1.first = 'Daniela'
        self.emp_2.first = 'Alexis'

        self.assertEqual(self.emp_1.fullname, 'Daniela Rojas')
        self.assertEqual(self.emp_2.fullname, 'Alexis Bort')

    def test_apply_raise(self):
        #print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            #test good response from website
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Rojas/May')
            self.assertEqual(schedule, 'success')
            
            #test bad response from website
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Bort/June')
            self.assertEqual(schedule, 'Bad response!')

if __name__ == '__main__':
    unittest.main()