# Funny JSON Explorer

## 运行

`python main.py -f <file> -s <style> -i <icon>`

`<file>` 为JSON文件的路径

`<style>` 可选`tree` 和 `rectangle`，默认为`tree`

`<icon>` 可选`icon1` ~ `icon4`，默认为`icon1`

在`config.json`中可以添加或修改图标组类型

## 结果示例

<img src="figs/rectangle+icon3.png"  width="400"> <img src="figs/rectangle+icon4.png"  width="400">

<img src="figs/tree+icon3.png"  width="400"> <img src="figs/tree+icon4.png"  width="400">

## 类图

<img src="figs/ClassDiagram.png"  width="800">

## 设计模式

#### 组合模式


Component是组件接口，Composite是中间节点，Leaf是叶节点。

可以将json数据对象组合成树状结构， 并且能像使用独立对象一样使用它们。

#### 抽象工厂模式

Style是抽象工厂，Tree与Rectangle是具体工厂，依据具体风格渲染组合树。

添加新风格时不用修改已有代码，只需在style.py中添加新的具体工厂，重写对应的渲染方法

#### 生成器模式

Builder接口声明生成Component组件的通用构造步骤。

Director定义调用构造步骤的顺序。

CompositeBuilder和LeafBuilder是具体生成器，分别负责构造中间结点和叶子结点。

#### 迭代器模式

CompositeIterator实现了深度优先遍历组合树的方法