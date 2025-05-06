import csv
import os


def read_csv_file(filename: str) -> list:
    """
    Reads a CSV file and returns a list of dictionaries representing the rows.

    :param filename: Path to the CSV file.
    :return: List of dictionaries, where each dictionary represents a row in the CSV file.
    """

    base_path = os.path.dirname(os.path.dirname(__file__))  # вихід з /src
    file_path = os.path.join(base_path, "data", filename)

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        render = csv.reader(csvfile)
        data = [list(map(int, row)) for row in render]
    return data
