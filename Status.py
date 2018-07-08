def max_hit_points(resilience_at_level_one):
  '''Hit points are a measure of an actor's combat readiness. They are an
  aggregate of physical health (accounting for disease and injuries),
  mental state, and will to fight and take risks. A human actor's maximum
  hit points are fixed, barring extraordinary circumstances, at 35 + half
  of their starting Resilience score, rounded down. This does not change as
  Resilience grows.'''
  return 35 + resilience_at_level_one // 2

def hit_point_recovery(resilience):
  '''On completion of a short rest, an actor recovers a small portion of
  their hit points. Under certain conditions, such as suffering from
  virulent diseases, or with an especially low resilience score, it is
  possible that an actor's recovery can cause them to lose hit points.
  
  Ordinarily, Resilience scores that low are not achievable by players,
  even at level one. On a long rest, all of an actor's hit points are
  restored, barring extraordinary circumstances.'''
  return 5 + resilience // 10

def max_vitality_points():
  '''Vitality points are a measure of an actor's ability to withstand
  physical shock. Severe attacks cause injuries that require greater
  recovery times and more rest. Player characters are given a maximum of
  3 vitality points, although under some extraordinary circumstances,
  this amount can be different or can change.
  
  An actor's maximum vitality points do not grow or progress with any
  attributes. Changes to this value should related to events in the story
  of the actor.'''
  return 3

def vital_threshold(resilience_at_level_one):
  '''An actor's vital threshold is the amount of damage which will
  incur a vital hit against them. Vital hits diminish an actor's VP.
  An actor's vitality threshold is fixed from level one at 10 + one tenth
  of their starting resilience score (rounded down).'''
  return 10 + resilience_at_level_one // 10

def damage(is_hit, how_hard, vital_threshold, vp, hp):
  '''When an actor is attacked, the amount of damage they take determines
  whether they suffer a normal hit or a vital hit. A vital hit meets or
  exceeds their vital threshold (VT). On a successful hit, a target always
  takes damage to their HP, but will lose 1 VP on a vital hit as well.
  
  If an attack deals enough damage to reach VT multiple times over, the
  target suffers as many times VP damage. For example, with VT = 10:
  
    10-19 damage: 1 VP
    20-29 damage: 2 VP
    30-39 damage: 3 VP
  
  Or with VT = 5:
  
      5-9 damage: 1 VP
    10-14 damage: 2 VP
    15-19 damage: 3 VP
  
  When an actor drops to 0 HP, but they still have nonzero VP, they are
  Incapacitated, and their VT drops to half its usual value. Such an actor
  loses the movement portion of their turn, and is lying down on the
  ground. They cannot use weapons or items which would require an upright
  posture.
  
  When an actor drops to 0 VP, they become Unconscious and their VT drops
  to 0. They are unable to move on their own and don't respond to attempts
  to rouse them. After a short rest, they will regain consciousness, a
  small amount of HP, 1 VP, and 1 Exhaustion Point (EP).
  
  An actor dies when their VP drops below 0, or if their exhaustion rises
  above their maximum VP.'''
  state = 'normal'
  if is_hit:
    if how_hard > vital_threshold:
      try:
        vp -= how_hard //= vital_threshold
      except ZeroDivisionError:
        vp -= -1
        state = 'dead'
    hp -= how_hard
  
  if vp == 0:
    state = 'unconscious'
  elif vp != 0 and hp <= 0:
    hp = 0
    state = 'incapacitated'
  return (hp, vp, state)

def vitality_point_recovery(vp, ep):
  '''If an actor is suffering from exhaustion (EP > 0), they lose one point
  of exhaustion per long rest. An actor must recover from their exhaustion
  before they can recover any VP.
  
  If an actor is not suffering from exhaustion, they are restored to their
  maximum VP.'''
  if ep > 0:
    out = (vp, ep - 1)
  else:
    out = (max_vitality_points(), 0)
  return out
  
  
  


