import hashlib
import os

def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


def main():

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("File does not exist!")
        return

    original_hash = calculate_hash(file_path)

    print("\nOriginal Hash:")
    print(original_hash)

    input("\nModify the file if you want, then press Enter...")

    current_hash = calculate_hash(file_path)

    print("\nCurrent Hash:")
    print(current_hash)

    if original_hash == current_hash:
        print("\n[+] File Integrity Maintained")
    else:
        print("\n[!] Warning: File Modified")


main()
