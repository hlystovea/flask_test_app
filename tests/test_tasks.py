from app.tasks.models import Task
from app.tasks.schemes import task_schema


class TestTasks:
    def test_get_tasks(self, client, task_1, task_2):
        response = client.get('/tasks')
        tasks = Task.query.all()

        assert response.status_code == 200
        assert len(response.json) == len(tasks)
        assert task_schema.dump(task_1) in response.json
        assert task_schema.dump(task_2) in response.json

    def test_get_task(self, client, task_1):
        response = client.get(f'/tasks/{task_1.id}')

        assert response.status_code == 200
        assert response.json == task_schema.dump(task_1)

    def test_create_task(self, client, db):
        data = {
            'title': 'title',
            'description': 'description',
        }
        response = client.post('/tasks', json=data)
        assert response.status_code == 201
        assert response.json['title'] == data['title']
        assert response.json['description'] == data['description']

    def test_delete_task(self, client, db, task_2):
        response = client.get(f'/tasks/{task_2.id}')
        assert response.status_code == 200

        response = client.delete(f'/tasks/{task_2.id}')
        assert response.status_code == 200

        response = client.get(f'/tasks/{task_2.id}')
        assert response.status_code == 404

    def test_update_task(self, client, db, task_1):
        response = client.get(f'/tasks/{task_1.id}')
        assert response.status_code == 200
        assert response.json['title'] == task_1.title

        new_data = {
            'title': 'foo',
            'description': 'bar',
        }
        response = client.put(
            f'/tasks/{task_1.id}',
            json={'title': new_data['title']}
        )
        assert response.status_code == 200
        assert response.json['title'] == new_data['title']

        response = client.put(
            f'/tasks/{task_1.id}',
            json={'description': new_data['description']}
        )
        assert response.status_code == 200
        assert response.json['description'] == new_data['description']
