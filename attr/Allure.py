import sys
sys.path.append('..')

from dice_kernel import skill_check
from formatinfo import digest
class Allure:
  '''Allure namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Allure'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_bargain(allure, proficiency, dc):
  '''(2 GP) Haggle with vendors and strike deals.'''
  return skill_check(allure, proficiency, dc)

def s_charm(allure, proficiency, dc):
  '''(2 GP) Influence others with your wit and silver tongue.'''
  return skill_check(allure, proficiency, dc)

def s_deceive(allure, proficiency, dc):
  '''(2 GP) Lie, distract, and equivocate.'''
  return skill_check(allure, proficiency, dc)

def s_investigate(allure, proficiency, dc):
  '''(2 GP) Query locals for information.'''
  return skill_check(allure, proficiency, dc)

def s_persuade(allure, proficiency, dc):
  '''(2 GP) Influence others with sound statements and facts.'''
  return skill_check(allure, proficiency, dc)

def s_sing(allure, proficiency, dc):
  '''(2 GP) Create music of the voice.'''
  return skill_check(allure, proficiency, dc)



# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Allure, globals())

