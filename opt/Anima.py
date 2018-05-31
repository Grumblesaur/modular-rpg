from dice_kernel import skill_check
from formatinfo import digest

# Anima namespace. Do not edit the class. Instead, add skills
# and perks below. Prefix skill names with "s_" and perk names with
# "p_". Do not remove the call to "digest" from the bottom of the
# file.

class Anima:
  '''Anima is an attribute which measures an actor's ability to wield their
  mind as a tool to manipulate reality. It models spirit, willpower, and
  concentration.'''
  name   = 'Anima'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_conjuration(anima, proficiency, dc):
  '''Conjuration is a school of magic which involves the creation of
  magical objects and phenomena, such as sudden storms, bound weapons,
  hovering light sources, and others. Perks or spells which call for
  Conjuration will require a check with this skill.'''
  return skill_check(anima, proficiency, dc)

def s_illusion(anima, proficiency, dc):
  '''Illusion is a school of magic which involves the creation of false
  sensory effects and the art of hiding what is plainly seen. Making
  objects or creatures invisible or throwing voices are some things which
  can be done with this skill. Perks or spells which call for Illusion
  will require a skill check with this skill.'''
  return skill_check(anima, proficiency, dc)

def s_divination(anima, proficiency, dc):
  '''Divination is a school of magic which involves supernatural foresight,
  communication with otherworldly beings, and gathering information from
  one's environment. Scrying and dowsing are some things which can be done
  with this skill. Perks or spells which call for Divination will require a
  skill check with this skill.'''
  return skill_check(anima, proficiency, dc)

def s_manipulation(anima, proficiency, dc):
  '''Manipulation is a school of magic which involves mental charms and
  telekinetic forces, for affecting the movement of objects and creatures
  and the mindset of sentient beings. Perks or spells which call for
  Manipulation will require a skill with this check.'''
  return skill_check(anima, proficiency, dc)

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Anima, globals())

