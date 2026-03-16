import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def store_hash(file_path, hash_value):
    with open("hash_store.txt", "w") as f:
        f.write(file_path + "," + hash_value)


def check_integrity(file_path):
    new_hash = calculate_hash(file_path)

    with open("hash_store.txt", "r") as f:
        data = f.read().split(",")

    stored_hash = data[1]

    if new_hash == stored_hash:
        print("File Integrity Verified. No changes detected.")
    else:
        print("WARNING: File has been modified!")


print("1. Generate Hash")
print("2. Check File Integrity")

choice = input("Enter your choice: ")
file_path = input("Enter file name: ")

if choice == "1":
    hash_value = calculate_hash(file_path)
    store_hash(file_path, hash_value)
    print("Hash stored successfully!")

elif choice == "2":
    check_integrity(file_path)