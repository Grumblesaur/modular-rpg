import random
from enum import Enum
class Outcomes(Enum):
  Critical = 2
  Success  = 1
  Draw     = 0
  Failure  = -1
  Fumble   = -2


def skill_check(attribute_score, skill_proficiency, dc):
  return crit_check(base_roll(), attribute_score + skill_proficiency, dc)

def base_roll(lower=1, upper=100):
  return random.randint(lower,upper)

def crit_check(raw_roll, modded_roll, dc):
  confirmation = random.randint(1,10)
  if raw_roll == 100:
    if confirmation == 10:
      outcome = Outcomes.Critical
    else:
      outcome = Outcomes.Success
  elif raw_roll == 1:
    if confirmation == 1:
      outcome = Outcomes.Fumble
    else:
      outcome = Outcomes.Failure
  else:
    if modded_roll > dc:
      outcome = Outcomes.Success
    elif modded_roll < dc:
      outcome = Outcomes.Failure
    else:
      outcome = Outcomes.Draw
  return outcome
    
