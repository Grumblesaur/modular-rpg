import sys
sys.path.append('..')

from dice_kernel import skill_check
from formatinfo import digest
class Finesse:
  '''Finesse namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Finesse'
  skills = { }
  perks  = { }

def s_draw(finesse, proficiency, dc):
  '''Sketch objects, creatures, and scenes.'''
  return skill_check(finesse, proficiency, dc)
# Add your skills and perks here
def s_fasten(finesse, proficiency, dc):
  '''(2 GP) Secure objects and creatures with straps and knots.'''
  return skill_check(finesse, proficiency, dc)

def s_handwrite(finesse, proficiency, dc):
  '''(2 GP) Forge signatures, calligraph documents, and compare handwriting.'''
  return skill_check(finesse, proficiency, dc)

def s_tamper(finesse, proficiency, dc):
  '''(2 GP) Pick locks, disarm traps, and maneuver small objects.'''
  return skill_check(finesse, proficiency, dc)

def s_wield_aimed(finesse, profifiency, dc):
  '''(1 GP) Fight with weapons which require precision distance shots.'''
  return skill_check(finesse, proficiency, dc)


# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Finesse, globals())

