import random
import timeit
import matplotlib.pyplot as plt


def generate_tasks(num_tasks=10000, enqueue_prob=0.7):
    """
    Generate a list of tasks.
    Each task is either:
      ("enqueue", value) with probability enqueue_prob
      ("dequeue", None)  with probability 1 - enqueue_prob
    """
    tasks = []

    for _ in range(num_tasks):
        if random.random() < enqueue_prob:
            value = random.randint(1, 1000000)
            tasks.append(("enqueue", value))
        else:
            tasks.append(("dequeue", None))

    return tasks


class ArrayQueue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        # insert at head
        self._data.insert(0, item)

    def dequeue(self):
        # remove from tail
        if len(self._data) == 0:
            raise IndexError("dequeue from empty queue")
        return self._data.pop()

    def peek(self):
        if len(self._data) == 0:
            raise IndexError("peek from empty queue")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):
        # add at head
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1

    def dequeue(self):
        # remove tail element
        if self.head is None:
            raise IndexError("dequeue from empty queue")

        # only one node
        if self.head == self.tail:
            value = self.tail.data
            self.head = None
            self.tail = None
            self._size -= 1
            return value

        # find node right before tail
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        value = self.tail.data
        curr.next = None
        self.tail = curr
        self._size -= 1
        return value

    def peek(self):
        if self.tail is None:
            raise IndexError("peek from empty queue")
        return self.tail.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def __str__(self):
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.data)
            curr = curr.next
        return str(values)


def run_tasks(queue, tasks):
    """
    Execute all tasks on the given queue.
    If a dequeue is requested on an empty queue, skip it.
    """
    for op, value in tasks:
        if op == "enqueue":
            queue.enqueue(value)
        else:
            if not queue.is_empty():
                queue.dequeue()


def measure_time(queue_class, tasks, repeats=1):
    """
    Measure execution time for one task list.
    """
    timer = timeit.Timer(lambda: run_tasks(queue_class(), tasks))
    return timer.timeit(number=repeats)


def measure_performance(num_lists=100, num_tasks=10000):
    """
    Generate 100 task lists and measure both queue implementations.
    """
    array_times = []
    linked_times = []

    all_task_lists = [generate_tasks(num_tasks=num_tasks) for _ in range(num_lists)]

    for tasks in all_task_lists:
        array_time = measure_time(ArrayQueue, tasks)
        linked_time = measure_time(LinkedQueue, tasks)

        array_times.append(array_time)
        linked_times.append(linked_time)

    return array_times, linked_times


def print_results(array_times, linked_times):
    print("Array-based queue times:")
    for i, t in enumerate(array_times, start=1):
        print(f"Run {i}: {t:.6f} seconds")

    print("\nLinked-list queue times:")
    for i, t in enumerate(linked_times, start=1):
        print(f"Run {i}: {t:.6f} seconds")

    print("\nSummary:")
    print(f"Array queue average time:  {sum(array_times) / len(array_times):.6f} seconds")
    print(f"Linked queue average time: {sum(linked_times) / len(linked_times):.6f} seconds")
    print(f"Array queue min time:      {min(array_times):.6f} seconds")
    print(f"Linked queue min time:     {min(linked_times):.6f} seconds")
    print(f"Array queue max time:      {max(array_times):.6f} seconds")
    print(f"Linked queue max time:     {max(linked_times):.6f} seconds")


def plot_results(array_times, linked_times):
    """
    Overlay both distributions on the same plot with consistent bins/range.
    """
    min_time = min(min(array_times), min(linked_times))
    max_time = max(max(array_times), max(linked_times))
    bins = 15

    plt.figure(figsize=(10, 6))
    plt.hist(array_times, bins=bins, range=(min_time, max_time), alpha=0.6, label="Array Queue")
    plt.hist(linked_times, bins=bins, range=(min_time, max_time), alpha=0.6, label="Linked Queue")

    plt.xlabel("Execution Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Performance Distribution of Queue Implementations")
    plt.legend()
    plt.grid(True)
    plt.show()





def main():
    array_times, linked_times = measure_performance(num_lists=100, num_tasks=10000)
    print_results(array_times, linked_times)
    plot_results(array_times, linked_times)


if __name__ == "__main__":
    main()