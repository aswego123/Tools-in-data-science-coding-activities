from flask import Flask, render_template_string, request

app = Flask(__name__)

questions = [
    {
        'question': 'Which is the farthest planet from the Sun?',
        'options': ['Neptune', 'Uranus', 'Saturn', 'Pluto', 'Jupiter'],
        'answer': 'Pluto'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Mars', 'Venus', 'Jupiter', 'Mercury'],
        'answer': 'Mars'
    },
    {
        'question': 'Which planet has the most moons?',
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune'],
        'answer': 'Saturn'
    },
    {
        'question': 'Which planet is closest to the Sun?',
        'options': ['Venus', 'Earth', 'Mercury', 'Mars', 'Jupiter'],
        'answer': 'Mercury'
    }
]

TEMPLATE = '''
<!doctype html>
<title>Quiz App</title>
<h2>Quiz App</h2>
<form method="post">
    <p>{{ q['question'] }}</p>
    {% for opt in q['options'] %}
        <input type="radio" name="answer" value="{{ opt }}" required> {{ opt }}<br>
    {% endfor %}
    <input type="hidden" name="qid" value="{{ qid }}">
    <button type="submit">Submit</button>
</form>
{% if feedback %}
    <p><strong>{{ feedback }}</strong></p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def quiz():
    qid = int(request.form.get('qid', 0))
    feedback = ''
    if request.method == 'POST':
        selected = request.form.get('answer')
        correct = questions[qid]['answer']
        if selected == correct:
            feedback = 'Correct!'
        else:
            feedback = f'Incorrect. The correct answer is {correct}.'
        qid += 1
        if qid >= len(questions):
            return '<h2>Quiz Complete!</h2>'
    q = questions[qid]
    return render_template_string(TEMPLATE, q=q, qid=qid, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
