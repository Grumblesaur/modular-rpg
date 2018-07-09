from enum import Enum
class Outcomes(Enum):
  Fumble  = -2,
  Failure = -1,
  Draw    = 0,
  Pass    = 1,
  Marvel  = 2

class Action:
  class Types(Enum):
    Movement  = 0
    Primary   = 1
    Secondary = 2
    Tertiary  = 3

  class States(Enum):
    Not_Taken = 0
    Taken     = 1

class Damage(Enum):
  Raw         = 0
  Bludgeoning = 1,
  Crushing    = 2,
  Piercing    = 3,
  Slashing    = 4,
  Sonic       = 5,
  Shock       = 6,
  Fire        = 7,
  Frost       = 8,
  Corrosion   = 9,
  Psychic     = 10
 
class Turn:
  '''Each actor's turn consists of a primary action, a secondary
  action, a tertiary action, and a movement. These components may
  be taken in any order, and movement may be split up before,
  between, or after any other components of the turn.'''
  duration = 6 # seconds
  def __init__(self):
    self.components = {
      Action.Types.Primary   : Action.States.Not_Taken,
      Action.Types.Secondary : Action.States.Not_Taken,
      Action.Types.Tertiary  : Action.States.Not_Taken,
      Action.Types.Movement  : Action.States.Not_Taken
    }
  
