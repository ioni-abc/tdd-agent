import unittest


import unittest

import datetime

import re

from unittest import mock

class AgentTest_get_current_time(unittest.TestCase):

    def test_get_current_time_1(self):
        # The method returns a string, per the ":return: string" in the spec.
        timeutils = TimeUtils()
        result = timeutils.get_current_time()
        self.assertIsInstance(result, str)

    def test_get_current_time_2(self):
        # The format is '%H:%M:%S', e.g. "19:19:22": two digits, colon, two digits, colon, two digits.
        timeutils = TimeUtils()
        result = timeutils.get_current_time()
        self.assertRegex(result, r'^\d{2}:\d{2}:\d{2}$')
        self.assertEqual(len(result), 8)

    def test_get_current_time_3(self):
        # The string contains only the time, not the date.
        timeutils = TimeUtils()
        result = timeutils.get_current_time()
        self.assertNotIn('-', result)
        self.assertNotIn(' ', result)
        self.assertEqual(result.count(':'), 2)

    def test_get_current_time_4(self):
        # The string is a valid time in the '%H:%M:%S' format.
        timeutils = TimeUtils()
        result = timeutils.get_current_time()
        parsed = datetime.datetime.strptime(result, '%H:%M:%S')
        self.assertTrue(0 <= parsed.hour <= 23)
        self.assertTrue(0 <= parsed.minute <= 59)
        self.assertTrue(0 <= parsed.second <= 59)

    def test_get_current_time_5(self):
        # With the current time fixed at 2023-06-14 19:19:22 (as in the docstring example),
        # the method returns "19:19:22".
        fixed_now = datetime.datetime(2023, 6, 14, 19, 19, 22)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.get_current_time()

        self.assertEqual(result, "19:19:22")

class AgentTest_get_current_date(unittest.TestCase):

    def test_get_current_date_1(self):
        # The method returns a string, per the ":return: string" in the spec.
        timeutils = TimeUtils()
        result = timeutils.get_current_date()
        self.assertIsInstance(result, str)

    def test_get_current_date_2(self):
        # The format is "%Y-%m-%d", e.g. "2023-06-14": four digits, dash, two digits, dash, two digits.
        timeutils = TimeUtils()
        result = timeutils.get_current_date()
        self.assertRegex(result, r'^\d{4}-\d{2}-\d{2}$')
        self.assertEqual(len(result), 10)

    def test_get_current_date_3(self):
        # The string contains only the date, not the time.
        timeutils = TimeUtils()
        result = timeutils.get_current_date()
        self.assertNotIn(':', result)
        self.assertNotIn(' ', result)

    def test_get_current_date_4(self):
        # With the current datetime fixed at 2023-06-14 19:19:22 (as in the docstring example),
        # the method returns "2023-06-14".
        fixed_now = datetime.datetime(2023, 6, 14, 19, 19, 22)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.get_current_date()

        self.assertEqual(result, "2023-06-14")

    def test_get_current_date_5(self):
        # The "%Y-%m-%d" format zero-pads month and day, so 2001-07-08 is returned as "2001-07-08".
        fixed_now = datetime.datetime(2001, 7, 8, 1, 1, 1)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.get_current_date()

        self.assertEqual(result, "2001-07-08")

import unittest

import datetime

import re

from unittest import mock

class AgentTest_add_seconds(unittest.TestCase):

    def test_add_seconds_1(self):
        # The method returns a string, per the ":return: string" in the spec.
        fixed_now = datetime.datetime(2023, 6, 14, 19, 19, 22)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.add_seconds(600)

        self.assertIsInstance(result, str)

    def test_add_seconds_2(self):
        # Docstring example: with the current time 19:19:22, add_seconds(600) returns "19:29:22".
        fixed_now = datetime.datetime(2023, 6, 14, 19, 19, 22)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.add_seconds(600)

        self.assertEqual(result, "19:29:22")

    def test_add_seconds_3(self):
        # Adding zero seconds leaves the current time unchanged, in '%H:%M:%S' format.
        fixed_now = datetime.datetime(2023, 6, 14, 19, 19, 22)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.add_seconds(0)

        self.assertEqual(result, "19:19:22")

    def test_add_seconds_4(self):
        # Adding seconds past midnight wraps to the next day's time, still in '%H:%M:%S' format.
        fixed_now = datetime.datetime(2023, 6, 14, 23, 59, 30)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.add_seconds(60)

        self.assertEqual(result, "00:00:30")

    def test_add_seconds_5(self):
        # The '%H:%M:%S' format zero-pads every field, so 1:1:1 plus 1 second is "01:01:02".
        fixed_now = datetime.datetime(2001, 7, 18, 1, 1, 1)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.add_seconds(1)

        self.assertEqual(result, "01:01:02")
        self.assertRegex(result, r'^\d{2}:\d{2}:\d{2}$')

import datetime

class AgentTest_string_to_datetime(unittest.TestCase):

    def test_string_to_datetime_1(self):
        # The spec says the method returns a datetime instance.
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2001-7-18 1:1:1")
        self.assertIsInstance(result, datetime.datetime)

    def test_string_to_datetime_2(self):
        # Docstring example: "2001-7-18 1:1:1" converts to 2001-07-18 01:01:01.
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2001-7-18 1:1:1")
        self.assertEqual(result, datetime.datetime(2001, 7, 18, 1, 1, 1))

    def test_string_to_datetime_3(self):
        # A zero-padded string in the common "%Y-%m-%d %H:%M:%S" layout converts field by field.
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2023-06-14 19:19:22")
        self.assertEqual(result, datetime.datetime(2023, 6, 14, 19, 19, 22))
        self.assertEqual(result.year, 2023)
        self.assertEqual(result.month, 6)
        self.assertEqual(result.day, 14)
        self.assertEqual(result.hour, 19)
        self.assertEqual(result.minute, 19)
        self.assertEqual(result.second, 22)

    def test_string_to_datetime_4(self):
        # Midnight is a valid time and converts to hour, minute and second of zero on the same date.
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2001-07-18 00:00:00")
        self.assertEqual(result, datetime.datetime(2001, 7, 18, 0, 0, 0))

    def test_string_to_datetime_5(self):
        # The end of a year, with a two-digit month and day, converts to the matching datetime.
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2001-12-31 23:59:59")
        self.assertEqual(result, datetime.datetime(2001, 12, 31, 23, 59, 59))

import datetime

import re

from unittest import mock

class AgentTest_datetime_to_string(unittest.TestCase):

    def test_datetime_to_string_1(self):
        # The spec says the method returns a string, per the ":return: string" in the docstring.
        timeutils = TimeUtils()
        result = timeutils.datetime_to_string(datetime.datetime(2023, 6, 14, 19, 30, 3))
        self.assertIsInstance(result, str)

    def test_datetime_to_string_2(self):
        # The output layout matches the docstring example "2023-06-14 19:30:03".
        timeutils = TimeUtils()
        result = timeutils.datetime_to_string(datetime.datetime(2023, 6, 14, 19, 30, 3))
        self.assertEqual(result, "2023-06-14 19:30:03")

    def test_datetime_to_string_3(self):
        # The "%Y-%m-%d %H:%M:%S" layout zero-pads every field, so 1:1:1 on 2001-07-18 is "2001-07-18 01:01:01".
        timeutils = TimeUtils()
        result = timeutils.datetime_to_string(datetime.datetime(2001, 7, 18, 1, 1, 1))
        self.assertEqual(result, "2001-07-18 01:01:01")
        self.assertRegex(result, r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')

    def test_datetime_to_string_4(self):
        # Docstring example: the instance's own datetime attribute, fixed at 2023-06-14 19:30:03, converts to "2023-06-14 19:30:03".
        fixed_now = datetime.datetime(2023, 6, 14, 19, 30, 3)

        class FixedDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_now

        with mock.patch('datetime.datetime', FixedDatetime):
            timeutils = TimeUtils()
            result = timeutils.datetime_to_string(timeutils.datetime)

        self.assertEqual(result, "2023-06-14 19:30:03")

    def test_datetime_to_string_5(self):
        # Midnight on the last day of the year keeps the date and shows 00:00:00 for the time.
        timeutils = TimeUtils()
        result = timeutils.datetime_to_string(datetime.datetime(2001, 12, 31, 0, 0, 0))
        self.assertEqual(result, "2001-12-31 00:00:00")
        self.assertEqual(len(result), 19)

class AgentTest_get_minutes(unittest.TestCase):

    def test_get_minutes_1(self):
        # The spec says the method returns an int, per the ":return: int" in the docstring.
        timeutils = TimeUtils()
        result = timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        self.assertIsInstance(result, int)

    def test_get_minutes_2(self):
        # Docstring example: "2001-7-18 1:1:1" and "2001-7-18 2:1:1" are 60 minutes apart.
        timeutils = TimeUtils()
        result = timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        self.assertEqual(result, 60)

    def test_get_minutes_3(self):
        # Two identical times have no minutes passed between them.
        timeutils = TimeUtils()
        result = timeutils.get_minutes("2001-07-18 01:01:01", "2001-07-18 01:01:01")
        self.assertEqual(result, 0)

    def test_get_minutes_4(self):
        # The result is rounded to the nearest whole minute.
        # 1 minute 20 seconds is 1.33 minutes, which rounds to 1.
        # 1 minute 40 seconds is 1.67 minutes, which rounds to 2.
        timeutils = TimeUtils()
        result_down = timeutils.get_minutes("2001-07-18 01:00:00", "2001-07-18 01:01:20")
        result_up = timeutils.get_minutes("2001-07-18 01:00:00", "2001-07-18 01:01:40")
        self.assertEqual(result_down, 1)
        self.assertEqual(result_up, 2)

    def test_get_minutes_5(self):
        # Times spanning midnight into the next date are still measured correctly.
        # From 2001-7-18 23:30:00 to 2001-7-19 0:15:00 is 45 minutes.
        timeutils = TimeUtils()
        result = timeutils.get_minutes("2001-7-18 23:30:00", "2001-7-19 0:15:00")
        self.assertEqual(result, 45)

import datetime

class AgentTest_get_format_time(unittest.TestCase):

    def test_get_format_time_1(self):
        # The spec says the method returns a formatted time string.
        timeutils = TimeUtils()
        result = timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
        self.assertIsInstance(result, str)

    def test_get_format_time_2(self):
        # Docstring example: get_format_time(2001, 7, 18, 1, 1, 1) returns "2001-07-18 01:01:01".
        timeutils = TimeUtils()
        result = timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
        self.assertEqual(result, "2001-07-18 01:01:01")

    def test_get_format_time_3(self):
        # The "%Y-%m-%d %H:%M:%S" layout zero-pads month, day, hour, minute and second,
        # so single-digit inputs produce two-digit fields.
        timeutils = TimeUtils()
        result = timeutils.get_format_time(2001, 7, 8, 9, 5, 3)
        self.assertEqual(result, "2001-07-08 09:05:03")
        self.assertRegex(result, r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
        self.assertEqual(len(result), 19)

    def test_get_format_time_4(self):
        # Two-digit values are kept as they are, with no extra padding,
        # e.g. the last moment of a year.
        timeutils = TimeUtils()
        result = timeutils.get_format_time(2023, 12, 31, 23, 59, 59)
        self.assertEqual(result, "2023-12-31 23:59:59")

    def test_get_format_time_5(self):
        # Midnight is a valid time and its hour, minute and second are shown as 00.
        timeutils = TimeUtils()
        result = timeutils.get_format_time(2001, 1, 1, 0, 0, 0)
        self.assertEqual(result, "2001-01-01 00:00:00")