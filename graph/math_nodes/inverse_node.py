from graph.utility_graph_node import UtilityGraphNode
from graph.exceptions import NodeConnectionError


class InverseNode(UtilityGraphNode):
    """Node representing an inverse operation"""
    def __init__(self):
        UtilityGraphNode.__init__(self)
        self.max_inputs = 1

    @UtilityGraphNode.output.getter
    def output(self):
        if not self.connected_inputs:
            raise NodeConnectionError("An inverse node \
            must have a connected input to produce an output")

        if self._output:
            return self._output

        self._output = 1.0 - max(1, self.connected_inputs[0].output)

        return self._output