from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks', __name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Study how Flask works", "status": "Incomplete"},
    {"id": 2, "title": "Create API", "description": "Build a simple API", "status": "Incomplete"}
]
task_id_counter = 1

@tasks_bp.route('', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json
    if 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input, title and description are required'}), 400
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    task_id_counter += 1
    tasks.append(task)
    return jsonify(task), 201

@tasks_bp.route('', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task), 200

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200
