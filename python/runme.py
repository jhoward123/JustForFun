

def main():
    print("Please enter your name: ")
    name = input("Name: ")
    just_letters = ''.join([x for x in name if x.isalpha()])

    print(f"Hello, {name}.\nYou have {len(just_letters)} letters in your name.")


if __name__ == "__main__":
    main()

