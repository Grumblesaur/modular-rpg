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
  '''Destruction is a school of magic which involves the disintegration of
  matter, the sapping of resources from organic lifeforms, and chain
  reactions. Igniting fires and inducing magical illness are some abilities
  that stem from the school of Destruction. Perks or spells that call for
  Destruction will require a skill check with this skill.'''
  return skill_check(corpus, proficiency, dc)

def s_augmentation(corpus, proficiency, dc):
  '''Augmentation is a school of magic which involves bolstering physical
  size and strength, protecting from or preventing damage, and fine-tuning
  the senses. With Augmentation, a caster might enlarge stick to make a
  better lever, or focus a creature's hearing on distant sounds. Perks or
  spells which call for Augmentation will require this skill check.'''
  return skill_check(corpus, proficiency, dc)

def s_diminution(corpus, proficiency, dc):
  '''Diminution is a school of magic which involves reducing physical size
  and strength, revealing or increasing the weaknesses of creatures and
  objects, and obscuring the senses. With Diminution, a caster might deafen
  an animal to sneak up on it, or shrink a stone to skip across water. Perks
  or skills which call for Diminution will require this skill check.'''
  return skill_check(corpus, proficiency, dc)

 

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Corpus, globals())

