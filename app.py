from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/calculate', methods=['POST'])
def calculate_grade():
    data = request.get_json()
    if not data or 'marks' not in data:
        return jsonify({"error": "Please provide a list of marks"}), 400
    marks = data['marks']
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    else:
        grade = 'F'
    return jsonify({
        "total_marks": total,
        "average_marks": round(average, 2),
        "grade": grade
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)