objects = [[], [], []]

collision_pairs = {}

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] +=ol

def update():
    for layer in objects:
        for o in layer:
            o.update()

def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('?')

def clear():
    for layer in objects:
        layer.clear()

def collide(a,b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'New group {group} append')
        collision_pairs[group] = [[], [], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

