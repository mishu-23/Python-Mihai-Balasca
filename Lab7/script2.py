import os
import sys
def prefixes(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} nu e corect")

        files = os.listdir(dir_path)

        if not files:
            print(f"Nu sunt fisiere in {dir_path}")

        files.sort()

        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(dir_path, filename)
            if os.path.isdir(old_path):
                continue

            new_filename = f"{index}_{filename}"
            new_path = os.path.join(dir_path, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Am redenumit {filename} cu {new_filename}")
            except Exception as e:
                print(f"Eroare la redenumirea {filename}")
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Foloseste: python script2.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    prefixes(dir_path)