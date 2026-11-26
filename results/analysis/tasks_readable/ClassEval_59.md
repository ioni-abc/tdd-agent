# ClassEval_59

## Skeleton (what the agent sees)

```python
from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    this is a class as movie booking system, which allows to add movies, book tickets and check the available movies within a given time range. 
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
```

## Method `add_movie`

### Docstring

```python
def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
```

### Reference code (`solution_code`)

```python
def add_movie(self, name, price, start_time, end_time, n):
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime.strptime(start_time, '%H:%M'),
            'end_time': datetime.strptime(end_time, '%H:%M'),
            'seats': np.zeros((n, n))
        }
        self.movies.append(movie)
```

### Tests (`MovieBookingSystemTestAddMovie`)

setUp (runs before each test):

```python
def setUp(self):
    self.system = MovieBookingSystem()
```

**test_add_movie_1**: `stated`
- reason: The docstring's example shows the movie dict with the name, price, start_time and end_time parsed to datetime(1900, 1, 1, H, M), and seats as an n-by-n zero array, which is everything the test asserts.

```python
def test_add_movie_1(self):
    self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    self.assertEqual(len(self.system.movies), 1)
    self.assertEqual(self.system.movies[0]['name'], 'Batman')
    self.assertEqual(self.system.movies[0]['price'], 49.9)
    self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
    self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
    self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))
```

**test_add_movie_2**: `stated`
- reason: The docstring says the method adds a new movie into self.movies, so a programmer would append each call's movie to the list, which gives the expected count of 2 and the Batman-then-Superman order.

```python
def test_add_movie_2(self):
    self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    self.system.add_movie('Superman', 49.9, '17:05', '19:25', 3)
    self.assertEqual(len(self.system.movies), 2)
    self.assertEqual(self.system.movies[0]['name'], 'Batman')
    self.assertEqual(self.system.movies[1]['name'], 'Superman')
```

**test_add_movie_3**: `stated`
- reason: The docstring says the movie is added to self.movies with the name, price, start and end times parsed to datetimes, and an n-by-n seat array, and its example output matches what the test checks.

```python
def test_add_movie_3(self):
    self.system.add_movie('Batman', 39.9, '17:05', '19:25', 3)
    self.assertEqual(len(self.system.movies), 1)
    self.assertEqual(self.system.movies[0]['name'], 'Batman')
    self.assertEqual(self.system.movies[0]['price'], 39.9)
    self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
    self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
    self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))
```

**test_add_movie_4**: `stated`
- reason: The docstring's example shows the movie dict with the name, price, datetime start and end times parsed from 'HH:MM' strings, and an n×n zero seats array, which covers every assertion in the test.

```python
def test_add_movie_4(self):
    self.system.add_movie('Batman', 29.9, '17:05', '19:25', 3)
    self.assertEqual(len(self.system.movies), 1)
    self.assertEqual(self.system.movies[0]['name'], 'Batman')
    self.assertEqual(self.system.movies[0]['price'], 29.9)
    self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
    self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
    self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))
```

**test_add_movie_5**: `stated`
- reason: The docstring's example shows the movie stored with the given name and price, start and end times converted to datetimes on 1900-01-01, and an n-by-n seats array, which covers every assertion in the test.

```python
def test_add_movie_5(self):
    self.system.add_movie('Batman', 19.9, '17:05', '19:25', 3)
    self.assertEqual(len(self.system.movies), 1)
    self.assertEqual(self.system.movies[0]['name'], 'Batman')
    self.assertEqual(self.system.movies[0]['price'], 19.9)
    self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
    self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
    self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))
```

## Method `book_ticket`

### Docstring

```python
def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """
```

### Reference code (`solution_code`)

```python
def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'] == name:
                for seat in seats_to_book:
                    if movie['seats'][seat[0]][seat[1]] == 0:
                        movie['seats'][seat[0]][seat[1]] = 1
                    else:
                        return "Booking failed."
                return "Booking success."
        return "Movie not found."
```

### Tests (`MovieBookingSystemTestBookTicket`)

setUp (runs before each test):

```python
def setUp(self):
    self.system = MovieBookingSystem()
    self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
```

**test_book_ticket_1**: `unstated`
- reason: The docstring covers the success message and says seat values change, but never says that a booked seat is set to the value 1, which is what the test asserts.
- missing: The docstring should state that each successfully booked seat in the movie's seat grid is set to 1 (and that seats are free at 0), so an implementation that uses a different marker would be visibly wrong.

```python
def test_book_ticket_1(self):
    result = self.system.book_ticket('Batman', [(0, 0), (1, 1), (2, 2)])
    self.assertEqual(result, 'Booking success.')
    self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
    self.assertEqual(self.system.movies[0]['seats'][1][1], 1)
    self.assertEqual(self.system.movies[0]['seats'][2][2], 1)
```

**test_book_ticket_2**: `stated`
- reason: The docstring's example shows that re-booking an already-taken seat returns "Booking failed.", and it says self.movies' seats change on successful booking, which covers the test's check that the seat stays at 1.

```python
def test_book_ticket_2(self):
    self.system.book_ticket('Batman', [(0, 0)])
    result = self.system.book_ticket('Batman', [(0, 0)])
    self.assertEqual(result, 'Booking failed.')
    self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
```

**test_book_ticket_3**: `stated`
- reason: The docstring's own example shows `book_ticket('batman', ...)` returning "Movie not found.", and it says seats change only on successful booking, so a programmer following it would pass both assertions.

```python
def test_book_ticket_3(self):
    result = self.system.book_ticket('batman', [(0, 0)])
    self.assertEqual(result, 'Movie not found.')
    self.assertEqual(self.system.movies[0]['seats'][0][0], 0)
```

**test_book_ticket_4**: `stated`
- reason: The docstring says that booking succeeds, returns "Booking success.", and updates the seats in self.movies, which is exactly what this test checks for two free seats.

```python
def test_book_ticket_4(self):
    result = self.system.book_ticket('Batman', [(0, 0), (1, 1)])
    self.assertEqual(result, 'Booking success.')
    self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
    self.assertEqual(self.system.movies[0]['seats'][1][1], 1)
```

**test_book_ticket_5**: `stated`
- reason: The docstring says a successful booking returns "Booking success." and updates the seats in self.movies, which is exactly what this test checks for a single free seat on a fresh movie.

```python
def test_book_ticket_5(self):
    result = self.system.book_ticket('Batman', [(0, 0)])
    self.assertEqual(result, 'Booking success.')
    self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
```

## Method `available_movies`

### Docstring

```python
def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
```

### Reference code (`solution_code`)

```python
def available_movies(self, start_time, end_time):
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        available_movies = []
        for movie in self.movies:
            if start_time <= movie['start_time'] and movie['end_time'] <= end_time:
                available_movies.append(movie['name'])

        return available_movies
```

### Tests (`MovieBookingSystemTestAvailableMovies`)

setUp (runs before each test):

```python
def setUp(self):
    self.system = MovieBookingSystem()
    self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    self.system.add_movie('Spiderman', 59.9, '20:00', '22:30', 4)
```

**test_available_movies_1**: `stated`
- reason: The docstring says to return movies "within the specified time range", which a programmer would read as movies whose start and end both fall inside the window, and this test checks exactly that case with both movies fully inside 16:00–23:00.

```python
def test_available_movies_1(self):
    result = self.system.available_movies('16:00', '23:00')
    self.assertEqual(result, ['Batman', 'Spiderman'])
```

**test_available_movies_2**: `stated`
- reason: The docstring says to return available movies "within the specified time range", and this test's window (23:00-23:59) contains no movies under either a containment or an overlap reading, so the expected empty list follows directly.

```python
def test_available_movies_2(self):
    result = self.system.available_movies('23:00', '23:59')
    self.assertEqual(result, [])
```

**test_available_movies_3**: `stated`
- reason: "Within the specified time range" tells a programmer to include only movies that fit entirely inside the window, which excludes Spiderman (ends after 20:00) and keeps Batman (starts after 17:00 and ends before 20:00), matching the expected result.

```python
def test_available_movies_3(self):
    result = self.system.available_movies('17:00', '20:00')
    self.assertEqual(result, ['Batman'])
```

**test_available_movies_4**: `stated`
- reason: The docstring says to return movies "within the specified time range," and a programmer would read that as keeping movies whose start and end times both fall inside the range, which gives Batman and Spiderman for 10:00 to 23:00.

```python
def test_available_movies_4(self):
    result = self.system.available_movies('10:00', '23:00')
    self.assertEqual(result, ['Batman', 'Spiderman'])
```

**test_available_movies_5**: `stated`
- reason: The docstring says to return movies available within the given time range, and a programmer would naturally keep only movies whose showtimes fall inside that range, which gives ['Spiderman'] here.

```python
def test_available_movies_5(self):
    result = self.system.available_movies('20:00', '23:00')
    self.assertEqual(result, ['Spiderman'])
```

## Tests in no method's test class

### `MovieBookingSystemTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    system = MovieBookingSystem()
    system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    self.assertEqual(len(system.movies), 1)
    self.assertEqual(system.movies[0]['name'], 'Batman')
    self.assertEqual(system.movies[0]['price'], 49.9)
    self.assertEqual(system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
    self.assertEqual(system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
    self.assertEqual(system.movies[0]['seats'].shape, (3, 3))

    result = system.book_ticket('Batman', [(0, 0), (1, 1), (2, 2)])
    self.assertEqual(result, 'Booking success.')
    self.assertEqual(system.movies[0]['seats'][0][0], 1)
    self.assertEqual(system.movies[0]['seats'][1][1], 1)
    self.assertEqual(system.movies[0]['seats'][2][2], 1)

    result = system.available_movies('16:00', '23:00')
    self.assertEqual(result, ['Batman'])
```
