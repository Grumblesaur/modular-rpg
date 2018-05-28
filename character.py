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
  Crit_Fail = -2,
  Fail      = -1,
  Draw      = 0,
  Pass      = 1,
  Crit_Pass = 2







