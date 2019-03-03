import connection


def get_new_id(filename):
    csv_content = list(connection.import_from_csv(filename))
    csv_content.sort(key=lambda x: int(x['id']))
    new_id = int(csv_content[-1]['id']) + 1
    return new_id

