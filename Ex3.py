import random
import timeit
import matplotlib.pyplot as plt


def generate_tasks(num_tasks=10000, push_prob=0.7):
    """
    Generate a list of tasks.
    Each task is either:
      ("push", value) with probability push_prob
      ("pop", None)   with probability 1 - push_prob
    """
    tasks = []

    for _ in range(num_tasks):
        if random.random() < push_prob:
            value = random.randint(1, 1000000)
            tasks.append(("push", value))
        else:
            tasks.append(("pop", None))

    return tasks


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if len(self._data) == 0:
            raise IndexError("peek from empty stack")
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


class LinkedStack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        x = self.head.data
        self.head = self.head.next
        self._size -= 1
        return x

    def peek(self):
        if self.head is None:
            raise IndexError("peek from empty stack")
        return self.head.data

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


def run_tasks(stack, tasks):
    """
    Execute all tasks on the given stack.
    If a pop is requested on an empty stack, skip it.
    """
    for op, value in tasks:
        if op == "push":
            stack.push(value)
        else:  # pop
            if not stack.is_empty():
                stack.pop()


def measure_time(stack_class, tasks, repeats=1):
    """
    Measure execution time for one task list.
    """
    timer = timeit.Timer(lambda: run_tasks(stack_class(), tasks))
    return timer.timeit(number=repeats)


def measure_performance(num_lists=100, num_tasks=10000):
    """
    Generate 100 task lists and measure both implementations.
    """
    array_times = []
    linked_times = []

    all_task_lists = [generate_tasks(num_tasks=num_tasks) for _ in range(num_lists)]

    for tasks in all_task_lists:
        array_time = measure_time(Stack, tasks)
        linked_time = measure_time(LinkedStack, tasks)

        array_times.append(array_time)
        linked_times.append(linked_time)

    return array_times, linked_times


def print_results(array_times, linked_times):
    print("Array-based stack times:")
    for i, t in enumerate(array_times, start=1):
        print(f"Run {i}: {t:.6f} seconds")

    print("\nLinked-list stack times:")
    for i, t in enumerate(linked_times, start=1):
        print(f"Run {i}: {t:.6f} seconds")

    print("\nSummary:")
    print(f"Array stack average time:  {sum(array_times) / len(array_times):.6f} seconds")
    print(f"Linked stack average time: {sum(linked_times) / len(linked_times):.6f} seconds")
    print(f"Array stack min time:      {min(array_times):.6f} seconds")
    print(f"Linked stack min time:     {min(linked_times):.6f} seconds")
    print(f"Array stack max time:      {max(array_times):.6f} seconds")
    print(f"Linked stack max time:     {max(linked_times):.6f} seconds")


def plot_results(array_times, linked_times):
    """
    Overlay both distributions on the same plot with consistent bins/range.
    """
    min_time = min(min(array_times), min(linked_times))
    max_time = max(max(array_times), max(linked_times))

    bins = 15

    plt.figure(figsize=(10, 6))
    plt.hist(array_times, bins=bins, range=(min_time, max_time), alpha=0.6, label="Array Stack")
    plt.hist(linked_times, bins=bins, range=(min_time, max_time), alpha=0.6, label="Linked Stack")

    plt.xlabel("Execution Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Performance Distribution of Stack Implementations")
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    array_times, linked_times = measure_performance(num_lists=100, num_tasks=10000)
    print_results(array_times, linked_times)
    plot_results(array_times, linked_times)


if __name__ == "__main__":
    main()