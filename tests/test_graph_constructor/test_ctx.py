import numpy as np


def test_ugraph_build_ctx():
    from utensor_cgen.ir import uTensorGraph
    from utensor_cgen.ir.graph_builder import GraphFinalizedError

    ugraph = uTensorGraph()

    with ugraph.begin_construction():
        ugraph.add_op(
            'Constant',
            name='x',
            values=np.array([1]),
            is_output=True
        )

    assert ugraph.is_finalized
    assert ugraph.output_nodes == ['x']
    try:
        ugraph.add_op('Constant', name='y', values=np.array([2]))
    except GraphFinalizedError:
        pass
