import matplotlib.pyplot as plt
import numpy as np


class LSystem:
    def __init__(self, starting_word, iteration_limit, angle, length):
        self.rules = {
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        }
        self.starting_word = starting_word
        self.iteration_limit = iteration_limit
        self.angle = np.radians(angle)
        self.length = length

    def set_rules(self, word):
        new_word = ""
        for char in word:
            new_word += self.rules.get(char, char)
        return new_word

    def generate_word(self):
        word = self.starting_word
        for _ in range(self.iteration_limit):
            word = self.set_rules(word)
        return word

    def show(self, word):
        positions = [(0, 0)]
        angles = [np.pi / 2]
        stack = []

        x, y = 0, 0
        angle = np.pi / 2

        for char in word:
            if char == "F":
                x += self.length * np.cos(angle)
                y += self.length * np.sin(angle)
                positions.append((x, y))
            elif char == "+":
                angle += self.angle
            elif char == "-":
                angle -= self.angle
            elif char == "[":
                stack.append((x, y, angle))
            elif char == "]":
                x, y, angle = stack.pop()

        positions = np.array(positions)
        plt.plot(positions[:, 0], positions[:, 1], color='green', linewidth=1)
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    def run(self):
        end_word = self.generate_word()
        self.show(end_word)


if __name__ == "__main__":
    fractal_plant = LSystem("X", 5, 25, 3)
    fractal_plant.run()
