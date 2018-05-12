import random

def default_score(**kwargs):
  return random.randint(0, 60) - 30

def biased_score(**kwargs):
  return sum([random.randint(1,10) for x in range(6)]) - 30

def biased_score2(**kwargs):
  return sum(sorted([random.randint(1,10) for x in range(7)])[1:]) - 30

class Character(object):
  attr_names = [
    'Vigor',     'Resilience', 'Agility', 'Finesse',
    'Knowledge', 'Intuition',  'Allure',  'Presence'
  ]
   
  def __init__(
    self, name,
    attributes={},
    score_gen=default_score,
    **score_gen_args
  ):
    if attributes:
      self.attributes = attributes
    else:
      self.attributes = { }
      for attr in Character.attr_names:
        self.attributes[attr] = default_score(**score_gen_args)
    self.name = name
  
  def __repr__(self):
    return 'Character({name}, {attrs})'.format(
      name=self.name,
      attrs=self.attributes
    )
  
  def __str__(self):
    return repr(self)


if __name__ == "__main__":
  x = Character('Heniele')
  print(x)
  print()
  y = Character('Darcielle', score_gen=biased_score)
  print(y)
  print()
  z = Character('Herenia', score_gen=biased_score)
  print(z)
  print()

