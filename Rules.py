import sys
sys.path.append('./attr')

import random
from Enumerations import Outcomes
from attr.Vigor import Vigor
from attr.Resilience import Resilience
from attr.Agility import Agility
from attr.Allure import Allure
from attr.Presence import Presence
from attr.Intuition import Intuition
from attr.Knowledge import Knowledge
from attr.Finesse import Finesse
from opt.Arcana import Arcana
from opt.Anima import Anima
from opt.Corpus import Corpus

import dice_kernel

modules = (
  Vigor, Resilience, Agility, Allure,
  Presence, Intuition, Knowledge, Finesse,
  Corpus, Anima, Arcana, 
)

all_skills = { }
all_perks  = { }
attribute_names = [ ]
for module in modules:
  all_skills = {**all_skills, **module.skills}
  all_perks  = {**all_perks,  **module.perks}
  attribute_names.append(module.name)

class Rules:
  # Gameplay Parameters
  attributes = attribute_names
  skills     = all_skills
  perks      = all_perks
  
  # Attribute Score Generation Parameters
  sides      = 10
  dice       = 4
  drop       = 1
  target     = len(attributes) * (dice + 1)
  handicap   = target // 2
  
  def score(sides=sides, dice=dice, drop=drop, handicap=handicap):
    '''Generates a single attribute score.'''
    return sum(
      sorted([random.randint(1, sides) for x in range(dice)])[drop:]
    ) - handicap
  
  def score_array(sides=sides, dice=dice, drop=drop, handicap=handicap,
                  target=target, nscores=len(attributes)):
    '''Generates a full array of attributes, adjusted
    for a target attribute score total.'''
    calc_last_as_diff = target is not None
    array = [
      Rules.score(sides, dice, drop, handicap) for x in
      range(nscores - int(calc_last_as_diff))
    ]
    if calc_last_as_diff:
      array.append(target - sum(array))
    return array
    
  def starting_growth_points():
    '''When creating a character, you have a number of growth points
    equal to three times the number of attributes in use.'''
    return len(attributes) * 3
  
  def growth_points():
    '''Growth points are awarded on leveling up, and can be used to
    improve skill proficiencies or purchase perks. Growth points
    can be saved for later use.'''
    return len(attributes) * 2
  
  def attribute_points(growth_distro, actor_attributes, attribute_focus):
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
      gained = get_growing_attribute(roll, growth_distro)
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
    found = None
    for attribute in growth_distro:
      if roll in growth_distro['attribute']:
        if found is not None:
          raise ValueError('growth distro ranges overlap')
        found = attribute
    if found is None:
      raise ValueError(
        'growth distribution does not define range including %s' % roll
      )
    return found
  
  def growth_distribution(vigor=range(1,13),      resilience=range(13,26),
                          allure=range(26,38),    presence=range(38,51),
                          agility=range(51,63),   finesse=range(63,76),
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
      'Agility' : agility, 'Finesse' : finesse,
      'Knowledge' : knowledge, 'Intuition' : intuition
    }
 
  def initiative(agility_score):
    '''Initiative is a measure of reaction time and preparedness for
    combat. Actors with higher initiative will tend to take their turn
    first at the beginning of a round.
    
    Initiative is re-rolled at the start of each round, to simulate the
    change in the flow of battle. Actors take their turns in order from
    highest to lowest.
    '''
    return dice_kernel.base_roll() + agility_score
 
  def dodge_class(armor, distance, agility_score, intuition_score):
    '''Dodge class determines how resistant to physical damage an actor
    is. Actors roll their attacks against their target's dodge class. DC 
    is the sum of 50, any bonus from armor, one tenth of the distance
    between attacker and target (rounded down), and one tenth of the higher
    of Agility and Intuition, rounded down.
    
    Distance is measured in feet.'''
    ac  = 50 + armor + (distance // 10)
    ac += agility_score // 10
    return ac
   
  def starting_hit_points(resilience_score):
    '''At first level, an actor starts with a max HP of 10, and adds
    half their Resilience score rounded down or zero, whichever is
    higher.'''
    return max(resilience_score // 2, 0) + 10
  
  def max_skill_ranks(character_level):
    '''An actor cannot invest more than skill point into a skill proficiency
    than one per their character level plus one.'''
    return character_level + 1

  def skill_check(DC, attribute_score, skill_proficiency, gm_bonus=0):
    dice_kernel.skill_check(
      attribute_score, skill_proficiency, DC - gm_bonus
    )
  
  
  
