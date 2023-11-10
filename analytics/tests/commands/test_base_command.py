import unittest
from src.commands.base_command import BaseCommannd

class TestBaseCommand(unittest.TestCase):
    def test_execute_raises_not_implemented_error(self):
        command = NewSubclass()
        command.execute()

class NewSubclass(BaseCommannd):
    def execute(self):
        pass