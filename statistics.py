def print_organisms(organisms):
    print('*' * 10 + 'ORGANISMS' + '*' * 10)
    for organism in organisms:
        print(organism)


def print_oldest_organism(organisms):
    max_age = 0
    oldest_organism = organisms[-1]
    for organism in organisms[:-1]:
        if organism.age > max_age:
            oldest_organism = organism
            max_age = organism.age
    print(oldest_organism)


def print_organisms_statistics(organisms):
    stat = {
        'num_organisms': len(organisms),
        's_age': 0,
        's_generation': 0,
        's_meat': 0,
        's_sun': 0,
        's_plant': 0,
        's_size': 0,
        's_speed': 0,
        's_protection': 0,
        's_strong': 0,
        's_active_gens': 0,
        's_0': 0,
        's_5': 0
    }
    for organism in organisms:
        stat['s_age'] += organism.age
        stat['s_generation'] += organism.generation
        stat['s_meat'] += organism.passive_gens.nutrition['meat']
        stat['s_sun'] += organism.passive_gens.nutrition['sun']
        stat['s_plant'] += organism.passive_gens.nutrition['plant']
        stat['s_size'] += organism.passive_gens.size
        stat['s_speed'] += organism.passive_gens.speed
        stat['s_protection'] += organism.passive_gens.protection
        stat['s_strong'] += organism.passive_gens.strong
        stat['s_active_gens'] += len(organism.active_gens)
        stat['s_0'] += organism.active_gens.count(0)
        stat['s_5'] += organism.active_gens.count(5)

    for key, value in stat.items():
        print(f'\n{str(key)} = {str(value)}, average = {str(value / stat["num_organisms"])}')

    print(f'average photosintesis gens: {str(stat["s_0"]*100/stat["s_active_gens"])}%')
    print(f'average sleep gens: {str(stat["s_5"] * 100 / stat["s_active_gens"])}%')
