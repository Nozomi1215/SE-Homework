from abc import ABC, abstractmethod
from node import Component

class Icon:
    def __init__(self, map):
        self.composite = map['composite']
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

    def __init__(self):
        super().__init__()
        print("Tree style created")

    def render_leaf(self, component: Component) -> None:
        if component.name:
            print(': ' + component.name)
        else:
            print('')

    def render_composite(self, component: Component) -> None:
        if component.parent is not None:
            self.render_composite(component.parent)
            print('   ' if component.last_flag else '│  ', end='')

    def render(self, component: Component) -> None:
        if component.parent is not None:
            self.render_composite(component.parent)
            icon = self.icon.composite if component._children and component._children[0].is_composite() else self.icon.leaf
            print(f'{"└─" if component.last_flag else "├─"}{icon}{component.name}', end='')
            if icon == self.icon.composite:
                print('')
        for child in component._children:
            if child.is_composite():
                self.render(child)
            else:
                self.render_leaf(child)

    
class Rectangle(Style):

    def __init__(self):
        super().__init__()
        print("Rectangle style created")
        self.max_length = 50
        self.current_length = 0
        self.begin_mark = '┌' 
        self.end_mark = '┐'
        self.last_line = False

    def is_last_line(self, component: Component) -> bool:
        while component:
            if not component.last_flag:
                return False
            component = component.parent
        self.last_line = True
        return True
    
    def render_leaf(self, component : Component) -> None:
        content = ': ' + component.name if component.name else ''
        line_fill = '─' * (self.max_length - self.current_length - len(content) - 1)
        print(content + line_fill + self.end_mark)
    
    def render_composite(self, component: Component) -> None:
        if component.parent is not None:
            self.render_composite(component.parent)
            self.current_length += 3
            print('└──' if self.last_line else '│  ', end='')

    def render(self, component: Component) -> None:
        if component.parent is not None:
            self.current_length = 0
            self.render_composite(component.parent)
            icon = self.icon.composite if component._children and component._children[0].is_composite() else self.icon.leaf
            print(self.begin_mark + '─' + icon + component.name, end='')
            self.current_length += 3 + len(component.name)
            self.begin_mark = '├'
            if icon == self.icon.composite:
                print('─' * (self.max_length - self.current_length - 1) + self.end_mark)
                self.end_mark = '┤'
        for child in component._children:
            if child.is_composite():
                if not child._children[0].is_composite() and self.is_last_line(child):
                    self.begin_mark = '┴'
                    self.end_mark = '┘'
                self.render(child)
            else:
                self.render_leaf(child)
