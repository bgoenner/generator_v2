use <./h.r.3.3_pdk_merged.scad>
use <./polychannel_v2.scad>
use <./routing.scad>

px = 0.0076;
layer = 0.01;


difference() {
    %cube([2550*px,1590*px,280*layer]);
    union() {
polychannel_route("connect10", 
        ["serp10", "out_fluid"], ["mix0", "b_fluid"],
            [["cube", [0.1, 0.1, 0.1], [8.208, 7.74991, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.74991, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect20", 
        ["serp20", "out_fluid"], ["mix0", "a_fluid"],
            [["cube", [0.1, 0.1, 0.1], [8.208, 5.93009, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 5.93009, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 6.156, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 6.156, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.436, 6.156, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.436, 6.156, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.436, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.436, 7.296, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.296, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.296, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect_m0", 
        ["serp7", "in_fluid"], ["mix0", "out_fluid"],
            [["cube", [0.1, 0.1, 0.1], [9.576, 6.386089999999999, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.576, 6.386089999999999, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.576, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.576, 7.296, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.12, 7.296, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.12, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [9.12, 7.296, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.89409, 7.296, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.89409, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.89409, 7.296, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("out", 
        ["PIN", "out"], ["serp7", "out_fluid"],
            [["cube", [0.1, 0.1, 0.1], [7.296, 5.016, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 5.244, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 5.244, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 5.244, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 5.244, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 5.244, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 5.244, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 6.38191, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.664, 6.38191, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("soln1", 
        ["PIN", "soln1"], ["serp10", "in_fluid"],
            [["cube", [0.1, 0.1, 0.1], [7.296, 7.068, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.296, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.74991, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.74991, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("soln2", 
        ["PIN", "soln2"], ["serp20", "in_fluid"],
            [["cube", [0.1, 0.1, 0.1], [7.296, 5.93009, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 5.93009, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 0.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 1.0], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 1.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 1.4000000000000001], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 1.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.156, 1.8], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.384, 1.8], [0, [0, 0, 1]]]]
);
        
// Components
// mix0
diffmix_25px_0(xpos = 1110.0, ypos = 900.0, zpos = 15, orientation = "N");
// serp10
serpentine_100px_0(xpos = 930.0, ypos = 870.0, zpos = 15, orientation = "FS");
// serp20
serpentine_100px_0(xpos = 930.0, ypos = 630.0, zpos = 15, orientation = "FS");
// serp7
serpentine_100px_0(xpos = 1110.0, ypos = 690.0, zpos = 15, orientation = "S");

    
    // PINS
        polychannel_route("out", 
        ["PIN"], ["net", "out"],
[["cube", [0.1, 0.1, 0.1], [7.296, 5.016, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 5.016, 0.8], [0, [0, 0, 1]]]]
);

        polychannel_route("soln1", 
        ["PIN"], ["net", "soln1"],
[["cube", [0.1, 0.1, 0.1], [7.296, 7.068, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 7.068, 1.8], [0, [0, 0, 1]]]]
);

        polychannel_route("soln2", 
        ["PIN"], ["net", "soln2"],
[["cube", [0.1, 0.1, 0.1], [7.296, 6.384, 2.8000000000000003], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [7.296, 6.384, 1.8], [0, [0, 0, 1]]]]
);

        } // end union
        } // end difference
        
interconnect_32channel(1275.0, 795.0, 280);
