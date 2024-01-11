import wikipedia
def main():
    try:
        user_input = input("Page title/Search phrase: ")
        while user_input != "":
             print(wikipedia.search(user_input))
             print(wikipedia.summary(user_input))
             info = wikipedia.page(user_input)
             print(info.url)
             user_input = input("Page title/Search phrase: ")
        else:
              print("")
    except wikipedia.exceptions.DisambiguationError as e:
           print(e.options)
main()
