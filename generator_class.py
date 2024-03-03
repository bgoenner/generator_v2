
import json
import regex, mmap, re

class Nets:
    
    def __init__(
            self,
            net = None,
            dev1 = None,
            p1 = None,
            dev2 = None,
            p2 = None,
            ):
        self.net = net
        self.dev1 = dev1
        self.p1   = p1
        self.dev2 = dev2
        self.p2   = p2
        self.route = []

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

    def compress_routes(self):

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
                    

    def print_routes(self):
        pass

    def print_net(self):
        r = str(self.route).replace(']],', ']],\n')

        print(f"""
        Net: {self.net}
        Dev1: {self.dev1} : {self.p1}
        Dev2: {self.dev2} : {self.p2}
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
            x1 = float(x1)/self.def_scale
            y1 = float(y1)/self.def_scale
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
            x1 = float(x1)/self.def_scale
            y1 = float(y1)/self.def_scale

            x2 = float(x2)/self.def_scale
            y2 = float(y2)/self.def_scale
            
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
        y1=None):
        
        self.name = name
        self.comp = comp
        self.x1   = x1
        self.y1   = y1

class Pin:
    
    def __init__(self,
        name=None,
        net=None,
        direction=None,
        layer=None,
        l_size=[0,0,0,0],
        fixed=[0,0,'']):
        
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