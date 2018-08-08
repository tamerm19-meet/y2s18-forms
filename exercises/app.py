from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods = ['GET', 'POST'])
def add_student_route():
	if resquest.method == 'GET':
		return render_template('add.html')
	else:
		student_name = request.form['student_name']
		student_year = request.form['student_year']

		add_student(student_name, student_year, False)

		return render_template('add.html', student_name = student_name, student_year = student_year)
		# print("Recieved a POST request")
		# return render_template('add.html')
app.run(debug=True)
