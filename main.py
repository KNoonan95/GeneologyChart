from pyvis.network import Network

net = Network()

net.add_nodes(
    [1, 2, 3, 4, 5],
    profile=['Father', 'Mother', 'Uncle', 'Son', 'Daughter'], 
    title=['Father', 'Mother', 'Uncle', 'Son', 'Daughter'],
    color=['#d47410', '#22b492', '#42adbh5', '#4a21b1', '#e627a1']  
)

net.add_edges([(1, 2), (1, 3), (1,4) , (1,5) , (2, 3), (2, 4)])

net.show('family_graph.html') 


def dummy_test();
    pass
