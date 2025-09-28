# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# 메모리 기반의 간단한 TODO 리스트 (서버 재시작 시 초기화됨)
todos = []

@app.route('/api/random')
def random_number():
    """1부터 99 사이의 랜덤한 정수를 생성하고 JSON 형태로 반환합니다."""
    number = random.randint(1, 99)
    return jsonify({'number': number})

@app.route('/api/echo/<text>')
def echo(text):
    """사용자가 보낸 텍스트를 그대로 반환합니다."""
    return jsonify({'echo': text})

@app.route('/api/todo', methods=['GET', 'POST', 'DELETE'])
def todo_api():
    """
    GET: 현재 할 일 목록 반환
    POST: {"task": "..."} JSON 형식으로 요청 시 할 일 추가
    DELETE: {"task": "..."} JSON 형식으로 요청 시 할 일 삭제
    """
    global todos
    if request.method == 'GET':
        return jsonify({'todos': todos})

    elif request.method == 'POST':
        data = request.get_json()
        task = data.get('task')
        if task and task not in todos:
            todos.append(task)
            return jsonify({'message': '할 일이 추가되었습니다.', 'todos': todos})
        return jsonify({'message': '유효하지 않거나 이미 존재하는 항목입니다.', 'todos': todos}), 400

    elif request.method == 'DELETE':
        data = request.get_json()
        task = data.get('task')
        if task in todos:
            todos.remove(task)
            return jsonify({'message': '할 일이 삭제되었습니다.', 'todos': todos})
        return jsonify({'message': '해당 항목이 존재하지 않습니다.', 'todos': todos}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
