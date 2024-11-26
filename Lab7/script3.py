import os
import sys

def size(dir_path):
    size = 0

    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} nu este o cale valida")

        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    size += os.path.getsize(file_path)
                except Exception as e:
                    print(e)

        return size
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Foloseste; python script3.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    size = size(dir_path)

    if size != None:
        print(f"Dimensiunea totala a {dir_path} este: {size} bytes")