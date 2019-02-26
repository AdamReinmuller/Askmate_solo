import connection
import util
import csv
import time


def get_questions():
    """
    :return: questions in a list of ordered dictionaries
    """
    questions = connection.import_from_csv(connection.question_file)
    return questions


def get_answers(question_id=-1):
    """
    :return: all answers in a list of ordered dictionaries or just the related ones to the question_id
    """
    answers = connection.import_from_csv(connection.answer_file)
    if question_id == -1:
        return answers
    related_answers = []
    for row in answers:
        if row['question_id'] == question_id:
            related_answers.append(row)
    related_answers.sort(key=lambda x: x['submission_time'], reverse=True)
    return related_answers


def write_to_questions(title, message):
    """
    :return: writes a list of ordered dictionaries to question_file
    """
    list_of_odicts = get_questions()
    new_id = util.get_new_id(connection.question_file)
    current_time = round(time.time())
    new_row = {'id': str(new_id),
               'submission_time': str(current_time),
               'view_number': str(0),
               'vote_number': str(0),
               'title': title,
               'message': message,
               'image': 'no image'}
    list_of_odicts.insert(0, new_row)
    connection.export_to_csv(connection.question_file, list_of_odicts)


def write_to_answers(question_id, message):
    """
    :return: writes a list of ordered dictionaries to answer_file
    """
    list_of_odicts = get_answers()
    new_id = util.get_new_id(connection.answer_file)
    current_time = round(time.time())
    new_row = {'id': str(new_id),
               'submission_time': str(current_time),
               'vote_number': str(0),
               'question_id': question_id,
               'message': message,
               'image': 'no image'}
    list_of_odicts.insert(0, new_row)
    connection.export_to_csv(connection.answer_file, list_of_odicts)


def get_question_by_id(question_id):
    """
    :return: ordered dictionary by id
    """
    questions = get_questions()
    for row in questions:
        if row['id'] == question_id:
            return row


def get_answer_by_id(answer_id):
    """
    :return: ordered dictionary by id
    """
    answers = get_answers()
    for row in answers:
        if row['id'] == answer_id:
            return row


def delete_question_by_id(question_id):
    questions = get_questions()
    answers = get_answers()
    for row in questions:
        if row['id'] == question_id:
            questions.remove(row)
    connection.export_to_csv(connection.question_file, questions)
    for row in answers:
        if row['question_id'] == question_id:
            answers.remove(row)
    connection.export_to_csv(connection.answer_file, answers)


def delete_answer_by_id(answer_id):
    answers = get_answers()
    for row in answers:
        if row['id'] == answer_id:
            answers.remove(row)
    connection.export_to_csv(connection.answer_file, answers)


def edit_question(question_id, new_title, new_message):
    """
    :return: edits the question_file
    """
    questions = get_questions()
    for row in questions:
        if row['id'] == question_id:
            row['title'] = new_title
            row['message'] = new_message
            break
    connection.export_to_csv(connection.question_file, questions)


def edit_answer(answer_id, new_message):
    """
    :return: edits the answer_file
    """
    answers = get_answers()
    for row in answers:
        if row['id'] == answer_id:
            row['message'] = new_message
            break
    connection.export_to_csv(connection.answer_file, answers)


def get_question_id_of_answer(answer_id):
    """
    :param answer_id:
    :return: corresponding question_id of the given answer
    """
    answers = get_answers()
    for row in answers:
        if row['id'] == answer_id:
            return row['question_id']
