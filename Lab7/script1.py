import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Foloseste: python script1.py <directory_path> <file_extension>")
        sys.exit(1)

    dir_path = sys.argv[1]
    file_ext = sys.argv[2]

    if not file_ext.startswith('.'):
        print("Error: extensia nu incepe cu punct")

    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} nu-i valida")

        print(f"Cautam fisiere cu extensia {file_ext} in {dir_path}...")
        files = [file for file in os.listdir(dir_path) if file.endswith(file_ext)]

        if not files:
            print(f"Nu s-au gasit fisiere cu extensia {file_ext} in {dir_path}")
            return

        for file in files:
            file_path = os.path.join(dir_path, file)
            try:
                with open(file_path, 'r') as file:
                    print(f"Continut din {file.name}\n")
                    print(file.read())
            except Exception as e:
                print(f"Eroare la citirea {file}: {e}")
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()