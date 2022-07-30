# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    # temp=0b11
    def call(temp,x,y):
            if temp==0b00:
                temp=0b11
            else:
                temp=0b00
            try :
                assert temp == dut.out.value, "success"
            except AssertionError:
                print ("FAILTEST case :  SELECTION ={x} INPUT ={y} OUTPUT ={dut.out.value} ")
            return temp
            
   ##         await Timer(2, units='ns')
    
    dut.sel.value=0b00000
    dut.inp0.value=0b00
    temp=0b11
    await Timer(2, units='ns')
    temp=call(temp,dut.sel.value,dut.inp0.value)
    dut.sel.value=0b00001
    dut.inp1.value=0b11
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00010
    dut.inp2.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00011
    dut.inp3.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b00100
    dut.inp4.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00101
    dut.inp5.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b00110
    dut.inp6.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b00111
    dut.inp7.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01000
    dut.inp8.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01001
    dut.inp9.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01010
    dut.inp10.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01011
    dut.inp11.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01100
    dut.inp12.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01101
    dut.inp13.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b01110
    dut.inp14.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b01111
    dut.inp15.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10000
    dut.inp16.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10001
    dut.inp17.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10010
    dut.inp18.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10011
    dut.inp19.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10100
    dut.inp20.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10101
    dut.inp21.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b10110
    dut.inp22.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b10111
    dut.inp23.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11000
    dut.inp24.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11001
    dut.inp25.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11010
    dut.inp26.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11011
    dut.inp27.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11100
    dut.inp28.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    dut.sel.value=0b11101
    dut.inp29.value=0b11
    await Timer(2, units='ns')
    temp=call(temp) 
    dut.sel.value=0b11110
    dut.inp30.value=0b00
    await Timer(2, units='ns')
    temp=call(temp)
    

