import numpy as np


def test_op_max(ugraph):
    with ugraph.begin_construction():
        tensor_x, = ugraph.add_op(
            'Constant',
            values=np.random.rand(3, 5, 9, 2).astype('float32'),
            name='x'
        )
        tensor_out1, = ugraph.add_op(
            'MaxOperator',
            tensor_x,
            name='max',
            axis=0,
            keepdims=True,
            is_output=True,
        )
        tensor_out2, = ugraph.add_op(
            'MaxOperator',
            tensor_x,
            name='max2',
            axis=1,
            keepdims=True,
            is_output=True,
        )
        tensor_out3, = ugraph.add_op(
            'MaxOperator',
            tensor_x,
            name='max3',
            axis=-1,
            keepdims=False,
            is_output=True,
        )
    assert tensor_out1.shape == [1, 5, 9, 2]
    assert tensor_out2.shape == [3, 1, 9, 2]
    assert tensor_out3.shape == [3, 5, 9]
