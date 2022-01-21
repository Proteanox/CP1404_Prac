import wikipedia


def main():
    print("wiki test")

    loop = True
    while loop:
        print_menu()
        choice = input(" Enter a choice;").upper()
        if choice == "A":
            search()
        elif choice == "B":
            suggest()
        elif choice == "C":
            summary()
        elif choice == "D":
            page_output()
        elif choice == "Q":
            print(" You Quit!")
            loop = False
        else:
            print("Wrong Input")


def print_menu():
    print("MENU\nSearch = A\nSuggest = B\nSummary = C\nPage = D\n Quit = Q")


def search():
    """choice A"""
    print("-" * 55)
    word = input(" Enter your Search Word: ")
    print(wikipedia.search(word))


def suggest():
    """Choice B"""
    print("-" * 55)
    phrase = input(" Enter your word for Suggestions")
    print(wikipedia.suggest(phrase))


def summary():
    """Choice C"""
    print("-" * 55)
    phrase = input(" Enter a word to obtain summary")
    print(wikipedia.summary(phrase))


def page_output():
    """Choice D"""
    print("-" * 55)
    word = input(" Enter a word to output page details")
    page = wikipedia.page(word)
    print(f"Page Title: {page.title} \n URL: {page.url} \n Content: {page.content} \n Summary: {page.summary} "
          f"\n {page.images[0]} \n Links: {page.links}")


main()
