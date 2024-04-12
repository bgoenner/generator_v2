use <./h.r.3.3_pdk_merged.scad>
use <./polychannel_v2.scad>
use <./routing.scad>

px = 0.0076;
layer = 0.01;


difference() {
    %cube([2550*px,1590*px,280*layer]);
    union() {
polychannel_route("connect0", 
        [["serp1", "in_fluid"], ["serp0", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [3.648, 3.87809, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.648, 3.87809, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.648, 4.104, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.648, 4.104, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.824, 4.104, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.824, 4.104, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.824, 4.104, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.596, 4.104, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.596, 4.104, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.596, 4.78591, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [1.596, 4.78591, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect1", 
        [["serp1", "out_fluid"], ["mix0", "b_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [0.228, 4.78591, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.228, 4.78591, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.228, 4.78591, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.228, 4.78591, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.228, 3.648, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.228, 3.648, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.648, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.648, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.648, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect2", 
        [["mix1", "a_fluid"], ["mix0", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [7.29809, 3.42, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.29809, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.29809, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 3.42, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 3.42, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 3.42, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.42, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.42, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.71809, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.71809, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.71809, 3.42, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect3", 
        [["serp3_1", "in_fluid"], ["serp3", "in_fluid"], ["serp2", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [3.64591, 6.612, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.64591, 6.61409, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.64591, 6.61409, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.64591, 6.612, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 6.612, 0.4], [0, [0, 0, 1]]]]
);
        polychannel_route("connect3", 
        [["serp3_1", "in_fluid"], ["serp3", "in_fluid"], ["serp2", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [0.23009, 6.612, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [0.23009, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [2.736, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [2.736, 6.612, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [2.736, 6.612, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [2.736, 6.612, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [2.736, 6.612, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.42, 6.612, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.64591, 6.612, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect41", 
        [["serp4", "in_fluid"], ["serp3", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [10.03409, 6.612, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.03409, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 6.612, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.26, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.612, 0.4], [0, [0, 0, 1]]]]
);
        polychannel_route("connect42", 
        [["serp4_1", "in_fluid"], ["serp3_1", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.156, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.156, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.156, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.905909999999999, 6.156, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.156, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.156, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [6.612, 6.612, 0.8], [0, [0, 0, 1]]]]
);
        polychannel_route("connect5", 
        [["serp4_1", "out_fluid"], ["serp4", "out_fluid"], ["mix1", "b_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [10.716, 3.6500899999999996, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.6500899999999996, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.876, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.716, 3.876, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 3.876, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 3.876, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 5.928, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 5.928, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.87409, 5.928, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.87409, 5.928, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.87409, 5.928, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 5.928, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 5.928, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.156, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.612, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.612, 0.8], [0, [0, 0, 1]]]]
);
        polychannel_route("connect5", 
        [["serp4_1", "out_fluid"], ["serp4", "out_fluid"], ["mix1", "b_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [16.872, 6.156, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.156, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [16.872, 6.156, 1.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect6", 
        [["serp5", "in_fluid"], ["mix1", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [10.485909999999999, 3.42, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.485909999999999, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.485909999999999, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 3.42, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 3.876, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 3.876, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 3.876, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 6.60991, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [10.488, 6.60991, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("out", 
        [["PIN", "out"], ["serp5", "out_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [11.4, 6.384, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.384, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.60991, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [13.224, 6.60991, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("soln1", 
        [["PIN", "soln1"], ["mix0", "a_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.42, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.42, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.42, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.42, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.065910000000001, 3.42, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 3.42, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 7.068, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.524, 7.068, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.98, 7.068, 1.8], [0, [0, 0, 1]]]]
);
        polychannel_route("soln2", 
        [["PIN", "soln2"], ["serp0", "in_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [4.104, 3.87809, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 3.87809, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 3.87809, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 3.87809, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [4.104, 5.7, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 5.7, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 5.7, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 7.068, 1.8], [0, [0, 0, 1]]]]
);
        polychannel_route("soln3", 
        [["PIN", "soln3"], ["serp2", "in_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 6.612, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 7.068, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [3.192, 7.068, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.892, 7.068, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.892, 7.068, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.892, 7.068, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.348, 7.068, 1.8], [0, [0, 0, 1]]]]
);
        
// Components
// mix0
diffmix_25px_0(xpos = 900.0, ypos = 420.0, zpos = 15, orientation = "FS");
// mix1
diffmix_25px_0(xpos = 1350.0, ypos = 420.0, zpos = 15, orientation = "S");
// serp0
serpentine_50px_0(xpos = 450.0, ypos = 420.0, zpos = 15, orientation = "S");
// serp1
serpentine_150px_0(xpos = 0.0, ypos = 420.0, zpos = 15, orientation = "S");
// serp2
serpentine_300px_2(xpos = 0.0, ypos = 840.0, zpos = 15, orientation = "FN");
// serp3
serpentine_300px_2(xpos = 900.0, ypos = 840.0, zpos = 15, orientation = "N");
// serp3_1
serpentine_300px_2(xpos = 450.0, ypos = 840.0, zpos = 15, orientation = "N");
// serp4
serpentine_300px_2(xpos = 1800.0, ypos = 840.0, zpos = 15, orientation = "N");
// serp4_1
serpentine_300px_2(xpos = 1800.0, ypos = 420.0, zpos = 15, orientation = "FS");
// serp5
serpentine_300px_0(xpos = 1350.0, ypos = 840.0, zpos = 15, orientation = "N");

    
    
// PINS
    polychannel_route("out", 
    ["PIN"], ["net", "out"],
[["cube", [0.1, 0.1, 0.1], [11.4, 6.384, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [11.4, 6.384, 1.8], [0, [0, 0, 1]]]]
);

    polychannel_route("soln1", 
    ["PIN"], ["net", "soln1"],
[["cube", [0.1, 0.1, 0.1], [7.98, 7.068, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.98, 7.068, 1.8], [0, [0, 0, 1]]]]
);

    polychannel_route("soln2", 
    ["PIN"], ["net", "soln2"],
[["cube", [0.1, 0.1, 0.1], [8.664, 7.068, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 7.068, 1.8], [0, [0, 0, 1]]]]
);

    polychannel_route("soln3", 
    ["PIN"], ["net", "soln3"],
[["cube", [0.1, 0.1, 0.1], [9.348, 7.068, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.348, 7.068, 1.8], [0, [0, 0, 1]]]]
);

} // end union
} // end difference

interconnect_32channel(1275.0, 795.0, 280);
