"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


from collections import Counter, deque

"""
Немного переработал решение, теперь данные хранятся не в ловре а в дереве реализованном на основе класса.
Можно было пойти еще дальше в сторону ООП но долго рабирался в алгоритме и не успел.
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def print_tree(self, dic, binary_code=''):
        if not isinstance(self.left_child[0], BinaryTree) and binary_code != '':
            print_binary_code = binary_code + '0'
            dic[self.left_child[0]] = print_binary_code
        else:
            left_binary_code = binary_code + '0'
            self.left_child[0].print_tree(dic, left_binary_code)
        if not isinstance(self.right_child[0], BinaryTree) and binary_code != '':
            print_binary_code = binary_code + '1'
            dic[self.right_child[0]] = print_binary_code
        else:
            right_binary_code = binary_code + '1'
            self.right_child[0].print_tree(dic, right_binary_code)


def haffman(string):
    word_dict = dict()
    count = Counter(string)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    while len(sorted_elements) > 1:
        a = sorted_elements.popleft()
        b = sorted_elements.popleft()
        weight = a[1] + b[1]
        new_tree = BinaryTree(weight)
        new_tree.left_child = a
        new_tree.right_child = b
        for i, _count in enumerate(sorted_elements):
            if weight > _count[1]:
                continue
            else:
                sorted_elements.insert(i, (new_tree, weight))
                break
        else:
            sorted_elements.append((new_tree, weight))
    sorted_elements[0][0].print_tree(word_dict)
    return word_dict


s = "beep boop beer!"
code_table = haffman(s)
for i in s:
    print(code_table[i], end=' ')
print(code_table)

"""
Проверка корректности заполнения дерева
print("Левая ветка")
print(sorted_elements[0][0].left_child)
print(sorted_elements[0][0].left_child[0].left_child)
print(sorted_elements[0][0].left_child[0].right_child)
print(sorted_elements[0][0].left_child[0].right_child[0].left_child)
print(sorted_elements[0][0].left_child[0].right_child[0].right_child)
print("Правая ветка")
print(sorted_elements[0][0].right_child)
print(sorted_elements[0][0].right_child[0].left_child)
print(sorted_elements[0][0].right_child[0].right_child)
print(sorted_elements[0][0].right_child[0].left_child[0].left_child)
print(sorted_elements[0][0].right_child[0].left_child[0].right_child)
print(sorted_elements[0][0].right_child[0].left_child[0].left_child[0].left_child)
print(sorted_elements[0][0].right_child[0].left_child[0].left_child[0].right_child)
"""


