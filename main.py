class DocumentReadError(Exception):
    """Custom exception used to wrap low-level system and decoding errors."""
    pass


def read_robust_file(filename):
    """
    Attempts to open and read a file as UTF-8 text safely.
    Uses custom error wrapping, context managers, and an else block.
    """
    try:
        # Use a context manager to automatically close the file safely
        with open(filename, mode='r', encoding='utf-8') as file:
            content = file.read()

    # Handle low-level exceptions and translate them into DocumentReadError
    except FileNotFoundError:
        raise DocumentReadError(f"System Error: The file '{filename}' could not be found.")

    except PermissionError:
        raise DocumentReadError(f"System Error: Access denied. Missing permission to read '{filename}'.")

    except UnicodeDecodeError:
        raise DocumentReadError(f"Format Error: '{filename}' cannot be decoded as clean UTF-8 text.")

    else:
        # Display file content ONLY on full execution success using else
        print(f"\n--- File Contents of '{filename}' ---")
        print(content)
        print("---------------------------------------")


def main():
    print("--- Robust File Reader Console ---")

    # Ask for a filename
    filename = input("Enter the path/name of the file you want to read: ").strip()

    try:
        read_robust_file(filename)
    except DocumentReadError as error:
        print(f"\n[Read Failed] {error}")


if __name__ == "__main__":
    main()
