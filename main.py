# import hdlparse.verilog_parser as vlog
# # generate random integer values
# from random import seed
# from random import randint
# # seed random number generator
# seed(1)
#
MODULE_PATH = "/Users/rawansameh/Desktop/pythonProject1/TestFiles/spm.synthesis.v"
path = "./libraries/ProjectFiles/TestLEF.lef"
Comp = []

#
# # HDL Parse Declarations
# vlog_ex = vlog.VerilogExtractor()
# vlog_mods = vlog_ex.extract_objects_from_source(MODULE_PATH)
# # vhdl_comps = vlog_ex.extract_objects(MODULE_PATH, vlog)
#
# with open(MODULE_PATH, 'rt') as fh:
#     code = fh.read()
# vlog_mods = vlog_ex.extract_objects(MODULE_PATH)
#
# print('\n')
#
# for m in vlog_mods:
#     print('Module {}'.format(m.name))
#     for p in m.ports:
#         if p.mode == 'input':
#             print('\t{:8}{};'.format("reg", p.name))
#         else:
#             print('\t{:8}{};'.format("wire", p.name))

class Net:
    def __init__(self, port, comp_name):
        self.port = port
        self.comp_name = comp_name
        # self.pin = pin

    def print_net(self):
        print("\t - ", self.port, " ( ", self.comp_name, " ", " )", " + USE SIGNAL ;")


def parse():
    file = open(MODULE_PATH, 'rt')
    lines = file.readlines()
    file.close()

    wires =[]
    inputs ={}

    for line in lines:
        line = line.strip()
        if line.find("wire") != -1:
            semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
            wires.append(line[5:semicolonLoc])


  #This is for the Nets and Pins:
        #if line.find("input") != -1:
           # semicolonLoc = line.find(";")
            #wirename = wire
            #line = line.split(" ")
            #inputs[line[6:semicolonLoc]] = 0

        # if line.find("output") != -1:
        #     semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
        # print(line[6:semicolonLoc])
        if line.startswith("module"):
            bracket = line.find("(")
            global module_name
            module_name = line[7:bracket]
        if line.find("sky130") != -1:
            # print(line[0:line.find(" (")])
            line = line[0:line.find(" (")]
            line = line.split(" ")[::-1]
            Comp.append(line[0] + " " + line[1])
            # print(line[0] + " " + line[1])


    print("COMPONENTS %d ;" % len(Comp))
    for x in Comp:
        print("\t - %s" % x)
    print ("END COMPONENTS")


parse()



