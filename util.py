import connection


def get_new_id(filename):
    csv_content = connection.import_from_csv(filename)
    new_id = int(csv_content[-1]['id']) + 1
    return new_id

