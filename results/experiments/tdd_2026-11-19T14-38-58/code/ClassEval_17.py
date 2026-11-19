from datetime import datetime, timedelta, date

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
        self.events.append(event)

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
        if event in self.events:
            self.events.remove(event)

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
        def _day(value):
            if isinstance(value, datetime):
                return value.date()
            return value

        target = _day(date)
        return [event for event in self.events
                if isinstance(event, dict) and _day(event.get('date')) == target]

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
        for event in self.events:
            if not isinstance(event, dict):
                continue
            ev_start = event.get('start_time', event.get('date'))
            ev_end = event.get('end_time')
            if ev_start is None or ev_end is None:
                continue
            # Two intervals overlap when each starts before the other ends.
            if ev_start < end_time and start_time < ev_end:
                return False
        return True

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
        day_start = datetime(date.year, date.month, date.day)
        slots = []
        for hour in range(24):
            slot_start = day_start + timedelta(hours=hour)
            slot_end = slot_start + timedelta(hours=1)
            if self.is_available(slot_start, slot_end):
                slots.append((slot_start, slot_end))
        return slots

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
        now = datetime.now()
        upcoming = []
        for event in self.events:
            if not isinstance(event, dict):
                continue
            start = event.get('start_time', event.get('date'))
            if start is None:
                continue
            if isinstance(start, date) and not isinstance(start, datetime):
                start = datetime(start.year, start.month, start.day)
            if start >= now:
                upcoming.append((start, event))
        upcoming.sort(key=lambda item: item[0])
        count = max(0, num_events)
        return [event for _, event in upcoming[:count]]