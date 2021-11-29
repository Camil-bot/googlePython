import scrape


def read_from_file(user_input):
    while True:
        if user_input == 'yes':
            with open('titles.txt', 'r') as file:
                for line in file.readlines():
                    print(line)
            break
        elif user_input == 'no':
            print('oke :(')
            break
        else:
            print("Not a valid input")


def write_to_file(user_write):
    if user_write == 'yes':
        print("Proceed to Writing")
        continue_writing = True
        with open('titles.txt', 'a') as file:
            while continue_writing:
                i = input()
                if i == '<quit>':
                    continue_writing = False
                    break
                file.write(i + "\n")
    else:
        print('oke :(')


if __name__ == "__main__":
    scrape.scrape()
    read_from_file(input('Whould you like read? \n'))
    write_to_file(input('Whould you like write? \n'))
