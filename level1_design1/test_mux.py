# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    # temp=0b11
    def call(temp):
            if temp==0b00:
                temp=0b11
            else:
                temp=0b00
            try :
                assert temp == dut.out.value, "success"
            except AssertionError:
                print ("FAIL:  input missing")
            return temp
            
   ##         await Timer(2, units='ns')
    
    dut.sel.value=0b00000
    dut.inp0.value=0b00
    temp=0b11
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00001
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00010
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00011
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b00100
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00101
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b00110
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00111
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01000
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01001
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01010
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01011
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01100
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01101
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01110
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01111
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10000
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10001
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10010
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10011
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10100
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10101
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10110
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10111
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11000
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11001
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11010
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11011
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11100
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11101
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11110
    dut.inp0.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    

