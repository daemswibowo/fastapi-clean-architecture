import factory
from app.data.factories.base_factory import BaseFactory
from app.data.models.todo_model import Todo


class TodoFactory(BaseFactory):
    class Meta:
        model = Todo

    # define the data
    title = factory.Faker('sentence')
    is_done = factory.Faker('random_element', elements=[True, False])
