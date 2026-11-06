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
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        """
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        target = date.date() if isinstance(date, datetime) else date
        result = []
        for ev in self.events:
            ev_date = ev.get('date')
            if ev_date is None:
                continue
            ev_day = ev_date.date() if isinstance(ev_date, datetime) else ev_date
            if ev_day == target:
                result.append(ev)
        return result

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        for ev in self.events:
            ev_start = ev.get('start_time')
            ev_end = ev.get('end_time')
            if ev_start is None or ev_end is None:
                continue
            if ev_start < end_time and start_time < ev_end:
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        day_start = datetime(date.year, date.month, date.day)
        day_end = day_start + timedelta(days=1)

        busy = []
        for ev in self.get_events(date):
            s = ev.get('start_time')
            e = ev.get('end_time')
            if s is None or e is None:
                continue
            s = max(s, day_start)
            e = min(e, day_end)
            if s < e:
                busy.append((s, e))
        busy.sort(key=lambda x: x[0])

        slots = []
        cursor = day_start
        for s, e in busy:
            if s > cursor:
                slots.append((cursor, s))
            if e > cursor:
                cursor = e
        if cursor < day_end:
            slots.append((cursor, day_end))
        return slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param num_events: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events,list.
        """
        def sort_key(ev):
            d = ev.get('date')
            s = ev.get('start_time')
            return (d if d is not None else datetime.min,
                    s if s is not None else datetime.min)

        return sorted(self.events, key=sort_key)[:num_events]