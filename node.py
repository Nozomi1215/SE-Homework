from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):

    def __init__(self):
        self.name = None
        self.last_flag = False

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def elements_count(self) -> int:
        pass

    def create_iterator(self):
        raise NotImplementedError("This method should be overridden.")

class Leaf(Component):
    def operation(self) -> str:
        return f"Leaf: {self.name}"

    def elements_count(self) -> int:
        return 1
    
    def create_iterator(self):
        return iter([])

class Composite(Component):
    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch: {self.name}({'+'.join(results)})"

    def elements_count(self) -> int:
        results = 0
        for child in self._children:
            results += child.elements_count()
        return results
    
    def create_iterator(self):
        return iter(self._children)