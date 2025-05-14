import os


def read_file(filename: str):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", filename)

    with open(file_path, "r") as file:
        lines = file.readlines()

    first_line = int(lines[0].strip())
    second_line = list(map(int, lines[1].strip().split()))

    return first_line, second_line

if __name__ == "__main__":
    filename = "case1.txt"
    w, h = read_file(filename)
    print(f"Width: {w}, Heights: {h}")