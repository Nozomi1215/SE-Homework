from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import node
from style import Icon


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_name(self) -> None:
        pass

    @abstractmethod
    def set_flag(self) -> None:
        pass

    @abstractmethod
    def set_parent(self) -> None:
        pass

class CompositeBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = node.Composite()

    @property
    def product(self) -> node.Composite:
        product = self._product
        self.reset()
        return product

    def set_name(self, name) -> None:
        self._product.name = name

    def set_flag(self, flag) -> None:
        self._product.last_flag = flag

    def set_parent(self, parent) -> None:
        self._product.parent = parent

class LeafBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = node.Leaf()

    @property
    def product(self) -> node.Leaf:
        product = self._product
        self.reset()
        return product

    def set_name(self, name) -> None:
        self._product.name = name

    def set_flag(self, flag) -> None:
        self._product.last_flag = flag

    def set_parent(self, parent) -> None:
        self._product.parent = parent

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


    def build_composite(self, name, flag, parent) -> node.Composite:
        self.builder.set_name(name)
        self.builder.set_flag(flag)
        self.builder.set_parent(parent)
        return self.builder.product

    def build_leaf(self, name, flag, parent) -> node.Leaf:
        self.builder.set_name(name)
        self.builder.set_flag(flag)
        self.builder.set_parent(parent)
        return self.builder.product