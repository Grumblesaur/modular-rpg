from dice_kernel import skill_check
from formatinfo import digest
class Presence:
  '''Presence namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Presence'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_blend(presence, proficiency, dc):
  '''Act natural, and disappear within plain sight.'''
  return skill_check(presence, proficiency, dc)

def s_handle_animal(presence, proficiency, dc):
  '''Show a beast who's boss.'''
  return skill_check(presence, proficiency, dc)

def s_intimidate(presence, proficiency, dc):
  '''Instill fear and exude dominance.'''
  return skill_check(presence, proficiency, dc)



# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Presence, globals())

