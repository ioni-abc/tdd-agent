import unittest


import unittest

class AgentTest_book_room(unittest.TestCase):

    def test_book_room_1(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertEqual(hotel.book_room('single', 1, 'guest 1'), 'Success!')

    def test_book_room_2(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 1, 'guest 1')
        self.assertEqual(hotel.book_room('single', 5, 'guest 1'), 4)
        self.assertEqual(hotel.get_available_rooms('single'), 4)

    def test_book_room_3(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 1, 'guest 1')
        self.assertEqual(hotel.book_room('single', 4, 'guest 1'), 'Success!')
        self.assertEqual(hotel.book_room('single', 1, 'guest 1'), False)

    def test_book_room_4(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertEqual(hotel.book_room('triple', 1, 'guest 1'), False)

    def test_book_room_5(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 2, 'guest 1')
        self.assertEqual(hotel.get_available_rooms('single'), 3)
        self.assertEqual(hotel.booked_rooms['single']['guest 1'], 2)

import unittest

class AgentTest_check_in(unittest.TestCase):

    def test_check_in_1(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 1, 'guest 1')
        self.assertIsNone(hotel.check_in('single', 1, 'guest 1'))
        self.assertEqual(hotel.booked_rooms, {'single': {}})

    def test_check_in_2(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 1, 'guest 1')
        self.assertEqual(hotel.check_in('single', 2, 'guest 1'), False)
        self.assertEqual(hotel.booked_rooms['single']['guest 1'], 1)

    def test_check_in_3(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 1, 'guest 1')
        self.assertEqual(hotel.check_in('triple', 1, 'guest 1'), False)
        self.assertEqual(hotel.booked_rooms['single']['guest 1'], 1)

    def test_check_in_4(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 3, 'guest 1')
        hotel.check_in('single', 1, 'guest 1')
        self.assertEqual(hotel.booked_rooms['single']['guest 1'], 2)

    def test_check_in_5(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertEqual(hotel.check_in('single', 1, 'guest 1'), False)

import unittest

class AgentTest_check_out(unittest.TestCase):

    def test_check_out_1(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.check_out('single', 2)
        self.assertEqual(hotel.available_rooms['single'], 7)

    def test_check_out_2(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.check_out('single', 2)
        self.assertEqual(hotel.available_rooms, {'single': 7, 'double': 3})

    def test_check_out_3(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.check_out('triple', 2)
        self.assertEqual(hotel.available_rooms, {'single': 5, 'double': 3, 'triple': 2})

    def test_check_out_4(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertIsNone(hotel.check_out('single', 2))

    def test_check_out_5(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 3, 'guest 1')
        self.assertEqual(hotel.get_available_rooms('single'), 2)
        hotel.check_out('single', 3)
        self.assertEqual(hotel.get_available_rooms('single'), 5)

import unittest

class AgentTest_get_available_rooms(unittest.TestCase):

    def test_get_available_rooms_1(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertEqual(hotel.get_available_rooms('single'), 5)

    def test_get_available_rooms_2(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertEqual(hotel.get_available_rooms('double'), 3)

    def test_get_available_rooms_3(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        self.assertIsInstance(hotel.get_available_rooms('single'), int)

    def test_get_available_rooms_4(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.book_room('single', 2, 'guest 1')
        self.assertEqual(hotel.get_available_rooms('single'), 3)
        self.assertEqual(hotel.get_available_rooms('double'), 3)

    def test_get_available_rooms_5(self):
        hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        hotel.check_out('single', 2)
        self.assertEqual(hotel.get_available_rooms('single'), 7)
        hotel.check_out('triple', 2)
        self.assertEqual(hotel.get_available_rooms('triple'), 2)