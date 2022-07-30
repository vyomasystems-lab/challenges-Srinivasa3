# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #dut.sel.value=0b00000
    dut.inp0.value=0b11
    await Timer(2, units='ns')
    if dut.inp0.value == dut.out.value :
        print("PASS")
    else:
        print("FAIL Either slection or input is missing")

