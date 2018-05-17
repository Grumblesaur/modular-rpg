import random

from Vigor import Vigor
from Resilience import Resilience
from Agility import Agility

modules = (Vigor, Resilience, Agility)

all_skills = { }
all_perks  = { }
attribute_names = [ ]
for module in modules:
  all_skills = {**all_skills, **module.skills}
  all_perks  = {**all_perks,  **module.perks}
  attribute_names.append(module.name)

class Params:
  # Gameplay Parameters
  attributes = attribute_names
  skills     = all_skills
  perks      = all_perks
  
  # Attribute Score Generation Parameters
  sides      = 10
  dice       = 4
  drop       = 1
  target     = len(attributes) * dice
  handicap   = target // 2
  
  def score(sides=sides, dice=dice, drop=drop, handicap=handicap):
    '''Generates a single attribute score.'''
    return sum(
      sorted([random.randint(1, sides) for x in range(dice)])[drop:]
    ) - handicap
  
  def score_array(sides=sides, dice=dice, drop=drop, handicap=handicap,
                  target=target, nscores=len(attributes):
    '''Generates a full array of attributes, adjusted
    for a target attribute score total.'''
    calc_last_as_diff = target is not None
    array = [
      score(sides, dice, drop, handicap) for x in
      range(nscores - int(calc_last_as_diff))
    ]
    if calc_last_as_diff:
      array.append(target - sum(array))
    return array
    
  def growth_points(n=len(attributes)):
    '''Growth points are a resource which can be distributed
    a character's attributes upon each level.'''
  
    

