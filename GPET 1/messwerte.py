from praktikum import *
var_rm = resourceManager()
var_instrlist = instr find(var_rm)
var_instr = connect Instrument(var_rm, "ASRL6::INSTR")
var_read = query cmd(var instr,"READ?")
print var_read
close Instrument(var_instr)
close ResourceManager(var_rm)