import turtle
import sys

sys.setrecursionlimit(10000)


class LSystem:
    def __init__(self, starting_word, iteration_limit, angle, length):
        self.rules = {
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        }
        self.starting_word = starting_word
        self.iteration_limit = iteration_limit
        self.angle = angle
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
        screen = turtle.Screen()
        turtle.speed("fastest")
        turtle.bgcolor("white")
        turtle.color("green")
        turtle.width(3)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.setheading(90)

        stack = []
        for char in word:
            if char == "F":
                turtle.forward(self.length)
            elif char == "+":
                turtle.left(self.angle)
            elif char == "-":
                turtle.right(self.angle)
            elif char == "[":
                position = turtle.position()
                angle = turtle.heading()
                stack.append((position, angle))
            elif char == "]":
                position, angle = stack.pop()
                turtle.penup()
                turtle.setposition(position)
                turtle.setheading(angle)
                turtle.pendown()
            screen.mainloop()

    def run(self):
        end_word = self.generate_word()
        self.show(end_word)
        turtle.done()


if __name__ == "__main__":
    fractal_plant = LSystem("X", 5, 25, 3)
    fractal_plant.run()
