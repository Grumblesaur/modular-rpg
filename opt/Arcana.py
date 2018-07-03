from dice_kernel import skill_check
from formatinfo import digest
# Arcana namespace. Do not edit the class. Instead, add skills
# and perks below. Prefix skill names with "s_" and perk names with
# "p_". Do not remove the call to "digest" from the bottom of the
# file.

class Arcana:
  '''Arcana is an attribute which measures an actor's ability control and
  influence matter and material. It models an actor's capacity for creativity,
  dominance, and preservation with magic.'''
  name   = 'Arcana'
  skills = { }
  perks  = { }

# Add your skills and perks here
def s_enchantment(arcana, proficiency, dc):
  '''Enchantment is a school of magic which involves the imbuement of objects
  and creatures with magic, both temporary and permanent. Enchantment permits an
  actor to create magical traps or infuse weapons with elemental power, among
  other things. Perks or spells which call for Conjuration will require a check
  with this skill.'''
  return skill_check(arcana, proficiency, dc)

def s_alchemy(arcana, proficiency, dc):
  '''Alchemy is a school of magic which involves the production of substances
  whose properties are a combination and a magnification of those of their
  ingredients. Alchemy can be used to make medicines, poisons, fertilizers,
  and other useful concoctions. Perks or spells which call for Alchemy will
  require a check with this skill.'''
  return skill_check(arcana, proficiency, dc)

def s_transmutation(arcana, proficiency, dc):
  '''Transmutation is a school of magic which involves the conversion of matter
  into different states and forms by magical means, and the morphing of
  creatures into the forms of others'. Transmutation is the method by which
  actors shapeshift and mythic metals are forged. Perks or spells which call
  for Transmutation will require a check with this skill.'''
  return skill_check(arcana, proficiency, dc)

def s_obvocation(arcana, proficiency, dc):
  '''Obvocation is a school of magic which involves projecting one's will and
  spirit into other bodies and other realms. With Obvocation, an actor can warg
  into the senses of other creatures, summon otherwordly spirits, or cast their
  will over another's. Perks or spells which call for Obvocation will require
  a check with this skill.'''
  return skill_check(arcana, proficiency, dc)



# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Arcana, globals())

