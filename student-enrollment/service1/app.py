from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/courses')
def get_courses():
    courses = ["Math", "Physics", "Chemistry"]
    return jsonify(courses)

if __name__ == '__main__':
    app.run(port=5000)
