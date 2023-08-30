"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tereza Srbová
email: terezasrbova.ts@gmail.com
discord: Tereza S#9721
"""
from task_template import TEXTS

REGISTERED_USERS = {"bob": "123",
                    "ann": "pass123",
                    "mike": "password123",
                    "liz": "pass123"}
TEXTS_COUNT = len(TEXTS)


def execute():
    username = input("username:")
    password = input("password:")
    if (username not in REGISTERED_USERS or
            REGISTERED_USERS[username] != password):
        print("unregistered user, terminating the program..")
        return
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("----------------------------------------")
    print(f"We have {TEXTS_COUNT} texts to be analyzed.")
    text_number = input(
        f"Enter a number btw. 1 and {TEXTS_COUNT} to select:")
    if (not text_number.isnumeric() or
            int(text_number) not in range(1, TEXTS_COUNT + 1)):
        print("Invalid input,terminating the program..")
        return
    text = TEXTS[int(text_number) - 1]
    print("----------------------------------------")
    print(f"There are {get_count_of_words(text)} "
          f"words in the selected text.")
    print(f"There are "
          f"{get_count_of_words_with_first_letter_upper_case(text)} "
          f"titlecase words.")
    print(f"There are "
          f"{get_count_of_words_with_all_letters_upper_case(text)} "
          f"uppercase words.")
    print(f"There are "
          f"{get_count_of_words_with_all_letters_lower_case(text)} "
          f"lowercase words.")
    print(f"There are {get_count_of_numbers(text)} numeric strings.")
    print(f"The sum of all the numbers {get_sum_of_numbers(text)}")
    print("----------------------------------------")
    draw_chart(text)


def get_count_of_words(text):
    return len(text.split())


def get_count_of_words_with_first_letter_upper_case(text):
    return len([word for word in text.split() if
                len(word) and word[0].isupper()])


def get_count_of_words_with_all_letters_upper_case(text):
    return len([word for word in text.split() if word.isupper()])


def get_count_of_words_with_all_letters_lower_case(text):
    return len([word for word in text.split() if word.islower()])


def get_count_of_numbers(text):
    return len([word for word in text.split() if word.isnumeric()])


def get_sum_of_numbers(text):
    return sum([int(word) for word in text.split() if word.isnumeric()])


def get_count_of_individual_word_lengths(text):
    counts = {}
    for word in text.split():
        word_length = len([ch for ch in word if ch.isalnum()])
        if word_length in counts.keys():
            counts[word_length] += 1
        else:
            counts[word_length] = 1
    return counts


def draw_chart(text):
    counts = get_count_of_individual_word_lengths(text)
    maximal_length = max(counts.keys())
    header = "   OCCURRENCES   "
    column_width = max([max(counts.values()), len(header)])
    print("LEN|" + header + "|NR.")
    print("----------------------------------------")
    for i in range(1, maximal_length + 1):
        words_count = counts[i] if i in counts.keys() else 0
        print(f"{i}|".rjust(4, " ") +
              (words_count*"*").ljust(column_width, " ") + f"|{words_count}")


if __name__ == "__main__":
    execute()
