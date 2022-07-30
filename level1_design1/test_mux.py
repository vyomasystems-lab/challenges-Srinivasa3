# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #dut.sel.value=0b00000
    dut.inp0.value=0b1
    await Timer(2, units='ns')
    dut._log.info(dut.inp0.value) 
    temp=0b1
    await Timer(2, units='ns')
    try :
        assert temp == dut.out.value, "success"
    except AssertionError:
        print ("FAIL Either slection or input is missing")
   ## else :
      ##  dut.sel.value=0b00000
     ##   dut.inp0.value=0b11
     ##   await Timer(2, units='ns')
    dut.sel.value=0b00000
    dut.inp0.value=0b0
    await Timer(2, units='ns')
    dut._log.info(dut.inp0.value) 
    temp=~temp
    await Timer(2, units='ns')
    print(temp)
    await Timer(2, units='ns')
    try :
        assert temp == dut.out.value, "success"
    except AssertionError:
        print ("FAIL Either slection or input is missing")



