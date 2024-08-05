import os

def files1(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folders = input("Enter a list of folder paths separated by spaces: ").split()
    for folder in folders:
        files, error_message = files1(folder)
        if files:
            print("Files in:",folder)
            for file in files:
                print(file)
        else:
            print(error_message)

if __name__ == "__main__":
    main()