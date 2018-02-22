"""
Day 12: Digital Plumber
"""
import abstract_day
import re
import networkx
from networkx.algorithms.components.connected import connected_components


class Day121(abstract_day.AbstractDay):

    def __init__(self, input_content, *, get_groups=None):
        super().__init__(input_content)
        self.get_groups = False if get_groups is None else get_groups

    @staticmethod
    def to_edges(l):
        """
            treat `l` as a Graph and returns it's edges
            to_edges(['a','b','c','d']) -> [(a,b), (b,c),(c,d)]
        """
        it = iter(l)
        last = next(it)

        for current in it:
            yield last, current
            last = current

    def to_graph(self, l):
        graph = networkx.Graph()
        for part in l:
            # each sublist is a bunch of nodes
            graph.add_nodes_from(part)
            # it also implies a number of edges:
            graph.add_edges_from(self.to_edges(part))
        return graph

    def get_result(self):
        list_connections = [set(re.findall(r"[\w']+", line.strip())) for line in self.input_content.split('\n')]
        graph = self.to_graph(list_connections)

        list_groups = list(connected_components(graph))
        if not self.get_groups:
            list_groups = list(subset for subset in list_groups if '0' in subset)[0]
        return list_groups


class Day121bis(abstract_day.AbstractDay):
    """
    First easy solution implemented.
    (Works for problem 1)
    """
    def __init__(self, input_content, *, get_groups=None):
        super().__init__(input_content)
        self.get_groups = False if get_groups is None else get_groups

    def get_result(self):
        list_connections = [set(re.findall(r"[\w']+", line.strip())) for line in self.input_content.split('\n')]
        # print(list_connections)

        final = list_connections[0].copy()
        prev = set()
        while prev != final:  # should be a better way to do that (merge all sets with common elements)
            prev = final
            for sub_group in list_connections[1:]:
                if bool(final & sub_group):
                    final = final.union(sub_group)
        return len(final)
