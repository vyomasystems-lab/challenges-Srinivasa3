# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_reset_test(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk) 
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state.value} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b000, "Reset function is not working" 
    assert dut.seq_seen.value == 0, "Design not proper"

@cocotb.test()
async def test_SEQ_1(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.reset.value = 0
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk) 
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state.value} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b000, "State Transition not working" 
    assert dut.seq_seen.value == 0, "Design not proper"

@cocotb.test()
async def test_SEQ_2(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.reset.value = 0
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state.value} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b001, "State Transition not working" 
    assert dut.seq_seen.value == 0, "Design not proper"

@cocotb.test()
async def test_SEQ_3(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.reset.value = 0
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state.value} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b001, "State Transition not working" 
    assert dut.seq_seen.value == 0, "Design not proper"

@cocotb.test()
async def test_SEQ_4(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.reset.value = 0
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state.value} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b010, "State Transition not working" 
    assert dut.seq_seen.value == 0, "Design not proper"