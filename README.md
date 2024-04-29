# SCAD generator V2

A redevelopment of a verilog/def to SCAD converter for the OpenMFDA project. Was developed as a coding exercise but has become a pretty robust set of code.

### Improvements from previous version
- Calls the TLEF file for some definitions, the effort is to pull from the geometric definitions used in OpenROAD to reduce the amount of redundent variables.
- Implements the polychannel from the Dr. Gregory Nordin which a much more robust channel router
- Better annotations in the SCAD file. Allowing for better post PnR debugging and understanding of generated geometry.

### Design paradigm
The code is developed keeping in mind with the development of two interacting definitions 
- "platform" which defines most (if not all) constrains around the chip such as I/O locations, placement area, amount of routing layers, etc.
- "design" which is the netlist of components to be placed (defined elsewhere). 

All components will need a LEF and SCAD pairing which require manual validation.

Arguments
--platform
Name of the platform to build the design around

--design
Name of the design file, usually the top verilog module

--def_file
Final output of the OpenROAD flow for the OpenMFDA project

--results_dir
Where to place all generated files.

--px
The descrete pixel size of the target 3D printer, usually fixed in size for the printer.

--layer
The descrete layer height of the target 3D printer, this is more variable for an SLA printer.

--bottom_layer
Number of layers to seperate the final routing/placement layer and the edge of the device.

--lpv (layer per via)
Number of layers to sperate each routing layer when a via is made. Routing will not account for any added channel heights when routing or rendering.

--xbulk
X dimmesion of device, this is not PnR area.

--ybulk
Y dimmesion of device, this is not PnR area.

--zbulk
Z dimmesion of device, does not take into account bottom_layer

--xchip
Held over from previous code, unused.

--ychip
Held over from previous code, unused.

--def_scale
units to scale def_file. In the tests 1000 is used since def is in microns and rendered files are in mm.

--pitch
Wire pitch of device, this is defined elsewhere for PnR. Changing this will have no effect.

--res
SCAD render smoothness for curves, spheres and cylinders.

--dimm_file
Optional file to selectively change routing channel definitions. (Not implemented yet)  

--tlef
Tech LEF file for platform definitions

--comp_file
Verilog file to get components.

--pin_file
File used to declare direction to render I/O pins. More generaic definition to allow for side defintion I/Os. (Not required if all I/Os are on top)
