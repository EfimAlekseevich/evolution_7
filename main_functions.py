def perform_actions(organism, organisms, settings):
    num_step = organism.passive_gens.speed
    while num_step > 0:
        if do_action(organism, organisms, settings):
            break
        num_step -= 1
    organism.age += 1


def do_action(organism, organisms, settings):
    action = organism.get_active_gen()
    if action == 0:
        organism.health += organism.passive_gens.nutrition['sun'] * settings.environment.sun *\
                           organism.passive_gens.size
    elif action == 5:
        organism.health -= settings.environment.losses.sleep
    else:
        perform_move(action, organism, settings)
    if verify_collisions(organism, organisms, settings):
        return True
    else:
        return verify_organism(organism, organisms, settings)


def verify_organism(organism, organisms, settings):
    organism.health -= settings.environment.losses.common
    if organism.health < 1:
        return death(organism, organisms, settings)
    elif organism.health > settings.max_health:
        give_birth(organism, organisms, settings)


def death(organism, organisms, settings):
    if len(organisms) > 1:
        organisms.remove(organism)
        return True
    else:
        organism.age = 0
        organism.generation += 1
        organism.health = int(settings.max_health * settings.parent_health)
        organism.full_mutation(settings)


def give_birth(organism, organisms, settings):
    organism.health = int(settings.max_health * settings.parent_health)
    heir = organism.get_heir(settings)
    heir.health = int(settings.max_health * settings.heir_health)
    correct_place(heir, settings)
    organisms.append(heir)


def perform_move(direction, organism, settings):

    if direction < 4:
        organism.y -= 1
    elif direction > 6:
        organism.y += 1

    if direction % 3 == 0:
        organism.x += 1
    elif (direction-1) % 3 == 0:
        organism.x -= 1

    correct_place(organism, settings)
    organism.health -= settings.environment.losses.move


def correct_place(organism, settings):
    if organism.x < 0:
        organism.x = 0
    elif organism.x > settings.environment.width:
        organism.x = settings.environment.width

    if organism.y < 0:
        organism.y = settings.environment.height
    elif organism.y > settings.environment.height:
        organism.y = 0


def verify_collisions(organism, organisms, settings):
    for other_organism in organisms:
        if other_organism is not organism:
            proximity = get_proximity(organism, other_organism)
            if proximity < 0:
                if interaction(organism, other_organism, organisms, settings, proximity):
                    return True


def eating(winner, food, organisms, settings):
    benefit = (winner.passive_gens.nutrition['plant'] * food.passive_gens.nutrition['sun'] *
               settings.environment.eat_sun) + \
              (winner.passive_gens.nutrition['meat'] * food.passive_gens.nutrition['plant'] *
               settings.environment.eat_plant)
    winner.health += benefit
    organisms.remove(food)


def get_proximity(organism_1, organism_2):
    dif_x = organism_1.x - organism_2.x
    dif_y = organism_1.y - organism_2.y
    distance = (dif_x**2+dif_y**2)**0.5
    proximity = distance - organism_1.radius - organism_2.radius
    return proximity


def interaction(organism, other_organism, organisms, settings, proximity):
    if organism.passive_gens.strong + organism.passive_gens.size >= \
            other_organism.passive_gens.protection + other_organism.passive_gens.size:
        eating(organism, other_organism, organisms, settings)
    elif other_organism.passive_gens.strong + other_organism.passive_gens.size > \
            organism.passive_gens.protection + organism.passive_gens.size:
        eating(other_organism, organism, organisms, settings)
        if other_organism.health > settings.max_health:
            give_birth(other_organism, organisms, settings)
        return True
    else:
        handle_losses(organism, other_organism, organisms, settings, proximity)


def handle_losses(organism, other_organism, organisms, settings, proximity):
    losses = organism.passive_gens.nutrition['sun'] * other_organism.passive_gens.nutrition['sun'] * \
             settings.environment.losses.sun_sun * proximity
    organism.health += losses * other_organism.passive_gens.strong // organism.passive_gens.protection
    other_organism.health += losses * organism.passive_gens.strong // other_organism.passive_gens.protection
    verify_organism(other_organism, organisms, settings)
