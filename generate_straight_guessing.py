from random_guesses import generate_test, answer_provided

import csv

TRIALS = 100       # How many times to run the simulation.
TEST_LENGTH = 100  # How many questions in the test.
CHOICES = 4        # How many choices are available for each question.


# Store the results. The data already in there is info for the CSV file.
b_results = [[f"Q{q+1}" for q in range(TRIALS)]]

b_results[0].insert(0, "Test #")

add = ["Total Correct", "Total Questions", "Percentage Correct"]
for item in add:
    b_results[0].append(item)

for i in range(TRIALS):
    # Generate an answer key.
    test = generate_test(TEST_LENGTH, CHOICES)

    # A temporary results storage unit for each test. The first item tells
    # which test is being run currently.
    b_temp = [i+1]

    for j in test:
        b_temp.append(answer_provided(j, 2))

    # Add the number of correct questions and total number of questions.
    b_temp.append(sum(b_temp[1:]))

    b_temp.append(TEST_LENGTH)

    # Add the percentage correct.
    b_temp.append(round(b_temp[-2] / TEST_LENGTH, 3))

    b_results.append(b_temp)

# Write the results to CSV files.
with open("only_b_results.csv", "w", newline="") as r:
    writer = csv.writer(r)
    for row in b_results:
        writer.writerow(row)