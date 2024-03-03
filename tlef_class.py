

class TLEF_def:

    class VIA:
        def __init__(self, name, v_type):
            self.name = name
            self.v_type = v_type
            self.via = {}

        def add_layer(self, name, shape, size):
            new_layer = {
                'shape':shape,
                'x1':size[0],
                'y1':size[1],
                'x2':size[2],
                'y2':size[3]
            }

            self.via[name] = new_layer

    class SITE:
        def __init__(
            self,
            name=None,
            s_class=None,
            symmetry=None,
            size=[0,0]):

            self.name = name
            self.s_class = s_class
            self.symmetry = symmetry
            self.size = size
            

    class LAYER:
        def __init__(
            self, 
            name=None,
            l_type=None,
            minwidth=None,
            width=None,
            direction=None):

            self.layer_n = name
            self.l_type = l_type
            self.minwidth = minwidth
            self.width = width
            self.direction = direction  

    def __init__(self):
        
        self.vias    = {}
        self.layers_r= {}
        self.layers_c= {}
        self.site    = {}

    def add_via(
        self,
        name,
        shape,
        size
    ):
        nv = self.VIA(
            name=name,
            shape=shape,
            size=size
        )

        self.via[name] = nv

    def add_layer_route(
        self,
        name,
        l_type,
        minwidth,
        width,
        direction):
        
        nl = self.LAYER(
            name=name,
            l_type=l_type,
            minwidth=minwidth,
            width=width,
            direction=direction
        )

        self.layers_r[name] = nl

    def add_layer_cut(
        self,
        name,
        width
        ):

        nl = self.LAYER(
            name=name,
            width=width
        )

        self.layers_c[name] = nl

    def add_site(
        self,
        name,
        s_class,
        symmetry,
        size
        ):

        ns = self.SITE(
            name=name,
            s_class=s_class,
            symmetry=symmetry,
            size=size
        )

        self.site[name] = ns

