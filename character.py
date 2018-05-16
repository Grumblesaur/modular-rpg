import random
from enum import Enum

"""Tabletop rules described algorithmically."""


def params():
  '''The recommended parameters for attribute design are:
     SIDES: Ten sides to the stat creation die, numbered 1 through 10.
     DICE:  The number of dice rolled in the creation of each attribute.
     DROP:  The number of dice to discount, starting from the lowest value.
     TARGET TOTAL: The desired total of a character's attribute scores.
     HANDICAP: An amount to subtract from each generated attribute score.'''

  ATTRIBUTE_NAMES = [
    'Vigor',     'Resilience', 'Agility', 'Finesse',
    'Knowledge', 'Intuition',  'Allure',  'Presence'
  ]
  SIDES        = 10
  DICE         = 4
  DROP         = 1
  TARGET_TOTAL = len(ATTRIBUTE_NAMES) * DICE
  HANDICAP     = TARGET_TOTAL // 2
  SKILL_NAMES = [ ] #TODO: add some skills
  class P:
    def __init__(self, **kwargs):
      self.ATTRIBUTE_NAMES = kwargs['ATTRIBUTE_NAMES']
      self.SIDES = kwargs['SIDES']
      self.DICE  = kwargs['DICE']
      self.DROP  = kwargs['DROP']
      self.TARGET_TOTAL = kwargs['TARGET_TOTAL']
      self.HANDICAP     = kwargs['HANDICAP']
      self.SKILL_NAMES  = kwargs['SKILL_NAMES']
  return P(**locals())

Params = params()

def attribute_score(sides=Params.SIDES, dice=Params.DICE,
                    drop=Params.DROP, handicap=Params.HANDICAP):
  '''The default rule for rolling an attribute is 4d10h3 - 15.'''
  return sum(sorted(
    [random.randint(1, sides) for x in range(dice)]
  )[drop:]) - handicap

def attribute_array(sides=Params.SIDES, dice=Params.DICE, drop=Params.DROP,
                    handicap=Params.HANDICAP, names=Params.ATTRIBUTE_NAMES,
                    target=Params.TARGET_TOTAL):
  '''If there is a target attribute total, the last attribute is calculated
     by subtracting the sum of the all scores but the last attribute and
     subtracting them from the target attribute total.'''
  out = [attribute_score(
    sides, dice, drop, handicap
  ) for x in range(len(names) - int(target is not None))]
  if target is not None:
    out.append(target - sum(out))
  return out

def growth_points(n=len(Params.ATTRIBUTE_NAMES)):
  '''Growth points are points which can be distributed among
     a character's attributes upon each level.'''
  return n / 2

def skill_points(n=len(Params.SKILL_NAMES)):
  '''Skill points are points which can be distributed among
     a character's skill proficiencies upon each level.'''
  return n / 4

def max_skill_ranks(character_level):
  '''The greatest number of points that can be allocated to a skill
     proficiency is one greater than the character's level.
     Bonuses from equipment, boons, or other things granted by the
     dungeon master are not subject to this limitation.'''
  return character_level + 1

def skill_proficiency_cap():
  '''Proficiency is capped to create bounded accuracy. The cap limits
     the total of all allocations to a skill proficiency, including
     skill ranks, equipment, boons, perks, and other sources.'''
  return 30

class Outcomes(Enum):
  CRIT_FAIL = -2,
  FAIL      = -1,
  DRAW      = 0,
  PASS      = 1,
  CRIT_PASS = 2

def skill_check(DC, relevant_attribute_score, skill_proficiency, dm_modifier=0):
  '''When a character makes a skill check, they roll 1d100. When they roll
     1 or 100, it is possible they may score a critical fail or pass,
     respectively. A d10 is used to confirm a crit. A 10 confirms 100 as a
     critical pass, while 9 and below indicate an ordinary pass. A 1
     confirms 1 as a critical fail, while 2 and above indicate an ordinary
     fail. Critical passes and fails are, at the DM's discretion, intended
     to be extraordinary, but can be forgone as a rule if appropriate for
     the game.
     
     Otherwise, the outcome is a pass when the sum of the player's skill
     proficiency, the score of the attribute relevant to the skill, and any
     additional bonus or handicap added by the DM as the situation might
     call for exceeds the difficulty class (DC) of the check. When the DC
     exceeds the sum, the outcome is a fail. When the two values are
     exactly equal, the outcome is a draw, and the DM is advised to make a
     ruling or commence a tiebreaker roll or coinflip.'''
     
  roll = random.randint(1, 100)
  confirm_if_crit = (1, 10)
  aggregate = roll + relevant_attribute_score + skill_proficiency + dm_modifier
  if roll == 100:
    if confirm_if_crit == 10:
      outcome = Outcomes.CRIT_PASS
    else:
      outcome = Outcomes.PASS
  elif roll == 1:
    if confirm_if_crit == 1:
      outcome = Outcomes.CRIT_FAIL
    else:
      outcome = Outcomes.FAIL
  elif aggregate > DC:
    outcome = Outcomes.PASS
  elif aggregate < DC:
    outcome = Outcomes.FAIL
  else:
    outcome = Outcomes.DRAW
  return outcome






