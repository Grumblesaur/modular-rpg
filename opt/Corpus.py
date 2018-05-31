from dice_kernel import skill_check
from formatinfo import digest
class Corpus:
  '''Corpus namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Corpus'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_restoration(corpus, proficiency, dc):
  '''Restoration is a school of magic which involves the mending of wounds
  and broken objects, the revivification or enthrallment of mortal
  creatures, and the purification of substances. Should a perk or a spell
  call for Restoration, it will require a skill check with this skill.'''
  return skill_check(corpus, proficiency, dc)

def s_destruction(corpus, proficiency, dc):
  '''Destruction is a school of magic which involves...'''
  return skill_check(corpus, proficiency, dc)

def s_augmentation(corpus, proficiency, dc):
  '''Augmentation is a school of magic which involves...'''
  return skill_check(corpus, proficiency, dc)

def s_diminution(corpus, proficiency, dc):
  '''Diminution is a school of magic which involves...'''
  return skill_check(corpus, proficiency, dc)

 

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Corpus, globals())

