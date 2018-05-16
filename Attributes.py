from Vigor import Vigor
from Resilience import Resilience
from Agility import Agility

modules = (Vigor, Resilience, Agility)

all_skills = { }
all_perks  = { }
for module in modules:
  all_skills = {**all_skills, **module.skills}
  all_perks  = {**all_perks,  **module.perks}

print(all_skills)
print(all_perks)
