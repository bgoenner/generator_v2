

def test_paser_nets():

    import os

    from generator_v2 import get_nets

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    nets = get_nets(i_file)

    print([x.print_net() for x in nets])