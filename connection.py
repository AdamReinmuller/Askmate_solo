import csv

question_file = 'data/question.csv'
answer_file = 'data/answer.csv'


def import_from_csv(filename):
    """
    :param filename: relative path
    :return: list of ordered dictionaries
    """
    with open(filename, "r") as f:
        csv_content = list(csv.DictReader(f))
    return csv_content


def export_to_csv(filename, list_of_ordered_dicts):
    """
    :param filename: relative path
    :return: writes list of ordered dictionaries to filename
    """
    fieldnames = list_of_ordered_dicts[0].keys()
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(list_of_ordered_dicts)


