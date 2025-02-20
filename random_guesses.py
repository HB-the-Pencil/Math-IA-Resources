import random as r

def generate_test(length, choices=4):
    """
    Generate an answer key for a test of length questions.

    :param length: Number of questions in test.
    :param choices: Number of choices per question.

    :return: Returns a list of the correct answers (answers are in numerical
        form, random from 1 to choices)
    """
    answers = []

    for i in range(length):
        answers.append(r.randint(1, choices))

    return answers


def answer_randomly(answer, choices=4):
    """
    Select a random answer to a question and validate its correctness.

    :param answer: The correct answer.
    :param choices: Number of choices available to be made.

    :return: Returns 1 if the answer is true and 0 if the answer is false.
    """
    choice = r.randint(1, choices)

    if choice == answer:
        return 1
    return 0


def answer_provided(answer, value):
    """
    Answer a question with a passed value and validate its correctness.

    :param answer: The correct answer.
    :param value: The value to be given as the answer.

    :return: Returns 1 if the answer is true and 0 if the answer is false.
    """
    if value == answer:
        return 1
    return 0