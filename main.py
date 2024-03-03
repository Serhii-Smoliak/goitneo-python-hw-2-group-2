"""This module implements functionality for a CLI Bot."""


def input_error(func):
    """Decorator function for handling errors."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            print(f"A KeyError occurred: {error}")
            return None
        except ValueError:
            print(
                "Invalid number of arguments. Enter the 'help' "
                "command for additional information on the command."
            )
            return None
        except IndexError:
            print("Invalid index. Please provide a valid index.")
            return None

    return inner


def parse_input(user_input):
    """ "This function parses user-entered arguments and returns them."""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def get_all(contacts):
    """This function returns all user data."""

    if len(contacts) == 0:
        print("Contacts not found. Plese add a first contact.")
    for name, phone in contacts.items():
        print(f"{name:10} | {phone:15}")


@input_error
def add_contact(args, contacts):
    """This function adds a new user to the storage."""

    name, phone = args
    contacts[name] = phone
    print("Contact added.")


@input_error
def change_contact(args, contacts):
    """This function changes the user's phone number in the storage."""

    name, phone = args
    user_name = name.capitalize()
    contacts[user_name] = phone
    print("Contact changed.")


@input_error
def get_phone_contact(args, contacts):
    """This function returns the user's phone number."""

    [name] = args
    user_name = name.capitalize()
    if user_name not in contacts:
        print("Contact not found.")
        return
    print(contacts[user_name])


def help_message():
    """Bot command assistant function"""

    help_text = """
            >>> WELLCOME TO THE BOT COMMAND HELPER:

            hello (It is customary to say hello as a rule of good manners)
            all (Display all users info)
            add (Add a new user. Arguments: user_name phone_number)
            change (Change user phone. Arguments: user_name phone_number)
            phone (Display user phone. Argument: user_name)
            exit AND close (Finishes the work of the bot)

            >>> GOOD LUCK!
            """
    print(help_text)


def main():
    """Primary function for interacting with the user via the command line."""

    contacts = {}
    print(
        "!!! Welcome to the assistant bot !!! \n"
        "Enter the 'help' command for additional information on the command."
    )

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("Hi! How can I help you?")
        elif command == "all":
            get_all(contacts)
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            get_phone_contact(args, contacts)
        elif command == "help":
            help_message()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
