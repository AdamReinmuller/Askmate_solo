from flask import Flask, render_template, request, redirect
import data_manager
import util

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.get_questions()
    return render_template('index', questions=questions)


@app.route('/post-question', methods=['GET', 'POST'])
def post_question():
    if request.method == 'GET':
        return render_template('post-question.html')
    elif request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        data_manager.write_to_questions(title, message)
        return redirect('/')


@app.route('/question/<question_id>', methods=['GET', 'POST'])
@app.route('/question/<question_id>/add-answer', methods=['GET', 'POST'])
def display_question(question_id):
    question = data_manager.get_question_by_id(question_id)
    if request.path == '/question/' + question_id + '/add-answer' and request.method == 'POST':
        message = request.form['message']
        data_manager.write_to_answers(question_id, message)
        return redirect('/question/' + question_id)
    elif request.path == '/question/' + question_id + '/add-answer' and request.method == 'GET':
        return render_template('add-answer.html', question=question)
    elif request.method == 'GET':
        answers = data_manager.get_answers(question_id)
        if len(answers) > 0:
            return render_template('question.html', question=question, answers=answers)
        else:
            return render_template('question.html', question=question)


@app.route('/answer/<answer_id>/delete')
@app.route('/question/<question_id>/delete')
def delete_qa(question_id="", answer_id=""):
    if request.path == '/question/' + question_id + '/delete':
        data_manager.delete_question_by_id(question_id)
        return redirect('/')
    elif request.path == '/answer/' + answer_id + '/delete':
        question_id = data_manager.get_question_id_of_answer(answer_id)
        data_manager.delete_answer_by_id(answer_id)
        return redirect('/question/' + question_id)


@app.route('/edit-question/<question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        data_manager.edit_question(question_id, title, message)
        return redirect('/question/' + question_id)
    elif request.method == 'GET':
        question = data_manager.get_question_by_id(question_id)
        return render_template('edit-question.html', question=question)


@app.route('/edit-answer/<answer_id>', methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'POST':
        question_id = data_manager.get_question_id_of_answer(answer_id)
        message = request.form['message']
        data_manager.edit_answer(answer_id, message)
        return redirect('/question/' + question_id)
    elif request.method == 'GET':
        answer = data_manager.get_answer_by_id(answer_id)
        return render_template('edit-answer.html', answer=answer)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
