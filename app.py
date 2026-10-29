from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/calculate', methods=['POST'])
def calculate_grade():
    data = request.get_json()
    if not data or 'marks' not in data:
        return jsonify({"error": "Please provide a list of marks"}), 400
    marks = data['marks']
    if not isinstance(marks, list) or len(marks) == 0:
        return jsonify({"error": "Marks must be a non-empty list"}), 400
    total = sum(marks)
    average = total / len(marks)
    return jsonify({
        "total_marks": total,
        "average_marks": round(average, 2)
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
