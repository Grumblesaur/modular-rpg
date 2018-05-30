import sys
import random
from Rules import Rules

linewidth = 70

try:
  iterations = int(sys.argv[1])
except IndexError:
  iterations = 10

try:
  debug = bool(sys.argv[2])
except IndexError:
  debug = False

def debug_print(*args):
  if debug:
    for arg in args:
      print(arg,)

def avg(vec):
  return sum(vec) / len(vec)

print('Attribute arrays w/ score total:')
score_arrays = [ ]
score_totals = [ ]
for x in range(iterations):
  p = Rules.score_array()
  random.shuffle(p)
  score_arrays.append(p)
  score_totals.append(sum(p))

debug_print('\t'.join([name[:3] for name in Rules.attributes]))
debug_print('-' * linewidth)
for x in range(len(score_arrays)):
  debug_print('\t'.join(
    list(map(str,score_arrays[x])) + [str(score_totals[x])]
  ))
debug_print('-' * linewidth)
print('avg attribute score:', avg([avg(array) for array in score_arrays]))
print()

print('Attribute arrays w/no target score total:')
notarget_arrays = [ ]
notarget_totals = [ ]
for x in range(iterations):
  p = Rules.score_array(target=None)
  random.shuffle(p)
  notarget_arrays.append(p)
  notarget_totals.append(sum(p))
debug_print('\t'.join([name[:3] for name in Rules.attributes]))
debug_print('-' * linewidth)
for x in range(len(score_arrays)):
  debug_print('\t'.join(
    list(map(str, notarget_arrays[x])) + [str(notarget_totals[x])]
  ))
debug_print('-' * linewidth)
print('avg unbounded attribute score:', avg(
  [avg(array) for array in notarget_arrays])
)
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
debug_print('Some possible lv 1 values are')
debug_print(adversary_classes)
print('avg ac:', avg(adversary_classes))
print()


print('Attack outcomes test')
print('Parameters:')
print("ac is a random value from the previous test's output")
print("attr_score is a random value from the attribute arrays test")
print("weap_prof is a random valuein the range [0,2]")
print("dmg_die is 1d6")
print("s_threat and f_threat are default")
attack_damages = [ ]
for x in range(iterations):
  attack_damages.append(Rules.attack(
    random.choice(adversary_classes),
    random.choice(random.choice(score_arrays)),
    random.choice([0,1,2]),
    "1d6"
  ))
debug_print("some possible attack outcomes:")
debug_print(attack_damages)
print('avg damage:', avg(attack_damages))
print()


print('Level 3 hit points test')
print('Parameters:')
print('resilience_score is a random value from the attribute arrays')
starting_hit_points_values = [ ]
level_three_hp = [ ]
for x in range(iterations):
  resilience = random.choice(random.choice(score_arrays))
  starting_hit_points_values.append(Rules.starting_hit_points(resilience))
  level_three_hp.append(
    starting_hit_points_values[x]
    + Rules.hit_point_max_increase(resilience)
    + Rules.hit_point_max_increase(resilience)
  )  
debug_print('some possible level 3 hit points values:')
debug_print(level_three_hp)
print('avg HP at lv 3:', avg(level_three_hp))
print()




