import loguru
from app.data.factories.todo_factory import TodoFactory, Todo


# GET /v1/todos test
def test_should_get_todo_successfully_when_client_hit_todo_detail_endpoint(client):
    # arrange
    todo = TodoFactory()

    # action
    response = client.get(f"/v1/todos/{todo.id}")

    # assert
    assert response.status_code == 200
    loguru.logger.info(f"response {response.json()}")
    assert response.json() == {"data": todo.to_dict()}
