import sys
sys.path.append('..')

from dice_kernel import skill_check
from formatinfo import digest
class Intuition:
  '''Intuition namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Intuition'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_disguise(intuition, proficiency, dc):
  '''Transform into other people, if you have the materials.'''
  return skill_check(intuition, proficiency, dc)

def s_forage(intuition, proficiency, dc):
  '''Scavenge the environment for organic materials.'''
  return skill_check(intuition, proficiency, dc)

def s_listen(intuition, proficiency, dc):
  '''Tune in to nearby sounds.'''
  return skill_check(intuition, proficiency, dc)

def s_look(intuition, proficiency, dc):
  '''Observe your environment.'''
  return skill_check(intuition, proficiency, dc)

def s_search(intuition, proficiency, dc):
  '''Scour the environment for lost items or hidden objects.'''
  return skill_check(intuition, proficiency, dc)

def s_sense_motive(intuition, proficiency, dc):
  '''Get a feel for another's intentions, and the veracity of their
  statements.'''
  return skill_check(intuition, proficiency, dc)

def s_track_creature(intuition, proficiency, dc):
  '''Follow a creature to hunt them.'''
  return skill_check(intuition, proficiency, dc)






# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Intuition, globals())

