import random
import timeit


class PriorityQueueSort:

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self.data = sorted(self.data)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)


class PriorityQueueInsert:

    def __init__(self):
        self.data = []

    def enqueue(self, value):

        if len(self.data) == 0:
            self.data.append(value)
            return

        for i in range(len(self.data)):
            if value < self.data[i]:
                self.data.insert(i, value)
                return

        self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)


def generate_tasks(n=1000):

    tasks = []

    for _ in range(n):

        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1,1000)))
        else:
            tasks.append(("dequeue", None))

    return tasks


def run_experiment(queue_class):

    tasks = generate_tasks()

    q = queue_class()

    for task in tasks:

        if task[0] == "enqueue":
            q.enqueue(task[1])
        else:
            q.dequeue()


def measure():

    t1 = timeit.timeit(lambda: run_experiment(PriorityQueueSort), number=100)

    t2 = timeit.timeit(lambda: run_experiment(PriorityQueueInsert), number=100)

    print("PriorityQueueSort time:", t1)
    print("PriorityQueueInsert time:", t2)


if __name__ == "__main__":
    measure()


"""
Discussion (Question 5):

PriorityQueueInsert is usually faster.

Reason:
PriorityQueueSort sorts the entire list after every enqueue operation,
which is expensive (O(n log n)).

PriorityQueueInsert inserts the element directly in the correct position,
which only requires shifting elements (O(n)).

Therefore the second implementation generally performs better.
"""
