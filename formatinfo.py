import util

def wordcase(s):
  return ' '.join([word.capitalize() for word in s.split(' ')])

skill_tag = 's_'
perk_tag  = 'p_'

def digest(cls, scope_dict):
  for key in scope_dict:
    if key.startswith(skill_tag):
      skill = key.replace(skill_tag, '')
      skill = util.wordcase(skill.replace('_',' '))
      cls.skills[skill] = (cls.name, scope_dict[key])
    elif key.startswith(perk_tag):
      perk = key.replace(perk_tag, '')
      perk = util.wordcase(perk.replace('_', ' '))
      cls.perks[perk] = (cls.name, scope_dict[key])
  
