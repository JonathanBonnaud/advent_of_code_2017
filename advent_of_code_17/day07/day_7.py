"""
Day 7: Recursive Circus
"""
import abstract_day


class Node:
    def __init__(self, input_line):
        components = input_line.split('->')
        node_part = components[0].split()
        self.label = node_part[0]
        self.weight = int(node_part[1].strip('()'))
        self.children = components[1].strip().split(', ') if len(components) > 1 else None

    def __repr__(self):
        if self.children:
            return '{} ({}) -> {}'.format(self.label,
                                          self.weight,
                                          self.children)
        else:
            return '{} ({})'.format(self.label, self.weight)


class ComplexNode:
    def __init__(self, label, weight, *, parent=None, children=None):
        self.label = label
        self.weight = weight
        self.parent = parent
        self.children = [] if children is None else children

        # Properly link parent and children
        """"
        if parent:
            parent.children.append(self)
        for child in self.children:
            child.unset_parent()
            child.parent = self
        """

    def __repr__(self):
        if self.children:
            return '{} ({}) -> {}'.format(self.label,
                                          self.weight,
                                          self.children)
        else:
            return '{} ({})'.format(self.label, self.weight)

    def __str__(self, indentation=''):
        """
        :param indentation: Indentation put in front of the node's label.
        :type indentation: strings
        :return: A string representing the node.
        :rtype: string
        """
        r = '%s%s (%s + %s = %s)' % (indentation, self.label, self.weight,
                                     self.get_full_weight()-self.weight,
                                     self.get_full_weight())
        if self.children:
            r += '\n'
            indentation += '\t'
            for child in self.children:
                r = r + child.__str__(indentation)
                if child != self.children[-1]:
                    r += '\n'
        return r

    def remove_children(self):
        self.children = list()

    def set_parent(self, parent_node):
        """
        Set the parent node of the current node. Updated nodes: the current node and its former parent.
        :param parent_node: The node to be removed.
        :type parent_node:
        """
        if parent_node:
            if self.parent:
                self.parent.children.remove()
            self.parent = parent_node
            parent_node.children.append(self)

    def get_full_weight(self):
        children_weights = 0
        if self.children:
            for child in self.children:
                children_weights += child.get_full_weight()
        return self.weight + children_weights

    @staticmethod
    def all_same(weights):
        return all(x == weights[0] for x in weights)

    def balance_weights(self, rebalanced_weights):
        if self.children:
            if not self.all_same([child.get_full_weight() for child in self.children]):
                for child in self.children:
                    child.balance_weights(rebalanced_weights)

                # Process the weights
                list_weights = [child.get_full_weight() for child in self.children]
                m = max(list_weights)
                n = min(list_weights)
                pos_max = [i for i, j in enumerate(list_weights) if j == m]
                if len(pos_max) < len(list_weights):
                    if len(pos_max) > 1:
                        TAG = 'MIN'
                        unbalanced = [self.children[pos] for pos in [i for i in range(len(self.children))] if pos not in pos_max]
                    else:
                        TAG = 'MAX'
                        unbalanced = [self.children[pos] for pos in pos_max]
                    for child in self.children:
                        if child.label == unbalanced[0].label:
                            unbalanced_weight = child.weight
                            child.weight = unbalanced_weight - (m - n) if TAG == 'MAX' \
                                else unbalanced_weight + (m - n)
                            rebalanced_weights.append(child.weight)
        return rebalanced_weights


class Day71(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The name of the bottom program (root of the tree).
        :rtype Node
        """
        nodes = [node for node in
                 [Node(line) for line in self.input_content.split('\n')] if node.children]
        curr_node = nodes[0]
        lock = 1
        while lock == 1:
            lock = 0
            for n in nodes[1:]:
                if curr_node.label in n.children:
                    lock = 1
                    curr_node = n
        return curr_node


class Day72(abstract_day.AbstractDay):

    def get_result(self):
        """
        :return: The weight of the exact one program (that weight was wrong)
          in order for the tower to be balanced.
        """
        all_nodes = [
            ComplexNode(
                line.split('->')[0].split()[0],
                int(line.split('->')[0].split()[1].strip('()')),
                children=line.split('->')[1].strip().split(', ') if len(line.split('->')) > 1 else None
            ) for line in self.input_content.split('\n')
        ]
        leaves = [node for node in all_nodes if not node.children]
        parents = [node for node in all_nodes if node.children]

        # Build the tree
        nodes = dict()
        nodes_parent = dict()
        for leaf in leaves:
            nodes[leaf.label] = leaf
        for parent in parents:
            nodes[parent.label] = parent
            for child in parent.children:
                nodes_parent[child] = parent.label
            parent.remove_children()
        root_node = None
        for node_label in nodes.keys():
            node = nodes[node_label]
            if node_label in nodes_parent.keys():
                parent_node = nodes[nodes_parent[node_label]]
                node.set_parent(parent_node)
            else:
                root_node = node

        rebalanced_weight = root_node.balance_weights([])
        return rebalanced_weight[0]
