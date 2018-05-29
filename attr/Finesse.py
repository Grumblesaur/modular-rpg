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

# Add your skills and perks here
def s_example(finesse, proficiency, dc):
  '''Example skill check.'''
  return skill_check(finesse, proficiency, dc)

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Finesse, globals())
