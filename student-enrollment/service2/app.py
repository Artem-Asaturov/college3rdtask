from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/students')
def get_students():
    students = [{"name": "John", "course": "Math"}, {"name": "Alice", "course": "Physics"}]
    return jsonify(students)

if __name__ == '__main__':
    app.run(port=5001)
