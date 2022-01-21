import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue

        end = file.split('.')[-1]
        if end not in extension_to_category:
            category = input(f"Input Your Categorization Scale {end}")
            extension_to_category[end] = category
            try:
                # We don't expect to get an exception due to the if statement
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(file, f"{file}/{end}")

main()