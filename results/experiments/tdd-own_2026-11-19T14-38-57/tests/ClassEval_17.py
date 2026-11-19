import unittest


import unittest

from datetime import datetime, timedelta

class AgentTest_add_event(unittest.TestCase):

    def test_add_event_1(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        calendar.add_event(event)
        self.assertEqual(calendar.events, [event])

    def test_add_event_2(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'}
        calendar.add_event(event1)
        calendar.add_event(event2)
        self.assertEqual(len(calendar.events), 2)
        self.assertEqual(calendar.events, [event1, event2])

    def test_add_event_3(self):
        calendar = CalendarUtil()
        existing = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        new_event = {'date': datetime(2023, 3, 15, 0, 0), 'start_time': datetime(2023, 3, 15, 14, 0), 'end_time': datetime(2023, 3, 15, 15, 30), 'description': 'Review'}
        calendar.events = [existing]
        calendar.add_event(new_event)
        self.assertEqual(calendar.events, [existing, new_event])

    def test_add_event_4(self):
        calendar = CalendarUtil()
        self.assertEqual(calendar.events, [])
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        calendar.add_event(event)
        self.assertEqual(len(calendar.events), 1)
        self.assertEqual(calendar.events[0]['description'], 'New Year')
        self.assertEqual(calendar.events[0]['start_time'], datetime(2023, 1, 1, 0, 0))
        self.assertEqual(calendar.events[0]['end_time'], datetime(2023, 1, 1, 1, 0))

    def test_add_event_5(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 2, 0, 0), 'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}
        calendar.add_event(event)
        self.assertEqual(calendar.events, [{'date': datetime(2023, 1, 2, 0, 0), 'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}])
        self.assertNotIn('start_time', calendar.events[0])

import unittest

from datetime import datetime, timedelta

class AgentTest_remove_event(unittest.TestCase):

    def test_remove_event_1(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        calendar.events = [event]
        calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [])

    def test_remove_event_2(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'}
        calendar.events = [event1, event2]
        calendar.remove_event(event1)
        self.assertEqual(calendar.events, [event2])

    def test_remove_event_3(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'}
        calendar.events = [event1, event2]
        calendar.remove_event(event2)
        self.assertEqual(calendar.events, [event1])
        self.assertEqual(len(calendar.events), 1)

    def test_remove_event_4(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 3, 15, 0, 0), 'start_time': datetime(2023, 3, 15, 14, 0), 'end_time': datetime(2023, 3, 15, 15, 30), 'description': 'Review'}
        calendar.events = [event]
        self.assertEqual(len(calendar.events), 1)
        calendar.remove_event({'date': datetime(2023, 3, 15, 0, 0), 'start_time': datetime(2023, 3, 15, 14, 0), 'end_time': datetime(2023, 3, 15, 15, 30), 'description': 'Review'})
        self.assertEqual(len(calendar.events), 0)
        self.assertNotIn(event, calendar.events)

    def test_remove_event_5(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'}
        event3 = {'date': datetime(2023, 3, 15, 0, 0), 'start_time': datetime(2023, 3, 15, 14, 0), 'end_time': datetime(2023, 3, 15, 15, 30), 'description': 'Review'}
        calendar.events = [event1, event2, event3]
        calendar.remove_event(event2)
        self.assertEqual(calendar.events, [event1, event3])
        self.assertEqual(calendar.events[0]['description'], 'New Year')
        self.assertEqual(calendar.events[1]['description'], 'Review')

import unittest

from datetime import datetime, timedelta

class AgentTest_get_events(unittest.TestCase):

    def test_get_events_1(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        calendar.events = [event]
        result = calendar.get_events(datetime(2023, 1, 1, 0, 0))
        self.assertEqual(result, [event])

    def test_get_events_2(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 9, 0), 'end_time': datetime(2023, 1, 1, 10, 0), 'description': 'Breakfast'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'}
        event3 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 14, 0), 'end_time': datetime(2023, 1, 1, 15, 0), 'description': 'Review'}
        calendar.events = [event1, event2, event3]
        result = calendar.get_events(datetime(2023, 1, 1, 0, 0))
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [event1, event3])
        self.assertNotIn(event2, result)

    def test_get_events_3(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        calendar.events = [event]
        result = calendar.get_events(datetime(2023, 3, 15, 0, 0))
        self.assertEqual(result, [])

    def test_get_events_4(self):
        calendar = CalendarUtil()
        self.assertEqual(calendar.events, [])
        result = calendar.get_events(datetime(2023, 1, 1, 0, 0))
        self.assertEqual(result, [])

    def test_get_events_5(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 3, 15, 0, 0), 'start_time': datetime(2023, 3, 15, 14, 0), 'end_time': datetime(2023, 3, 15, 15, 30), 'description': 'Review'}
        calendar.events = [event1, event2]
        result = calendar.get_events(datetime(2023, 3, 15, 0, 0))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['description'], 'Review')
        self.assertEqual(result[0]['start_time'], datetime(2023, 3, 15, 14, 0))
        self.assertEqual(result[0]['end_time'], datetime(2023, 3, 15, 15, 30))

import unittest

from datetime import datetime, timedelta

class AgentTest_is_available(unittest.TestCase):

    def test_is_available_1(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertFalse(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0)))

    def test_is_available_2(self):
        calendar = CalendarUtil()
        self.assertEqual(calendar.events, [])
        self.assertTrue(calendar.is_available(datetime(2023, 1, 1, 9, 0), datetime(2023, 1, 1, 10, 0)))

    def test_is_available_3(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertTrue(calendar.is_available(datetime(2023, 3, 15, 14, 0), datetime(2023, 3, 15, 15, 30)))

    def test_is_available_4(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 9, 0), 'end_time': datetime(2023, 1, 1, 10, 0), 'description': 'Breakfast'}]
        self.assertFalse(calendar.is_available(datetime(2023, 1, 1, 9, 30), datetime(2023, 1, 1, 11, 0)))

    def test_is_available_5(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 9, 0), 'end_time': datetime(2023, 1, 1, 10, 0), 'description': 'Breakfast'}]
        self.assertTrue(calendar.is_available(datetime(2023, 1, 1, 12, 0), datetime(2023, 1, 1, 13, 0)))
        self.assertEqual(len(calendar.events), 1)

import unittest

from datetime import datetime, timedelta

class AgentTest_get_available_slots(unittest.TestCase):

    def test_get_available_slots_1(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        result = calendar.get_available_slots(datetime(2023, 1, 1))
        self.assertEqual(result, [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])

    def test_get_available_slots_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        result = calendar.get_available_slots(datetime(2023, 1, 1))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        slot = result[0]
        self.assertIsInstance(slot, tuple)
        self.assertEqual(len(slot), 2)
        self.assertIsInstance(slot[0], datetime)
        self.assertIsInstance(slot[1], datetime)

    def test_get_available_slots_3(self):
        calendar = CalendarUtil()
        calendar.events = [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},
            {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 9, 0), 'end_time': datetime(2023, 1, 2, 10, 0), 'description': 'Meeting'},
        ]
        result = calendar.get_available_slots(datetime(2023, 1, 1))
        self.assertEqual(result, [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])

    def test_get_available_slots_4(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}
        calendar.events = [event]
        result = calendar.get_available_slots(datetime(2023, 1, 1))
        for slot_start, slot_end in result:
            self.assertFalse(slot_start < event['end_time'] and event['start_time'] < slot_end)
            self.assertGreaterEqual(slot_start, datetime(2023, 1, 1, 0, 0))
            self.assertLessEqual(slot_end, datetime(2023, 1, 2, 0, 0))

    def test_get_available_slots_5(self):
        calendar = CalendarUtil()
        event = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}
        calendar.events = [event]
        result = calendar.get_available_slots(datetime(2023, 1, 1))
        self.assertEqual(calendar.events, [event])
        self.assertEqual(len(calendar.events), 1)
        self.assertEqual(result, [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])

import unittest

from datetime import datetime, timedelta

class AgentTest_get_upcoming_events(unittest.TestCase):

    def test_get_upcoming_events_1(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]
        result = calendar.get_upcoming_events(1)
        self.assertIsInstance(result, list)

    def test_get_upcoming_events_2(self):
        calendar = CalendarUtil()
        self.assertEqual(calendar.events, [])
        result = calendar.get_upcoming_events(3)
        self.assertEqual(result, [])

    def test_get_upcoming_events_3(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}
        calendar.events = [event1, event2]
        calendar.get_upcoming_events(1)
        self.assertEqual(calendar.events, [event1, event2])
        self.assertEqual(len(calendar.events), 2)

    def test_get_upcoming_events_4(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}
        calendar.events = [event1, event2]
        result = calendar.get_upcoming_events(1)
        self.assertGreater(len(result), 0)
        for item in result:
            self.assertIn(item, calendar.events)
            self.assertIn('description', item)

    def test_get_upcoming_events_5(self):
        calendar = CalendarUtil()
        event1 = {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}
        event2 = {'date': datetime(2023, 1, 2, 0, 0), 'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}
        calendar.events = [event1, event2]
        result = calendar.get_upcoming_events(2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [event1, event2])