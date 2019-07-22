from os import path, makedirs
from datetime import datetime
from constantes import starts_parameters, statistics_dir, os, user, records


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


def print_organisms_statistics(organisms_sums, num_organisms):
    for key, value in organisms_sums.items():
        print(f'\n{str(key)} = {str(value)}, average = {str(value / num_organisms)}')
    print(f'average photosintesis gens: {str(organisms_sums["s a g 0"] * 100 / organisms_sums["s a gens"])}%')
    print(f'average sleep gens: {str(organisms_sums["s a g 5"] * 100 / organisms_sums["s a gens"])}%')


def get_organisms_statistics(organisms):
    sums = {
        's age': 0,
        's generation': 0,
        's p g meat': 0,
        's p g sun': 0,
        's p g plant': 0,
        's p g size': 0,
        's p g speed': 0,
        's p g protection': 0,
        's p g strong': 0,
        's a gens': 0,
        's a g 0': 0,
        's a g 5': 0
    }
    for organism in organisms:
        sums['s age'] += organism.age
        sums['s generation'] += organism.generation
        sums['s p g meat'] += organism.passive_gens.nutrition['meat']
        sums['s p g sun'] += organism.passive_gens.nutrition['sun']
        sums['s p g plant'] += organism.passive_gens.nutrition['plant']
        sums['s p g size'] += organism.passive_gens.size
        sums['s p g speed'] += organism.passive_gens.speed
        sums['s p g protection'] += organism.passive_gens.protection
        sums['s p g strong'] += organism.passive_gens.strong
        sums['s a gens'] += len(organism.active_gens)
        sums['s a g 0'] += organism.active_gens.count(0)
        sums['s a g 5'] += organism.active_gens.count(5)
    return sums


def get_stat_file():
    try:
        last_start = get_last_start()
    except:
        create_starts_file()
        return get_stat_file()
    start = str(last_start + 1)
    write_start(start)

    return prepare_stat_file(start)


def get_last_start():
    file = open('starts.csv', 'r+')
    starts = file.readlines()
    file.close()
    try:
        return int(starts[-1].split(',')[0])
    except:
        return 0


def create_starts_file():
    file = open('starts.csv', 'w')
    file.write(starts_parameters)
    file.close()


def write_start(start):
    with open('starts.csv', 'a') as file:
        line = ','.join((start, str(datetime.now()), user, os))
        file.write('\n' + line)


def prepare_stat_file(start):
    if not path.exists(statistics_dir):
        makedirs(statistics_dir)
    stat_filename = f'N{start}=={str(datetime.now().strftime("%Y.%m.%d..%H.%M"))}=={user}=={os}'
    stat_file = open(f'{statistics_dir}{stat_filename}.csv', 'w')
    stat_file.write(','.join(records))
    return stat_file
