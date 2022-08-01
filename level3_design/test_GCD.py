import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def GCD_test(dut):
    """Test for GCD 143 and 78"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    A=143
    B=78
    await FallingEdge(dut.clk)
    dut.Start.value=0b1
    await FallingEdge(dut.clk)
    dut.data_in.value=A
    dut.data_in.value=B
    dut._log.info(f"Inp = {dut.data_in.value} Out = {dut.A_out.value}")
    assert dut.A_out.value == 0b000, "Design is not working"
