# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux00(dut):
    """Test for mux0"""
    dut.sel.value = 0b00000
    dut.inp0.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp0.value)}, DUT={(dut.out.value)}')
    assert dut.inp0.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux01(dut):
    """Test for mux1"""
    dut.sel.value = 0b00001
    dut.inp1.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp1.value)}, DUT={(dut.out.value)}')
    assert dut.inp1.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux02(dut):
    """Test for mux2"""
    dut.sel.value = 0b00010
    dut.inp2.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp2.value)}, DUT={(dut.out.value)}')
    assert dut.inp2.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux03(dut):
    """Test for mux3"""
    dut.sel.value = 0b00011
    dut.inp3.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp3.value)}, DUT={(dut.out.value)}')
    assert dut.inp3.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux04(dut):
    """Test for mux4"""
    dut.sel.value = 0b00100
    dut.inp4.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp4.value)}, DUT={(dut.out.value)}')
    assert dut.inp4.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux05(dut):
    """Test for mux5"""
    dut.sel.value = 0b00101
    dut.inp5.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp5.value)}, DUT={(dut.out.value)}')
    assert dut.inp5.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux06(dut):
    """Test for mux6"""
    dut.sel.value = 0b00110
    dut.inp6.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp6.value)}, DUT={(dut.out.value)}')
    assert dut.inp6.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux07(dut):
    """Test for mux7"""
    dut.sel.value = 0b00111
    dut.inp7.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp7.value)}, DUT={(dut.out.value)}')
    assert dut.inp7.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux08(dut):
    """Test for mux8"""
    dut.sel.value = 0b01000
    dut.inp8.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp8.value)}, DUT={(dut.out.value)}')
    assert dut.inp8.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux09(dut):
    """Test for mux9"""
    dut.sel.value = 0b01001
    dut.inp9.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp9.value)}, DUT={(dut.out.value)}')
    assert dut.inp9.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux10(dut):
    """Test for mux10"""
    dut.sel.value = 0b01010
    dut.inp10.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp10.value)}, DUT={(dut.out.value)}')
    assert dut.inp10.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux11(dut):
    """Test for mux11"""
    dut.sel.value = 0b01011
    dut.inp11.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp11.value)}, DUT={(dut.out.value)}')
    assert dut.inp11.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux12(dut):
    """Test for mux12"""
    dut.sel.value = 0b01100
    dut.inp12.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp12.value)}, DUT={(dut.out.value)}')
    assert dut.inp12.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux13(dut):
    """Test for mux13"""
    dut.sel.value = 0b01101
    dut.inp13.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp13.value)}, DUT={(dut.out.value)}')
    assert dut.inp13.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux14(dut):
    """Test for mux14"""
    dut.sel.value = 0b01110
    dut.inp14.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp14.value)}, DUT={(dut.out.value)}')
    assert dut.inp14.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux15(dut):
    """Test for mux15"""
    dut.sel.value = 0b01111
    dut.inp15.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp15.value)}, DUT={(dut.out.value)}')
    assert dut.inp15.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux16(dut):
    """Test for mux16"""
    dut.sel.value = 0b10000
    dut.inp16.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp16.value)}, DUT={(dut.out.value)}')
    assert dut.inp16.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux17(dut):
    """Test for mux17"""
    dut.sel.value = 0b10001
    dut.inp17.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp17.value)}, DUT={(dut.out.value)}')
    assert dut.inp17.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux18(dut):
    """Test for mux18"""
    dut.sel.value = 0b10010
    dut.inp18.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp18.value)}, DUT={(dut.out.value)}')
    assert dut.inp18.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux19(dut):
    """Test for mux19"""
    dut.sel.value = 0b10011
    dut.inp19.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp19.value)}, DUT={(dut.out.value)}')
    assert dut.inp19.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux20(dut):
    """Test for mux20"""
    dut.sel.value = 0b10100
    dut.inp20.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp20.value)}, DUT={(dut.out.value)}')
    assert dut.inp20.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux21(dut):
    """Test for mux21"""
    dut.sel.value = 0b10101
    dut.inp21.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp21.value)}, DUT={(dut.out.value)}')
    assert dut.inp21.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux22(dut):
    """Test for mux22"""
    dut.sel.value = 0b10110
    dut.inp22.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp22.value)}, DUT={(dut.out.value)}')
    assert dut.inp22.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux23(dut):
    """Test for mux23"""
    dut.sel.value = 0b10111
    dut.inp23.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp23.value)}, DUT={(dut.out.value)}')
    assert dut.inp23.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux24(dut):
    """Test for mux24"""
    dut.sel.value = 0b11000
    dut.inp24.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp24.value)}, DUT={(dut.out.value)}')
    assert dut.inp24.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux25(dut):
    """Test for mux25"""
    dut.sel.value = 0b11001
    dut.inp25.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp25.value)}, DUT={(dut.out.value)}')
    assert dut.inp25.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux26(dut):
    """Test for mux26"""
    dut.sel.value = 0b11010
    dut.inp26.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp26.value)}, DUT={(dut.out.value)}')
    assert dut.inp26.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux27(dut):
    """Test for mux27"""
    dut.sel.value = 0b11011
    dut.inp27.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp27.value)}, DUT={(dut.out.value)}')
    assert dut.inp27.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux28(dut):
    """Test for mux28"""
    dut.sel.value = 0b11100
    dut.inp28.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp28.value)}, DUT={(dut.out.value)}')
    assert dut.inp28.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux29(dut):
    """Test for mux29"""
    dut.sel.value = 0b11101
    dut.inp29.value = 0b11
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp29.value)}, DUT={(dut.out.value)}')
    assert dut.inp29.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux30(dut):
    """Test for mux30"""
    dut.sel.value = 0b11110
    dut.inp30.value = 0b10
    await Timer(2, units='ns')
    dut._log.info(f'Sel = {(dut.sel.value)} Input= {(dut.inp30.value)}, DUT={(dut.out.value)}')
    assert dut.inp30.value == dut.out.value, "Output is not matching"