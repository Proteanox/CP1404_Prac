import os


def main():
    category_by_end = {}
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue
        # split csv index
        end = file.split('.')[-1]
        if end not in category_by_end:
            category = input(f"Input Your Categorization Scale {end}")
            category_by_end[end] = category
            try:
                # We don't expect to get an exception due to the if statement
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(file, f"{file}/{end}")

main()