from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stages')
def stages():
    return render_template('stages.html')


@app.route('/caregivers')
def caregivers():
    return render_template('caregivers.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    result = None
    if request.method == 'POST':
        # Get all quiz answers
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        
        # Count correct answers
        correct_count = 0
        if q1 == 'correct':
            correct_count += 1
        if q2 == 'correct':
            correct_count += 1
        if q3 == 'correct':
            correct_count += 1
        if q4 == 'correct':
            correct_count += 1
        
        # Generate result message
        if correct_count == 4:
            result = f'Perfect score! You got all 4 questions correct! 🎉'
        elif correct_count == 3:
            result = f'Great job! You got 3 out of 4 correct. Keep learning!'
        elif correct_count == 2:
            result = f'Good effort! You got 2 out of 4 correct. Review the material and try again.'
        elif correct_count == 1:
            result = f'You got 1 out of 4 correct. Make sure to review all the sections thoroughly.'
        else:
            result = f'No answers were correct. Please review the Alzheimer\'s disease information and try again.'
    
    return render_template('quiz.html', result=result)


@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(debug=True)
