# Macro_Floorplanner

☕️ This project specifies the design and development of a small utility that gets a Verilog netlist, the library LEF file, a pin location
file, the core utilization as well as the aspect ratio to generate a floorplan and outputs a DEF file.

☕️ The DEF file output contains site positioning, die area, rows, components and pins. The components and netlist parts are parsed from the verilog netlist. A LEF parser https://github.com/trimcao/lef-parser was utilized to parse the input LEF to get the site information as well as the pin specifications.

☕️ The nets output is missing the components and pins they are attached to.
