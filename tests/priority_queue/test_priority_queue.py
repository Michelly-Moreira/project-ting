from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"quantidade_de_linhas": 9})
    priority_queue.enqueue({"quantidade_de_linhas": 4})
    priority_queue.enqueue({"quantidade_de_linhas": 2})
    priority_queue.enqueue({"quantidade_de_linhas": 5})
    priority_queue.enqueue({"quantidade_de_linhas": 7})
    priority_queue.enqueue({"quantidade_de_linhas": 11})
    priority_queue.enqueue({"quantidade_de_linhas": 3})

    assert len(priority_queue) == 7
    assert priority_queue.search(1) == {"quantidade_de_linhas": 6}

    assert len(priority_queue) == 6
    priority_queue.dequeue({"quantidade_de_linhas": 5})

    assert len(priority_queue) == 5
    priority_queue.dequeue({"quantidade_de_linhas": 7})
    with pytest.raises(Exception):
        priority_queue.search(7)
