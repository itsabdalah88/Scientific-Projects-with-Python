import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        if num >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        drawn_counts = {}
        for ball in drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        success = all(
            drawn_counts.get(color, 0) >= count
            for color, count in expected_balls.items()
        )
        if success:
            successes += 1

    return successes / num_experiments