import os
import sys

def count(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} nu este valabila")

        files = os.listdir(dir_path)

        if not files:
            print(f"{dir_path} nu contine fisiere")
            return

        count_ext = {}
        for file in files:
            file_path = os.path.join(dir_path, file)

            if os.path.isdir(file_path):
                continue

            _, extension = os.path.splitext(file)
            if extension not in count_ext:
                count_ext[extension] = 0
            count_ext[extension] += 1

        if count_ext:
            print("Extensiile sunt:\n")
            for ext, count in count_ext.items():
                print(f"{ext or "No extension"}: {count}")
        else:
            print("Nu s-au gasit fisiere cu extensii")

    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Foloseste: python script4.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    count(dir_path)