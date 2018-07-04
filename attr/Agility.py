import sys
sys.path.append('..')

from dice_kernel import skill_check
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
  '''Move with rhythm to entertain, seduce, or summon.'''
  return skill_check(agility, proficiency, dc)

def s_hide(agility, proficiency, dc):
  '''Conceal yourself in difficult spaces with your flexibility.'''
  return skill_check(agility, proficiency, dc)

def s_sneak(agility, proficiency, dc):
  '''Stalk or skulk and stay out of sight with fleetness of foot.'''
  return skill_check (agility, proficiency, dc)


# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Agility, globals())

