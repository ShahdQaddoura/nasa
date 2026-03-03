import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow.keras as keras
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

"""
THIS PYTHON SCRIPT IS THE SAME AS THE JUPYTER NOTEBOOK, JUST TRANSFORMED INTO A SCRIPT FOR CONVENIENCE.

THIS SCRIPT ALSO SAVES THE NEURAL NETWORKS SO THEY CAN BE USED EVEN AFTER CLOSING THE SCRIPT/EDITOR.
"""


df = pd.read_csv('C:\\Users\\Owner\\Documents\\Uni\\Courses\\Fall 2024 (Year 1, Term I)\\LAS205 (Digital Cultures)\\Projects\\Project 1 - Python AI\\data_csv.csv')

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

df["time"] = df["time"].apply(normalize_time)
df["attempts"] = df["attempts"].apply(normalize_attempts)

# I
x_accuracy = list()
x_improvement = list()

y_accuracy = list()
y_grades = list()
y_improvement = list()

for i in range(df.shape[0]):
    x_accuracy.append(df["accuracy"][i])
    x_improvement.append([df["accuracy"][i], df["time"][i], df["attempts"][i]])

    y_accuracy.append(df["next_difficulty"][i])
    y_grades.append(df["grade"][i])
    y_improvement.append([df["improvement"][i]])

x_accuracy = np.array(x_accuracy)
x_improvement = np.array(x_improvement)

y_accuracy = np.array(y_accuracy)
y_grades = np.array(y_grades)
y_improvement = np.array(y_improvement)


x_accuracy_train, y_accuracy_train, x_accuracy_test, y_accuracy_test = x_accuracy[:int(0.8 * len((x_accuracy)))], y_accuracy[:int(0.8 * len((y_accuracy)))], x_accuracy[int(0.8 * len((x_accuracy))):], y_accuracy[int(0.8 * len((y_accuracy))):]

y_accuracy_train, y_accuracy_test = keras.utils.to_categorical(y_accuracy_train, 3), keras.utils.to_categorical(y_accuracy_test, 3)

model_difficulty_predictor = Sequential()
model_difficulty_predictor.add(Dense(units = 256, activation = "relu", input_shape = (1,)))
model_difficulty_predictor.add(Dense(units = 128, activation = "relu"))
model_difficulty_predictor.add(Dense(units = 3, activation = "sigmoid"))


model_difficulty_predictor.compile(loss = "categorical_crossentropy", metrics = ["accuracy"])

nb_of_epochs_difficulty = 100
history = model_difficulty_predictor.fit(x_accuracy_train, y_accuracy_train, epochs = nb_of_epochs_difficulty, verbose = 0, validation_data = (x_accuracy_test, y_accuracy_test))


chart_x = range(1,nb_of_epochs_difficulty + 1)
chart_y_train = history.history['accuracy']
chart_y_test = history.history['val_accuracy']

plt.plot(chart_x, chart_y_train, "r-", label = "training accurcay")
plt.plot(chart_x, chart_y_test, "b-", label = "validation accuracy")
plt.xlabel("Training epochs")
plt.ylabel("Accuracy")
plt.title("Accuracy of the difficulty predictor model")
plt.legend()
plt.show()



# II
b_accuracy, m_accuracy = polyfit(x_accuracy, y_grades, 1)
y_hat_accuracy = x_accuracy * m_accuracy + b_accuracy
plt.scatter(x_accuracy, y_grades)
plt.title("Line of best fit for accuracy and grades")
plt.plot(x_accuracy, y_hat_accuracy, "r-")
plt.show()


# III
x_improvement_train, x_improvement_test = x_improvement[:int(0.8*len(x_improvement))], x_improvement[int(0.8*len(x_improvement)):]
y_improvement_train, y_improvement_test = y_improvement[:int(0.8*len(y_improvement))], y_improvement[int(0.8*len(y_improvement)):]

model_improvement = Sequential()
model_improvement.add(Dense(units = 256, activation = "relu", input_shape = (3,)))
model_improvement.add(Dense(units = 128, activation = "relu"))
model_improvement.add(Dense(units = 3, activation = "sigmoid"))

y_improvement_train, y_improvement_test = keras.utils.to_categorical(y_improvement_train, 3), keras.utils.to_categorical(y_improvement_test, 3)

model_improvement.compile(loss = "categorical_crossentropy", metrics = ["accuracy"])

nb_of_epochs_improvement = 200
history_improvement = model_improvement.fit(x_improvement_train, y_improvement_train, epochs = nb_of_epochs_improvement, verbose = 0, validation_data = (x_improvement_test, y_improvement_test))


chart_x = range(1, nb_of_epochs_improvement + 1)
chart_y_train = history_improvement.history['accuracy']
chart_y_test = history_improvement.history['val_accuracy']

plt.plot(chart_x, chart_y_train, "r-", label = "training accurcay")
plt.plot(chart_x, chart_y_test, "b-", label = "validation accuracy")
plt.xlabel("Training epochs")
plt.ylabel("Accuracy")
plt.title("Accuracy of the area of improvement predictor model")
plt.legend()
plt.show()


# SAVERS
model_difficulty_predictor.save("Assets\\model_difficulty_predictor.h5")

model_improvement.save("Assets\\model_improvement.h5")


print("\nDone!\n")