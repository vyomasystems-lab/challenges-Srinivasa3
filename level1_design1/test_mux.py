# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    def call():
    if temp==0b00:
        temp=0b11
    else:
        temp=0b00
    await Timer(2, units='ns')
    try :
        assert temp == dut.out.value, "success"
    except AssertionError:
        print ("FAIL Either slection or input is missing")
    dut.sel.value=0b00000
    dut.inp0.value=0b11
    await Timer(2, units='ns')
    call()



