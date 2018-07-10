from Enumerations import Damage


class Weapon(object):
  name_default   = '(unarmed)'
  die_default    = '1d4'
  types_default  = [Damage.Bludgeoning]
  range_default  = 0
  reach_default  = 0
  thrown_default = False
  hands_default  = 1
  
  def __init__(self,
      name=name_default,
      die=die_default,
      types=types_default,
      max_range=range_default,
      reach=reach_default,
      thrown=thrown_default,
      hands=hands_default
    ):
    
    self.name        = name
    self.die         = die
    self.types       = types
    self.range       = max_range
    self.reach       = reach
    self.thrown      = thrown
    self.hands       = hands
    self.description = ""
    self.cost        = 0
    self.weight      = 0

  
  fstr = '''{name}:
  {description}
    damage        {die}/{types}
    throwable     {throwable}
    range/reach   {range_}/{reach}
    hands/weight  {hands}/{weight}
    cost          {cost}'''
  
  def __str__(self):
    types = ' | '.join([repr(t).replace('Damage', '') for t in self.types])
    throwable = "yes" if self.thrown else "no"
    return Weapon.fstr.format(
      name=self.name, description=self.description, die=self.die,
      types=self.types, throwable=throwable, range_=self.range,
      reach=self.reach, hands=self.hands, weight=self.weight,
      cost=self.cost
    )

  
  @staticmethod
  def Ranged(name, die, types, max_range, hands):
    return Weapon(
      name, die, types, max_range, reach=0, thrown=False, hands=hands
    )
  
  @staticmethod
  def Thrown(name, die, types, max_range, reach, hands):
    return Weapon(name, die, types, max_range, reach, thrown=True, hands=hands)
  
  @staticmethod
  def Melee(name, die, types, reach, hands):
    return Weapon(
      name, die, types, max_range=0, reach=reach, thrown=False, hands=hands
    )

instances = [
  Weapon.Thrown('dagger', '1d6', [Damage.Piercing, Damage.Slashing], 25, 0, 1)
  
]


if __name__ == "__main__":
  for weapon in instances:
    print(weapon)

