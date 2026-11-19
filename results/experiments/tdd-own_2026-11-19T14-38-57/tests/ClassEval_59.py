import unittest


import unittest

from datetime import datetime

import numpy as np

class AgentTest_add_movie(unittest.TestCase):

    def test_add_movie_1(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(len(system.movies), 1)
        movie = system.movies[0]
        self.assertEqual(movie['name'], 'Batman')
        self.assertEqual(movie['price'], 49.9)
        self.assertEqual(movie['start_time'], datetime(1900, 1, 1, 17, 5))
        self.assertEqual(movie['end_time'], datetime(1900, 1, 1, 19, 25))
        self.assertTrue(np.array_equal(movie['seats'], np.zeros((3, 3))))

    def test_add_movie_2(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.add_movie('Superman', 39.5, '20:00', '22:10', 2)
        self.assertEqual(len(system.movies), 2)
        self.assertEqual(system.movies[0]['name'], 'Batman')
        self.assertEqual(system.movies[1]['name'], 'Superman')
        self.assertEqual(system.movies[1]['price'], 39.5)
        self.assertEqual(system.movies[1]['start_time'], datetime(1900, 1, 1, 20, 0))
        self.assertEqual(system.movies[1]['end_time'], datetime(1900, 1, 1, 22, 10))

    def test_add_movie_3(self):
        system = MovieBookingSystem()
        system.add_movie('Matrix', 10.0, '09:30', '11:45', 4)
        seats = system.movies[0]['seats']
        self.assertEqual(seats.shape, (4, 4))
        self.assertTrue(np.all(seats == 0))
        self.assertEqual(seats.dtype, np.float64)

    def test_add_movie_4(self):
        system = MovieBookingSystem()
        system.add_movie('Short', 5.0, '08:00', '08:30', 1)
        seats = system.movies[0]['seats']
        self.assertEqual(seats.shape, (1, 1))
        self.assertTrue(np.array_equal(seats, np.array([[0.]])))

    def test_add_movie_5(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.add_movie('Batman', 30.0, '21:00', '23:00', 2)
        self.assertEqual(len(system.movies), 2)
        self.assertEqual(system.movies[0]['price'], 49.9)
        self.assertEqual(system.movies[1]['price'], 30.0)
        self.assertEqual(system.movies[1]['start_time'], datetime(1900, 1, 1, 21, 0))
        self.assertEqual(system.movies[1]['end_time'], datetime(1900, 1, 1, 23, 0))
        self.assertEqual(system.movies[1]['seats'].shape, (2, 2))

import numpy as np

class AgentTest_book_ticket(unittest.TestCase):

    def test_book_ticket_1(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        result = system.book_ticket('Batman', [(0, 0), (0, 1)])
        self.assertEqual(result, 'Booking success.')

    def test_book_ticket_2(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.book_ticket('Batman', [(0, 0), (0, 1)])
        result = system.book_ticket('Batman', [(0, 0)])
        self.assertEqual(result, 'Booking failed.')

    def test_book_ticket_3(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(system.book_ticket('Superman', [(0, 0)]), 'Movie not found.')
        self.assertEqual(system.book_ticket('batman', [(0, 0)]), 'Movie not found.')

    def test_book_ticket_4(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        result = system.book_ticket('Batman', [(0, 0), (0, 1)])
        self.assertEqual(result, 'Booking success.')
        seats = system.movies[0]['seats']
        self.assertNotEqual(seats[0, 0], 0)
        self.assertNotEqual(seats[0, 1], 0)
        self.assertEqual(seats[0, 2], 0)
        self.assertEqual(seats[1, 0], 0)
        self.assertEqual(seats[2, 2], 0)

    def test_book_ticket_5(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.book_ticket('Batman', [(0, 0)])
        seats_before = system.movies[0]['seats'].copy()
        result = system.book_ticket('Batman', [(1, 1), (0, 0)])
        self.assertEqual(result, 'Booking failed.')
        self.assertTrue(np.array_equal(system.movies[0]['seats'], seats_before))
        self.assertEqual(system.movies[0]['seats'][1, 1], 0)

import unittest

from datetime import datetime

import numpy as np

class AgentTest_available_movies(unittest.TestCase):

    def test_available_movies_1(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(system.available_movies('12:00', '22:00'), ['Batman'])

    def test_available_movies_2(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(system.available_movies('08:00', '10:00'), [])

    def test_available_movies_3(self):
        system = MovieBookingSystem()
        self.assertEqual(system.available_movies('12:00', '22:00'), [])

    def test_available_movies_4(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.add_movie('Superman', 39.5, '20:00', '22:10', 2)
        system.add_movie('Matrix', 10.0, '09:30', '11:45', 4)
        result = system.available_movies('12:00', '23:00')
        self.assertEqual(result, ['Batman', 'Superman'])
        self.assertNotIn('Matrix', result)

    def test_available_movies_5(self):
        system = MovieBookingSystem()
        system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        system.add_movie('Superman', 39.5, '20:00', '22:10', 2)
        result = system.available_movies('12:00', '23:00')
        self.assertIsInstance(result, list)
        for name in result:
            self.assertIsInstance(name, str)