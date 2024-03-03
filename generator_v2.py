
import os, sys

import re
import mmap
import argparse

from generator_class import * 

import solid
import regex

## Regex parsing
pin_block_reg = r'^PINS\s*\d*\s*;\w*\n(?|.*\n)*END\s*PINS$'
pin_line_reg  = r'^\s*-\s*(?P<pin>\w*)\s*\+\s*NET\s*(?P<net>\w*)\s*\+\s*DIRECTION\s*(?P<direction>\w*)\s*\+\sUSE\s*SIGNAL\s*\+\s*PORT\s*\+\s*LAYER\s*(?P<layer>\w*)\s*(\(\s*(?P<lx1>[-\d]*)\s*(?P<ly1>[-\d]*)\s*\))\s*(\(\s*(?P<lx2>[-\d]*)\s*(?P<ly2>[-\d]*)\s*\))\s*\+\s*FIXED\s*(\(\s*(?P<fx1>\d*)\s*(?P<fy1>\d*)\s*\)\s*(?P<fdir>\w))\s*;'

comp_block_reg = r'^COMPONENTS\s*\d*\s*;\w*\n(?|.*\n)*END\s*COMPONENTS$'
comp_line_reg = r'^\s*-\s*(?P<name>\w*)\s*(?P<comp>\w*)\s*\+\s*PLACED\s*(\(\s*(?P<x1>\d*)\s*(?P<y1>\d*)\s*\) (\w*))\s*;'

nets_block_reg = r'^NETS\s*\d*\s*;\w*\n(?|.*\n)*END\s*NETS$'
nets_line_reg = r'-\s*(?P<net>\w*)\s*(\(\s*(?P<dev1>\w*)\s*(?P<p1>\w*)\s*\))\s*(\(\s*(?P<dev2>\w*)\s*(?P<p2>\w*)\s*\))\s*\+\s*USE SIGNAL.*\s*\+\s*ROUTED.*\n(?|\s*NEW.*)*;$'
nets_route_reg= r'(?:ROUTED|NEW)\s*(?P<layer>\w*)\s*((?:\(\s*(?P<x1>[\d\*]*)\s*(?P<y1>[\d\*]*)\s*(?P<z1>[\d\*]*)\s*\)))\s((?:\(\s*(?P<x2>[\d\*]*)\s*(?P<y2>[\d\*]*)\s*(?P<z2>[\d\*]*)\s*\)|(?P<via>\w*)))'

# solid imports

pdk = solid.import_scad(os.getcwd()+'/support_libs/h.r.3.3_pdk_merged.scad')
pc = solid.import_scad(os.getcwd()+'/support_libs/polychannel_v2.scad')
routing = solid.import_scad(os.getcwd()+'/support_libs/routing.scad')

mfda_scad = None

def get_pins(in_def):
    
    mod_re = bytes(pin_block_reg, 'utf-8')

    # parse template
    with open(in_def, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        mo = regex.findall(mod_re, data, re.MULTILINE)

    for m in mo:

        obj = get_pin_line(m)

        # iterate through pin objects
        for o in obj:
            print(o.group('pin'))
            print(o.group('net'))
            print(o.group('direction'))
            # layer
            print(o.group('layer'))
            print(o.group('lx1'))
            print(o.group('ly1'))
            print(o.group('lx2'))
            print(o.group('ly2'))
            # Fixed 
            print(o.group('fx1'))
            print(o.group('fy1'))
            print(o.group('fdir'))

            

def get_pin_line(in_pin):
    
    #if not isinstance(bytes):
    mod_re = bytes(pin_line_reg, 'utf-8')

    # parse template
    if not isinstance(in_pin, bytes):
        with open(in_pin, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
    else:
        data = in_pin
    
    mo = regex.finditer(mod_re, data, re.MULTILINE)

    return mo
        

def get_component(in_def):
    
    mod_re = bytes(comp_block_reg, 'utf-8')

    # parse template
    with open(in_def, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        mo = regex.findall(mod_re, data, re.MULTILINE)

    mo_l = get_comp_line(mo)

    comp_list = []

    for l in mo_l:

        nc = Component(
            name=l.group('name'),
            comp=l.group('comp'),
            x1=l.group('x1'),
            y1=l.group('y1')
        )

        comp_list.append(nc)

    write_components(comp_list)


def get_comp_line(in_comp):
    
    mod_re = bytes(comp_line_reg, 'utf-8')

    if isinstance(in_comp, list):
        in_comp = in_comp[0]

    # parse template
    if not isinstance(in_comp, bytes):
        with open(in_comp, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            mo = regex.findall(mod_re, data, re.MULTILINE)
    else:
        data = in_comp

    mo = regex.finditer(mod_re, data, re.MULTILINE)

    return mo

def write_components(o_file, comp_list, layer_h):

    o_file.write("""
    union() {
    """)

    for c in comp_list:
        o_file.write("""
        {c.name}(orientation = "{c.direction}", xpos = {c.x1}, ypos = {c.y1}, zpos = {layer_h});
        """)

    o_file.write("""
    }
    """)

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

tlef_f = './def_test/test_1.tlef'

def get_nets(in_def):
    mod_re = bytes(nets_block_reg, 'utf-8')
    #mod_re = regex.compile(nets_block_reg, re.MULTILINE)

    # parse template
    with open(in_def, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        mo = regex.findall(mod_re, data, re.MULTILINE)

    mo_l = get_net_lines(mo)

    nets_list = []

    nb = NetBuilder(
        px        =net_property['px'],
        layer     =net_property['layer'],
        lpv       =net_property['lpv'],
        def_scale =net_property['def_scale'],
        bottom_layers=net_property['bot_layers']
    )
    nb.import_tlef(tlef_f)
    nb.import_met(mets)

    for l in mo_l:
        mo_r = get_net_route(l.group(0))

        n = Nets(net=l.group('net').decode('utf-8'),
            dev1=l.group('dev1').decode('utf-8'),
            p1=l.group('p1').decode('utf-8'),
            dev2=l.group('dev2').decode('utf-8'),
            p2=l.group('p2').decode('utf-8'),
            )

        nb.set_net(n)

        for route in mo_r:
            r_deco = {}
            v_deco = ''
            #print(route.group('layer'))
            for coor in ['x1', 'y1', 'z1', 'x2', 'y2', 'z2']:
                if route.group(coor) is not None:
                    r_deco[coor] = route.group(coor).decode('utf-8')
                else:
                    r_deco[coor] = None
            
            if route.group('x2') is not None:
                nb.add_route(
                route.group('layer').decode('utf-8'),
                r_deco['x1'],
                r_deco['y1'],
                r_deco['z1'],
                x2=r_deco['x2'],
                y2=r_deco['y2'],
                z2=r_deco['z2']
            )
            elif route.group('via') is not None:
                nb.add_route(
                route.group('layer').decode('utf-8'),
                r_deco['x1'],
                r_deco['y1'],
                r_deco['z1'],
                via=route.group('via').decode('utf-8')
            )

            else:
                raise ValueError('Issue parsing route')

            

        nets_list.append(nb.export_net())
            
    return nets_list
    

def get_net_lines(in_net):
    mod_re = bytes(nets_line_reg, 'utf-8', )

    if isinstance(in_net, list):
        in_net = in_net[0]

    # parse template
    if not isinstance(in_net, bytes):
        with open(in_net, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
    else:
        data = in_net

    mo = regex.finditer(mod_re, data, re.MULTILINE)
    return mo

def get_net_route(in_net_line):
    mod_re = bytes(nets_route_reg, 'utf-8')

    # parse template
    if not isinstance(in_net_line, bytes):
        with open(in_net_line, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
    else:
        data = in_net_line
    
    mo = regex.finditer(mod_re, data, 0)
    return mo

def write_nets(o_file, net_list, shape='cube', size=[0.1, 0.1, 0.1]):

    rot = '[0, [0,0,1]]'

    for n in net_list:
        #o_file.write("""
        #// routing {n.net}
        #// connect {dev1}, {p1} to {dev2}, {p2}
        #polychannel(""")
        pc_route = []

        for r in n.route:
            size = str(size)
            pt1 = [r.x1, r.y1, r.z1]
            pt2 = [r.x2, r.y2, r.z2]
            
            pc_pt1 = [shape, size, pt1, rot]
            pc_pt2 = [shape, size, pt2, rot]

            pc_rotue.append(pc_pt1)
            pc_rotue.append(pc_pt2)
            # todo


        pc.polychannel_route(
            n.net, [dev1, p1], [dev2, p2],
            pc_route
        )






tlef_bl_re = r'(?P<key>(?:LAYER|SITE|VIA|PROPERTYDEFINITIONS|UNITS))\s*(?|.*\s*)*?END\s*\w*'
tlef_layer_re = r'LAYER\s*(?P<layer_name>\w*)\s*(?|(?:TYPE\s*(?P<type>(?:ROUTING|CUT))\s*;|DIRECTION\s*(?P<direction>(?:HORIZONTAL|VERTICAL))\s*;|MINWIDTH\s*(?P<minwidth>[\d.]*)\s*;|WIDTH\s*(?P<width>[\d.]*)\s*;)\s*)*END\s*(\w*)\s$'
tlef_via_re  = r'VIA\s*(?P<via_name>\w*)\s*(?P<type>\w*)(?|.*\n)*?(?:END\s*(?&via_name)\s*$)'
tlef_via_l_re= r'LAYER (?P<via_name>\w*)\s*;\s*(?:RECT\s*(?P<x1>[\d.-]*)\s*(?P<y1>[\d.-]*)\s*(?P<x2>[\d.-]*)\s*(?P<y2>[\d.-]*)\s*;)*'
tlef_site_re= r'SITE*\s(?P<site_name>\w*)\s*(?|(?:CLASS\s*(?P<class>\w*)\s*;|SYMMETRY\s*(?P<symmetry>\w*)\s*;|\s*SIZE\s*(?P<size_x>\d*)\s*BY\s*(?P<size_y>\d*)\s*;)\s*)*END\s*(\w*)\s*$'

def get_tlef_layer(tlef):
    
    mod_re = bytes(tlef_layer_re, 'utf-8')

    # parse template
    with open(tlef, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)

    mo = regex.finditer(mod_re, data, 0)
    

def get_tlef_via(tlef):
    
    mod_re = bytes(tlef_via_re, 'utf-8')

    # parse template
    with open(tlef, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)

    mo = regex.finditer(mod_re, data, 0)
    

def tlef_via_layer(in_via):
    
    mod_re = bytes(tlef_via_l_re, 'utf-8')

    if not isinstance(in_net_line, bytes):
        with open(in_via, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
    else:
        data = in_via

    mo = regex.finditer(mod_re, data, 0)
    return mo

    

def get_tlef_site(tlef):

    mod_re = bytes(tlef_site_re, 'utf-8')

    # parse template
    with open(tlef, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)

    mo = regex.finditer(mod_re, data, 0)
    
def main(platform, design, def_file, results_dir, px, layer, bttm_layer, lpv, xbulk, ybulk, zbulk, xchip, ychip, def_scale, pitch, res, dimm_file, comp_file):
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--platform', type=str)
    parser.add_argument('--design', type=str)
    parser.add_argument('--def_file', type=str)
    parser.add_argument('--results_dir', type=str)
    parser.add_argument('--px', type=float)
    parser.add_argument('--layer', type=float)
    parser.add_argument('--bottom_layer', type=int)
    parser.add_argument('--lpv', type=int)
    parser.add_argument('--xbulk', type=int)
    parser.add_argument('--ybulk', type=int)
    parser.add_argument('--zbulk', type=int)
    parser.add_argument('--xchip', type=int, nargs=2)
    parser.add_argument('--ychip', type=int, nargs=2)
    parser.add_argument('--def_scale', type=float)
    parser.add_argument('--pitch', type=int)
    parser.add_argument('--res', type=int)
    parser.add_argument('--dimm_file', type=str)
    parser.add_argument('--comp_file', type=str)

    args = parser.parse_args()

    main(
        args.platform,
        args.design,
        args.def_file,
        args.results_dir,
        args.px,
        args.layer,
        args.bottom_layer,
        args.lpv,
        args.xbulk,
        args.ybulk,
        args.zbulk,
        args.xchip,
        args.ychip,
        args.def_scale,
        args.pitch,
        args.res,
        args.dimm_file,
        args.comp_file
    )