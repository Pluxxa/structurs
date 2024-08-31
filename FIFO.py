class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.queue.append(item)

    def dequeue(self):
        """Удаляет элемент из начала очереди и возвращает его."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None  # Или можно выбросить исключение

    def peek(self):
        """Возвращает первый элемент очереди без его удаления."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.queue)

# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.peek())  # 2
print(queue.size())  # 2
