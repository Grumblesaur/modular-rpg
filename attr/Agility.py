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
def s_example(agility, proficiency, dc):
  '''Example skill check.'''
  return dice_kernel.skill_check(agility, proficiency, dc)

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Agility, globals())
