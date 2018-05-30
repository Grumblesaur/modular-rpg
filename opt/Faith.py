from dice_kernel import skill_check
from formatinfo import digest
class Faith:
  '''Faith namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Faith'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_example(faith, proficiency, dc):
  '''Example skill check.'''
  return skill_check(faith, proficiency, dc)

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Faith, globals())

