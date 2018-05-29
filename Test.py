import sys
import random
from Rules import Rules

linewidth = 70

try:
  iterations = sys.argv[1]
except IndexError:
  iterations = 10


print('Attribute arrays w/ score total:')
score_arrays = [ ]
score_totals = [ ]
for x in range(iterations):
  p = Rules.score_array()
  score_arrays.append(p)
  score_totals.append(sum(p))

print('\t'.join([name[:3] for name in Rules.attributes]))
print('-' * linewidth)
for x in range(len(score_arrays)):
  print('\t'.join(list(map(str, score_arrays[x])) + [str(score_totals[x])]))
print('-' * linewidth)
print()

print('Adversary class test')
print('Parameters:')
print('armor_value is 0; distance is 0; agility_score and intuition_score are')
print('random numbers from the previous score arrays')
adversary_classes = [ ]
for x in range(iterations):
  adversary_classes.append(Rules.adversary_class(
    0,
    0,
    random.choice(random.choice(score_arrays)),
    random.choice(random.choice(score_arrays))
  ))
print('Some possible lv 1 values are')
print(adversary_classes)
print()

print('Attack outcomes test')
print('Parameters:')
print("ac is a random value from the previous test's output; attr_score is a")
print("random value from the Attribute arrays test; weap_prof is a random value")
print("in the range [0,2]; dmg_die is 1d6; s_threat and f_threat are default")
attack_damages = [ ]
for x in range(iterations):
  attack_damages.append(Rules.attack(
    random.choice(adversary_classes),
    random.choice(random.choice(score_arrays)),
    random.choice([0,1,2]),
    "1d6"
  ))
print("some possible attack outcomes:")
print(attack_damages)
print()




