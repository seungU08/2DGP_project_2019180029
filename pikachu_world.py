objects = [ [] , [] , []]

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

