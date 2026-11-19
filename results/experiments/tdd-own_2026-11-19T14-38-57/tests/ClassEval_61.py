import unittest


import unittest

class AgentTest_play(unittest.TestCase):

    def test_play_1(self):
        # A new player has no current song, so play returns False.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.play(), False)

    def test_play_2(self):
        # With a current song set, play returns that song.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.play(), "song1")

    def test_play_3(self):
        # Play returns the current song, not simply the first song in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.play(), "song2")

    def test_play_4(self):
        # Play returns the current song and does not change the current song.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        musicPlayer.play()
        self.assertEqual(musicPlayer.current_song, "song1")

    def test_play_5(self):
        # After the current song is cleared, play returns False.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        musicPlayer.current_song = None
        self.assertIs(musicPlayer.play(), False)

import unittest

class AgentTest_add_song(unittest.TestCase):

    def test_add_song_1(self):
        # Adding a song to a new player puts that song in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song1"])

    def test_add_song_2(self):
        # Matches the docstring example: adding "song1" gives ['song1'].
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song1"])

    def test_add_song_3(self):
        # Adding two songs in sequence keeps them in the order they were added.
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        musicPlayer.add_song("song2")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2"])

    def test_add_song_4(self):
        # Adding a song to a playlist that already has songs keeps the existing songs.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.add_song("song3")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2", "song3"])

    def test_add_song_5(self):
        # Adding a single song increases the playlist length by exactly one.
        musicPlayer = MusicPlayer()
        before = len(musicPlayer.playlist)
        musicPlayer.add_song("My Song")
        self.assertEqual(len(musicPlayer.playlist), before + 1)
        self.assertIn("My Song", musicPlayer.playlist)

import unittest

class AgentTest_stop(unittest.TestCase):

    def test_stop_1(self):
        # A new player has no current song, so stop returns False.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.stop(), False)

    def test_stop_2(self):
        # Matches the docstring example: with a current song set, stop returns True.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertIs(musicPlayer.stop(), True)

    def test_stop_3(self):
        # Stop returns True for any current song, not only the first song in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertIs(musicPlayer.stop(), True)

    def test_stop_4(self):
        # After the current song is cleared, stop returns False.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        musicPlayer.current_song = None
        self.assertIs(musicPlayer.stop(), False)

    def test_stop_5(self):
        # A populated playlist with no current song still means stop returns False.
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        musicPlayer.add_song("song2")
        self.assertIsNone(musicPlayer.current_song)
        self.assertIs(musicPlayer.stop(), False)

import unittest

class AgentTest_remove_song(unittest.TestCase):

    def test_remove_song_1(self):
        # Matches the docstring example: removing "song1" from ["song1", "song2"] leaves ['song2'].
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song2"])

    def test_remove_song_2(self):
        # Removing the second song leaves the first song in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.remove_song("song2")
        self.assertEqual(musicPlayer.playlist, ["song1"])

    def test_remove_song_3(self):
        # Removing the only song in the playlist leaves the playlist empty.
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, [])

    def test_remove_song_4(self):
        # Removing a song decreases the playlist length by exactly one and the song is no longer in it.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        before = len(musicPlayer.playlist)
        musicPlayer.remove_song("song2")
        self.assertEqual(len(musicPlayer.playlist), before - 1)
        self.assertNotIn("song2", musicPlayer.playlist)

    def test_remove_song_5(self):
        # Removing a song from the middle keeps the remaining songs in their original order.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3", "song4"]
        musicPlayer.remove_song("song2")
        self.assertEqual(musicPlayer.playlist, ["song1", "song3", "song4"])

import unittest

class AgentTest_switch_song(unittest.TestCase):

    def test_switch_song_1(self):
        # Matches the docstring example: switching from "song1" to "song2" returns True.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertIs(musicPlayer.switch_song(), True)

    def test_switch_song_2(self):
        # After switching, the current song is the next song in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        musicPlayer.switch_song()
        self.assertEqual(musicPlayer.current_song, "song2")

    def test_switch_song_3(self):
        # When the current song is the last song, there is no next song, so switch_song returns False.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertIs(musicPlayer.switch_song(), False)

    def test_switch_song_4(self):
        # In a longer playlist, switching from a middle song moves to the song immediately after it.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song2"
        self.assertIs(musicPlayer.switch_song(), True)
        self.assertEqual(musicPlayer.current_song, "song3")

    def test_switch_song_5(self):
        # An empty playlist has no next song, so switch_song returns False.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.switch_song(), False)

import unittest

class AgentTest_previous_song(unittest.TestCase):

    def test_previous_song_1(self):
        # Matches the docstring example: switching back from "song2" to "song1" returns True.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertIs(musicPlayer.previous_song(), True)

    def test_previous_song_2(self):
        # After switching to the previous song, the current song is the one before it in the playlist.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        musicPlayer.previous_song()
        self.assertEqual(musicPlayer.current_song, "song1")

    def test_previous_song_3(self):
        # When the current song is the first song, there is no previous song, so previous_song returns False.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertIs(musicPlayer.previous_song(), False)

    def test_previous_song_4(self):
        # In a longer playlist, switching back from a later song moves to the song immediately before it.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song3"
        self.assertIs(musicPlayer.previous_song(), True)
        self.assertEqual(musicPlayer.current_song, "song2")

    def test_previous_song_5(self):
        # An empty playlist has no previous song, so previous_song returns False.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.previous_song(), False)

import unittest

class AgentTest_set_volume(unittest.TestCase):

    def test_set_volume_1(self):
        # Matches the docstring example: setting volume to 50 stores 50 and returns True.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(50), True)
        self.assertEqual(musicPlayer.volume, 50)

    def test_set_volume_2(self):
        # 0 is the lower bound of the valid range, so it is accepted.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(0), True)
        self.assertEqual(musicPlayer.volume, 0)

    def test_set_volume_3(self):
        # 100 is the upper bound of the valid range, so it is accepted.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(100), True)
        self.assertEqual(musicPlayer.volume, 100)

    def test_set_volume_4(self):
        # A volume above 100 is invalid, so set_volume returns False.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(101), False)

    def test_set_volume_5(self):
        # A volume below 0 is invalid, so set_volume returns False and the volume is not changed from its default of 50.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(-1), False)
        self.assertEqual(musicPlayer.volume, 50)

import unittest

from collections import Counter

class AgentTest_shuffle(unittest.TestCase):

    def test_shuffle_1(self):
        # Shuffling a non-empty playlist returns True.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        self.assertIs(musicPlayer.shuffle(), True)

    def test_shuffle_2(self):
        # Shuffling an empty playlist returns False and leaves the playlist empty.
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.shuffle(), False)
        self.assertEqual(musicPlayer.playlist, [])

    def test_shuffle_3(self):
        # Shuffling keeps the same songs in the playlist, with no songs added or removed.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3", "song4"]
        musicPlayer.shuffle()
        self.assertEqual(sorted(musicPlayer.playlist), ["song1", "song2", "song3", "song4"])

    def test_shuffle_4(self):
        # Shuffling preserves the length of the playlist and the count of each song, including duplicates.
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song1", "song2"]
        before = len(musicPlayer.playlist)
        musicPlayer.shuffle()
        self.assertEqual(len(musicPlayer.playlist), before)
        self.assertEqual(Counter(musicPlayer.playlist), Counter(["song1", "song1", "song2"]))

    def test_shuffle_5(self):
        # A playlist with a single song returns True and the playlist still holds that one song.
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        self.assertIs(musicPlayer.shuffle(), True)
        self.assertEqual(musicPlayer.playlist, ["song1"])