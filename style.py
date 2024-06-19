from abc import ABC, abstractmethod
from node import Component

class Icon:
    def __init__(self, map):
        self.node = map['node']
        self.leaf = map['leaf']

class Style(ABC):
    subclasses = {}

    def __init__(self, icon: Icon):
        self.icon = icon

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls.__name__.lower()] = cls

    def __init__(self):
        print(f"{self.__class__.__name__} style initialized")

    @abstractmethod
    def render_leaf(self, component):
        pass

    @abstractmethod
    def render_composite(self, component):
        pass

    @abstractmethod
    def render(self, component):
        pass

class Tree(Style):

    def __init__(self, icon: Icon):
        super().__init__(icon)
        print("Tree style created, ")

    def render_leaf(self, component : Component):
        if component.name is None:
            print('')
        else:
            print(': '  + component.name)

    def render_composite(self, component : Component):
        if component.parent is not None:
            self.render_composite(component.parent)
            if component.last_flag:
                print('   ', end='')
            else:
                print('|  ', end='')

    def render(self, component : Component):
        if component.parent is not None:
            self.render_composite(component.parent)
            
    
class Rectangle(Style):

    def __init__(self, icon: Icon):
        super().__init__(icon)
        print("Rectangle style created")

