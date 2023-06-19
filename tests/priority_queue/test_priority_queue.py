from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    with pytest.raises(TypeError):
        PriorityQueue()
