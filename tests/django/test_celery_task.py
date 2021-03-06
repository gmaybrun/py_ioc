from unittest.mock import patch

from touchstone import Container
from touchstone.django.celery_task import touchstone_task


class SampleOne:
    pass


class SampleTwo:
    pass


class TaskFoo:
    sample_one: SampleOne
    sample_two: SampleTwo


@patch("touchstone.django.properties.get_container")
@patch("touchstone.django.celery_task.get_container")
class TestTouchstoneTask:
    def test_touchstone_task(self, mock_container, mock_container_celery):
        container = Container()
        mock_container.return_value = container
        mock_container_celery.return_value = container
        task = touchstone_task(TaskFoo)
        assert type(task.sample_one) is SampleOne
        assert type(task.sample_two) is SampleTwo
