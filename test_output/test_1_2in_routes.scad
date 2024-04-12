polychannel_route("connect10", 
        [["serp10", "out_fluid"], ["mix0", "b_fluid"], ],
        [],
[["cube", [0.1, 0.1, 0.1], [8.208, 7.74991, 0.2], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.74991, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.208, 7.068, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.6], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.4], [0, [0, 0, 1]]],
 ["cube", [0.1, 0.1, 0.1], [8.661909999999999, 7.068, 0.2], [0, [0, 0, 1]]]]
);
        polychannel_route("connect20", 
        [["serp20", "out_fluid"], ["mix0", "a_fluid"], ],
        [],
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
        [["serp7", "in_fluid"], ["mix0", "out_fluid"], ],
        [],
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
        [["PIN", "out"], ["serp7", "out_fluid"], ],
        [],
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
        [["PIN", "soln1"], ["serp10", "in_fluid"], ],
        [],
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
        [["PIN", "soln2"], ["serp20", "in_fluid"], ],
        [],
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
        