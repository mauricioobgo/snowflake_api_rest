from .base_command import BaseCommannd

class Ping(BaseCommannd):
  def __init__(self):
    pass
  def execute(self):
    return "pong"