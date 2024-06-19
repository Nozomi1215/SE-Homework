from node import Component
from typing import Iterator

class CompositeIterator(Iterator):
    def __init__(self, root: Component):
        self.stack = []
        self.stack.append((root.create_iterator(), root))

    def __iter__(self):
        return self

    def __next__(self) -> Component:
        while self.stack:
            iterator, current_component = self.stack[-1]
            try:
                next_component = next(iterator)
                if next_component.is_composite():
                    self.stack.append((next_component.create_iterator(), next_component))
                return next_component
            except StopIteration:
                self.stack.pop()
        raise StopIteration