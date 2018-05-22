import dice_kernel
from formatinfo import digest
class Agility:
  '''Agility namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Agility'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_dance(agility, proficiency, dc):
  '''Move rhythmically on your feet.'''
  return dice_kernel.skill_check(agility, proficiency, dc)

def p_artful_dodger():
  '''Actors with this perk are performant with acrobatic
  evasive maneuvers when fewer than three other actors
  are within 10 feet of them.'''
  return {
    'defense bonus' : 1,
    'condition' : 'fewer than 3 other actors within 10 feet'
  }

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Agility, globals())

