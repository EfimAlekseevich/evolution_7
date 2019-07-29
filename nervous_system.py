from random import randint


class NervousSystem:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.weights_sets = []
        for index in range(10):
            weights_set = [0 for i in range(10)]
            self.weights_sets.append(weights_set)

    def __str__(self):
        out_str = ''
        for action, weights_set in enumerate(self.weights_sets):
            weights = " ".join(map(str, weights_set))
            out_str += f'\n{str(action)}: {weights}'
        return out_str

    def mutation(self, strong_mutation):
        num_mutations = randint(1, strong_mutation)
        for n in range(num_mutations):
            self.single_mutation()

    def single_mutation(self):
        set = randint(0, 9)
        weight = randint(0, 9)
        self.weights_sets[set][weight] += randint(-1, 1)

    def update_xy(self):
        sq = self.x**2 + self.y**2 + 1
        memory = 1
        self.x /= sq * memory
        self.y /= sq * memory
