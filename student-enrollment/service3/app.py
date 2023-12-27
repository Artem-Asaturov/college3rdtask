from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student_name = data.get('name')
    course_name = data.get('course')

    return jsonify({"message": f"{student_name} enrolled in {course_name}"})


if __name__ == '__main__':
    app.run(port=5002)
