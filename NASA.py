import pygame, time, random, Typing, Qlass
import numpy as np
from tensorflow.keras.models import load_model

pygame.init()

WIDTH, HEIGHT = 1224, 768 # WIDTH AND HEIGHT OF THE WINDOW

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption('N.A.S.A.: Dr. Nabil Approved Math Study Aid')
clock = pygame.time.Clock()
pygame.display.toggle_fullscreen()

BLACK = (10, 10, 20)
WHITE = (240, 237, 237)
RED = (255, 0, 70)
GREEN = (0, 196, 68)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)

ORANGE = (255, 200, 75)

def normalize_time(time):
    """
    To normalize time, any time below 5 minutes (5 * 60 = 300 seconds) will be divided by 300; any time above 5 minutes will be translated to 1.
    """

    if time >= 300:
        return 1.0
    else:
        return time / 300
    

def normalize_attempts(attempts):
    """
    The data is collected from tests, each having 10 questions, each question having 4 choices. So, the minimum possible attempts for each test is 10, while the maximum is 40.
    Using this knowledge, we can normalize the "attempts" in the data frame by:
    """

    minimum = 10
    maximum = 40

    return (attempts - minimum)/(maximum - minimum)

    "This ensures that a test answered by 10 attempts is translated to 0, while a test answered by 40 to 1."


right_arrow_black = pygame.image.load("Assets\\right_arrow_black.png")
right_arrow_black = pygame.transform.scale(right_arrow_black, (35 , 35))

right_arrow_gray = pygame.image.load("Assets\\right_arrow_gray.png")
right_arrow_gray = pygame.transform.scale(right_arrow_gray, (35 , 35))

left_arrow_black = pygame.transform.flip(right_arrow_black, True, False)  # image, x_flip, y_flip
left_arrow_gray = pygame.transform.flip(right_arrow_gray, True, False)  # image, x_flip, y_flip

key_list = []
dummy = []

TITLE_FONT = pygame.font.SysFont('constantia', 40)
WELCOME_TITLE = 'Welcome to N.A.S.A.: Dr. Nabil Approved Math Study Aid!'
WELCOME_SUBTITLE = ("Click the arrow to go the next page", "to choose the settings for this math session.")
SETTINGS_SUBTITLE = ("Click on the options", "('Easy', 'Algebra'...)", "to change the option.")

TEXT_FONT = pygame.font.SysFont('constantia', 30)
BIG_FONT = pygame.font.SysFont('constantia', 70)

try:
    model_difficulty_predictor = load_model("Assets\\model_difficulty_predictor.h5")
    model_improvement = load_model("Assets\\model_improvement.h5")
    is_ai_trained = True
except:
    is_ai_trained = False


has_name = False
name = ""
name_typing = False
page = 0
click_dummy = 0
clicked_at_least_once = False

difficulty = 0
alggeo = 1
ai_included = -1
number_of_ques = 6

started = False
test_started = False
dummy_start = 0

questions_to_be_asked = list()
question_nb_now = 0
user_choice = -1
wrong_attempts = 0
total_attempts = 0

finished_dummy = 0

Qlass.generate_porblems()

easy_questions = Qlass.Qlass.easy
medium_questions = Qlass.Qlass.medium
hard_questions = Qlass.Qlass.hard

algebra_questions = Qlass.Qlass.algebra_ques
geometry_questions = Qlass.Qlass.geometry_ques

easy_algebra = easy_questions.intersection(algebra_questions)
medium_algebra = medium_questions.intersection(algebra_questions)
hard_algebra = hard_questions.intersection(algebra_questions)

easy_geometry = easy_questions.intersection(geometry_questions)
medium_geometry = medium_questions.intersection(geometry_questions)
hard_geometry = hard_questions.intersection(geometry_questions)

all_questions = Qlass.Qlass.all_ques

test_finished = False

wrong_answer_messages = ["Wrong answer. Try again!", f"Wrong choice. Take your time, {name}.", "Don't rush. Try again!", f"It's ok, {name}. Pick another.", "Don't worry. You can do this!", "We all make mistakes. Don't worry."]
random_wrong_message = ""

right_answer_messages = ["Perfect! Keep going!", f"Bravo, {name}!", "Keep up the good work!", "Excellent job!", "Shahd is proud of you!", "Asmaa is proud of you!", "Ayk is proud of you!", f"You should be proud of yourself, {name}!"]
random_right_message = ""

metrics = dict()

NAME_RECTANGLE = pygame.Rect(112, 150, 1000, 65) # x, y, width, height
CONTINUE_RECTANGLE_RIGHT = pygame.Rect(WIDTH - 50, HEIGHT - 50, 35, 35)
CONTINUE_RECTANGLE_LEFT = pygame.Rect(50, HEIGHT - 50, 35, 35)

DIFFICULTY_RECTANGLE = pygame.Rect(160, 230, 160, 75)
ALGGEO_RECTANGLE = pygame.Rect(562, 240, 80, 50)
AI_RECTANGLE = pygame.Rect(875, 230, 160, 75)
REMOVE_QUESTION = pygame.Rect(480, 465, 15, 15)
ADD_QUESTION = pygame.Rect(570, 465, 15, 15)

START_RECTANGLE = pygame.Rect(335, 250, 550, 150)
EXIT_RECTANGLE = pygame.Rect(1075, 42, 100, 50)

OPTION_A = pygame.Rect(90, 260, 60, 60)
OPTION_B = pygame.Rect(90, 360, 60, 60)
OPTION_C = pygame.Rect(90, 460, 60, 60)
OPTION_D = pygame.Rect(90, 560, 60, 60)

options_buttons = ["pygame.draw.circle(screen, BLACK, (120, 290), 35, width = 3)",\
                   "pygame.draw.circle(screen, BLACK, (120, 390), 35, width = 3)",\
                   "pygame.draw.circle(screen, BLACK, (120, 490), 35, width = 3)",\
                   "pygame.draw.circle(screen, BLACK, (120, 590), 35, width = 3)"]

start_of_session = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            key_list.append(1)
            if name_typing:
                name = Typing.Typing(name, dummy)
        if event.type == pygame.KEYUP:
            key_list.remove(1)

    if len(key_list) == 0:
        dummy.clear()

    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse[0], mouse[1], 1, 1)
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    if left and click_dummy == 0:
        click_dummy += 1

    now = time.time()
    screen.fill(WHITE)


    if page == 0: # RUNS THE FIRST PAGE (NAME INPUTTING PAGE)
        if left:
            clicked_at_least_once = True

        if not name_typing and not has_name: # EXECUTES WHILE THE USER HAS NOT INPUTTED THEIR NAME
            screen.blit(TEXT_FONT.render("Click here and enter your name to start!", True, GRAY), (125, 168)) # DISPLAYS INSTRUCTIONS TO ENTER NAME

        screen.blit(TITLE_FONT.render(WELCOME_TITLE, True, BLACK), (113, 50)) # DISPLAYS TITLE
        pygame.draw.rect(screen, BLACK, NAME_RECTANGLE, border_radius = 10, width = 3) # DRAWS THE NAME INPUT BOX

        if mouse_rect.colliderect(NAME_RECTANGLE) and left:
            name_typing = True
        elif not mouse_rect.colliderect(NAME_RECTANGLE) and left:
            if len(name) == 0:
                name_typing = False

        if name_typing: # EXECUTES WHILE THE USER IS INPUTTING THEIR NAME
            screen.blit(TEXT_FONT.render(name, True, BLACK), (125, 170)) # RENDERS NAME AS USER IS TYPING
            if int(1.5 * (now - start_of_session)) % 2 == 0:
                pygame.draw.line(screen, BLACK, (TEXT_FONT.size(name)[0] + 126, 165), (TEXT_FONT.size(name)[0] + 126, 195), 2)
            
            if keys_pressed[pygame.K_RETURN] and len(name) != 0:
                has_name = True
                name_typing = False

        if has_name:
            screen.blit(TEXT_FONT.render(name, True, BLACK), (125, 170)) # RENDERS NAME
            screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
            screen.blit(TITLE_FONT.render(f"Welcome, {name}!", True, BLACK), (WIDTH / 2 - TITLE_FONT.size(f"Welcome, {name}!")[0] / 2, 350))

            screen.blit(TITLE_FONT.render(WELCOME_SUBTITLE[0], True, BLACK), (WIDTH / 2 - TITLE_FONT.size(WELCOME_SUBTITLE[0])[0] / 2, 400 + TITLE_FONT.size(WELCOME_SUBTITLE[0])[1]))
            screen.blit(TITLE_FONT.render(WELCOME_SUBTITLE[1], True, BLACK), (WIDTH / 2 - TITLE_FONT.size(WELCOME_SUBTITLE[1])[0] / 2, 400 + TITLE_FONT.size(WELCOME_SUBTITLE[1])[1] * 2))

            screen.blit(TITLE_FONT.render("Press Esc at any time to exit the program.", True, BLACK), (WIDTH / 2 - TITLE_FONT.size("Press Esc at any time to exit the program.")[0] / 2, HEIGHT - TITLE_FONT.size("Press Esc at any time to exit the program.")[1] - 20))

            if mouse_rect.colliderect(CONTINUE_RECTANGLE_RIGHT):
                screen.blit(right_arrow_gray, (WIDTH - 50, HEIGHT - 50))
                if not left and click_dummy == 1 and clicked_at_least_once:
                    wrong_answer_messages = ["Wrong answer. Try again!", f"Wrong choice. Take your time, {name}.", "Don't rush. Try again!", f"It's ok, {name}. Pick another.", "Don't worry. You can do this!", "We all make mistakes. Don't worry."]

                    right_answer_messages = ["Perfect! Keep going!", f"Bravo, {name}!", "Keep up the good work!", "Excellent job!", "Shahd is proud of you!", "Asmaa is proud of you!", "Ayk is proud of you!", f"You should be proud of yourself, {name}!"]

                    clicked_at_least_once = False
                    page += 1

    if page == 1:
        if left:
            clicked_at_least_once = True

        screen.blit(TITLE_FONT.render("Difficulty", True, BLACK), (160, 100))
        screen.blit(TITLE_FONT.render("Algebra/Geometry", True, BLACK), (460, 100))
        screen.blit(TITLE_FONT.render("AI", True, BLACK), (935, 100))

        if ai_included == 1:
            difficulty_color = GRAY
            screen.blit(TITLE_FONT.render("Difficulty", True, GRAY), (160, 100))
        elif ai_included == -1:
            if difficulty % 3 == 0:
                difficulty_text = "Easy"
                difficulty_color = GREEN
            elif difficulty % 3 == 1:
                difficulty_text = "Medium"
                difficulty_color = ORANGE
            elif difficulty % 3 == 2:
                difficulty_text = "Hard"
                difficulty_color = RED
        
        screen.blit(TITLE_FONT.render(difficulty_text, True, difficulty_color), (160 + TITLE_FONT.size("Difficulty")[0] / 2 - TITLE_FONT.size(difficulty_text)[0] / 2 , 250))
        if mouse_rect.colliderect(DIFFICULTY_RECTANGLE) and not left and click_dummy == 1 and ai_included == -1:
            difficulty += 1

        if alggeo % 3 == 0:
            alggeo_text = "Both"
        elif alggeo % 3 == 1:
            alggeo_text = "Algebra"
        elif alggeo % 3 == 2:
            alggeo_text = "Geometry"

        screen.blit(TITLE_FONT.render(alggeo_text, True, BLACK), (460 + TITLE_FONT.size("Algebra/Geometry")[0] / 2 - TITLE_FONT.size(alggeo_text)[0] / 2, 250))
        if mouse_rect.colliderect(ALGGEO_RECTANGLE) and not left and click_dummy == 1:
            alggeo += 1


        if not is_ai_trained:
            ai_text = ("Note:", "You can't use", "the AI model", "since it", "is not trained yet.")
        else:
            if ai_included == -1:
                ai_text = "No"
            elif ai_included == 1:
                ai_text = "Yes"

        if type(ai_text) == tuple:
            for i in range(len(ai_text)):
                screen.blit(TITLE_FONT.render(ai_text[i], True, RED), (935 + TITLE_FONT.size("AI")[0] / 2 - TITLE_FONT.size(ai_text[i])[0] / 2, 170 + TEXT_FONT.size(ai_text[i])[1] * (i + 1)))
        else:
            screen.blit(TITLE_FONT.render(ai_text, True, BLACK), (935 + TITLE_FONT.size("AI")[0] / 2 - TITLE_FONT.size(ai_text)[0] / 2, 250))
            if mouse_rect.colliderect(AI_RECTANGLE) and not left and click_dummy == 1:
                ai_included *= -1

        
        if ai_included == -1:
            screen.blit(TITLE_FONT.render("Number of questions: ", True, BLACK), (85, 450))
            screen.blit(TITLE_FONT.render(str(number_of_ques - 1), True, BLACK), (520, 445))

            if number_of_ques > 2:
                screen.blit(TEXT_FONT.render("-", True, BLACK), (480, 455))
            if number_of_ques < 16:
                screen.blit(TEXT_FONT.render("+", True, BLACK), (570, 455))

            if mouse_rect.colliderect(REMOVE_QUESTION) and number_of_ques > 2:
                screen.blit(TEXT_FONT.render("-", True, GRAY), (480, 455))
                if not left and click_dummy == 1:
                    number_of_ques -= 1
            if mouse_rect.colliderect(ADD_QUESTION) and number_of_ques < 16:
                screen.blit(TEXT_FONT.render("+", True, GRAY), (570, 455))
                if not left and click_dummy == 1:
                    number_of_ques += 1
        else:
            screen.blit(TEXT_FONT.render("-", True, GRAY), (480, 455))
            screen.blit(TEXT_FONT.render("+", True, GRAY), (570, 455))
            screen.blit(TITLE_FONT.render("Number of questions: ", True, GRAY), (85, 450))
            screen.blit(TITLE_FONT.render(str(number_of_ques - 1), True, GRAY), (520, 445))



        screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
        screen.blit(left_arrow_black, (50, HEIGHT - 50)) # RENDERS PREVIOUS PAGE BUTTON

        if mouse_rect.colliderect(CONTINUE_RECTANGLE_RIGHT):
            screen.blit(right_arrow_gray, (WIDTH - 50, HEIGHT - 50))
            if not left and click_dummy == 1 and clicked_at_least_once:
                page += 1
                clicked_at_least_once = False
                if ai_included == 1:
                    number_of_ques = 11

        if mouse_rect.colliderect(CONTINUE_RECTANGLE_LEFT):
            screen.blit(left_arrow_gray, (50, HEIGHT - 50))
            if not left and click_dummy == 1 and clicked_at_least_once:
                page -= 1
                clicked_at_least_once = False

        for i in range(len(SETTINGS_SUBTITLE)):
            screen.blit(TITLE_FONT.render(SETTINGS_SUBTITLE[i], True, BLACK), (WIDTH / 2 - TITLE_FONT.size(SETTINGS_SUBTITLE[i])[0] / 2, 600 + TITLE_FONT.size(SETTINGS_SUBTITLE[i])[1] * i))

    if page == 2:
        if left:
            clicked_at_least_once = True

        if mouse_rect.colliderect(START_RECTANGLE) and not left and click_dummy == 1:
            test_started = True
        
        if not test_started:
            screen.blit(BIG_FONT.render("Click here to start", True, BLACK), (WIDTH / 2 - BIG_FONT.size("Click here to start")[0] / 2, 300))
            screen.blit(left_arrow_black, (50, HEIGHT - 50))
            if mouse_rect.colliderect(CONTINUE_RECTANGLE_LEFT):
                screen.blit(left_arrow_gray, (50, HEIGHT - 50))
                if not left and click_dummy == 1 and clicked_at_least_once:
                    page -= 1
                    clicked_at_least_once = False


        if test_started and dummy_start == 0: # THIS BLOCK RUNS ONCE, SETS INITIAL STATE OF TEST
            start_of_test = time.time()

            for i in range(number_of_ques): # QUESTIONS ASSSIGNED HERE
                if ai_included == -1: # AI NOT INCLUDED

                    if alggeo % 3 == 0: # BOTH ALGEBRA AND GEOMETRY QUESTIONS
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_questions.pop())
                        elif difficulty % 3 == 1:
                            questions_to_be_asked.append(medium_questions.pop())
                        elif difficulty % 3 == 2:
                            questions_to_be_asked.append(hard_questions.pop())

                    elif alggeo % 3 == 1: # ONLY ALGEBRA
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_algebra.pop())
                        elif difficulty % 3 == 1:
                            questions_to_be_asked.append(medium_algebra.pop())
                        elif difficulty % 3 == 2:
                            questions_to_be_asked.append(hard_algebra.pop())

                    elif alggeo % 3 == 2: # ONLY GEOMETRY
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_geometry.pop())
                        elif difficulty % 3 == 1:
                            questions_to_be_asked.append(medium_geometry.pop())
                        elif difficulty % 3 == 2:
                            questions_to_be_asked.append(hard_geometry.pop())

                elif ai_included == 1: # AI INCLUDED
                    difficulty = 0
                    if alggeo % 3 == 0: # BOTH ALGEBRA AND GEOMETRY QUESTIONS
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_questions.pop())
                    elif alggeo % 3 == 1: # ONLY ALGEBRA
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_algebra.pop())
                    elif alggeo % 3 == 2: # ONLY GEOMETRY
                        if difficulty % 3 == 0:
                            questions_to_be_asked.append(easy_geometry.pop())



            dummy_start += 1
        

        if test_started and dummy_start != 0 and question_nb_now != number_of_ques and not test_finished: # RUNS WHEN TEST HAS STARTED
            seconds = int(now - start_of_test)
            minutes = seconds // 60

            if len(str(seconds % 60)) != 2:
                str_seconds = f"0{seconds % 60}"
            else:
                str_seconds = str(seconds % 60)

            if len(str(minutes)) != 2:
                str_minutes = f"0{minutes}"
            else:
                str_minutes = str(minutes)

            screen.blit(TITLE_FONT.render(f"{str_minutes}:{str_seconds}", True, BLACK), (10,HEIGHT - 45)) # RENDERS TIME ELAPSED SINCE START OF TEST


            if question_nb_now == number_of_ques - 1: # RUNS WHEN TEST IS FINISHED
                if ai_included == -1:
                    page = 3

                elif ai_included == 1:
                    if finished_dummy == 0: # RUNS ONCE
                        difficulty_prediction = model_difficulty_predictor.predict(np.array([metrics["accuracy"]]))[0]
                        difficulty = np.argmax(difficulty_prediction) # argmax RETURNS THE INDEX OF THE MAXIMUM FROM THE ARRAY
                        print(difficulty)

                        improvement_area = model_improvement.predict(np.array([metrics["accuracy"], normalize_time(seconds), normalize_attempts(metrics["total attempts"])]).reshape(1, 3))[0]
                        improvement_area = np.argmax(improvement_area)
                        print(improvement_area)

                        finished_dummy += 1

                    screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
                    screen.blit(TITLE_FONT.render(f"Time: {metrics['time']}", True, BLACK), (100, 150))
                    screen.blit(TITLE_FONT.render(f"Number of wrong attempts: {metrics['wrong attempts']}", True, BLACK), (100, 250))
                    screen.blit(TITLE_FONT.render(f"Number of total attempts: {metrics['total attempts']}", True, BLACK), (100, 350))
                    screen.blit(TITLE_FONT.render(f"Accuracy: {int(metrics['accuracy'] * 100)}%", True, BLACK), (100, 450))

                    if difficulty == 0:
                        difficulty_text_ai = "Next difficulty: Easy"
                    elif difficulty == 1:
                        difficulty_text_ai = "Next difficulty: Medium"
                    elif difficulty == 2:
                        difficulty_text_ai = "Next difficulty: Hard"
                    
                    if improvement_area == 0:
                        improvement_area_text_ai = "You should work on your accuracy."
                    elif improvement_area == 1:
                        improvement_area_text_ai = "You should work on your time."
                    elif improvement_area == 2:
                        improvement_area_text_ai = "You should work on your number of attempts."

                    screen.blit(TITLE_FONT.render(difficulty_text_ai, True, BLACK), (100, 550))
                    screen.blit(TITLE_FONT.render(improvement_area_text_ai, True, BLACK), (100, 650))
                    pygame.draw.rect(screen, WHITE, pygame.Rect(0, HEIGHT - 50, 120, 60))
                    pygame.draw.rect(screen, RED, EXIT_RECTANGLE , border_radius = 5)

                    if mouse_rect.colliderect(EXIT_RECTANGLE):
                        pygame.draw.rect(screen, ORANGE, EXIT_RECTANGLE, border_radius = 5)
                        if not left and click_dummy == 1:
                            pygame.quit()
                            exit()

                    pygame.draw.rect(screen, BLACK, EXIT_RECTANGLE, width = 3, border_radius = 5)
                    screen.blit(TEXT_FONT.render("Exit", True, BLACK), (1100, 55))
                    screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
                    if mouse_rect.colliderect(CONTINUE_RECTANGLE_RIGHT):
                        screen.blit(right_arrow_gray, (WIDTH - 50, HEIGHT - 50))
                        if not left and click_dummy == 1 and clicked_at_least_once: # RESETS THE TEST                    
                            questions_to_be_asked = list()
                            Qlass.generate_porblems()
                            metrics["time"] = 0
                            metrics["wrong attempts"] = 0
                            metrics["total attempts"] = 0
                            metrics["accuracy"] = 0
                            total_attempts = 0
                            wrong_attempts = 0
                            start_of_test = time.time()

                            easy_questions = Qlass.Qlass.easy
                            medium_questions = Qlass.Qlass.medium
                            hard_questions = Qlass.Qlass.hard

                            algebra_questions = Qlass.Qlass.algebra_ques
                            geometry_questions = Qlass.Qlass.geometry_ques

                            easy_algebra = easy_questions.intersection(algebra_questions)
                            medium_algebra = medium_questions.intersection(algebra_questions)
                            hard_algebra = hard_questions.intersection(algebra_questions)

                            easy_geometry = easy_questions.intersection(geometry_questions)
                            medium_geometry = medium_questions.intersection(geometry_questions)
                            hard_geometry = hard_questions.intersection(geometry_questions)

                            all_questions = Qlass.Qlass.all_ques

                            for i in range(number_of_ques):
                                if alggeo % 3 == 0: # BOTH ALGEBRA AND GEOMETRY QUESTIONS
                                    if difficulty % 3 == 0:
                                        questions_to_be_asked.append(easy_questions.pop())
                                    elif difficulty % 3 == 1:
                                        questions_to_be_asked.append(medium_questions.pop())
                                    elif difficulty % 3 == 2:
                                        questions_to_be_asked.append(hard_questions.pop())

                                elif alggeo % 3 == 1: # ONLY ALGEBRA
                                    if difficulty % 3 == 0:
                                        questions_to_be_asked.append(easy_algebra.pop())
                                    elif difficulty % 3 == 1:
                                        questions_to_be_asked.append(medium_algebra.pop())
                                    elif difficulty % 3 == 2:
                                        questions_to_be_asked.append(hard_algebra.pop())

                                elif alggeo % 3 == 2: # ONLY GEOMETRY
                                    if difficulty % 3 == 0:
                                        questions_to_be_asked.append(easy_geometry.pop())
                                    elif difficulty % 3 == 1:
                                        questions_to_be_asked.append(medium_geometry.pop())
                                    elif difficulty % 3 == 2:
                                        questions_to_be_asked.append(hard_geometry.pop())

                            question_nb_now = 0
                            finished_dummy = 0


            elif question_nb_now < number_of_ques: # KEEPS ASKING QUESTIONS UNTIL REACHED THE NUMBER OF QUESTIONS CHOSEN BY THE USER

                screen.blit(TEXT_FONT.render(f"{question_nb_now + 1}/{number_of_ques - 1}", True, BLACK), (WIDTH - TEXT_FONT.size(f"{question_nb_now}/{number_of_ques - 1}")[0] - 5, 10)) # RENDERS THE QUESTION NUMBER TOP RIGHT CORNER


                for i in range(len(questions_to_be_asked[question_nb_now].question)):
                    screen.blit(BIG_FONT.render(questions_to_be_asked[question_nb_now].question[i], True, BLACK), (75, 75 + 75 * i)) # RENDERS THE QUESTION

                if questions_to_be_asked[question_nb_now].requires_image:
                    for instruction in questions_to_be_asked[question_nb_now].image_instructions:
                        exec(instruction)

                for choice in questions_to_be_asked[question_nb_now].choices: # RENDERS CHOICES
                    screen.blit(BIG_FONT.render(str(choice), True, BLACK), (200, 250 + questions_to_be_asked[question_nb_now].choices.index(choice) * 100))

                    for circle in options_buttons:
                        exec(circle)

                screen.blit(pygame.font.SysFont("constantia", 55).render("A", True, BLACK), (100, 265))
                screen.blit(pygame.font.SysFont("constantia", 55).render("B", True, BLACK), (103, 368))
                screen.blit(pygame.font.SysFont("constantia", 55).render("C", True, BLACK), (98, 468))
                screen.blit(pygame.font.SysFont("constantia", 55).render("D", True, BLACK), (100, 566))

                if user_choice != questions_to_be_asked[question_nb_now].correct:
                    if mouse_rect.colliderect(OPTION_A):
                        exec(options_buttons[0].replace("BLACK", "GRAY"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("A", True, GRAY), (100, 265))
                        if not left and click_dummy == 1:
                            user_choice = 0
                            total_attempts += 1
                            if questions_to_be_asked[question_nb_now].correct != user_choice:
                                wrong_attempts += 1
                                random_wrong_message = random.choice(wrong_answer_messages)
                            else:
                                random_right_message = random.choice(right_answer_messages)

                    if mouse_rect.colliderect(OPTION_B):
                        exec(options_buttons[1].replace("BLACK", "GRAY"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("B", True, GRAY), (103, 368))
                        if not left and click_dummy == 1:
                            user_choice = 1
                            total_attempts += 1
                            if questions_to_be_asked[question_nb_now].correct != user_choice:
                                wrong_attempts += 1
                                random_wrong_message = random.choice(wrong_answer_messages)
                            else:
                                random_right_message = random.choice(right_answer_messages)

                    if mouse_rect.colliderect(OPTION_C):
                        exec(options_buttons[2].replace("BLACK", "GRAY"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("C", True, GRAY), (98, 468))
                        if not left and click_dummy == 1:
                            user_choice = 2
                            total_attempts += 1
                            if questions_to_be_asked[question_nb_now].correct != user_choice:
                                wrong_attempts += 1
                                random_wrong_message = random.choice(wrong_answer_messages)
                            else:
                                random_right_message = random.choice(right_answer_messages)

                    if mouse_rect.colliderect(OPTION_D):
                        exec(options_buttons[3].replace("BLACK", "GRAY"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("D", True, GRAY), (100, 566))
                        if not left and click_dummy == 1:
                            user_choice = 3
                            total_attempts += 1
                            if questions_to_be_asked[question_nb_now].correct != user_choice:
                                wrong_attempts += 1
                                random_wrong_message = random.choice(wrong_answer_messages)
                            else:
                                random_right_message = random.choice(right_answer_messages)
                

                if questions_to_be_asked[question_nb_now].correct != user_choice: # USER PICKS WRONG ANSWER 
                    if user_choice == 0:
                        exec(options_buttons[0].replace("BLACK", "RED"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("A", True, RED), (100, 265))

                    if user_choice == 1:
                        exec(options_buttons[1].replace("BLACK", "RED"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("B", True, RED), (103, 368))

                    if user_choice == 2:
                        exec(options_buttons[2].replace("BLACK", "RED"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("C", True, RED), (98, 468))

                    if user_choice == 3:
                        exec(options_buttons[3].replace("BLACK", "RED"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("D", True, RED), (100, 566))

                        
                    screen.blit(TITLE_FONT.render(random_wrong_message, True, BLACK), (WIDTH / 2 - TITLE_FONT.size(random_wrong_message)[0] / 2, HEIGHT - TITLE_FONT.size(random_wrong_message)[1] - 10)) # RENDERS WRONG ANSWER MOTIVATION MESSAGE

                else: # USER PICKS CORRECT ANSWER
                    if user_choice == 0:
                        exec(options_buttons[0].replace("BLACK", "GREEN"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("A", True, GREEN), (100, 265))

                    if user_choice == 1:
                        exec(options_buttons[1].replace("BLACK", "GREEN"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("B", True, GREEN), (103, 368))

                    if user_choice == 2:
                        exec(options_buttons[2].replace("BLACK", "GREEN"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("C", True, GREEN), (98, 468))

                    if user_choice == 3:
                        exec(options_buttons[3].replace("BLACK", "GREEN"))
                        screen.blit(pygame.font.SysFont("constantia", 55).render("D", True, GREEN), (100, 566))

                    screen.blit(TITLE_FONT.render(random_right_message, True, BLACK), (WIDTH / 2 - TITLE_FONT.size(random_right_message)[0] / 2, HEIGHT - TITLE_FONT.size(random_right_message)[1] - 10)) # RENDERS RIGHT ANSWER MOTIVATION MESSAGE


                    screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
                    if mouse_rect.colliderect(CONTINUE_RECTANGLE_RIGHT):
                        screen.blit(right_arrow_gray, (WIDTH - 50, HEIGHT - 50))
                        if not left and click_dummy == 1 and clicked_at_least_once:
                            clicked_at_least_once = False
                            question_nb_now += 1
                            user_choice = -1
                            random_wrong_message = ""
                            metrics["time"] = f"{str_minutes}:{str_seconds}"
                            metrics["wrong attempts"] = wrong_attempts
                            metrics["total attempts"] = total_attempts
                            metrics["accuracy"] = (total_attempts - wrong_attempts) / total_attempts


    if page == 3:
        if left:
            clicked_at_least_once = True

        test_finished = True

        screen.blit(TITLE_FONT.render(f"Time: {metrics["time"]}", True, BLACK), (100, 150))
        screen.blit(TITLE_FONT.render(f"Number of wrong attempts: {metrics["wrong attempts"]}", True, BLACK), (100, 250))
        screen.blit(TITLE_FONT.render(f"Number of total attempts: {metrics["total attempts"]}", True, BLACK), (100, 350))
        screen.blit(TITLE_FONT.render(f"Accuracy: {int(metrics["accuracy"] * 100)}%", True, BLACK), (100, 450))

        screen.blit(right_arrow_black, (WIDTH - 50, HEIGHT - 50)) # RENDERS NEXT PAGE BUTTON
        if mouse_rect.colliderect(CONTINUE_RECTANGLE_RIGHT):
            screen.blit(right_arrow_gray, (WIDTH - 50, HEIGHT - 50))
            if not left and click_dummy == 1 and clicked_at_least_once:
                page = 1
                started = False
                test_started = False
                dummy_start = 0

                questions_to_be_asked = list()
                question_nb_now = 0
                user_choice = -1
                wrong_attempts = 0
                total_attempts = 0

                Qlass.generate_porblems()

                easy_questions = Qlass.Qlass.easy
                medium_questions = Qlass.Qlass.medium
                hard_questions = Qlass.Qlass.hard

                algebra_questions = Qlass.Qlass.algebra_ques
                geometry_questions = Qlass.Qlass.geometry_ques

                easy_algebra = easy_questions.intersection(algebra_questions)
                medium_algebra = medium_questions.intersection(algebra_questions)
                hard_algebra = hard_questions.intersection(algebra_questions)

                easy_geometry = easy_questions.intersection(geometry_questions)
                medium_geometry = medium_questions.intersection(geometry_questions)
                hard_geometry = hard_questions.intersection(geometry_questions)

                all_questions = Qlass.Qlass.all_ques

                test_finished = False


    if not left: # MUST BE AT THE END
        click_dummy = 0

    pygame.display.update()
    clock.tick(60)
