import unittest




class TimeUtilsTestGetCurrentTime(unittest.TestCase):
    def test_get_current_time_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

import datetime

import re

import unittest

class AgentTest_get_current_time(unittest.TestCase):
    def test_get_current_time_1(self):
        timeutils = TimeUtils()
        result = timeutils.get_current_time()
        self.assertIsInstance(result, str)
        self.assertRegex(result, r"^\d{2}:\d{2}:\d{2}$")

    def test_get_current_time_2(self):
        timeutils = TimeUtils()
        timeutils.datetime = datetime.datetime(2001, 7, 18, 1, 1, 1)
        self.assertEqual(timeutils.get_current_time(), "01:01:01")

class TimeUtilsTestGetCurrentDate(unittest.TestCase):
    def test_get_current_date_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

import datetime

import unittest

class AgentTest_get_current_date(unittest.TestCase):
    def test_get_current_date_1(self):
        timeutils = TimeUtils()
        result = timeutils.get_current_date()
        self.assertIsInstance(result, str)
        self.assertRegex(result, r"^\d{4}-\d{2}-\d{2}$")

    def test_get_current_date_2(self):
        timeutils = TimeUtils()
        timeutils.datetime = datetime.datetime(2001, 7, 18, 1, 1, 1)
        self.assertEqual(timeutils.get_current_date(), "2001-07-18")

class TimeUtilsTestAddSeconds(unittest.TestCase):
    def test_add_seconds_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(600),
                         (timeutils.datetime + datetime.timedelta(seconds=600)).strftime("%H:%M:%S"))

    def test_add_seconds_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(500),
                         (timeutils.datetime + datetime.timedelta(seconds=500)).strftime("%H:%M:%S"))

    def test_add_seconds_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(400),
                         (timeutils.datetime + datetime.timedelta(seconds=400)).strftime("%H:%M:%S"))

import datetime

import unittest

class AgentTest_add_seconds(unittest.TestCase):
    def test_add_seconds_1(self):
        timeutils = TimeUtils()
        timeutils.datetime = datetime.datetime(2001, 7, 18, 1, 1, 1)
        self.assertEqual(timeutils.add_seconds(600), "01:11:01")

    def test_add_seconds_2(self):
        timeutils = TimeUtils()
        timeutils.datetime = datetime.datetime(2001, 7, 18, 23, 59, 30)
        self.assertEqual(timeutils.add_seconds(60), "00:00:30")

class TimeUtilsTestStringToDatetime(unittest.TestCase):
    def test_string_to_datetime_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-18 1:1:1'), datetime.datetime(2001, 7, 18, 1, 1, 1))

    def test_string_to_datetime_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-17 1:1:1'), datetime.datetime(2001, 7, 17, 1, 1, 1))

    def test_string_to_datetime_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-16 1:1:1'), datetime.datetime(2001, 7, 16, 1, 1, 1))

import datetime

import unittest

class AgentTest_string_to_datetime(unittest.TestCase):
    def test_string_to_datetime_1(self):
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2023-06-14 19:30:03")
        self.assertIsInstance(result, datetime.datetime)
        self.assertEqual(result, datetime.datetime(2023, 6, 14, 19, 30, 3))

    def test_string_to_datetime_2(self):
        timeutils = TimeUtils()
        result = timeutils.string_to_datetime("2001-12-31 23:59:59")
        self.assertIsInstance(result, datetime.datetime)
        self.assertEqual(result, datetime.datetime(2001, 12, 31, 23, 59, 59))

class TimeUtilsTestDatetimeToString(unittest.TestCase):
    def test_datetime_to_string_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

import unittest

class AgentTest_datetime_to_string(unittest.TestCase):
    def test_datetime_to_string_1(self):
        timeutils = TimeUtils()
        dt = datetime.datetime(2001, 7, 18, 1, 1, 1)
        self.assertEqual(timeutils.datetime_to_string(dt), "2001-07-18 01:01:01")

    def test_datetime_to_string_2(self):
        timeutils = TimeUtils()
        timeutils.datetime = datetime.datetime(2000, 1, 1, 0, 0, 0)
        dt = datetime.datetime(2023, 6, 14, 19, 30, 3)
        self.assertEqual(timeutils.datetime_to_string(dt), "2023-06-14 19:30:03")

class TimeUtilsTestGetMinutes(unittest.TestCase):
    def test_get_minutes_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1"), 60)

    def test_get_minutes_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 3:1:1"), 120)

    def test_get_minutes_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 4:1:1"), 180)

import datetime

import unittest

class AgentTest_get_minutes(unittest.TestCase):
    def test_get_minutes_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_minutes("2001-7-18 23:30:00", "2001-7-19 0:30:00"), 60)

    def test_get_minutes_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_minutes("2001-7-18 1:01:00", "2001-7-18 1:02:29"), 1)
        self.assertEqual(timeutils.get_minutes("2001-7-18 1:01:00", "2001-7-18 1:03:40"), 3)

class TimeUtilsTestGetFormatTime(unittest.TestCase):
    def test_get_format_time_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_format_time(2001, 7, 18, 1, 1, 1), "2001-07-18 01:01:01")

    def test_get_format_time_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_format_time(2001, 7, 17, 1, 1, 1), "2001-07-17 01:01:01")

    def test_get_format_time_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_format_time(2001, 7, 16, 1, 1, 1), "2001-07-16 01:01:01")

import unittest

class AgentTest_get_format_time(unittest.TestCase):
    def test_get_format_time_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_format_time(2023, 6, 14, 19, 30, 3), "2023-06-14 19:30:03")

    def test_get_format_time_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_format_time(1999, 12, 31, 23, 59, 59), "1999-12-31 23:59:59")
        self.assertEqual(timeutils.get_format_time(2000, 1, 1, 0, 0, 0), "2000-01-01 00:00:00")