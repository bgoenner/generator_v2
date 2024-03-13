polychannel_route("connect10", 
            ["serp10", "out_fluid"], ["mix0", "b_fluid"]
            [['cube', [0.1, 0.1, 0.1], [1080.0, 1019.725, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1080.0, 930.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1080.0, 930.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1139.725, 930.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1139.725, 930.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1139.725, 930.0, 0.2], [0, [0, 0, 1]]]]);
        polychannel_route("connect20", 
            ["serp20", "out_fluid"], ["mix0", "a_fluid"]
            [['cube', [0.1, 0.1, 0.1], [1080.0, 780.275, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1080.0, 780.275, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1080.0, 810.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1080.0, 810.0, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1110.0, 810.0, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1110.0, 810.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1110.0, 960.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1110.0, 960.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1139.725, 960.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1139.725, 960.0, 0.4], [0, [0, 0, 1]]]]);
        polychannel_route("connect_m0", 
            ["serp7", "in_fluid"], ["mix0", "out_fluid"]
            [['cube', [0.1, 0.1, 0.1], [1260.0, 840.275, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1260.0, 840.275, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1260.0, 960.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1260.0, 960.0, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1200.0, 960.0, 0.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1200.0, 960.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1200.0, 960.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1170.275, 960.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1170.275, 960.0, 0.4], [0, [0, 0, 1]]]]);
        polychannel_route("out", 
            ["PIN", "out"], ["serp7", "out_fluid"]
            [['cube', [0.1, 0.1, 0.1], [960.0, 660.0, 0.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 690.0, 0.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 690.0, 1.0], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1140.0, 690.0, 1.0], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1140.0, 690.0, 0.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1140.0, 690.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1140.0, 690.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [1140.0, 839.725, 0.4], [0, [0, 0, 1]]]]);
        polychannel_route("soln1", 
            ["PIN", "soln1"], ["serp10", "in_fluid"]
            [['cube', [0.1, 0.1, 0.1], [960.0, 930.0, 1.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 1.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 1.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 1.4000000000000001], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 1.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 1.0], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 0.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 960.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 1019.725, 0.4], [0, [0, 0, 1]]]]);
        polychannel_route("soln2", 
            ["PIN", "soln2"], ["serp20", "in_fluid"]
            [['cube', [0.1, 0.1, 0.1], [960.0, 780.275, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 0.4], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 0.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 0.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 1.0], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 1.2], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 1.4000000000000001], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 1.6], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 810.0, 1.8], [0, [0, 0, 1]]],
 ['cube', [0.1, 0.1, 0.1], [960.0, 840.0, 1.8], [0, [0, 0, 1]]]]);
        