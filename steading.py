__author__ = 'Adam'

import random
import json
f = open("steading.json")
info = json.load(f)
f.close()

prosp_levels = len(info["tags"]["prosperity"])
pop_levels = len(info["tags"]["population"])
def_levels = len(info["tags"]["defenses"])


class Steading:
    tags = {}
    prosperity_level = 0
    population_level = 0
    defenses_level = 0

    def __init__(self, population_level=random.randint(0, pop_levels), prosp_level=None, def_level=None):
        # determine the population level
        self.population_level = population_level

        # assign tags if given
        # if not given, generate them according to the population default
        if prosp_level is not None:
            self.prosperity_level = prosp_level
        else:
            pass
        if def_level is not None:
            self.defenses_level = def_level
        else:
            pass

    # assigns the correct value for the prosperity, population, and defenses tags based on their levels
    def correct_levels(self):
        self.tags["prosperity"] = info["tags"]["prosperity"][self.prosperity_level]
        self.tags["population"] = info["tags"]["population"][self.population_level]
        self.tags["defenses"] = info["tags"]["defenses"][self.defenses_level]

