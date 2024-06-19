import argparse
import json
from style import Style, Icon
import builder
import iterator

class FJE:
    def __init__(self, args):
        with open(args.file, 'r') as f:
            self.data = json.load(f)
        
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.style = Style.subclasses[args.style.lower()]()
        self.style.icon = Icon(self.config[args.icon])
        self.root = None

    def load(self):
        director = builder.Director()

        def build(data, parent = None, last_flag = False):
            if isinstance(data, dict):
                for name, children in data.items():
                    director.builder = builder.CompositeBuilder()
                    component = director.build_composite(name, last_flag, parent)
                if isinstance(children, dict):
                    for index, (key, value) in enumerate(children.items()):
                        component.add(build({key: value}, component, index == len(children.items()) - 1))
                else:
                    component.add(build(children, component, True))
                return component
            else:
                director.builder = builder.LeafBuilder()
                return director.build_leaf(data, last_flag, parent)
        
        self.root = build({'root' : self.data}, last_flag=True)
        # print(self.root.elements_count())
        # iter = iterator.CompositeIterator(root)
        # for item in iter:
        #     print(item.name)
        # print(self.root.operation())

    def show(self):
        self.style.render(self.root)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='data.json', help='Path to JSON file')
    parser.add_argument('-s', '--style', type=str, default='tree', help='Style: tree or rectangle')
    parser.add_argument('-i', '--icon', type=str, default='icon1', help='Icon: icon1, icon2...')
    args = parser.parse_args()

    fje = FJE(args)
    fje.load()
    fje.show()

if __name__ == '__main__':
    main()