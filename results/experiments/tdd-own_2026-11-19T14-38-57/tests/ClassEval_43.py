import unittest


import unittest

class AgentTest_add_employee(unittest.TestCase):

    def test_add_employee_1(self):
        hr = HRManagementSystem()
        self.assertTrue(hr.add_employee(1, 'John', 'Manager', 'Sales', 100000))

    def test_add_employee_2(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertFalse(hr.add_employee(1, 'John', 'Manager', 'Sales', 100000))

    def test_add_employee_3(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertFalse(hr.add_employee(1, 'Alice', 'Engineer', 'IT', 80000))

    def test_add_employee_4(self):
        hr = HRManagementSystem()
        self.assertTrue(hr.add_employee(1, 'John', 'Manager', 'Sales', 100000))
        self.assertTrue(hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000))
        self.assertTrue(hr.add_employee(3, 'Bob', 'Analyst', 'Finance', 60000))

    def test_add_employee_5(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertIn(1, hr.employees)
        self.assertEqual(
            hr.employees[1],
            {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )

import unittest

class AgentTest_remove_employee(unittest.TestCase):

    def test_remove_employee_1(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertTrue(hr.remove_employee(1))

    def test_remove_employee_2(self):
        hr = HRManagementSystem()
        self.assertFalse(hr.remove_employee(1))

    def test_remove_employee_3(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.remove_employee(1)
        self.assertNotIn(1, hr.employees)

    def test_remove_employee_4(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertTrue(hr.remove_employee(1))
        self.assertFalse(hr.remove_employee(1))

    def test_remove_employee_5(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000)
        hr.add_employee(3, 'Bob', 'Analyst', 'Finance', 60000)
        self.assertTrue(hr.remove_employee(2))
        self.assertNotIn(2, hr.employees)
        self.assertIn(1, hr.employees)
        self.assertIn(3, hr.employees)
        self.assertEqual(
            hr.employees[3],
            {'name': 'Bob', 'position': 'Analyst', 'department': 'Finance', 'salary': 60000}
        )

import unittest

class AgentTest_get_employee(unittest.TestCase):

    def test_get_employee_1(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        self.assertEqual(
            hr.get_employee(1),
            {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )

    def test_get_employee_2(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        self.assertIs(hr.get_employee(2), False)

    def test_get_employee_3(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertEqual(
            hr.get_employee(1),
            {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )

    def test_get_employee_4(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.remove_employee(1)
        self.assertIs(hr.get_employee(1), False)

    def test_get_employee_5(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000)
        hr.add_employee(3, 'Bob', 'Analyst', 'Finance', 60000)
        self.assertEqual(
            hr.get_employee(2),
            {'name': 'Alice', 'position': 'Engineer', 'department': 'IT', 'salary': 80000}
        )
        self.assertEqual(
            hr.get_employee(3),
            {'name': 'Bob', 'position': 'Analyst', 'department': 'Finance', 'salary': 60000}
        )

import unittest

class AgentTest_update_employee(unittest.TestCase):

    def test_update_employee_1(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        self.assertTrue(
            hr.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        )

    def test_update_employee_2(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        self.assertIs(
            hr.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000}),
            False
        )
        self.assertNotIn(2, hr.employees)

    def test_update_employee_3(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        hr.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        self.assertEqual(
            hr.get_employee(1),
            {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000}
        )

    def test_update_employee_4(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        self.assertTrue(
            hr.update_employee(1, {'name': 'Johnny', 'position': 'Director', 'department': 'Marketing', 'salary': 120000})
        )
        self.assertEqual(
            hr.employees[1],
            {'name': 'Johnny', 'position': 'Director', 'department': 'Marketing', 'salary': 120000}
        )

    def test_update_employee_5(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000)
        hr.add_employee(3, 'Bob', 'Analyst', 'Finance', 60000)
        self.assertTrue(
            hr.update_employee(2, {'name': 'Alice', 'position': 'Senior Engineer', 'department': 'IT', 'salary': 95000})
        )
        self.assertEqual(
            hr.get_employee(2),
            {'name': 'Alice', 'position': 'Senior Engineer', 'department': 'IT', 'salary': 95000}
        )
        self.assertEqual(
            hr.get_employee(1),
            {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )
        self.assertEqual(
            hr.get_employee(3),
            {'name': 'Bob', 'position': 'Analyst', 'department': 'Finance', 'salary': 60000}
        )

import unittest

class AgentTest_list_employees(unittest.TestCase):

    def test_list_employees_1(self):
        hr = HRManagementSystem()
        hr.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        self.assertEqual(
            hr.list_employees(),
            {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        )

    def test_list_employees_2(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        result = hr.list_employees()
        self.assertIn(1, result)
        self.assertEqual(
            result[1],
            {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )

    def test_list_employees_3(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000)
        hr.add_employee(3, 'Bob', 'Analyst', 'Finance', 60000)
        result = hr.list_employees()
        self.assertEqual(len(result), 3)
        self.assertEqual(
            result[1],
            {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        )
        self.assertEqual(
            result[2],
            {'employee_ID': 2, 'name': 'Alice', 'position': 'Engineer', 'department': 'IT', 'salary': 80000}
        )
        self.assertEqual(
            result[3],
            {'employee_ID': 3, 'name': 'Bob', 'position': 'Analyst', 'department': 'Finance', 'salary': 60000}
        )

    def test_list_employees_4(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.add_employee(2, 'Alice', 'Engineer', 'IT', 80000)
        hr.remove_employee(1)
        result = hr.list_employees()
        self.assertNotIn(1, result)
        self.assertIn(2, result)
        self.assertEqual(
            result[2],
            {'employee_ID': 2, 'name': 'Alice', 'position': 'Engineer', 'department': 'IT', 'salary': 80000}
        )

    def test_list_employees_5(self):
        hr = HRManagementSystem()
        hr.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        hr.update_employee(1, {'name': 'Johnny', 'position': 'Director', 'department': 'Marketing', 'salary': 120000})
        self.assertEqual(
            hr.list_employees()[1],
            {'employee_ID': 1, 'name': 'Johnny', 'position': 'Director', 'department': 'Marketing', 'salary': 120000}
        )