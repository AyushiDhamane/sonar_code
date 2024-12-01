import os

def greet_user(name: str) -> str:
    """
    Generate a greeting message for the user.
    Args:
        name (str): Name of the user.
    Returns:
        str: Greeting message.
    """
    # Vulnerability: No input validation for "name"
    if name == "":
        return "Hello, Stranger!"
    return f"Hello, {name}!"  # Possible format string vulnerability


def read_file_content(filename: str) -> str:
    """
    Read the content of a file.
    Args:
        filename (str): File name to read.
    Returns:
        str: Content of the file.
    """
    # Vulnerability: No validation or sanitization of "filename"
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def execute_command(command: str):
    """
    Execute a system command.
    Args:
        command (str): Command to execute.
    """
    # Critical Vulnerability: Unsanitized user input passed to os.system
    os.system(command)


def main():
    """
    Main function to run the application.
    """
    print("1. Greet a user")
    print("2. Read a file")
    print("3. Execute a command")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        name = input("Enter your name: ")
        print(greet_user(name))
    elif choice == "2":
        filename = input("Enter the filename to read: ")
        print(read_file_content(filename))
    elif choice == "3":
        command = input("Enter a system command to execute: ")
        execute_command(command)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
