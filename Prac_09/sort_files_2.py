import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue

        end = file.split('.')[-1]
