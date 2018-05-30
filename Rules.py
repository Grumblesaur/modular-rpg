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
  target     = len(attributes) * dice
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
    
  def growth_points():
    '''Growth points are awarded on leveling up, and can be used to
    improve skill proficiencies or purchase perks. Growth points
    can be saved for later use.'''
    return len(attributes)
  
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
  
  def adversary_class(armor, distance, agility_score, intuition_score):
    '''Adversary class determines how resistant to physical damage an actor
    is. Actors roll their attacks against their target's adversary class. AC
    is the sum of 50, any bonus from armor, one tenth of the distance
    between attacker and target (rounded down), and one tenth of the higher
    of Agility and Intuition, rounded down.
    
    Distance is measured in feet.'''
    ac  = 50 + armor + (distance // 10)
    ac += max(agility_score, intuition_score) // 10
    return ac
   
  def hit_point_max_increase(resilience_score):
    '''Upon leveling up, an actor receives an increase in maximum hit
    points equal to 1d10 + 1. Additionally, they receive one tenth of
    their Resilience score, rounded down, to their max HP. For example,
    if the actor has a Resilience score of 37, their max HP increases
    by an additional 3. For actors with negative Resilience scores,
    this factor has a lower bound of zero.
    
    Hit point increases should be calculated after attribute points
    are distributed.'''
    return 1 + max(resilience_score // 10, 0) + random.randint(1,10)
    
  def starting_hit_points(resilience_score):
    '''At first level, an actor starts with a max HP of 10, and adds
    half their Resilience score rounded down or zero, whichever is
    higher.'''
    return max(resilience_score // 2, 0) + 10
  
  def attack(ac, attr_score, weap_prof, dmg_die, s_threat=1, f_threat=1):
    '''When an actor attacks, their attack must meet or beat the
    adversary class of their target. The accuracy of an actor's attack
    is determined by one tenth of the attribute score required by the
    weapon in use and the actor's proficiency with the weapon. The weapon
    (which could just be the actor's fist or foot) has a damage die, a
    success threat, and a failure threat. The success threat determines
    the range of values over which the weapon will roll double the number
    of damage dice.
    
    The failure threat determines the range of values over which the
    attack will automatically miss.
    
    The damage die is a string of the form MdN, where M is the number of
    dice to roll, and N is the number of sides on the die.'''
    
    attr_mod     = attr_score // 10
    dice, sides  = Rules.parse_damage_die(dmg_die)
    roll_damage  = lambda: sum(
      [random.randint(1,sides) for x in range(dice)]
    )
    raw_hit_roll = random.randint(1,100)
    
    critical_status = Rules.attack_crit(raw_hit_roll, s_threat, f_threat)
    if critical_status == Outcomes.Crit_Pass:
      damage = roll_damage() + roll_damage() + attr_mod
    elif critical_status == Outcomes.Crit_Fail:
      damage = 0
    elif critical_status is None:
      hit_total = raw_hit_roll + weap_prof + attr_mod
      if hit_total > ac:
        damage = roll_damage() + attr_mod
      elif hit_total < ac:
        damage = 0
      else:
        damage = min(roll_damage(), roll_damage()) + attr_mod
    return damage
  
  def parse_damage_die(s):
    '''Returns a tuple of `(dice, sides)` from a string `'MdN'` where
    M is the number of dice to roll and N is the number of sides of each
    die.'''
    return tuple(map(int,s.split('d')))

  def attack_crit(roll, s_threat=1, f_threat=1):
    '''Critical attacks naturally have a critical threat range of 1. An
    attacker scores a critical automatically on 100, although if their
    critical threat range is wider than 1, that range expands downward
    from 100. If the threat range is 2, a critical success happens on
    99 or 100. Critical successes and critical failures have differing
    threat ranges, which may be affected by equipment, perks, or other
    things.
    
    Critical failures expand upwards from 1 in a similar manner. If the
    threat range is 2, a critical failure happens on 1 or 2.
    
    Criticals of either type do not need to be confirmed for attacks.'''
    outcome = None
    if roll in range(101-s_threat,101):
      outcome = Outcomes.Crit_Pass
    elif roll in range(1, 1+f_threat):
      outcome = Outcomes.Crit_Fail
    return outcome

  def max_skill_ranks(character_level):
    '''An actor cannot invest more than skill point into a skill proficiency
    than one per their character level plus one.'''
    return character_level + 1

  def skill_check(DC, attribute_score, skill_proficiency, dm_modifier=0):
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
    confirm_if_crit = random.randint(1, 10)
    aggregate = roll + attribute_score + skill_proficiency + dm_modifier
    if roll == 100:
      if confirm_if_crit == 10:
        outcome = Outcomes.Crit_Pass
      else:
        outcome = Outcomes.Pass
    elif roll == 1:
      if confirm_if_crit == 1:
        outcome = Outcomes.Crit_Fail
      else:
        outcome = Outcomes.Fail
    elif aggregate > DC:
      outcome = Outcomes.Pass
    elif aggregate < DC:
      outcome = Outcomes.Fail
    else:
      outcome = Outcomes.Draw
    return outcome

