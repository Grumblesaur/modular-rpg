from formatinfo import digest
class Resilience:
  '''Resilience namespace. Do not edit the class. Instead, add skills
  and perks below. Prefix skill names with "s_" and perk names with
  "p_". Do not remove the call to "digest" from the bottom of the
  file.'''
  name   = 'Resilience'
  skills = { }
  perks  = { }

# Add your skills and perks here

s_swim = 'Move through deep water by your arms and legs.'
p_tough = 'Gain an extra 1HP per level.'

# Fill the namespace without needing to type skill names and descriptions
# into a crowded dict. Do not remove this call.
digest(Resilience, globals())

