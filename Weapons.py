from Enumerations import Damage


class Weapon(object):
  default_fields = {
    'name' : 'weapon',    # The weapon's moniker or identifier
    'description' : '',   # Optional flavor text.
    'range' : 0,          # Greatest distance for which a thrown or
                          #   launched weapon is effective (unit: tiles).
    'reach' : 1,          # Greatest distance for which a weapon is
                          #   effective without being thrown or launched.
    'two-handed' : False, # Must be wielded with two hands, no exceptions.
    'versatile' : False,  # Can be wielded with one hand if Vigor >= 25.
    'light' : True,       # Can be wielded in off-hand without -10 penalty
                          #   to hit.
    'die' : '1d6',        # Dice algebra string indicating damage output.
    'damage' : [          # List of Damage enum items indicating the types
      Damage.Slashing     #   of damage which can be dealt when wielding
    ],                    #   this weapon.
    'short' : False,      # -10 to hit when attacking with this weapon
                          #   against or as a mounted actor.
    'long' : False,       # -10 to hit when attacking with this weapon
                          #   against a target in an adjacent tile.
    'heavy' : False,      # -10 to hit when attacking with this weapon with
                          #   both Vigor and Resilience below 20.
    'quickdraw' : False,  # Stowing and retrieving this weapon are Tertiary
                          #   actions.
  }
  
  def __init__(self, **kw):
    fields = { }
    self.other = { }
    for key in default_fields:
      if key not in kw:
        fields[key] = default_fields[key]
      elif key not in default_fields:
        self.other[key] = kw[key]
      else:
        fields[key] = kw[key]
    
    self.name        = fields['name']
    self.description = fields['description']
    self.range       = fields['range']
    self.reach       = fields['reach']
    self.two_handed  = fields['two-handed']
    self.versatile   = fields['versatile']
    self.light       = fields['light']
    self.die         = fields['die']
    self.damage      = fields['damage']
    self.short       = fields['short']
    self.long        = fields['long']
    self.heavy       = fields['heavy']
    self.quickdraw   = fields['quickdraw']




if __name__ == "__main__":
  for weapon in instances:
    print(weapon)

