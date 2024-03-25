


def main(platform, design, def_file, results_dir, px, layer, bottom_layer, lpv, xbulk, ybulk, zbulk, xchip, ychip, def_scale, pitch, res, dimm_file):
    import generator_v2

    #main(platform, 
    #   design, 
    #   def_file, 
    #   results_dir, 
    #   px, 
    #   layer, 
    #   bttm_layer, 
    #   lpv, 
    #   xbulk, 
    #   ybulk, 
    #   zbulk, 
    #   xchip, 
    #   ychip, 
    #   def_scale, 
    #   pitch, 
    #   res, 
    #   dimm_file, 
    #   tlef, 
    #   comp_file, 
    #   pin_con_dir_f, 
    #   transparent=False)

    # implied component file
    comp_file = f"designs/{platform}/{design}/{design}.v"

    # get pins from comp_file and make them TOP

    generator_v2.main(
        platform,
        design,
        def_file,
        results_dir,
        px,
        layer,
        bottom_layer, 
        lpv,
        xbulk,
        ybulk,
        zbulk,
        xchip,
        ychip,
        def_scale,
        pitch,
        res,
        dimm_file,
        comp_file
        )
    



if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--platform', metavar='<platform>', dest='platform', type=str,
                    help="Design platform.")
    ap.add_argument('--design', metavar='<design_name>', dest='design', type=str,
                    help="The design name.")
    ap.add_argument('--def_file', metavar='<path>', dest='def_file', type=str,
                    help="Path to the .def file from OpenROAD flow.")
    ap.add_argument('--results_dir', metavar='<path>', dest='results_dir', type=str,
                    help="Path where the results are generated.")
    ap.add_argument('--px', metavar='<value>', dest='px', type=float,
                    help="Metric pixel size.")
    ap.add_argument('--layer', metavar='<value>', dest='layer', type=float,
                    help="Metric layer size.")
    ap.add_argument('--bottom_layer', metavar='<value>', dest='bottom_layer', type=int,
                    help="Value of bottom layer (routing).")
    ap.add_argument('--lpv', metavar='<value>', dest='lpv', type=int,
                    help="Multiples of layers per via.")
    ap.add_argument('--xbulk', metavar='<value>', dest='xbulk', type=int,
                    help="Horizontal length of the bulk in pixels.")
    ap.add_argument('--ybulk', metavar='<value>', dest='ybulk', type=int,
                    help="Vertical length of the bulk in pixels.")
    ap.add_argument('--zbulk', metavar='<value>', dest='zbulk', type=int,
                    help="Height of the bulk in layers.")
    ap.add_argument('--xchip', metavar='<values>', dest='xchip', nargs = '+', type=int,
                    help="Left and right endpoints of chip in multiples of pixels.")
    ap.add_argument('--ychip', metavar='<values>', dest='ychip', nargs = '+', type=int,
                    help="Bottom and top endpoints of chip in multiples of pixels.")
    ap.add_argument('--def_scale', metavar='<value>', dest='def_scale', type=int,
                    help="Multiplier used in the def file for unit precision.")
    ap.add_argument('--pitch', metavar='<value>', dest='pitch', type=int,
                    help="PNR pitch for the platform.")
    ap.add_argument('--res', metavar='<value>', dest='res', type=int,
                    help="Resolution of the scad rendering.")
    ap.add_argument('--dimm_file', metavar='<path>', dest='dimm_file', type=str,
                    help="Optional .csv file with routing dimensions.", default = None)
    args = ap.parse_args()

    main(args.platform,
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
             args.dimm_file)