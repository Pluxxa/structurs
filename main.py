class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Добавляет элемент в вершину стека."""
        self.stack.append(item)

    def pop(self):
        """Удаляет элемент с вершины стека и возвращает его."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # Или можно выбросить исключение

    def peek(self):
        """Возвращает верхний элемент стека без его удаления."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.stack) == 0

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.stack)

# Пример использования:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2
