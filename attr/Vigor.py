from dice_kernel import skill_check
from formatinfo import digest
class Vigor:
  '''Vigor namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Vigor'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_brawl(vigor, proficiency, dc):
  '''Fight with fist and foot.'''
  return skill_check(agility, proficiency, dc)

def s_climb(vigor, proficiency, dc):
  '''Scale walls, ropes, and slopes.'''
  return skill_check(agility, proficiency, dc)

def s_jump(vigor, proficiency, dc):
  '''Cross gaps and grasp for things just out of reach.'''
  return skill_check(agility, proficiency, dc)

def s_lift(vigor, proficiency, dc):
  '''Hoist heavy objects with your arms'''
  return skill_check(agility, proficiency, dc)

def s_wield_melee(vigor, proficiency, dc):
  '''Fight with a chosen type of melee weapon.'''
  return skill_check(agility, proficiency, dc)


# Fill the namespace without needing to type skill names and description 
# into a crowded dict. Do not remove this call.
digest(Vigor, globals())

