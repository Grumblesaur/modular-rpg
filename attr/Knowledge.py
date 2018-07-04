import sys
sys.path.append('..')

from dice_kernel import skill_check
from formatinfo import digest
class Knowledge:
  '''Knowledge namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Knowledge'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_appraise_item(knowledge, proficiency, dc):
  '''Judge the worth of art, craftsmanship, or other items of value.'''
  return skill_check(knowledge, proficiency, dc)

def s_cook_item(knowledge, proficiency, dc):
  '''Prepare and serve a selected type of food, if you have the ingredients.'''
  return skill_check(knowledge, proficiency, dc)

def s_craft_item(knowledge, proficiency, dc):
  '''Create new gear and trinkets of a chosen type, if you have the tools and
  materials.'''
  return skill_check(knowledge, proficiency, dc)

def s_navigate(knowledge, proficiency, dc):
  '''Reconcile your direction with your destination, if you have the tools.'''
  return skill_check(knowledge, proficiency, dc)

def s_play_instrument(knowledge, proficiency, dc):
  '''Perform musically with a chosen instrument, if you have the equipment.'''
  return skill_check(knowledge, proficiency, dc)

def s_recall(knowledge, proficiency, dc):
  '''Flex your mind to remember details which escaped you.'''
  return skill_check(knowledge, proficiency, dc)

def s_repair_item(knowledge, proficiency, dc):
  '''Mend broken objects of a chosen type, if you have the tools and
  materials.'''
  return skill_check(knowledge, proficiency, dc)

def s_treat_disease(knowledge, proficiency, dc):
  '''Tend to illnesses of a chosen type, if you have the materials.'''
  return skill_check(knowledge, proficiency, dc)

def s_treat_injury(knowledge, proficiency, dc):
  '''Tend to injuries of a chosen type, if you have the materials.'''
  return skill_check(knowledge, proficiency, dc)


# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Knowledge, globals())

