from organism import Organism
from passive_gens import PassiveGens
from os import uname

caption = 'Evolution'
first_organism = Organism(100, 100, list(range(0, 10)), PassiveGens(), 0)
starts_parameters = 'number, datatime, user, os'

os = str(uname().sysname)
user = str(uname().nodename)
statistics_dir = 'statistics'
if os == 'Windows':
    statistics_dir += '\\'[0]
else:
    statistics_dir += '/'

records = [
    'cycle',
    'num org-s',
    'max FPS',
    'sun',
    'mutations',
    'max health',
    'parent health',
    'heir health',
    'common l',
    'move l',
    'sleep l',
    'sun-sun l',
    'eat plant',
    'eat sun',
    's age',
    's generation',
    's p g meat',
    's p g sun',
    's p g plant',
    's p g size',
    's p g speed',
    's p g protection',
    's p g strong',
    's a gens',
    's a g 0',
    's a g 5'
]

control_parameters = {
    'sun': '↔',
    'max FPS': '↕',
    'mutations': '±',
    'max health': '1',
    'parent health': '2',
    'heir health': '3',
    'common l': '4',
    'move l': '5',
    'sleep l': '6',
    'sun-sun l': '7',
    'eat plant': '8',
    'eat sun': '9'
}
