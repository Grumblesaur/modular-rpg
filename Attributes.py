import random

from attr.Vigor import Vigor
from attr.Resilience import Resilience
from attr.Agility import Agility
from attr.Allure import Allure
from attr.Presence import Presence
from attr.Intuition import Intuition
from attr.Knowledge import Knowledge
from attr.Dexterity import Dexterity

modules = (
  Vigor, Resilience, Agility, Allure,
  Presence, Intuition, Knowledge, Dexterity
)

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
    
  def growth_points():
    '''Growth points are awarded on leveling up, and can be used to
    improve skill proficiencies or purchase perks. Growth points
    can be saved for later use.'''
    return len(attributes)
  
  def attribute_points(growth_distribution, actor_attributes, attribute_focus):
    '''Attribute points are awarded on leveling up, and are used to
    improve the attribute score of an actor. Attribute points are
    distributed semi-randomly.
    
    The growth distribution is a table 1-100 defining stat growth
    probabilities.
    The actor attributes are in a table, which will be mutated.
    The attribute focus is a list of the attributes which will
    be bolstered by one point. An attribute can be bolstered
    by multiple points by including its name twice.
    
    If more attribute names are included than the player has points
    to spend, the names for which there are no points are discarded.
    As such, order matters. If the player does not select attributes
    to focus growth in, those points will be spent at random.
    
    The random growths will be selected via the included growth
    distro, and the delta of all growths will be returned from
    the function.'''
    total_points   = (len(attributes) // 2) + 1
    focused_growth = total_points // 2
    random_growth  =  total_points - focused_growth
    growths_delta = { }
    for x in range(focused_growth):
      try:
        gained = attribute_focus[x]
        actor_attributes[attr_name] += 1
        try:
          growths_delta[gained] += 1
        except KeyError:
          growths_delta[gained] = 1
      except IndexError:
        random_growth += 1
    
    for y in range(random_growth):
      roll = random.randint(1,100)
      gained = get_growing_attribute(roll, growth_distribution)
      actor_attributes[gained] += 1
      try:
        growths_delta[gained] += 1
      except KeyError:
        growths_delta[gained] = 1
    
    return growths_delta
    
  def get_growing_attribute(roll, growth_distro):
    '''Searches the growth distribution table for the roll and
    returns the name of the attribute to be incremented. If the
    roll value is not found, an exception is raised reporting
    the roll value which failed.'''
    for attribute in growth_distro:
      if roll in growth_distro['attribute']:
        return attribute
    raise ValueError('growth distribution does not define range including %s' % roll)
  
  def growth_distribution(vigor=range(1,13),      resilience=range(13,26),
                          allure=range(26,38),    presence=range(38,51),
                          agility=range(51,63),   dexterity=range(63,76),
                          knowledge=range(76,88), intuition=range(88,101)):
    '''The growth distribution determines the weight for the
    random portion of attribute growths. These distributions
    are fixed upon character creation. A player may select
    whatever distribution they like meeting the following conditions:
    
      1) The ranges do not overlap (one random number cannot boost two
         attribute scores).
      2) Every range has at least one value (i.e. every attribute should
         have at least a 1% change to grow).
      3) The upper and lower bounds of each range fall between 1 and 100
         (since the stat boost is randomly applied via d%).
      4) The ranges are contiguous (they don't skip numbers).
      5) The bounds of the ranges are integers.
    
    The default array gives a roughly-even frequency to each attribute.'''

    for table_range in locals().items():
      if not len(items[1]):
        raise ValueError('%s cannot have empty range.' % items[0])
    
    return {
      'Vigor' : vigor, 'Resilience' : resilience,
      'Allure' : allure, 'Presence' : presence,
      'Agility' : agility, 'Dexterity' : dexterity,
      'Knowledge' : knowledge, 'Intuition' : intuition
    }
    
    
     
    

