import hashlib
import os


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: File not found.")
        return None


def save_hash(file_path, hash_value):
    """Save the hash value to a file."""

    hash_file = file_path + ".hash"

    with open(hash_file, "w") as file:
        file.write(hash_value)

    print("Hash saved successfully.")
    print("Hash file:", hash_file)


def check_integrity(file_path):
    """Compare the current hash with the saved hash."""

    hash_file = file_path + ".hash"

    if not os.path.exists(hash_file):
        print("No previous hash found.")
        print("Please create a baseline hash first.")
        return

    current_hash = calculate_hash(file_path)

    if current_hash is None:
        return

    with open(hash_file, "r") as file:
        original_hash = file.read().strip()

    print("\nOriginal Hash:")
    print(original_hash)

    print("\nCurrent Hash:")
    print(current_hash)

    if original_hash == current_hash:
        print("\nRESULT: File has NOT been modified.")
    else:
        print("\nRESULT: WARNING! File has been modified.")


def main():
    print("==============================")
    print("     FILE INTEGRITY CHECKER")
    print("==============================")

    file_path = input("\nEnter the file path: ").strip()

    if not os.path.exists(file_path):
        print("Error: The file does not exist.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Create baseline hash")
        print("2. Check file integrity")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            file_hash = calculate_hash(file_path)

            if file_hash:
                print("\nSHA-256 Hash:")
                print(file_hash)

                save_hash(file_path, file_hash)

        elif choice == "2":
            check_integrity(file_path)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()