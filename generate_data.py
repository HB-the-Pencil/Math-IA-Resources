from random_guesses import generate_test, answer_randomly, answer_provided

import csv

TRIALS = 100       # How many times to run the simulation.
TEST_LENGTH = 100  # How many questions in the test.
CHOICES = 4        # How many choices are available for each question.


# Store the results. The data already in there is info for the CSV file.
random_results = [[f"Q{q+1}" for q in range(TRIALS)]]
sequential_results = [[f"Q{q+1}" for q in range(TRIALS)]]

random_results[0].insert(0, "Test #")
sequential_results[0].insert(0, "Test #")

add = ["Total Correct", "Total Questions", "Percentage Correct"]
for item in add:
    random_results[0].append(item)
    sequential_results[0].append(item)

for i in range(TRIALS):
    # Generate an answer key.
    test = generate_test(TEST_LENGTH, CHOICES)

    # The current answer for sequential guessing
    seq_answer = 1

    # A temporary results storage unit for each test. The first item tells
    # which test is being run currently.
    random_temp = [i+1]
    sequential_temp = [i+1]

    for j in test:
        random_temp.append(answer_randomly(j, CHOICES))
        sequential_temp.append(answer_provided(j, seq_answer))

        seq_answer += 1
        if seq_answer > CHOICES:
            seq_answer = 1

    # Add the number of correct questions and total number of questions.
    random_temp.append(sum(random_temp[1:]))
    sequential_temp.append(sum(sequential_temp[1:]))

    random_temp.append(TEST_LENGTH)
    sequential_temp.append(TEST_LENGTH)

    # Add the percentage correct.
    random_temp.append(round(random_temp[-2] / TEST_LENGTH, 3))
    sequential_temp.append(round(sequential_temp[-2] / TEST_LENGTH, 3))

    random_results.append(random_temp)
    sequential_results.append(sequential_temp)

# Write the results to CSV files.
with open("random_results.csv", "w", newline="") as r:
    writer = csv.writer(r)
    for row in random_results:
        writer.writerow(row)

with open("sequential_results.csv", "w", newline="") as r:
    writer = csv.writer(r)
    for row in sequential_results:
        writer.writerow(row)