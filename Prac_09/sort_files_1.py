import os


def main():
    os.chdir("FilesToSort")
    for file in os.listdir('.'):

        if os.path.isdir(file):
            continue

        end = file.split('.')[-1]

        # maintains the list set
        # handling errors
        try:
            os.mkdir(end)
        except FileExistsError:
            pass
        print(f"{file}/{end}")
        os.rename(file, f"{file}/{end}")


main()
