# import hdlparse.verilog_parser as vlog
# # generate random integer values
# from random import seed
# from random import randint
# # seed random number generator
# seed(1)
#
MODULE_PATH = "TestFiles/spm.synthesis.v"
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


def parse():
    file = open(MODULE_PATH, 'rt')
    lines = file.readlines()
    file.close()


    print('Components')
    for line in lines:
        line = line.strip()
        if line.find("wire") != -1:
            semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
            #print(line[5:semicolonLoc])

        if line.find("input") != -1:
            semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
            #print(line[6:semicolonLoc])

        if line.find("output") != -1:
            semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
           # print(line[6:semicolonLoc])



        if line.find("sky130") != -1:
            # print(line[0:line.find(" (")])
            line = line[0:line.find(" (")]
            line = line.split(" ")[::-1]
            print(line[0]+ " " + line[1])

        # if line.find("sky130" and "." and ";") != -1:
            # print(line[0:line.find(" (")])




parse()

# for c in vhdl_comps:
#     print('Component "{}":'.format(c.name))

