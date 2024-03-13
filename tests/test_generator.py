

def test_paser_nets():

    import os

    from generator_v2 import get_nets

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    nets = get_nets(i_file)

    print(nets)
    print([x.print_net() for x in nets])

def test_write_nets():

    import os

    from generator_v2 import write_nets, get_nets

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    o_file = os.getcwd()+'/test_output/test_1_2in_routes.scad'

    nets = get_nets(i_file)

    #write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1])
    write_nets(o_file, nets)

def test_write_nets():

    import os

    from generator_v2 import write_components, get_components

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    o_file = os.getcwd()+'/test_output/test_1_2in_comp.scad'

    comps = get_components(i_file)

    #write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1])
    write_components(o_file, comps, 30, 10)