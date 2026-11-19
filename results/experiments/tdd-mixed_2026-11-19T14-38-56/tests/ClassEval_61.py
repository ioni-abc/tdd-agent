import unittest




class MusicPlayerTestPlay(unittest.TestCase):
    def test_play(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.play(), "song1")

    def test_play_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = []
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.play(), None)

    def test_play_3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        self.assertEqual(musicPlayer.play(),False)

import unittest

class AgentTest_play(unittest.TestCase):
    def test_play_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.play(), "song2")

    def test_play_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        musicPlayer.play()
        self.assertEqual(musicPlayer.current_song, "song1")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2"])

class MusicPlayerTestAddSong(unittest.TestCase):
    def test_add_song(self):
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song1"])

    def test_add_song2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        musicPlayer.add_song("song2")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2"])

    def test_add_song3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.add_song("song1")
        musicPlayer.add_song("song2")
        musicPlayer.add_song("song3")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2", "song3"])

class AgentTest_add_song(unittest.TestCase):
    def test_add_song_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.add_song("song3")
        self.assertEqual(musicPlayer.playlist, ["song1", "song2", "song3"])

    def test_add_song_2(self):
        musicPlayer = MusicPlayer()
        result = musicPlayer.add_song("song1")
        self.assertIsNone(result)

class MusicPlayerTestStop(unittest.TestCase):
    def test_stop(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.stop(), True)

    def test_stop_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = []
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.stop(), True)

    def test_stop_3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        self.assertEqual(musicPlayer.stop(), False)

import unittest

class AgentTest_stop(unittest.TestCase):
    def test_stop_1(self):
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.stop(), False)

    def test_stop_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1"]
        musicPlayer.current_song = "song1"
        self.assertIs(musicPlayer.stop(), True)

class MusicPlayerTestRemoveSong(unittest.TestCase):
    def test_remove_song(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song2"])

    def test_remove_song2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.current_song = "song1"
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song2", "song3"])

    def test_remove_song3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.current_song = "song1"
        musicPlayer.playlist = ["song1", "song2", "song3", "song4"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song2", "song3", "song4"])

    def test_remove_song4(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3", "song4", "song5"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, ["song2", "song3", "song4", "song5"])

class AgentTest_remove_song(unittest.TestCase):
    def test_remove_song_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.remove_song("song2")
        self.assertEqual(musicPlayer.playlist, ["song1", "song3"])

    def test_remove_song_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1"]
        musicPlayer.remove_song("song1")
        self.assertEqual(musicPlayer.playlist, [])

class MusicPlayerTestSwitchSong(unittest.TestCase):
    def test_switch_song(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.switch_song(), True)

    def test_switch_song2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.switch_song(), False)

    def test_switch_song3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song3"
        self.assertEqual(musicPlayer.switch_song(), False)

import unittest

class AgentTest_switch_song(unittest.TestCase):
    def test_switch_song_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song1"
        musicPlayer.switch_song()
        self.assertEqual(musicPlayer.current_song, "song2")

    def test_switch_song_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = []
        musicPlayer.current_song = None
        self.assertIs(musicPlayer.switch_song(), False)

class MusicPlayerTestPreviousSong(unittest.TestCase):
    def test_previous_song(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.previous_song(), True)

    def test_previous_song2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.previous_song(), False)

    def test_previous_song3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song3"
        self.assertEqual(musicPlayer.previous_song(), True)

class AgentTest_previous_song(unittest.TestCase):
    def test_previous_song_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        musicPlayer.current_song = "song2"
        musicPlayer.previous_song()
        self.assertEqual(musicPlayer.current_song, "song1")

    def test_previous_song_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = []
        musicPlayer.current_song = None
        self.assertIs(musicPlayer.previous_song(), False)

class MusicPlayerTestSetVolume(unittest.TestCase):
    def test_set_volume(self):
        musicPlayer = MusicPlayer()
        self.assertEqual(musicPlayer.set_volume(50), None)
        self.assertEqual(musicPlayer.volume, 50)

    def test_set_volume2(self):
        musicPlayer = MusicPlayer()
        self.assertEqual(musicPlayer.set_volume(100), None)
        self.assertEqual(musicPlayer.volume, 100)

    def test_set_volume3(self):
        musicPlayer = MusicPlayer()
        self.assertEqual(musicPlayer.set_volume(0), None)
        self.assertEqual(musicPlayer.volume, 0)

import unittest

class AgentTest_set_volume(unittest.TestCase):
    def test_set_volume_1(self):
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(75), True)
        self.assertEqual(musicPlayer.volume, 75)

    def test_set_volume_2(self):
        musicPlayer = MusicPlayer()
        self.assertIs(musicPlayer.set_volume(101), False)
        self.assertEqual(musicPlayer.volume, 50)

class MusicPlayerTestShuffle(unittest.TestCase):
    def test_shuffle(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        self.assertEqual(musicPlayer.shuffle(), True)

    def test_shuffle_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = []
        musicPlayer.current_song = "song1"
        self.assertEqual(musicPlayer.shuffle(), False)

    def test_shuffle_3(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2"]
        musicPlayer.current_song = "song2"
        self.assertEqual(musicPlayer.shuffle(), True)

import unittest

class AgentTest_shuffle(unittest.TestCase):
    def test_shuffle_1(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1", "song2", "song3"]
        result = musicPlayer.shuffle()
        self.assertEqual(result, True)
        self.assertCountEqual(musicPlayer.playlist, ["song1", "song2", "song3"])
        self.assertEqual(len(musicPlayer.playlist), 3)

    def test_shuffle_2(self):
        musicPlayer = MusicPlayer()
        musicPlayer.playlist = ["song1"]
        self.assertEqual(musicPlayer.shuffle(), True)
        self.assertEqual(musicPlayer.playlist, ["song1"])