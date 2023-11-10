import unittest
from src.commands.ping_command import Ping

class TestPing(unittest.TestCase):
    def test_execute_returns_pong(self):
        command = Ping()
        result = command.execute()
        self.assertEqual(result, "pong")