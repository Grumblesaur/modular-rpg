from enum import Enum

class Action:
  class Types(Enum):
    Movement  = 0
    Primary   = 1
    Secondary = 2
    Tertiary  = 3

  class States(Enum):
    Not_Taken = 0
    Taken     = 1
  
class Turn:
  duration = 6 # seconds
  def __init__(self):
    self.components = {
      Action.Types.Primary   : Action.States.Not_Taken,
      Action.Types.Secondary : Action.States.Not_Taken,
      Action.Types.Tertiary  : Action.States.Not_Taken
      Action.Types.Movement  : Action.States.Taken
    }
  
