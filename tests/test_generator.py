
## global definitions

bulk = {
    'x':2550,
    'y':1590,
    'z':280
}

net_property = {
    'px':0.0076,
    'layer':0.010,
    'lpv':20,
    'def_scale':1000,
    'bot_layers':20
}

mets = {
    'met1':0,
    'met2':1,
    'met3':2,
    'met4':3,
    'met5':4,
    'met6':5,
    'met7':6,
    'met8':7,
    'met9':8,
}


def test_paser_nets():

    import os

    from generator_v2 import get_nets

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    net_property = {
    'px':1,
    'layer':1,
    'lpv':1,
    'def_scale':1,
    'bot_layers':0
    }

    db = {
    'compress_routes' : False,
    }

    nets = get_nets(i_file, tlef_property=net_property, debug=db, testing=True, testing=True)

    print(nets)
    print([x.print_net() for x in nets])


def test_write_nets():

    import os

    from generator_v2 import write_nets, get_nets

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    o_file = os.getcwd()+'/test_output/test_1_2in_routes.scad'

    nets = get_nets(i_file, testing=True)

    #write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1])
    write_nets(o_file, nets)

def test_write_nets_2():

    import os

    from generator_v2 import write_nets, get_nets

    i_file = os.getcwd()+'/def_test/test_2_3in.def'

    o_file = os.getcwd()+'/test_output/test_2_3in_routes.scad'

    nets = get_nets(i_file, testing=True)

    #write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1])
    write_nets(o_file, nets)

def test_write_comps():

    import os

    from generator_v2 import write_components, get_components

    i_file = os.getcwd()+'/def_test/test_1_2in.def'

    o_file = os.getcwd()+'/test_output/test_1_2in_comp.scad'

    comps = get_components(i_file)

    #write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1])
    write_components(o_file, comps, 0.030, 0.010)


def test_parser_pins():
    import os
    from generator_v2 import get_pins

    i_file = os.getcwd()+'/def_test/test_1_2in.def'
    pin_f  = os.getcwd()+'/support_libs/pins.csv'

    pins = get_pins(i_file, pin_f)
    print(pins)

def test_write_pins():

    import os
    from generator_v2 import get_pins, write_pins

    i_file = os.getcwd()+'/def_test/test_1_2in.def'
    pin_f  = os.getcwd()+'/support_libs/pins.csv'

    o_file = os.getcwd()+'/test_output/test_1_2in_pin.scad'

    pins = get_pins(i_file, pin_f)

    write_pins(o_file, pins, bulk, net_property, mets, debug=True)

def test_combine_nets_comps_pins():

    use_statement = """use <./../support_libs/polychannel_v2.scad>
use <./../support_libs/routing.scad>
use <./../support_libs/h.r.3.3_pdk_merged.scad>

px    = 7.6e-3;
layer = 10e-3;
"""

    fb = '{'
    bb = '}'

    bulk_statement = f"""
difference(){fb}
    %cube([{bulk['x']}*px, {bulk['y']}*px, {bulk['z']}*layer]);
union(){fb}
"""

    import os
    from generator_v2 import write_components, get_components, write_nets, get_nets, write_pins, get_pins 



    i_file = os.getcwd()+'/def_test/test_1_2in.def'
    pin_f  = os.getcwd()+'/support_libs/pins.csv'

    o_file = os.getcwd()+'/test_output/test_1_2in_comb.scad'

    of = open(o_file, 'w+')
    of.write(use_statement)
    of.write(bulk_statement)
    of.close()

    nets = get_nets(i_file, testing=True)
    write_nets(o_file, nets, mode='a')

    comps = get_components(i_file)
    write_components(o_file, comps, 0.030, 0.010, mode='a')

    pins = get_pins(i_file, pin_f)
    write_pins(o_file, pins, bulk, net_property, mets, mode='a')

    interconnect_statement = f"""
{bb}
{bb}
%interconnect_32channel(2550/2, 1590/2, 280);;
"""

    of = open(o_file, 'a')
    of.write(interconnect_statement)
    of.close()

def test_main():

    import os
    from generator_v2 import main

    main(
    platform='h.r.3.3_pdk', 
    design='test_1_2in', 
    def_file='def_test/test_1_2in.def', 
    results_dir='test_output/main_test', 
    px=0.0076, 
    layer=0.01, 
    bttm_layer=20, 
    lpv=20, 
    xbulk=2550, 
    ybulk=1590, 
    zbulk=280, 
    xchip=[0, 2550], 
    ychip=[0, 1590], 
    def_scale=1000, 
    pitch=30, 
    res=120, 
    dimm_file=None, 
    comp_file="support_libs/h.r.3.3_pdk_merged.scad",
    tlef="def_test/test_1.tlef",
    pin_con_dir_f='support_libs/pins.csv')
    
def test_2_main():

    import os
    from generator_v2 import main

    main(
    platform='h.r.3.3_pdk', 
    design='test_2_3in', 
    def_file='def_test/test_2_3in.def', 
    results_dir='test_output/main_test', 
    px=0.0076, 
    layer=0.01, 
    bttm_layer=20, 
    lpv=20, 
    xbulk=2550, 
    ybulk=1590, 
    zbulk=280, 
    xchip=[0, 2550], 
    ychip=[0, 1590], 
    def_scale=1000, 
    pitch=30, 
    res=120, 
    dimm_file=None,
    tlef="def_test/test_1.tlef",
    comp_file="support_libs/h.r.3.3_pdk_merged.scad", 
    pin_con_dir_f='support_libs/pins_2.csv')

def test_3_main():

    import os
    from generator_v2 import main

    main(
    platform='h.r.3.3_pdk', 
    design='test_3', 
    def_file='def_test/test_3.def', 
    results_dir='test_output/main_test', 
    px=0.0076, 
    layer=0.01, 
    bttm_layer=20, 
    lpv=20, 
    xbulk=2550, 
    ybulk=1590, 
    zbulk=280, 
    xchip=[0, 2550], 
    ychip=[0, 1590], 
    def_scale=1000, 
    pitch=30, 
    res=120, 
    dimm_file=None,
    tlef="def_test/test_1.tlef",
    comp_file="support_libs/h.r.3.3_pdk_merged.scad", 
    pin_con_dir_f='support_libs/pins_2.csv')
    
