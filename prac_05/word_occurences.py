def word_count(string):
    text_count = dict()
    words = string.split()

    for i in words:
        if i in text_count:
            text_count[i] += 1
        else:
            text_count[i] = 1

    return text_count


def main():
    text = input("Input your text: ")
    while text != "":
        print(word_count(text))
        text = input("Input your text: ")


main()
