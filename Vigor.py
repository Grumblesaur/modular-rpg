from formatinfo import digest
class Vigor:
  '''Vigor namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Vigor'
  skills = { }
  perks  = { }

# Add your skills and perks here

s_climb  = 'Scale walls, cliffs, ropes, or other vertical surfaces.'

s_strike = 'Deal a physical blow not involving a weapon.'
p_smith  = '+5 Vigor while wielding a hammer or axe'



# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Vigor, globals())

