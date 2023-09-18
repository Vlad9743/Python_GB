# Доработать бинарное дерево с семинара, добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.

class Node:

    """ 
    Класс узла дерева
    Attributes:
    value - значенеи узла
    left, right - ссылки на левое и правое поддеревья

    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    """ 
    Класс бинарного дерева

    """

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """
        Метод добавленея нового узла
        Если элемент с таким значением уже присутствует в дереве, выдат предупреждение
        Attributes
        value - значение добавляемого узла
        """    
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        """
        Метод поиска заданного значения в поддереве.
        Возвращает ссылки на искомый и родительский узлы
        Attributes
        node - корень поддерева, в котором идет поиск
        value - искомое значение
        parent - ссылка на родительский элемент искомого узла
        """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
        
    def countTreesSize(self, node):
        """
        Метод досчет количества узлов текущего дерева
        Attributes
        node - корень поддерева, для которого идет подсчет
        """
        if node is None:
            return 0
        return 1 + self.countTreesSize(node.right) + self.countTreesSize(node.left)
          
    def printTree(self, node):
        """
        Метод вывода на экран текущего дерева по уровням
        Attributes
        node - корень поддерева, для производится вывод
        """
        if node is None:
            return 0
 
        currentNode = [node]
        while currentNode:
            currentLevel = []
            for element in currentNode:
                print(element.value, end = " ")
                if element.left:
                    currentLevel += [element.left]
                if element.right:
                    currentLevel += [element.right]
            print()
            currentNode = currentLevel

    def remove(self, node, value):
        """
        Метод удаления узла
        
        Attributes
        node - корень поддерева, в котором идет поиск
        value - значение добавляемого узла
        """   
        if node is None: return None
        if value < node.value:
            node.left = self.remove(node.left, value)
        elif value > node.value:
            node.right = self.remove(node.right, value)
        else:
            if node.left is None: return node.right
            if node.right is None: return node.left
            original, node = node,
            node.right
            while node.left:
                node = node.left

            node.right = self.remove_min(original.right)
            node. left = original. left
        return node


bt = BinaryTree(5)
bt.add(10)
bt.add(15)

print("Оригинальное дерево")
bt.printTree(bt.root)
print('-----------------------')
print("Текущее количество элементов:", bt.countTreesSize(bt.root))
print('-----------------------')

bt.add(3)
bt.add(4)
bt.add(2)
bt.add(2)
bt.add(12)
bt.add(7)
bt.add(8)
bt.add(16)

print("Расширенное дерево")
bt.printTree(bt.root)
print('-----------------------')
print("Текущее количество элементов:", bt.countTreesSize(bt.root))
print('-----------------------')

bt.remove(bt.root, 12)
bt.remove(bt.root, 78)
print("Измененное дерево")
bt.printTree(bt.root)
print('-----------------------')
print("Текущее количество элементов:", bt.countTreesSize(bt.root))
print('-----------------------')