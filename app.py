from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セキュアなキーに置き換えてください

# 質問と学科のデータを読み込み
with open('data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('data/departments.json', 'r', encoding='utf-8') as f:
    departments = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if 'responses' not in session:
        session['responses'] = []

    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option is None:
            error = '選択肢を選んでください。'
            return render_template('quiz.html', question=questions[question_id - 1], error=error)
        session['responses'].append(int(selected_option))

        if question_id >= len(questions):
            return redirect(url_for('result'))
        else:
            return redirect(url_for('quiz', question_id=question_id + 1))

    question = questions[question_id - 1]
    return render_template('quiz.html', question=question, question_id=question_id, total_questions=len(questions))

@app.route('/result')
def result():
    responses = session.get('responses', [])
    department_scores = {dept: 0 for dept in departments.keys()}

    for i, selected_option_index in enumerate(responses):
        option = questions[i]['options'][selected_option_index]
        for dept, points in option['points'].items():
            department_scores[dept] += points

    max_score = max(department_scores.values())
    best_departments = [dept for dept, score in department_scores.items() if score == max_score]

    return render_template('result.html', departments=best_departments, department_names=departments)

if __name__ == '__main__':
    app.run(debug=True)
