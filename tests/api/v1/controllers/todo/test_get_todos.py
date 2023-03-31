import loguru
from app.data.factories.todo_factory import TodoFactory, Todo


def transform_todo_to_dict(todo: Todo):
    return todo.to_dict()


# GET /v1/todos test
def test_should_get_todos_successfully_when_client_hit_todos_endpoint(client):
    # arrange
    todos = TodoFactory.create_batch(5)

    # action
    response = client.get("/v1/todos")

    # assert
    assert response.status_code == 200
    loguru.logger.info(f"response {response.json()}")
    assert response.json() == {"data": list(map(transform_todo_to_dict, todos))}
