import argparse
import json
from style import Style, Icon
import builder
import iterator
import node

class FJE:
    def __init__(self, args):
        with open(args.file, 'r') as f:
            self.data = json.load(f)
        
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.icon = Icon(self.config[args.icon])
        self.style = Style.subclasses[args.style.lower()]()

    def load(self):
        director = builder.Director()

        def build_component(data, parent = None, last_flag = False):
            if isinstance(data, dict):
                for name, children in data.items():
                    director.builder = builder.CompositeBuilder()
                    component = director.build_composite(name, last_flag, self.icon, parent)
                
                if isinstance(children, dict):
                    for index, (key, value) in enumerate(children.items()):
                        component.add(build_component({key: value}, component, index == len(children.items()) - 1))
                else:
                    component.add(build_component(children, component, True))
                return component
            else:
                director.builder = builder.LeafBuilder()
                Leaf = director.build_leaf(data, last_flag, self.icon, parent)
                return Leaf
        
        root = build_component({'root' : self.data}, last_flag=True)
        iter = iterator.CompositeIterator(root)
        for item in iter:
            print(item.name, item.icon)
        print(root.operation())

    


def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, default='data.json', help='Path to JSON file')
    parser.add_argument('-s', '--style', type=str, default='tree', help='Style: tree or rectangle')
    parser.add_argument('-i', '--icon', type=str, default='icon1', help='Icon: icon1, icon2...')
    args = parser.parse_args()

    fje = FJE(args)
    fje.load()

if __name__ == '__main__':
    main()