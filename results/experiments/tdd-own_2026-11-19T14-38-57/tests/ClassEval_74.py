import unittest


import unittest

class AgentTest_add_white_list(unittest.TestCase):

    def test_add_white_list_1(self):
        server = Server()
        self.assertEqual(server.add_white_list(88), [88])

    def test_add_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        result = server.add_white_list(66)
        self.assertCountEqual(result, [88, 66])
        self.assertCountEqual(server.white_list, [88, 66])

    def test_add_white_list_3(self):
        server = Server()
        server.add_white_list(88)
        self.assertIs(server.add_white_list(88), False)

    def test_add_white_list_4(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(88)
        self.assertEqual(server.white_list, [88])

    def test_add_white_list_5(self):
        server = Server()
        self.assertEqual(server.white_list, [])
        result = server.add_white_list(88)
        self.assertEqual(result, server.white_list)
        self.assertIn(88, server.white_list)
        self.assertEqual(len(server.white_list), 1)

class AgentTest_del_white_list(unittest.TestCase):

    def test_del_white_list_1(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.del_white_list(88), [])

    def test_del_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(66)
        result = server.del_white_list(88)
        self.assertEqual(result, [66])
        self.assertEqual(server.white_list, [66])

    def test_del_white_list_3(self):
        server = Server()
        self.assertIs(server.del_white_list(88), False)
        self.assertEqual(server.white_list, [])

    def test_del_white_list_4(self):
        server = Server()
        server.add_white_list(88)
        self.assertIs(server.del_white_list(66), False)
        self.assertEqual(server.white_list, [88])

    def test_del_white_list_5(self):
        server = Server()
        server.add_white_list(88)
        server.del_white_list(88)
        self.assertIs(server.del_white_list(88), False)
        self.assertNotIn(88, server.white_list)
        self.assertEqual(len(server.white_list), 0)

import unittest

class AgentTest_recv(unittest.TestCase):

    def test_recv_1(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.recv({"addr": 88, "content": "abc"}), "abc")

    def test_recv_2(self):
        server = Server()
        server.add_white_list(88)
        self.assertIs(server.recv({"addr": 66, "content": "abc"}), False)

    def test_recv_3(self):
        server = Server()
        self.assertIs(server.recv({"addr": 88, "content": "abc"}), False)

    def test_recv_4(self):
        server = Server()
        server.add_white_list(88)
        server.del_white_list(88)
        self.assertIs(server.recv({"addr": 88, "content": "abc"}), False)

    def test_recv_5(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(66)
        self.assertEqual(server.recv({"addr": 88, "content": "first"}), "first")
        self.assertEqual(server.recv({"addr": 66, "content": "second"}), "second")
        self.assertIs(server.recv({"addr": 22, "content": "third"}), False)

import unittest

class AgentTest_send(unittest.TestCase):

    def test_send_1(self):
        server = Server()
        result = server.send({"addr": 66, "content": "ABC"})
        self.assertIsNone(result)

    def test_send_2(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        self.assertEqual(server.send_struct, {"addr": 66, "content": "ABC"})

    def test_send_3(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("send"), {"addr": 66, "content": "ABC"})

    def test_send_4(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        server.send({"addr": 77, "content": "XYZ"})
        self.assertEqual(server.send_struct, {"addr": 77, "content": "XYZ"})
        self.assertEqual(server.show("send"), {"addr": 77, "content": "XYZ"})

    def test_send_5(self):
        server = Server()
        self.assertEqual(server.white_list, [])
        server.send({"addr": 66, "content": "ABC"})
        self.assertEqual(server.send_struct, {"addr": 66, "content": "ABC"})
        self.assertEqual(server.white_list, [])

import unittest

class AgentTest_show(unittest.TestCase):

    def test_show_1(self):
        server = Server()
        self.assertEqual(server.show("send"), {})

    def test_show_2(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("send"), {"addr": 66, "content": "ABC"})

    def test_show_3(self):
        server = Server()
        self.assertEqual(server.show("receive"), {})

    def test_show_4(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        self.assertIs(server.show("other"), False)

    def test_show_5(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("receive"), {})
        server.send({"addr": 77, "content": "XYZ"})
        self.assertEqual(server.show("send"), {"addr": 77, "content": "XYZ"})