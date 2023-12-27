from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get('http://localhost:5000/courses')
        response.raise_for_status()
        courses = response.json()
    except Exception as e:
        print("Error fetching courses:", str(e))
        courses = ["Math", "Physics", "Chemistry"]

    students = [{"name": "John", "course": "Math"}, {"name": "Alice", "course": "Physics"}]

    return render_template('index.html', courses=courses, students=students)

@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.json
    course = data.get('course')
    student_name = data.get('studentName')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5003, debug=True)
