import copy
import random
# Consider using the modules imported above.


class Hat:
    # Initialise the class with the __init__ method
    def __init__(self, **kwargs):
        self.contents = [i for i, value in kwargs.items() for _ in range(value)] # '_' used as a throwaway variable, only interesred in perfoming the loop

    # Define the draw method
    def draw(self, number):
        number = min(number, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)] # '_' used as a throwaway variable, only interesred in perfoming the loop

# Define the experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat) # deepcopy ensures the hat is copied so when the loop is run again, the hat is not altered
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for i, value in expected_balls.items() if balls_drawn.count(i) >= value])
        count += 1 if balls_req == len(expected_balls) else 0

    return count / num_experiments
