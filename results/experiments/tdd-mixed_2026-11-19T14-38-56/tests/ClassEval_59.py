import unittest




class MovieBookingSystemTestAddMovie(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()

    def tearDown(self):
        self.system = None

    def test_add_movie_1(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 49.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

    def test_add_movie_2(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.system.add_movie('Superman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 2)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[1]['name'], 'Superman')

    def test_add_movie_3(self):
        self.system.add_movie('Batman', 39.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 39.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

from datetime import datetime

import numpy as np

class AgentTest_add_movie(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()

    def tearDown(self):
        self.system = None

    def test_add_movie_1(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 5)
        seats = self.system.movies[0]['seats']
        self.assertEqual(seats.shape, (5, 5))
        self.assertTrue(np.all(seats == 0))

    def test_add_movie_2(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        movie = self.system.movies[0]
        self.assertEqual(set(movie.keys()), {'name', 'price', 'start_time', 'end_time', 'seats'})
        self.assertEqual(movie['start_time'], datetime(1900, 1, 1, 17, 5))
        self.assertEqual(movie['end_time'], datetime(1900, 1, 1, 19, 25))

class MovieBookingSystemTestBookTicket(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)

    def test_book_ticket_1(self):
        result = self.system.book_ticket('Batman', [(0, 0), (1, 1), (2, 2)])
        self.assertEqual(result, 'Booking success.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
        self.assertEqual(self.system.movies[0]['seats'][1][1], 1)
        self.assertEqual(self.system.movies[0]['seats'][2][2], 1)

    def test_book_ticket_2(self):
        self.system.book_ticket('Batman', [(0, 0)])
        result = self.system.book_ticket('Batman', [(0, 0)])
        self.assertEqual(result, 'Booking failed.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)

    def test_book_ticket_3(self):
        result = self.system.book_ticket('batman', [(0, 0)])
        self.assertEqual(result, 'Movie not found.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 0)

import numpy as np

class AgentTest_book_ticket(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)

    def test_book_ticket_1(self):
        self.system.book_ticket('Batman', [(0, 0)])
        result = self.system.book_ticket('Batman', [(1, 1), (0, 0)])
        self.assertEqual(result, 'Booking failed.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
        self.assertEqual(self.system.movies[0]['seats'][1][1], 0)
        self.assertEqual(np.sum(self.system.movies[0]['seats']), 1)

    def test_book_ticket_2(self):
        result = self.system.book_ticket('Batman', [(0, 0), (3, 3)])
        self.assertEqual(result, 'Booking failed.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 0)
        self.assertEqual(np.sum(self.system.movies[0]['seats']), 0)

class MovieBookingSystemTestAvailableMovies(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.system.add_movie('Spiderman', 59.9, '20:00', '22:30', 4)

    def test_available_movies_1(self):
        result = self.system.available_movies('16:00', '23:00')
        self.assertEqual(result, ['Batman', 'Spiderman'])

    def test_available_movies_2(self):
        result = self.system.available_movies('23:00', '23:59')
        self.assertEqual(result, [])

    def test_available_movies_3(self):
        result = self.system.available_movies('17:00', '20:00')
        self.assertEqual(result, ['Batman'])

class AgentTest_available_movies(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()

    def test_available_movies_1(self):
        result = self.system.available_movies('00:00', '23:59')
        self.assertEqual(result, [])

    def test_available_movies_2(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.system.add_movie('Spiderman', 59.9, '20:00', '22:30', 4)
        result = self.system.available_movies('17:05', '19:25')
        self.assertEqual(result, ['Batman'])