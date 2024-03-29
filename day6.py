class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.parent = next_node
        self.children = []

    def __repr__(self):
        return "Data: "+str(self.data)+", nbChild: "+str(len(self.children))

    def __str__(self):
        return "Data: "+str(self.data)+", nbChild: "+str(len(self.children))

    def get_next(self):
        return self.parent

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def search(self, data):
        found = False
        if self.data == data:
            return self
        else:
            current = None
            for child in self.children:
                current = child.search(data)
                if current is not None:
                    return current
          # possibly none
        return None

    def numberOfOrbit(self):
        count = -1
        current = self
        while current:
            count = count + 1
            current = current.get_next()
        return count


class LinkedTreeMultiHead(object):

    def __init__(self, heads=[]):
        self.heads = heads

    def search(self, data):
        for headNode in self.heads:
            node = headNode.search(data)
            if node is not None:
                return node
        return None

    def insert(self, newHeadNode):
        self.heads.append(newHeadNode)

    def remove(self, node):
        self.heads.remove(node)


def parse(lines):
    headNodes = LinkedTreeMultiHead()
    for line in lines:
        o1, o2 = line.split(')')
        nodeO1 = headNodes.search(o1)
        nodeO2 = headNodes.search(o2)
        if nodeO2 is None:
            nodeO2 = Node(o2)
        else:
            # remove node02 from headNodes.heads
            try:
                headNodes.remove(nodeO2)
            except:
                pass
        if nodeO1 is not None:
            nodeO1.add_child(nodeO2)
        else:
            nodeO1 = Node(o1)
            nodeO1.add_child(nodeO2)
            headNodes.insert(nodeO1)
    return headNodes


def countOrbit(children):
    result = 0
    for child in children:
        result = result + child.numberOfOrbit() + countOrbit(child.children)
    return result


def solve(linkedTreeMultiHead):
    result = 0
    for head in linkedTreeMultiHead.heads:
        result = result + countOrbit(head.children)
    return result


def findCommonAncestor(node1, node2):
    current = node1
    while current.search(node2.data) is None:
        current = current.get_next()
    return current


def solve_2(linkedTreeMultiHead, oFrom, oTo):
    result = 0
    nodeFrom = linkedTreeMultiHead.search(oFrom)
    nodeTo = linkedTreeMultiHead.search(oTo)
    commonAncestor = findCommonAncestor(nodeFrom, nodeTo)
    return nodeFrom.numberOfOrbit() + nodeTo.numberOfOrbit() - 2 * commonAncestor.numberOfOrbit()
