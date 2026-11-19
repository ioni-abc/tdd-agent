import unittest




class HotelTestBookRoom(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('peace hotel', {'single': 3, 'double': 2})

    def test_book_room_1(self):
        result = self.hotel.book_room('single', 2, 'guest 1')
        self.assertEqual(result, 'Success!')
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
        self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})

    def test_book_room_2(self):
        result = self.hotel.book_room('triple', 2, 'guest 1')
        self.assertFalse(result)
        self.assertEqual(self.hotel.booked_rooms, {})
        self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 2})

    def test_book_room_3(self):
        self.hotel.book_room('single', 2, 'guest 1')
        result = self.hotel.book_room('single', 2, 'guest 2')
        self.assertEqual(result, 1)
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
        self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})

    def test_book_room_4(self):
        self.hotel.book_room('single', 2, 'guest 1')
        result = self.hotel.book_room('single', 1, 'guest 2')
        self.assertEqual(result, 'Success!')
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2, 'guest 2': 1}})
        self.assertEqual(self.hotel.available_rooms, {'double': 2, 'single': 0})

import unittest

class AgentTest_book_room(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('peace hotel', {'single': 3, 'double': 2})

    def test_book_room_1(self):
        self.assertEqual(self.hotel.book_room('single', 3, 'guest 1'), 'Success!')
        result = self.hotel.book_room('single', 1, 'guest 2')
        self.assertIs(result, False)
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 3}})
        self.assertEqual(self.hotel.available_rooms, {'single': 0, 'double': 2})

    def test_book_room_2(self):
        self.assertEqual(self.hotel.book_room('single', 1, 'guest 1'), 'Success!')
        self.assertEqual(self.hotel.book_room('double', 2, 'guest 2'), 'Success!')
        self.assertEqual(
            self.hotel.booked_rooms,
            {'single': {'guest 1': 1}, 'double': {'guest 2': 2}}
        )
        self.assertEqual(self.hotel.available_rooms, {'single': 2, 'double': 0})

class HotelTestCheckIn(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
        self.hotel.booked_rooms = {'single': {'guest 1': 2}, 'double': {'guest 2': 1}}

    def test_check_in_1(self):
        self.hotel.check_in('single', 1, 'guest 1')
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 1}, 'double': {'guest 2': 1}})

    def test_check_in_2(self):
        self.assertFalse(self.hotel.check_in('single', 3, 'guest 1'))
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

    def test_check_in_3(self):
        self.assertFalse(self.hotel.check_in('double', 1, 'guest 1'))
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

    def test_check_in_4(self):
        self.hotel.check_in('double', 1, 'guest 2')
        self.assertEqual(self.hotel.booked_rooms, {'double': {}, 'single': {'guest 1': 2}})

import unittest

class AgentTest_check_in(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})

    def test_check_in_1(self):
        self.hotel.booked_rooms = {'single': {'guest 1': 2, 'guest 2': 1}}
        self.hotel.check_in('single', 2, 'guest 1')
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 2': 1}})

    def test_check_in_2(self):
        self.hotel.booked_rooms = {'single': {'guest 1': 2, 'guest 2': 1}}
        self.hotel.check_in('single', 1, 'guest 1')
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 1, 'guest 2': 1}})

class HotelTestCheckOut(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
        self.hotel.booked_rooms = {'single': {'guest 1': 2}, 'double': {'guest 2': 1}}

    def test_check_out_1(self):
        self.hotel.check_out('single', 1)
        self.assertEqual(self.hotel.available_rooms, {'single': 4, 'double': 2})
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

    def test_check_out_2(self):
        self.hotel.check_out('single', 3)
        self.assertEqual(self.hotel.available_rooms, {'single': 6, 'double': 2})
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

    def test_check_out_3(self):
        self.hotel.check_out('triple', 2)
        self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 2, 'triple': 2})
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

import unittest

class AgentTest_check_out(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
        self.hotel.booked_rooms = {'single': {'guest 1': 2}, 'double': {'guest 2': 1}}

    def test_check_out_1(self):
        self.hotel.available_rooms = {'single': 0, 'double': 2}
        self.hotel.check_out('single', 2)
        self.assertEqual(self.hotel.available_rooms, {'single': 2, 'double': 2})
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

    def test_check_out_2(self):
        self.hotel.check_out('single', 1)
        self.hotel.check_out('single', 2)
        self.assertEqual(self.hotel.available_rooms, {'single': 6, 'double': 2})
        self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})

class HotelTestAvailableRooms(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2, 'triple': 2})

    def test_get_available_rooms(self):
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 3)

    def test_get_available_rooms_2(self):
        self.hotel.book_room('single', 2, 'guest 1')
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 1)

    def test_get_available_rooms_3(self):
        self.hotel.book_room('single', 3, 'guest 1')
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 0)

import unittest

class AgentTest_get_available_rooms(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('peace hotel', {'single': 5, 'double': 3})

    def test_get_available_rooms_1(self):
        self.hotel.book_room('single', 2, 'guest 1')
        result = self.hotel.get_available_rooms('double')
        self.assertEqual(result, 3)

    def test_get_available_rooms_2(self):
        self.hotel.check_out('single', 2)
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 7)