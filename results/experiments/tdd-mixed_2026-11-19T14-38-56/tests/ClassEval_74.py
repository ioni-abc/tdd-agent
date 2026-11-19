import unittest




class ServerTestAddWhiteList(unittest.TestCase):
    def test_add_white_list_1(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.white_list, [88])

    def test_add_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.add_white_list(88), False)

    def test_add_white_list_3(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(11)
        self.assertEqual(server.add_white_list(11), False)

import unittest

class AgentTest_add_white_list(unittest.TestCase):
    def test_add_white_list_1(self):
        server = Server()
        self.assertEqual(server.add_white_list(88), [88])

    def test_add_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.add_white_list(11), [88, 11])
        self.assertEqual(server.white_list, [88, 11])

class ServerTestDelWhiteList(unittest.TestCase):
    def test_del_white_list_1(self):
        server = Server()
        server.add_white_list(88)
        server.del_white_list(88)
        self.assertEqual(server.white_list, [])

    def test_del_white_list_2(self):
        server = Server()
        self.assertEqual(server.del_white_list(88), False)

    def test_del_white_list_3(self):
        server = Server()
        self.assertEqual(server.del_white_list(11), False)

class AgentTest_del_white_list(unittest.TestCase):
    def test_del_white_list_1(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(11)
        server.add_white_list(22)
        self.assertEqual(server.del_white_list(11), [88, 22])
        self.assertEqual(server.white_list, [88, 22])

    def test_del_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(11)
        self.assertEqual(server.del_white_list(33), False)
        self.assertEqual(server.white_list, [88, 11])

class ServerTestRecv(unittest.TestCase):
    def test_recv_1(self):
        server = Server()
        server.add_white_list(88)
        server.recv({"addr": 88, "content": "abc"})
        self.assertEqual(server.receive_struct, {"addr": 88, "content": "abc"})

    def test_recv_2(self):
        server = Server()
        server.add_white_list(88)
        flag = server.recv({"addr": 66, "content": "abc"})
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, False)

    def test_recv_3(self):
        server = Server()
        flag = server.recv([88])
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, -1)

class AgentTest_recv(unittest.TestCase):
    def test_recv_1(self):
        server = Server()
        server.add_white_list(88)
        result = server.recv({"addr": 88, "content": "abc"})
        self.assertEqual(result, "abc")

    def test_recv_2(self):
        server = Server()
        server.add_white_list(88)
        server.recv({"addr": 88, "content": "abc"})
        flag = server.recv({"addr": 66, "content": "xyz"})
        self.assertEqual(flag, False)
        self.assertEqual(server.receive_struct, {"addr": 88, "content": "abc"})

class ServerTestSend(unittest.TestCase):
    def test_send_1(self):
        server = Server()
        server.send({"addr": 88, "content": "abc"})
        self.assertEqual(server.send_struct, {"addr": 88, "content": "abc"})

    def test_send_2(self):
        server = Server()
        flag = server.send({"addr": 88})
        self.assertEqual(flag, "info structure is not correct")

    def test_send_3(self):
        server = Server()
        flag = server.send({"content": "abc"})
        self.assertEqual(flag, "info structure is not correct")

import unittest

class AgentTest_send(unittest.TestCase):
    def test_send_1(self):
        server = Server()
        result = server.send({"addr": 66, "content": "ABC"})
        self.assertIsNone(result)

    def test_send_2(self):
        server = Server()
        server.send({"addr": 66, "content": "ABC"})
        server.send({"addr": 88, "content": "xyz"})
        self.assertEqual(server.send_struct, {"addr": 88, "content": "xyz"})

class ServerTestShow(unittest.TestCase):
    def test_show_1(self):
        server = Server()
        server.add_white_list(66)
        server.send({"addr": 88, "content": "abc"})
        server.recv({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("send"), {"addr": 88, "content": "abc"})

    def test_show_2(self):
        server = Server()
        server.add_white_list(66)
        server.send({"addr": 88, "content": "abc"})
        server.recv({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("receive"), {"addr": 66, "content": "ABC"})

    def test_show_3(self):
        server = Server()
        server.add_white_list(66)
        server.send({"addr": 88, "content": "abc"})
        server.recv({"addr": 66, "content": "ABC"})
        self.assertEqual(server.show("abcdefg"), False)

import unittest

class AgentTest_show(unittest.TestCase):
    def test_show_1(self):
        server = Server()
        self.assertEqual(server.show("send"), {})

    def test_show_2(self):
        server = Server()
        server.add_white_list(66)
        server.recv({"addr": 66, "content": "ABC"})
        server.recv({"addr": 88, "content": "xyz"})
        self.assertEqual(server.show("receive"), {"addr": 66, "content": "ABC"})