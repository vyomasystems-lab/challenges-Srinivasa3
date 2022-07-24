# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.sel.value=0b00011;
    dut.inp3.value=0b11; 

    #cocotb.log.info('##### CTB: Develop your test here ########')
    dut._log.info(f'sel={dut.sel.value:05}  inp={dut.inp3.value:05} out={dut.out.value:05}')
    assert dut.inp3.value == dut.out.value, "Error"
