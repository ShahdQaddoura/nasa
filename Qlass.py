import random
from fractions import Fraction
from math import sqrt

# class used to make question data and manipulation much easier in the main program
class Qlass: # 'Qlass' means questions class
    algebra_ques = set() # questions are stored in sets to find intersections later (intersection between easy and algebra questions, for example)
    geometry_ques = set()

    easy = set()
    medium = set()
    hard = set()

    all_ques = set()

    def __init__(self, question, choices, correct, type_question, requires_image, difficulty, recurring, image_instructions):
        self.question = question # question that will appear on screen
        self.choices = choices # choices that will appear on screen
        self.correct = correct # the index of the correct choice

        self.type_question = type_question # algebra / geometry

        if self.type_question.lower() == "algebra" or self.type_question[0].lower() == "a":
            Qlass.algebra_ques.add(self)
        elif self.type_question.lower() == "geometry" or self.type_question[0].lower() == "g":
            Qlass.geometry_ques.add(self)

        Qlass.all_ques.add(self)

        self.requires_image = requires_image # boolean if requires an image or note
        self.difficulty = difficulty # easy, medium, hard

        if self.difficulty == 0:
            Qlass.easy.add(self)
        elif self.difficulty == 1:
            Qlass.medium.add(self)
        elif self.difficulty == 2:
            Qlass.hard.add(self)

        self.recurring = recurring # question can appear more than once
        self.image_instructions = image_instructions # instructions in tuples as strings (pygame drawing instructions)

    def __str__(self):
        return f"{self.question}\n{self.choices}\n{self.correct}" # printing the question if needed
    

def list_shuffler(L): # A function that shuffles the items in a list (here, used to shuffle the index of the correct answer)
    L = set(L) # turns list into a set to eliminate any non-unique choices
    shuffled = list()

    while len(L) < 4:
        L.add(random.randint(-25, 25))

    L = list(L) # turns back to list to shuffle elemets

    while len(L) != 0: # shuffler
        shuffled.append(L.pop(random.randint(0, len(L) - 1)))

    return shuffled


def first_degree_equation_writer(): # creates a random solving first degree equation problem [EASY]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    while a == 0 or b == 0 or a == b or a == -b or a == 1 or a == -1:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    if b > 0:
        equation = f"{a}x+{b} = 0"
    elif b < 0:
        equation = f"{a}x{b} = 0"

    choices = list_shuffler([f"{Fraction(-b, a)}", f"{Fraction(b, a)}", f"{Fraction(-a, b)}", f"{Fraction(a, b)}"])
    correct = choices.index(f"{Fraction(-b, a)}")

    Qlass(tuple(["Solve for x:", f"{equation}"]), choices, correct, "algebra", False, 0, True, None)


def calculate_expression_writer(): # creates a random expression calculating problem [EASY]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    while a == 0 or b == 0 or a == -1:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    if b > 0:
        expression = f"{a}x+{b}"
    elif b < 0:
        expression = f"{a}x{b}"

    choices = list_shuffler([a*c+b, a*c-b, b*c+a, a*b+c])
    correct = choices.index(a*c+b)

    Qlass(tuple([f"Find the value for x = {c}:", f"{expression}"]), choices, correct, "algebra", False, 0, True, None)


def addition_writer(): # creates a random addition problem [EASY]
    a = random.randint(-50, 50)
    b = random.randint(-30, 30)

    while a == 0 or b == 0:
        a = random.randint(-50, 50)
        b = random.randint(-30, 30)

    if b > 0:
        expression = f"{a}+{b}"
    elif b < 0:
        expression = f"{a}{b}"

    choices = list_shuffler([a+b, a-b, a*b, Fraction(max(a, b), min(a, b))])
    correct = choices.index(a+b)

    Qlass(tuple(["Calculate:", f"{expression}"]), choices, correct, "algebra", False, 0, True, None)


def easy_fraction_writer(): # creates a simple fraction problem [EASY]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    expression = f"x/{a} = {b}"

    choices = list_shuffler([a*b, a-b, a+b])
    correct = choices.index(a*b)

    Qlass(tuple(["Solve for x:", f"{expression}"]), choices, correct, "algebra", False, 0, True, None)


def easy_evaluate(): # creates an easy evaluation problem [EASY]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    x = random.randint(-10, 10)
    y = random.randint(-10, 10)

    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    if b > 0:
        expression = f"{a}x+{b}y for x = {x} and y = {y}"
    elif b < 0:
        expression = f"{a}x{b}y for x = {x} and y = {y}"

    choices = list_shuffler([a*x+b*y, a*x-b*y, a*y-b*x, a*b-x*y])
    correct = choices.index(a*x+b*y)

    Qlass(tuple(["Find the value of:", f"{expression}"]), choices, correct, "algebra", False, 0, True, None)



def coefficient_of_x_writer(): # creates a random coefficient of x problems [MEDIUM]
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    e = random.randint(2, 10)

    while c == 0 or d == 0 or d == c or c == e or e == d:
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        e = random.randint(2, 10)

    if c > 0:
        expression_a = f"({e}x+{c})"
    elif c < 0:
        expression_a = f"({e}x{c})"

    if d > 0:
        expression_b = f"(x+{d})"
    elif d < 0:
        expression_b = f"(x{d})"

    expression = expression_a + expression_b

    choices = list_shuffler([d*e + c, c*e + d, c*d + e, - c - d - e])
    correct = choices.index(d*e + c)

    Qlass(tuple(["Find the coefficient of x in:", f"{expression}"]), choices, correct, "algebra", False, 1, True, None)


def multiplication_writer(): # creates a random multiplication problem [MEDIUM]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-15, 15)

    while a == 0 or b == 0 or c == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-15, 15)

    if c > 0:
        expression = f"({a})({b})+{c}"
    elif c < 0:
        expression = f"({a})({b}){c}"

    choices = list_shuffler([a*b+c, -a*b+c, -a*b-c, b*c-a])
    correct = choices.index(a*b+c)

    Qlass(tuple(["Calculate:", f"{expression}"]), choices, correct, "algebra", False, 1, True, None)


def subtraction_writer(): # creates a random subtraction problem [MEDIUM]
    a = random.randint(-30, 10)
    b = random.randint(-30, 10)
    c = random.randint(-30, 10)

    while a == 0 or b == 0 or c == 0:
        a = random.randint(-30, 10)
        b = random.randint(-30, 10)
        c = random.randint(-30, 10)

    expression_a = f"{a}"

    if b > 0:
        expression_b = f"+{b}"
    elif b < 0:
        expression_b = f"{b}"

    if c > 0:
        expression_c = f"+{c}"
    elif c < 0:
        expression_c = f"{c}"

    expression = expression_a + expression_b + expression_c

    choices = list_shuffler([a+b+c, a-b+c, a+b-c, -a+b+c])
    correct = choices.index(a+b+c)

    Qlass(tuple(["Calculate:", f"{expression}"]), choices, correct, "algebra", False, 1, True, None)


def num_squares_writer(): # creates a random number square problem [MEDIUM]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    if a > 0:
        expression = f"(x+{a})^2 = {b**2}"
    elif a < 0:
        expression = f"(x{a})^2 = {b**2}"

    choices = list_shuffler([b-a, -b+a, a**2-b**2, -a**2+b**2])
    correct = choices.index(b-a)

    Qlass(tuple(["Solve for x:", f"{expression}"]), choices, correct, "algebra", False, 1, True, None)


def expand_and_calculate(): # creates a random expansion and evaluation problem [MEDIUM]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(2, 10)
    d = random.randint(-10, 10)

    while a == 0 or b == 0 or c == 0 or d == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(2, 10)
        d = random.randint(-10, 10)

    if b > 0:
        expression = f"{a}(x+{b})+{c}x, x = {d}"
    elif b < 0:
        expression = f"{a}(x{b})+{c}x, x = {d}"

    choices = list_shuffler([a*d+a*b+c*d, b*c+2*a*d, a+b+c+d, d*b+a*c])
    correct = choices.index(a*d+a*b+c*d)

    Qlass(tuple(["Expand and evaluate:", f"{expression}"]), choices, correct, "algebra", False, 1, True, None)


def inequality_writer(): # creates a random inequality problem [HARD]
    a = random.randint(2, 5)
    b = random.randint(-5, 5)
    c = random.randint(-5, 5)

    while a == 0 or b == 0 or c == 0:
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)

    sign = random.choice(["<", ">"])

    root = (c-b) / a

    if b > 0:
        expression = f"{a}x+{b}{sign}{c}"
    elif b < 0:
        expression = f"{a}x{b}{sign}{c}"

    if sign == "<":
        correct = round(random.uniform(-5, root), 2)
        choices = set()
        choices.add(correct)
        while len(choices) < 4:
            choices.add(round(random.uniform(root , 5), 2))
        
        choices = list_shuffler(list(choices))
        correct = choices.index(correct)

    elif sign == ">":
        correct = round(random.uniform(root, 5), 2)
        choices = set()
        choices.add(correct)
        while len(choices) < 4:
            choices.add(round(random.uniform(-5, root), 2))
        
        choices = list_shuffler(list(choices))
        correct = choices.index(correct)

    Qlass(tuple(["A value of x that satisfies:", f"{expression}"]), choices, correct, "algebra", False, 2, True, None)


def nearest_fraction(): # creates a random fraction problem [HARD]
    a = random.randint(-300, 300)
    b = random.randint(-100, 100)

    while a == 0 or b == 0:
        a = random.randint(-300, 300)
        b = random.randint(-300, 300)

    choices = set([round(a/b, None)])
    
    while len(choices) != 4:
        choices.add(random.randint(-3, 3))

    choices = list_shuffler(list(choices))
    correct = choices.index(round(a/b, None))

    Qlass(tuple(["What is the nearest integer value of:", f"{str(Fraction(a, b))}"]), choices, correct, "algebra", False, 2, True, None)


def x_y_squares(): # creates a random x y squared problem [HARD]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    expression = f"x+y={a} and xy={b}"

    choices = list_shuffler([a**2-2*b, b**2-2*a, a+2*b, 2*a+b])
    correct = choices.index(a**2-2*b)

    Qlass(tuple(["Find x^2 + y^2 if:", f"{expression}"]), choices, correct, "algebra", False, 2, True, None)


def two_lines_intersection_x(): # creates a random two-line intersection problem, i.e. finding the x-coordinate of the intersection of two lines [HARD]
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)

    while a == 0 or b == 0 or c == 0 or d == 0 or a == c:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)

    if b > 0:
        expression_1 = f"y={a}x+{b}"
    elif b < 0:
        expression_1 = f"y={a}x{b}"

    if d > 0:
        expression_2 = f"y={c}x+{d}"
    elif d < 0:
        expression_2 = f"y={c}x{d}"

    expression = f"{expression_1}, {expression_2}"

    choices = list_shuffler([Fraction(d-b, a-c), Fraction(b-d, a-c), Fraction(a-b, a-c), Fraction(c-b, a-c)])
    correct = choices.index(Fraction(d-b, a-c))

    Qlass(tuple(["Find the x value of the intersection of:", f"{expression}"]), choices, correct, "algebra", False, 2, True, None)




def area_square(): # creates a simple problem to find the area of a square [EASY]
    a = random.randint(2, 15)

    choices = list_shuffler([a**2, 2*a, Fraction(a, 2), (a+1)**2])
    correct = choices.index(a**2)

    Qlass(tuple(["The area of a square of side:", f"{a}"]), choices, correct, "geometry", False, 0, True, None)


def area_rectangle(): # creates a simple problem to find the area of a rectangle [EASY]
    a = random.randint(2, 15)
    b = random.randint(2, 15)

    while a == b:
        a = random.randint(2, 15)
        b = random.randint(2, 15)

    choices = list_shuffler([a*b, a**2, b**2, (a+1)*(b+1)])
    correct = choices.index(a*b)

    Qlass(tuple(["The area of a rectangle of sides:", f"{a}, {b}"]), choices, correct, "geometry", False, 0, True, None)


def area_triangle(): # creates a simple problem to find the area of a triangle [EASY]
    a = random.randint(2, 15)
    b = random.randint(2, 15)

    while a == b:
        a = random.randint(2, 15)
        b = random.randint(2, 15)

    choices = list_shuffler([Fraction(a*b, 2), Fraction(a+b, 2), Fraction(a**2, 2), Fraction(b**2, 2)])
    correct = choices.index(Fraction(a*b, 2))

    Qlass(tuple(["The area of a triangle of respective", f"base and height: {a}, {b}"]), choices, correct, "geometry", False, 0, True, None)


def area_circle(): # creates a simple problem to find the area of a circle [EASY]
    a = random.randint(2, 15)

    choices = list_shuffler([round(3.14*a**2, 2), round(3.14*a*2, 2), round(3.14*(a+1)**2, 2), round(3.14*(a-1)**2, 2)])
    correct = choices.index(round(3.14*a**2, 2))

    Qlass(tuple(["The area of a circle of radius:", f"{a}"]), choices, correct, "geometry", False, 0, True, None)


def find_circle_subtraction(): # creates a problem to find the subtractive area between two circles [MEDIUM]
    a = random.randint(2, 15)
    b = random.randint(2, 15)

    while a == b:
        a = random.randint(2, 15)
        b = random.randint(2, 15)

    r1 = max(a, b)
    r2 = min(a, b)

    choices = list_shuffler([round(3.14*(r1**2-r2**2), 2), round(3.14*(r1*2-r2*2), 2), round(3.14*(r1**2-r2*2), 2), round(3.14*(r1*2-r2*2)/2, 2)])
    correct = choices.index(round(3.14*(r1**2-r2**2), 2))

    instructions = ("pygame.draw.circle(screen, GRAY, (800, 400), 100)", "pygame.draw.circle(screen, WHITE, (800, 400), 65)")

    Qlass(tuple(["The area of the gray part:", f"Big radius: {r1}, small radius: {r2}"]), choices, correct, "geometry", True, 1, True, instructions)


def angles_in_a_triangle(): # creates a problem to find the third angle in a triangle, given the two other angles [MEDIUM]
    a = random.randint(10, 70)
    b = random.randint(10, 70)

    choices = list_shuffler([180-a-b, abs(2*a-180), abs(2*b-180), abs(2*a+2*b-1-0)])
    correct = choices.index(180-a-b)

    instructions = ("pygame.draw.line(screen, BLACK, (750, 250), (1000, 550), width = 5)", "pygame.draw.line(screen, BLACK, (750, 250), (500, 550), width = 5)", "pygame.draw.line(screen, BLACK, (500, 550), (1000, 550), width = 5)", "screen.blit(TEXT_FONT.render('p', True, BLACK), (550, 510))", "screen.blit(TEXT_FONT.render('q', True, BLACK), (950, 510))")

    Qlass(tuple(["Measure the third angle:", f"p={a}, q={b}"]), choices, correct, "geometry", True, 1, True, instructions)


def angles_and_lines(): # creates a problem to find the second angle between two intersecting lines given the first [MEDIUM]
    a = random.randint(10, 90)

    choices = list_shuffler([180-a, a, 2*a, abs(180-2*a)])
    correct = choices.index(180-a)

    intructions = ("pygame.draw.line(screen, BLACK, (750, 250), (950, 550), width = 5)", "pygame.draw.line(screen, BLACK, (950, 250), (750, 550), width = 5)", "screen.blit(TEXT_FONT.render('p', True, BLACK), (840, 350))", "screen.blit(TEXT_FONT.render('q', True, BLACK), (860, 380))")

    Qlass(tuple(["Find q:", f"p={a}"]), choices, correct, "geometry", True, 1, True, intructions)


def pythagoras(): # creates a right triangle where the hypotenuse needs to be found [MEDIUM] 
    a = random.randint(2, 30)

    choices = list_shuffler([round(a*sqrt(2), 2), round(2*a*sqrt(2), 2), round(2*a*sqrt(3), 2), round(a*sqrt(3), 2)])
    correct = choices.index(round(a*sqrt(2), 2))

    instructions = ("pygame.draw.line(screen, BLACK, (800, 350), (800, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 350), (1000, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 550), (1000, 550), width = 5)", "screen.blit(TEXT_FONT.render('a', True, BLACK), (780, 450))", "screen.blit(TEXT_FONT.render('b', True, BLACK), (875, 555))", "screen.blit(TEXT_FONT.render('c', True, BLACK), (910, 430))")

    Qlass(tuple(["Find c:", f"a = b = {a}"]), choices, correct, "geometry", True, 1, True, instructions)


def complex_pythagoras(): # creates an advanced version of the pythagoras() problem [HARD]
    a = random.randint(2, 30)

    choices = list_shuffler([round((a*sqrt(2)) / 2, 2), round(2*a*sqrt(2), 2), round(a*sqrt(2), 2), round(a*sqrt(3) / 2, 2)])
    correct = choices.index(round((a*sqrt(2)) / 2, 2))

    instructions = ("pygame.draw.line(screen, BLACK, (800, 350), (800, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 350), (1000, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 550), (1000, 550), width = 5)", "screen.blit(TEXT_FONT.render('a', True, BLACK), (780, 450))", "screen.blit(TEXT_FONT.render('c', True, BLACK), (875, 470))", "pygame.draw.line(screen, BLACK, (800, 550), (900, 450), width = 5)", "screen.blit(TEXT_FONT.render('b', True, BLACK), (875, 555))")

    Qlass(tuple(["Find c:", f"a = b = {a}"]), choices, correct, "geometry", True, 2, True, instructions)


def area_of_top_triangle(): # creates an advanced version of the area_triangle() problem [HARD]
    a = random.randint(2, 30)

    choices = list_shuffler([round(a**2 / 4, 2), round(2*a / 4, 2), round(a/2, 2), round(a*sqrt(3) / 2, 2)])
    correct = choices.index(round(a**2 / 4, 2))

    instructions = ("pygame.draw.line(screen, BLACK, (800, 350), (800, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 350), (1000, 550), width = 5)", "pygame.draw.line(screen, BLACK, (800, 550), (1000, 550), width = 5)", "screen.blit(TEXT_FONT.render('a', True, BLACK), (780, 450))", "pygame.draw.line(screen, BLACK, (800, 550), (900, 450), width = 5)", "screen.blit(TEXT_FONT.render('b', True, BLACK), (875, 555))")

    Qlass(tuple(["Find the area of the top triangle:", f"a = b = {a}"]), choices, correct, "geometry", True, 2, True, instructions)


def slice_of_circle(): # creates an advanced version of the area_circle() problem [HARD]
    r = random.randint(2, 30)
    a = random.randint(10, 90)

    area = 3.14*r**2

    choices = list_shuffler([round(area * a / 360, 2), round(area * 360 / a, 2), round(area * a, 2), round(area * 3.14 / a, 2)])
    correct = choices.index(round(area * a / 360, 2))

    instructions = ("pygame.draw.circle(screen, BLACK, (800, 400), 100, width = 5)", "pygame.draw.line(screen, BLACK, (800, 400), (877, 460), width = 5)", "pygame.draw.line(screen, BLACK, (800, 400), (877, 340), width = 5)", "screen.blit(TEXT_FONT.render('a', True, BLACK), (815, 385))", "screen.blit(TEXT_FONT.render('r', True, BLACK), (845, 405))")

    Qlass(tuple(["The area of a slice of a circle of:", f"radius: {r}, angle: {a}"]), choices, correct, "geometry", True, 2, True, instructions)


def generate_porblems(): # generates a fresh batch of problems
    Qlass.all_ques.clear()

    Qlass.easy.clear()
    Qlass.medium.clear()
    Qlass.hard.clear()

    Qlass.algebra_ques.clear()
    Qlass.geometry_ques.clear()

    for _ in range(5):

        # ALGEBRA
        # EASY
        first_degree_equation_writer()
        calculate_expression_writer()
        addition_writer()
        easy_fraction_writer()
        easy_evaluate()

        # MEDIUM
        coefficient_of_x_writer()
        subtraction_writer()
        multiplication_writer()
        num_squares_writer()
        expand_and_calculate()

        # HARD
        inequality_writer()
        nearest_fraction()
        x_y_squares()
        two_lines_intersection_x()


        # GEOMETRY
        # EASY
        area_square()
        area_rectangle()
        area_triangle()
        area_circle()

        # MEDIUM
        find_circle_subtraction()
        angles_in_a_triangle()
        angles_and_lines()
        pythagoras()

        # HARD
        complex_pythagoras()
        area_of_top_triangle()
        slice_of_circle()

if __name__ == "__main__":
    generate_porblems()