# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.sel.value=0b00011;
    dut.inp3.value=0b11; 

    await Timer(2, units='ns')

    #cocotb.log.info('##### CTB: Develop your test here ########')
    dut._log.info(f'sel={int(dut.sel.value)}  inp={dut.inp+{int(dut.sel.value)}.value} out={dut.out.value}')
    assert dut.inp3.value == dut.out.value, "Error"
