from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 9})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 5})
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 11})
    priority_queue.enqueue({"qtd_linhas": 3})

    assert len(priority_queue) == 7
    assert priority_queue.search(1) == {"qtd_linhas": 2}

    delete = priority_queue.high_priority.dequeue()
    assert len(priority_queue) == 6
    assert delete == {"qtd_linhas": 4}

    delete = priority_queue.dequeue()
    assert len(priority_queue) == 5
    assert delete == {"qtd_linhas": 2}

    with pytest.raises(Exception):
        priority_queue.search(8)
