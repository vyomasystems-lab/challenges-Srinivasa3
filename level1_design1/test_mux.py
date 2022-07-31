# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer



@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.sel.value = 0b00001
    dut.inp2.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp2.value)}, DUT={(dut.out.value)}')
    assert dut.inp2.value == dut.out.value, "Output is not matching"
@cocotb.test()
async def test_mux(dut):
    """Test for mux0"""
    dut.sel.value = 0b00000
    dut.inp0.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp0.value)}, DUT={(dut.out.value)}')
    assert dut.inp0.value == dut.out.value, "Output is not matching"
