import random
from Enumerations import Outcomes

def skill_check(attribute_score, skill_proficiency, dc):
  return crit_check(base_roll(), attribute_score + skill_proficiency, dc)

def base_roll(lower=1, upper=100):
  '''All rolls used to determine an outcome of an event in %rpg are based
  on the roll of a 100-sided die. Damage and healing are generally left to
  smaller value ranges.'''
  return random.randint(lower,upper)

def crit_check(raw_roll, modifier, dc, threat_p=1, threat_f=1):
  '''When an actor rolls within their critical threat ranges, a critical
  confirmation is necessary. By default, both ranges are 1 wide. Critical
  failures occur on 1, and critical passes occur on 100. A wider critical
  pass threat range, such as 3, would cause crits on 98, 99, or 100. A wider
  critical failure threat range, such as 4, would cause crits on 1, 2, 3,
  or 4.
  
  To confirm a critical, a d10 is rolled. If the critical type is a pass,
  and the confirmation is a 10, an extraordinary outcome in favor of the
  player should result. If the confirmation is not a 10, it is an ordinary
  success. If the critical type is a failure, and the confirmation is a 1,
  an extraordinary outcome against the player's intentions should result.
  If the confirmation is not a 1, it is an ordinary failure.
  
  Otherwise, the outcome is left to be decided by whether the roll with
  modifiers exceeds the DC (a pass) or falls short of it (a failure).
  Where the two are equal, it is recommended that the game master hold
  a tiebreaker roll, or determine an appropriate outcome.'''
  pass_upper_bound = 101 # range() uses a half-open interval
  fail_lower_bound = 1
  modded_roll = raw_roll + modifier
  
  confirmation = random.randint(1,10)
  if raw_roll in range(pass_upper_bound - threat_p, pass_upper_bound):
    if confirmation == 10:
      outcome = Outcomes.Marvel
    else:
      outcome = Outcomes.Success
  elif raw_roll in range(fail_lower_bound, fail_lower_bound + threat_f):
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
   
