from Enumerations import Damage

class Weapon(object):
  def __init__(self, name, die, dmgtypes, hands):
    self.die   = die
    self.type  = dmgtypes
    self.name  = name
    self.hands = hands
    self.description = ''
    self.cost = 0
  
class Melee(Weapon):
  def __init__(self, weapon_name, damage_die, dmgtypes, reach, hands):
    super(Melee, self).__init__(weapon_name, damage_die, dmgtypes, hands)
    self.reach = reach
  
  header = "Name\tDie\tType\tReach\tHands"
   
  def __repr__(self):
    return "%s\t%s\t%s\t%s\t%s" % (
      self.name, self.die, self.type, self.reach or '-', self.hands
    )
  
class Ranged(Weapon):
  def __init__(self, weapon_name, damage_die, dmgtypes, max_range, hands):
    super(Ranged, self).__init__(weapon_name, damage_die, dmgtypes, hands)
    self.max_range = max_range
  
  header = "Name\tDie\tType\tRange\tHands"
  
  def __repr__(self):
    return "%s\t%s\t%s\t%s\t%s" % (
      self.name, self.die, self.type, self.max_range, self.hands
    )
  
  
class Thrown(Melee, Ranged):
  def __init__(self, name, die, dmgtypes, maxrange, reach, hands):
    Melee.__init__(self, name, die, dmgtypes, reach, hands)
    self.max_range = max_range
  
  header = "Name\tDie\tType\tRange\tReach\tHands"
  
  def __repr__(self):
    return "%s\t%s\t%s\t%s\t%s\t%s" % (
      self.name, self.die, self.type, self.range, self.reach, self.hands
    )


class Sword(Melee):
  def __init__(self, name, die, reach, hands):
    super(Sword, self).__init__(
      name, die, [Damage.Piercing, Damage.Slashing], reach, hands
    )

class Shortsword(Sword):
  def __init__(self, name='Shortsword'):
    super(Shortsword, self).__init__(
      name, '1d8', 0, 1
    )

class Longsword(Sword):
  def __init__(self, name='Longsword'):
    super(Longsword, self).__init__(
      name, '1d10', 0, 2
    )
  
class Dagger(Thrown):
  def __init__(self, name='Dagger'):
    super(Dagger, self).__init__(
      name, '1d6', [Damage.Piercing], 25, 0, 1
    )
    self.description = 'A dagger can be wielded as a melee weapon or thrown.'

class Bow(Ranged):
  def __init__(self, name, die, maxrange):
    super(Bow, self).__init__(
      name, die, [Damage.Piercing], maxrange, 2
    )
  
class Shortbow(Bow):
  def __init__(self, name='Shortbow'):
    super(Shortbow, self).__init__(
      name, '1d6', 150
    )

class Longbow(Bow):
  def __init__(self, name='Longbow'):
    super(Longbow, self).__init__(
      name, '1d6', 300
    )

class CompositeBow(Bow):
  def __init__(self, name='Composite Bow'):
    super(CompositeBow, self).__init__(
      name, '1d6', 225
    )

melee = [
  Shortsword(),
  Longsword(),
]

thrown = [
  Dagger()
]

ranged = [
  Shortbow(),
  CompositeBow(),
  Longbow()
]

if __name__ == "__main__":
  print(Melee.header)
  for weapon in melee:
    print(repr(weapon))
  
  print()
  
  print(Thrown.header)
  for weapon in thrown:
    print(repr(weapon))
  
  print()
  
  print(Ranged.header)
  for weapon in ranged:
    print(repr(weapon))

    
    






