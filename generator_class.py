
import json
import regex, mmap, re
import networkx as nx

class Nets:
    
    def __init__(
            self,
            net = None,
            devs = None,
            #dev1 = None,
            #p1 = None,
            #dev2 = None,
            #p2 = None,
            ):
        self.net = net
        #self.dev1 = dev1
        #self.p1   = p1
        #self.dev2 = dev2
        #self.p2   = p2
        self.devs = devs
        self.route = []
        self.compress = False
        self.route_len = 0

        self.dangle_routes = False

        # tlef definitions

    def add_route(self, 
        layer = None,
        x1 = None,
        y1 = None,
        z1 = None,
        x2 = None,
        y2 = None,
        z2 = None,
        via= None):
        
        if (via is not None) and (x2 is not None):
            ValueError("Cannot both define 'via' and 'x2'")
        # check stars
        elif x2 is not None:
            nr = [[x1, y1, z1], [x2, y2, z2]]
        elif via is not None:
            nr = [[x1, y1, z1], [via]]

        #print('Adding route: '+str(nr))
        self.route.append(nr)

    def calc_len_funct(self, in_route=None):
        if isinstance(in_route, list):
            pass
        elif isinstance(in_route, type(None)):
            in_route=self.route
        else:
            raise ValueError(f'in_route is {type(in_route)}; should be lsit')

        if not self.compress:
            raise Exception("Routes need compression")
        r_len = 0
        for i, r in enumerate(in_route):
            if i == 0:
                print(len(in_route))
                print(in_route)
                continue
            else:
                r_lenx = abs(in_route[i-1][0] - in_route[i][0])**2
                r_leny = abs(in_route[i-1][1] - in_route[i][1])**2
                r_lenz = abs(in_route[i-1][2] - in_route[i][2])**2
                r_len += (r_lenx+r_leny+r_lenz)**(1/2) 

        return r_len
        #self.route_len = r_len
            
    def calc_len(self):
        print(f"calc len {self.net}")
        print(self.route.nodes)
        if isinstance(self.route, nx.Graph):
            len_dict = {}
            for nd in self.route.nodes:
                if 'route' in self.route.nodes[nd]:
                    len_dict[nd] = self.calc_len_funct(self.route.nodes[nd]['route'])
            self.route_len = len_dict
        else:
            self.route_len = self.calc_len_funct()

    def report_len(self):
        if self.route_len == 0:
            self.calc_len()
        return self.route_len
            
    def report_route_graph(self):
        return nx.node_link_data(self.route)

    def compress_routes(self, debug=True, design='', report_route=True, subsegment=True):

        if self.compress:
            raise Exception("Routes already compressed")

        self.compress = True

        def check_inner(r_list, node, head=False):
            # that inner node is not inside
            if len(r_list) > 4:
                if node in r_list[2:-3]:
                    if debug: print(str(node)+" is inner")
                    # get sub list
                    ii = r_list.index(node)
                    if head:
                        l_list = r_list[:ii-1]
                    else:
                        l_list = r_list[ii-1:]
                    # if head reverse list
                    l_list = list(reversed(l_list))
                    # reinsert list
                    if head:
                        r_list = l_lsit+r_list[ii:]
                    else:
                        r_list = r_list[:ii]+l_list
                    
                    if debug: print("new list: "+r_list)
                else:
                    if head:
                        r_list.insert(0, node)
                    else:
                        r_list.append(node)
            else:
                if head:
                    r_list.insert(0, node)
                else:
                    r_list.append(node)

        def check_route_ends(r_nodes, r_list):
            r = r_nodes
            if r[0] == r_list[0]:
                if debug: print(str(r[0])+" at head")
                check_inner(r_list, r[1], head=True)
                self.route.pop(ind)
                return True
                #rn.insert(0, r[1])
            elif r[0] == r_list[-1]:
                if debug: print(str(r[0])+" at tail")
                check_inner(r_list, r[1], head=False)
                self.route.pop(ind)
                return True
                #rn.append(r[1])
            elif r[-1] == r_list[0]:
                if debug: print(str(r[1])+" at head")
                check_inner(r_list, r[0], head=True)
                self.route.pop(ind)
                return True
                #rn.insert(0, r[0])
            elif r[-1] == r_list[-1]:
                if debug: print(str(r[1])+" at tail")
                check_inner(r_list, r[0], head=False)
                self.route.pop(ind)
                return True
                #rn.append(0, r[0])
            else:
                return False

        def check_d_routes(r, d_routes):
            for dr in d_routes:
                if check_route_ends(r, dr['route']):
                    return True
            return False

        def subsegment_routes(route, d_routes):
            # check if route head or tail in other routes
            #r_head_in_dr = False
            #r_tail_in_dr = False

            # It is assumed in this method we do not have loops in a 'wire'

            dr_head_in_r = [False]*(len(d_routes)+1)
            dr_tail_in_r = [False]*(len(d_routes)+1)

            in_routes = []
            in_routes.append({'route':route, 'head':False, 'tail':False, 'break':[]})
            for dr in d_routes:
                in_routes.append({'route':dr['route'], 'head':False, 'tail':False, 'break':[]})

            def check_ends_in_route(route_ends_check, targ_route):
                for ind, pt in enumerate(targ_route):
                    if route_ends_check[0] == pt:
                        return "head", pt, ind
                    elif route_ends_check[-1] == pt:
                        return "tail", pt, ind
                return False, None, None

            #for ind, seg in enumerate(d_routes):
            #    seg_return = check_if_ends_in_route(self.route, seg['route'])
            #    if seg_return == "head":
            #        r_head_in_dr = ind
            #    elif seg_return == "tail":
            #        r_tail_in_dr = ind
            #    if r_head_in_dr and r_tail_in_dr: # stop once ends are found
            #        break

            # check route first
            #for ind, dr in enumerate(d_routes):
            #    seg_return = check_ends_in_route(dr['route'], route)
            #    if seg_return == "head":
            #        dr_head_in_r[ind] = "r"
            #    elif seg_return == "tail":
            #        dr_tail_in_r[ind] = "r"
            #    if dr_head_in_r[ind] and dr_tail_in_r[ind]: # stop once ends are found
            #        break

            # check d_routes

            # TODO what if a break is at another break
            for ind_ends, dr_ends in enumerate(in_routes):
                for ind_srch, dr_srch in enumerate(in_routes):
                    if ind_ends == ind_srch: # this means we are checking the same route, skip
                        continue 
                    seg_return, out_pt, out_pt_ind = check_ends_in_route(dr_ends['route'], dr_srch['route'])
                    if seg_return == "head":
                        #dr_head_in_r[ind_ends] = ind_ch
                        in_routes[ind_ends]['head'] = ind_srch
                        # TODO check if exists, ifso append
                        in_routes[ind_srch]['break'].append({'pt_ind':out_pt_ind ,'pt':out_pt, 'r_ind':[[ind_ends, 'head']]})
                    elif seg_return == "tail":
                        #dr_tail_in_r[ind_ends] = ind_ch
                        in_routes[ind_ends]['tail'] = ind_srch
                        in_routes[ind_srch]['break'].append({'pt_ind':out_pt_ind ,'pt':out_pt, 'r_ind':[[ind_ends, 'tail']]})
                    if in_routes[ind_ends]['head'] and in_routes[ind_ends]['tail']: # stop once ends are found
                        break
            
            new_routes = {}
            # break routes
            

            net_G = nx.Graph()
            if debug: print(f"Subsegment net {self.net}")

            for ind, r_t in enumerate(in_routes):
                br_count = 0 # since 0 is the head of the route
                last_br_ind = 0
                # we want to go low to high nodes
                r_t['break'] = sorted(r_t['break'], key=lambda k : k['pt_ind'])
                if debug: print(f'breaks for {ind}: ', r_t['break'])
                if debug: print(f'route: {r_t["route"]}')
                for br_pt in r_t['break']:
                    new_node = f'{ind}_{br_count}'
                    # check if node exists; they can be created through add_edge
                    if new_node in net_G.nodes:
                        net_G.nodes[new_node]['route'] = r_t['route'][last_br_ind:br_pt['pt_ind']+1]
                    else:
                        net_G.add_node(f'{ind}_{br_count}', route=r_t['route'][last_br_ind:br_pt['pt_ind']+1])
                    
                    net_G.add_edge(f'{ind}_{br_count}', f'br_{ind}_{br_count}')
                    net_G.add_edge(f'{ind}_{br_count+1}', f'br_{ind}_{br_count}')
                    # check if node is at 0 or 1; this adds the branching route node and edge
                    for ch_end in list(br_pt['r_ind']):
                        # number of breaks in ref route
                        num_br = len(in_routes[ch_end[0]]["break"])
                        if ch_end[1] == "head":
                            net_G.add_edge(f'{ch_end[0]}_{0}', f'br_{ind}_{br_count}')
                        elif ch_end[1] == "tail": # we assume last seg is # of break pts
                            net_G.add_edge(f'{ch_end[0]}_{num_br}', f'br_{ind}_{br_count}')
                    if debug: print(f"branch route {new_node}: {net_G.nodes[new_node]['route']}")
                    
                    last_br_ind = br_pt['pt_ind']
                    # create final route
                    if ind == len(r_t['break'])-1:
                        # last element is == to len? (but it works??? vvvv)
                        net_G.nodes[f'{ind}_{br_count+1}']['route'] = r_t['route'][last_br_ind:len(r_t['route'])]
                        if debug: print(f"last branch route {ind}_{br_count+1}: {net_G.nodes[f'{ind}_{br_count+1}']['route']}")

                    br_count += 1
                # create final route
                #if ind == len(r_t['break']):
                #net_G.nodes[f'{ind}_{br_count}']['route'] = r_t['route'][last_br_ind:-1]

                if len(r_t['break']) == 0:
                    if f'{ind}_0' in net_G:
                        net_G.nodes[f'{ind}_0']['route'] = r_t['route']
                    else:
                        net_G.add_node(f'{ind}_0', route=r_t['route'])

                    
            
            return net_G
            


        nr = []
        d_routes = []
        self.dangle_routes = False
        count = 0
        r_len = len(self.route)

        if debug:
            print("initial routes:")
            print(self.route)

        #while len(nr) + sum([len(x['route']) for x in d_routes]) < r_len+1:
        #while len(self.route) > 1:    
        while True:
            #print(len(self.route))
            if debug: print("sr:"+str(len(self.route))+":"+str(self.route))
            if len(nr)>=1 and debug:
                print("nr:"+str(len(nr))+":"+str(nr))
            r_init_len = len(self.route)
            for ind, r in enumerate(self.route):
                if len(nr) < 1:
                    self.route.pop(ind)
                    nr.append(r[0])
                    nr.append(r[1])
                    break
                else:
                    if debug: print("r:"+str(r))
                    if check_route_ends(r, nr):
                        break
                    if len(d_routes) > 0:
                        if check_d_routes(r, d_routes):
                            break
                        #for dr in d_routes:
                        #    if check_route_ends(r, dr['route']):
                        #        break
                    # no matches
                    # check if node is internal
                    if len(nr) > 4 and r[0] in nr[2:-3]:
                        d_routes.append({'head':r[0], 'route':r})
                        self.route.pop(ind)
                        self.dangle_routes = True
                        print("has dangling route")
                        break
                    if len(nr) > 4 and r[1] in nr[2:-3]:
                        d_routes.append({'head':r[1], 'route':r})
                        self.route.pop(ind)
                        self.dangle_routes = True
                        print("has dangling route")
                        break
                # TODO start new route after running through entire list
                if ind +1 == r_init_len:
                    # loops again otherwise ind is too large
                    if len(self.route) == r_init_len:
                        d_routes.append({'head':None, 'route':r})
                        self.route.pop(ind)
                        self.dangle_routes = True
                        print("has dangling route (Unconnected)")

                    #if r[0] == nr[0]:
                    #    if debug: print(str(r[0])+" at head")
                    #    check_inner(nr, r[1], head=True)
                    #    self.route.pop(ind)
                    #    break
                    #    #rn.insert(0, r[1])
                    #elif r[0] == nr[-1]:
                    #    if debug: print(str(r[0])+" at tail")
                    #    check_inner(nr, r[1], head=False)
                    #    self.route.pop(ind)
                    #    break
                    #    #rn.append(r[1])
                    #elif r[1] == nr[0]:
                    #    if debug: print(str(r[1])+" at head")
                    #    check_inner(nr, r[0], head=True)
                    #    self.route.pop(ind)
                    #    break
                    #    #rn.insert(0, r[0])
                    #elif r[1] == nr[-1]:
                    #    if debug: print(str(r[1])+" at tail")
                    #    check_inner(nr, r[0], head=False)
                    #    self.route.pop(ind)
                    #    break
                        #rn.append(0, r[0])

            if len(self.route) < 1:
                break
                    
            if debug: print('\n')
            count += 1
            if count > 100:
                raise Exception("Unable to complete route before 100 inters")

        if report_route:
            route_report_file = f"routes_out_{design}.txt"
            rep_out = open(route_report_file, 'a+')
            rep_out.write(f"Net:{self.net}\nDevs:{self.devs}\nroutes:\n{nr}\n")
            if self.dangle_routes:
                for r in d_routes:
                    rep_out.write(f"{r}\n")

        if self.dangle_routes and subsegment:
            self.route = subsegment_routes(nr, d_routes)
        else:
            self.dangling_routes = d_routes
            self.route = nx.Graph()
            self.route.add_node('', route=nr)

        if debug:
            print("Final routes:")
            print(self.route)

    def compress_routes_2(self, debug=False):

        class loose_list(list):
            def __init__(self):
                self.head_link = None
                self.tail_link = None
                super().__init__()
            def can_insert(self):
                return (self.head_link is not None and 
                    self.tail_link is not None)

        class main_list(list):
            def __init__(self):
                super().__init__()

        def add_to_list(r_list, route):
            # the first condition should never happen
            if (r[0] in comp_r) and (r[1] in comp_r):
                i0 = r_list.index(r[0])
                i1 = r_list.index(r[1])
                #i_min = min([i0, i1])

                return True
            elif (r[0] in comp_r[0]):
                r_list.insert(0, r[1])
                return True
            elif (r[0] in comp_r[-1]):
                r_list.append(r[1])
                return True
            elif (r[1] in comp_r[0]):
                r_list.insert(0, r[0])
                return True
            elif (r[1] in comp_r[-1]):
                r_list.append(r[0])
                return True
            # todo inserted in the center
            else:
                return False
        
        def check_inter(r_list, node):
            if len(r_list) > 4:
                if node in r_list[2:-3]:
                    # get sub list
                    # reverse list
                    # reinsert list
                    pass
                else:
                    pass

        def add_list_of_list(r_list, route):
            for sub_list in r_list:
                if add_to_list(r_list, route):
                    return True
                else:
                    break
            return False

        if debug:
            print("initial routes:")
            print(self.route)

        comp_r = []
        loose_r= []
        for r in self.route:
            if len(comp_r) == 0:
                comp_r += r
            else:
                if add_to_list(comp_r, r):
                    pass
                elif len(loose_r) == 0:
                    loose_r.append(r)
                elif add_list_of_list(loose_r, r):
                    pass
                    # check changed loose lists to be inserted
                
                else:
                    # create new list
                    loose_r.append(r)
                    # if sub_r not in r create new sub list

        if debug:
            print("Final routes:")
            print(self.route)
                    

    def print_routes(self):
        pass

    def print_net(self):
        r = str(self.route).replace(']],', ']],\n')

        dev_str = [f"Dev{i+1}: {x['dev']} : {x['port']}"+'\n' for i, x in enumerate(self.devs)]

        print(f"""
        Net: {self.net}
        {dev_str}
        Route: {r}
        """)

class NetBuilder:

    def __init__(self,
        px=None,
        layer=None,
        lpv=None,
        def_scale=None,
        bottom_layers=None):

        self.px   = px
        self.layer= layer
        self.lpv  = lpv
        self.def_scale  = def_scale
        self.bot_layers = bottom_layers 

        self.net = None
        self.vias= {}
        self.met_layers = None

    def set_net(self, net):
        self.net = net


    def import_tlef(self, tlef_f):
        
        print(tlef_f)
        # get layers
        layer_re = r'LAYER\s*(?P<layer_name>\w*)\s*(?|(?:TYPE\s*(?P<type>(?:ROUTING|CUT))\s*;|DIRECTION\s*(?P<direction>(?:HORIZONTAL|VERTICAL))\s*;|MINWIDTH\s*(?P<minwidth>[\d.]*)\s*;|WIDTH\s*(?P<width>[\d.]*)\s*;)\s*)*END\s*(\w*)\s$' 
        layer_re = bytes(layer_re, 'utf-8')

        self.layers_list = {
            "CUT":[],
            "ROUTING":[]}

        with open(tlef_f, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            mo_l = regex.finditer(layer_re, data, re.MULTILINE)

            for l in mo_l:
                self.layers_list[l.group('type').decode('utf-8')].append(l.group('layer_name').decode('utf-8'))

        # get vias
        via_re   = r'VIA\s*(?P<via_name>\w*)\s*(?P<type>\w*)(?|.*\n)*?(?:END\s*(?&via_name)\s*$)'
        via_l_re = r'LAYER (?P<met_name>\w*)\s*;\s*(?:RECT\s*(?P<x1>[\d.-]*)\s*(?P<y1>[\d.-]*)\s*(?P<x2>[\d.-]*)\s*(?P<y2>[\d.-]*)\s*;)*'

        via_re = bytes(via_re, 'utf-8')
        via_l_re=bytes(via_l_re, 'utf-8')


        # parse template
        with open(tlef_f, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            mo_v = regex.finditer(via_re, data, re.MULTILINE)
            
            for m in mo_v:
                #print(m.group(0))
                v_m = []
                mo_vl = regex.finditer(via_l_re, m.group(0), re.MULTILINE)
                for vl in mo_vl:
                    v_m.append(vl.group('met_name').decode('utf-8'))

                print("import via "+m.group('via_name').decode('utf-8')+"\n"+str(v_m))
                self.vias[m.group('via_name').decode('utf-8')] = v_m

    def get_vias_met(self, via):        
        met_v = []
        for v in self.vias[via]:
            if v in self.met_layers:
                met_v.append(v)

        return [met_v[0], met_v[1]]

    # expects a json met config or dictionary
    def import_met(self, config=None, met_f=None):
        
        if config is not None:
            if isinstance(config, dict):
                self.met_layers = config
            elif isinstance(config, str):
                self.met_layers = json.loads

        if met_f is not None:
            raise ValueError('met_f not currently implemented')

    def add_route(self, 
        layer = None,
        x1 = None,
        y1 = None,
        z1 = None,
        x2 = None,
        y2 = None,
        z2 = None,
        via= None,
        debug=False):


        if via is not None:
            x1 = float(x1)/self.def_scale*self.px
            y1 = float(y1)/self.def_scale*self.px
            x2 = x1
            y2 = y1
            v = self.get_vias_met(via)

            z1 = (self.bot_layers + self.met_layers[v[0]]*self.lpv)*self.layer

            z2 = (self.bot_layers + self.met_layers[v[1]]*self.lpv)*self.layer

            if debug:
                print("Add route v: "+str([[x1, y1, z1],[x2, y2, z2]]))
        elif x2 is not None:
            z1 = (self.bot_layers + self.met_layers[layer]*self.lpv)*self.layer
            z2 = z1

            if x2 == '*':
                x2 = x1
            if y2 == '*':
                y2 = y1
            x1 = float(x1)/self.def_scale*self.px
            y1 = float(y1)/self.def_scale*self.px

            x2 = float(x2)/self.def_scale*self.px
            y2 = float(y2)/self.def_scale*self.px
            
            if debug:
                print("Add route x2: "+str([[x1, y1, z1],[x2, y2, z2]]))
        self.net.add_route(layer, x1, y1, z1, x2, y2, z2)



    def export_net(self):
        return self.net

class Component:
    
    def __init__(self,
        name=None,
        comp=None,
        x1=None,
        y1=None,
        dir=None):
        
        self.name = name
        self.comp = comp
        self.x1   = x1#/def_scale
        self.y1   = y1#/def_scale
        self.dir  = dir

class Pin:
    
    def __init__(self,
        name=None,
        net=None,
        direction=None,
        layer=None,
        l_size=[0,0,0,0],
        fixed=[0,0,''],
        connect_dir=None):
        
        self.name = name
        self.net  = net
        self.direction = direction
        self.layer = layer
        self.lx1 = l_size[0]
        self.ly1 = l_size[1]
        self.lx2 = l_size[2]
        self.l2y = l_size[3]
        self.fx1 = fixed[0]
        self.fy1 = fixed[1]
        self.fdir = fixed[2]
        self.set_connect_dir(connect_dir)

    def set_connect_dir(self, cdir):
        if cdir.upper() == "TOP" or \
            connect_dir == 'z+':
            self.connect_dir = "z+"
        elif cdir.upper() == "BOTTOM" or \
            connect_dir == 'z-':
            self.connect_dir = "z-"
        elif cdir.upper() == "LEFT" or \
            connect_dir == 'x+':
            self.connect_dir = "x+"
        elif cdir.upper() == "RIGHT" or \
            connect_dir == 'x-':
            self.connect_dir = "x-"
        elif cdir.upper() == "FRONT" or \
            connect_dir == 'y+':
            self.connect_dir = "y+"
        elif cdir.upper() == "BACK" or \
            connect_dir == 'y-':
            self.connect_dir = "y-"
