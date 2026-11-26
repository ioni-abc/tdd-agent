# ClassEval_17

## Skeleton (what the agent sees)

```python
from datetime import datetime, timedelta

class CalendarUtil:
    """
    This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar,dict.
        >>> calendar = CalendarUtil()
        >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        >>> calendar.events
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]

        """

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        >>> calendar.events
        []

        """

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]

        """

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False

        """

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        >>> calendar.get_available_slots(datetime(2023, 1, 1))
        [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]

        """

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]

        """
```

## Method `add_event`

### Docstring

```python
def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar,dict.
        >>> calendar = CalendarUtil()
        >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        >>> calendar.events
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]

        """
```

### Reference code (`solution_code`)

```python
def add_event(self, event):
        self.events.append(event)
```

### Tests (`CalendarTestAddEvent`)

**test_add_event**: `stated`
- reason: The docstring says add_event adds the given event dict to the calendar, and the doctest shows calendar.events then holds that dict, which is exactly what the test checks.

```python
def test_add_event(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
```

**test_add_event_2**: `stated`
- reason: The docstring says to add the event to the calendar, and a programmer would naturally append each one, so adding two identical events and keeping both matches the expected list.

```python
def test_add_event_2(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
```

**test_add_event_3**: `stated`
- reason: The docstring says add_event appends the given event dict to the calendar's events list, and the test adds one event with a 23:00 end time and checks that events contains exactly that dict, which a programmer following the docstring would satisfy.

```python
def test_add_event_3(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])
```

**test_add_event_4**: `stated`
- reason: The docstring says add_event adds the given event dict to the calendar, and its example shows the dict being appended to `calendar.events`, so a programmer following it would append the event and pass this test.

```python
def test_add_event_4(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'}])
```

**test_add_event_5**: `stated`
- reason: The docstring says add_event adds the given event dict to the calendar, and its example shows the event appearing unchanged in `calendar.events`, which is exactly what this test checks.

```python
def test_add_event_5(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 20, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 20, 0), 'description': 'New Year'}])
```

## Method `remove_event`

### Docstring

```python
def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        >>> calendar.events
        []

        """
```

### Reference code (`solution_code`)

```python
def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
```

### Tests (`CalendarTestRemoveEvent`)

**test_remove_event**: `stated`
- reason: The docstring says to remove the given event from the calendar, and its example shows the matching event being removed and the events list becoming empty, which is exactly what the test checks.

```python
def test_remove_event(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                           'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [])
```

**test_remove_event_2**: `stated`
- reason: The docstring says to remove the given event from the calendar, and a programmer would delete the matching entry from the events list while leaving the other event in place, which is what the test checks.

```python
def test_remove_event_2(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
                       {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                        'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
    calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                           'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
         'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}])
```

**test_remove_event_3**: `stated`
- reason: The docstring says remove the given event dict from the calendar, so a programmer would delete the matching entry and leave the other events, which is what this test checks.

```python
def test_remove_event_3(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
                       {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                        'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
    calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                           'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
```

**test_remove_event_4**: `stated`
- reason: The docstring says the method removes the given event dict from the calendar, and this test checks that exactly the matching event is removed from a list of two, which a programmer following it would do.

```python
def test_remove_event_4(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},
                       {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                        'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
    calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                           'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])
```

**test_remove_event_5**: `stated`
- reason: The docstring says the method removes the given event from the calendar, and the test checks that exactly the matching event is removed while the other remains, which a programmer would implement.

```python
def test_remove_event_5(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'},
                       {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                        'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
    calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                           'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'}])
```

**test_remove_event_6**: `unstated`
- reason: The test removes an event from an empty calendar and expects no error and an empty list, but the docstring only says to remove an event and never says what happens when the event is absent, so a programmer could reasonably raise an error instead.
- missing: The docstring should state what happens when the given event is not in the calendar, for example whether it is silently ignored or an error is raised.

```python
def test_remove_event_6(self):
    calendar = CalendarUtil()
    calendar.events = []
    calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                           'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [])
```

## Method `get_events`

### Docstring

```python
def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.get_events(datetime(2023, 1, 1, 0, 0))
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]

        """
```

### Reference code (`solution_code`)

```python
def get_events(self, date):
        events_on_date = []
        for event in self.events:
            if event['date'].date() == date.date():
                events_on_date.append(event)
        return events_on_date
```

### Tests (`CalendarTestGetEvents`)

**test_get_events**: `stated`
- reason: The docstring says to get all events on a given date, so a programmer would filter stored events by calendar date, which returns the single matching event the test expects.

```python
def test_get_events(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_events(datetime(2023, 1, 1)), [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
```

**test_get_events_2**: `stated`
- reason: The docstring says the method returns all events on the given date, so a programmer would filter by date and return an empty list when no event falls on the queried day, which is what this test checks.

```python
def test_get_events_2(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_events(datetime(2023, 1, 2)), [])
```

## Method `is_available`

### Docstring

```python
def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        >>> calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0))
        False

        """
```

### Reference code (`solution_code`)

```python
def is_available(self, start_time, end_time):
        for event in self.events:
            if start_time < event['end_time'] and end_time > event['start_time']:
                return False
        return True
```

### Tests (`CalendarTestIsAvailable`)

**test_is_available**: `stated`
- reason: The docstring's own doctest shows the same case (a slot identical to an existing event returns False), so a programmer following it would return False here.

```python
def test_is_available(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0)), False)
```

**test_is_available_2**: `unstated`
- reason: The docstring says only that the calendar must be free for the slot, so a programmer could reasonably treat a slot starting exactly when another event ends as a conflict, while the test expects it to be available.
- missing: The docstring should state whether a time slot that begins exactly when an existing event ends (or ends exactly when one begins) counts as overlapping, and specify that such touching endpoints do not conflict.

```python
def test_is_available_2(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 1, 0), datetime(2023, 1, 1, 2, 0)), True)
```

**test_is_available_3**: `stated`
- reason: A programmer reading "True if the calendar is available for the given time slot, False otherwise" and the example of a slot that collides with an existing event would return False here, since the requested slot starts at the event's start and overlaps it.

```python
def test_is_available_3(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 0, 30)), False)
```

**test_is_available_4**: `stated`
- reason: A programmer reading "available for a given time slot" would treat any overlap with an existing event as unavailable, which is exactly what this partially overlapping slot tests, so the expected False follows from the docstring.

```python
def test_is_available_4(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 30), datetime(2023, 1, 1, 1, 0)), False)
```

**test_is_available_5**: `unstated`
- reason: The docstring says only that the slot must be free of events, so a programmer could reasonably treat a slot that starts exactly when an event ends as a conflict, while the test expects it to be available.
- missing: The docstring should say whether a time slot that only touches an existing event at its start or end boundary counts as overlapping, and if it does not, that back-to-back slots are available.

```python
def test_is_available_5(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 1, 0), datetime(2023, 1, 1, 1, 30)), True)
```

## Method `get_available_slots`

### Docstring

```python
def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        >>> calendar.get_available_slots(datetime(2023, 1, 1))
        [(datetime.datetime(2023, 1, 1, 23, 0), datetime.datetime(2023, 1, 2, 0, 0))]

        """
```

### Reference code (`solution_code`)

```python
def get_available_slots(self, date):
        available_slots = []
        start_time = datetime(date.year, date.month, date.day, 0, 0)
        end_time = datetime(date.year, date.month, date.day, 23, 59)

        while start_time < end_time:
            slot_end_time = start_time + timedelta(minutes=60)
            if self.is_available(start_time, slot_end_time):
                available_slots.append((start_time, slot_end_time))
            start_time += timedelta(minutes=60)


        return available_slots
```

### Tests (`CalendarTestGetAvailableSlots`)

**test_get_available_slots**: `unstated`
- reason: The docstring says only "all available time slots" without giving the slot length (one hour, aligned to the hour) or how a slot that touches an event's boundary counts as busy, so a correct implementation could return different slots than the test expects.
- missing: The docstring should state that the day is split into consecutive fixed-length slots (here one hour, starting at midnight), and that a slot is unavailable only if it overlaps an existing event's interval, with the event end treated as exclusive.

```python
def test_get_available_slots(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_available_slots(datetime(2023, 1, 1)),
                     [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])
```

**test_get_available_slots_2**: `stated`
- reason: The docstring's example shows hourly slots that are free when they only touch an event's boundary, so a programmer following it would divide the day into 60-minute slots and exclude only the one overlapping the 1:00-2:00 event, giving 23.

```python
def test_get_available_slots_2(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 1, 0),
                        'end_time': datetime(2023, 1, 1, 2, 0), 'description': 'New Year'}]
    self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 23)
```

**test_get_available_slots_3**: `unstated`
- reason: The docstring never says that slots are fixed-length hourly blocks starting at midnight, or that only events overlapping the requested day block them, so a correct implementation could return a different slot count and fail this test.
- missing: The docstring should state the slot length and starting boundary, and say whether events are matched by their start and end times against the requested day or by their date field, so the expected slot count can be derived.

```python
def test_get_available_slots_3(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                        'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
    self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)
```

**test_get_available_slots_4**: `unstated`
- reason: The test expects 24 hourly slots on the queried day even though the event's `date` field is that day while its start and end times fall on the next day, and the docstring does not say which field decides whether an event blocks a slot.
- missing: The docstring should state that slots are one hour long, cover the whole day from midnight, and that an event blocks a slot only when its start and end times overlap that slot, regardless of the event's `date` field.

```python
def test_get_available_slots_4(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                        'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
    self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)
```

**test_get_available_slots_5**: `unstated`
- reason: The docstring never says the slots are fixed one-hour blocks starting at midnight, so an implementation using another granularity or grid could return a different count than the 24 this test expects.
- missing: The docstring should state the slot length and grid, for example that the day is split into consecutive fixed-length slots starting at midnight, and how many slots a free day yields.

```python
def test_get_available_slots_5(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                        'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
    self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)
```

## Method `get_upcoming_events`

### Docstring

```python
def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0), 'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}, {'date': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]

        """
```

### Reference code (`solution_code`)

```python
def get_upcoming_events(self, num_events):
        now = datetime.now()
        upcoming_events = []
        for event in self.events:
            if event['start_time'] >= now:
                upcoming_events.append(event)
            if len(upcoming_events) == num_events:
                break
        return upcoming_events
```

### Tests (`CalendarTestGetUpcomingEvents`)

**test_get_upcoming_events**: `stated`
- reason: The docstring says the method returns the next n upcoming events, so a programmer would filter out events whose start time is already past, which is what this test checks by expecting an empty list for a 2023 event.

```python
def test_get_upcoming_events(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_upcoming_events(1), [])
```

**test_get_upcoming_events_2**: `unstated`
- reason: The docstring says "upcoming" and "from a given date," but the signature has no date parameter, so a programmer cannot tell that the reference point is the current time and that events starting before now must be excluded, which this test depends on.
- missing: The docstring should state that "upcoming" is measured against the current time, and that only events whose start time is at or after the current moment are returned, with already-started or past events excluded.

```python
def test_get_upcoming_events_2(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 1, 0),
                        'end_time': datetime(2023, 1, 1, 2, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_upcoming_events(1), [])
```

**test_get_upcoming_events_3**: `unstated`
- reason: The docstring says "upcoming events from a given date" but gives no reference point, so a programmer could reasonably filter by the current time, by a date argument, or by the event date rather than start time, and the test's expectation that a past-starting event is excluded is not stated.
- missing: The docstring should say that "upcoming" means events whose start time is at or after the current moment, and that events starting earlier are skipped, with the result capped at the requested count.

```python
def test_get_upcoming_events_3(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                        'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_upcoming_events(1), [])
```

**test_get_upcoming_events_4**: `stated`
- reason: "Upcoming" events are those still ahead of the current time, so a programmer would filter out the only event, which starts in the past, and return an empty list even when n=2 is requested.

```python
def test_get_upcoming_events_4(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                        'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_upcoming_events(2), [])
```

**test_get_upcoming_events_5**: `unstated`
- reason: The docstring says "upcoming" without saying that upcoming means starting at or after the current time, so a programmer could reasonably use a different reference point or timestamp and fail to exclude the past event this test expects to be dropped.
- missing: The docstring should state that events are compared against the current time using each event's start time, that only events starting at or after that time are returned in their stored order, and that at most n are returned.

```python
def test_get_upcoming_events_5(self):
    calendar = CalendarUtil()
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},
                       {'date': datetime(2124, 1, 2, 0, 0), 'start_time': datetime(2124, 1, 2, 1, 0),
                        'end_time': datetime(2124, 1, 2, 2, 0),
                        'description': 'New Year 2'}]
    self.assertEqual(calendar.get_upcoming_events(1), [
        {'date': datetime(2124, 1, 2, 0, 0), 'start_time': datetime(2124, 1, 2, 1, 0),
         'end_time': datetime(2124, 1, 2, 2, 0), 'description': 'New Year 2'}])
```

## Tests in no method's test class

### `CalendarTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    calendar = CalendarUtil()
    calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
    calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                           'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
    self.assertEqual(calendar.events, [])
    calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                        'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
    self.assertEqual(calendar.get_events(datetime(2023, 1, 1)), [
        {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
         'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])
    self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0)), False)
    self.assertEqual(calendar.get_available_slots(datetime(2023, 1, 1)),
                     [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])
    self.assertEqual(calendar.get_upcoming_events(1), [])
```
