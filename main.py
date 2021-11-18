# import hdlparse.verilog_parser as vlog
# # generate random integer values
# from random import seed
# from random import randint
# # seed random number generator
# seed(1)
import linecache
#
MODULE_PATH = "/Users/rawansameh/Desktop/pythonProject1/TestFiles/spm.synthesis.v"
path = "./Users/rawansameh/Desktop/pythonProject1/libraries/ProjectFiles/TestLEF.lef"
Comp = []
path_pin = "/Users/rawansameh/Desktop/spm.pin.lef"
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

    wires =[]
    inputs ={}
    outputs = {}
    for line in lines:
        line = line.strip()
        if line.find("wire") != -1:
            semicolonLoc = line.find(";")
            # wirename = wire
            # line = line.split(" ")
            wires.append(line[5:semicolonLoc])


  #This is for the Nets and Pins:
        if line.startswith("input"):
            semicolonLoc = line.find(";")
            b1 = line.find('[')
            b2 = line.find(']')
            c = line.find(':')
            if line.find('[') != -1:
                var = line[b1 + 1:c]
                line = line.replace(line[b1 - 1:b2 + 1], "")
                semicolonLoc2 = line.find(";")
                inputs[line[6:semicolonLoc2]] = var
            else:
                inputs[line[6:semicolonLoc]] = 0

        if line.find("output") != -1:
            semicolonLoc = line.find(";")
            b1 = line.find('[')
            b2 = line.find(']')
            c = line.find(':')
            if line.find('[') != -1:
                var = line[b1 + 1:c]
                line = line.replace(line[b1 - 1:b2 + 1], "")
                semicolonLoc2 = line.find(";")
                outputs[line[6:semicolonLoc2]] = var
            else:
                outputs[line[6:semicolonLoc]] = 0

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


    file2 = open(path_pin, 'rt')
    lines1 = file2.readlines()
    file2.close()
    pinsNorth= []
    LayersNorth = []

    pinsSouth = []
    LayersSouth = []

    for line1 in lines1:
        if line1.startswith("#N"):
            pass
        elif line1.startswith("#S"):
            break
        else:
            comma = line1.find(',')
            b11 = line1.find(']')
            b22 = line1.find(';')
            if line1.find(']') != -1:
                pinsNorth.append(line1[:b11+1:])
                LayersNorth.append(line1[comma+2:b22])
            else:
                pinsNorth.append(line1[:comma])
                LayersNorth.append(line1[comma + 2:b22])

    countS = 0
    for j in lines1:
        if j.find("#S")!= -1:
            break
        else:
            countS += 1


    for line4 in lines1:
        pinsSouth.append(lines1[countS+1])
        countS+=1
        if lines1[countS+1].startswith("#E"):
            break

    pinsSouth2 = []
    for x in pinsSouth:
        comma = x.find(',')
        b11 = x.find(']')
        b22 = x.find(';')
        # if x.find(']') != -1:
        LayersSouth.append(x[comma+2:b22])
        pinsSouth2.append(x.replace(x[comma:b22+2], " "))
        # else:
        #     LayersSouth.append(x[comma + 2:b22])
        #     pinsSouth = pinsSouth.replace(x[comma::], "")


    # pinEast = []
    # LayerEast = []
    #





parse()



