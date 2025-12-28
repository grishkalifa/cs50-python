def count_words(text):
    # Words are separated by whitespace in CS50 definition
    return len(text.split())


def count_letters(text):
    letters = 0
    for ch in text:
        if ch.isalpha():
            letters += 1
    return letters


def count_sentences(text):
    sentences = 0
    for ch in text:
        if ch in ".!?":
            sentences += 1
    return sentences


def calculate_L(letters, words):
    if words == 0:
        return 0
    return (letters / words) * 100


def calculate_S(sentences, words):
    if words == 0:
        return 0
    return (sentences / words) * 100


def calculate_grade(L, S):
    x = 0.0588 * L - 0.296 * S - 15.8
    grade = round(x)

    if grade >= 16:
        return x, "Grade 16+"
    elif grade < 1:
        return x, "Before Grade 1"
    else:
        return x, f"Grade {grade}"


def main():
    text = input("Insert text: ")

    words = count_words(text)
    letters = count_letters(text)
    sentences = count_sentences(text)

    L = calculate_L(letters, words)
    S = calculate_S(sentences, words)

    x, grade = calculate_grade(L, S)

    print(f"Words: {words}")
    print(f"Letters: {letters}")
    print(f"Sentences: {sentences}")
    print(f"L: {L:.2f}")
    print(f"S: {S:.2f}")
    print(f"Index (x): {x:.2f}")
    print(grade)


main()
