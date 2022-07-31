# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    def call(x,y):
            try :
                assert y == dut.out.value, "success"
                print (f"SELECTION ={x} INPUT ={y} OUTPUT ={dut.out.value} ")
            except AssertionError:
                print (f"FAILTEST case :  SELECTION ={x} INPUT ={y} OUTPUT ={dut.out.value} ")
                dut.out.value=0b00
            
   ##         await Timer(2, units='ns')
    
    dut.sel.value=0b00000
    dut.inp0.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp0.value)
    dut.sel.value=0b00001
    dut.inp1.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp1.value)
    dut.sel.value=0b00010
    dut.inp2.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp2.value)
    dut.sel.value=0b00011
    dut.inp3.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp3.value)
    dut.sel.value=0b00100
    dut.inp4.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp4.value)
    dut.sel.value=0b00101
    dut.inp5.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp5.value)
    dut.sel.value=0b00110
    dut.inp6.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp6.value)
    dut.sel.value=0b00111
    dut.inp7.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp7.value) 
    dut.sel.value=0b01000
    dut.inp8.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp8.value)
    dut.sel.value=0b01001
    dut.inp9.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp9.value) 
    dut.sel.value=0b01010
    dut.inp10.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp10.value)
    dut.sel.value=0b01011
    dut.inp11.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp11.value)
    dut.sel.value=0b01100
    dut.inp12.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp12.value)
    dut.sel.value=0b01101
    dut.inp13.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp13.value) 
    dut.sel.value=0b01110
    dut.inp14.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp14.value)
    dut.sel.value=0b01111
    dut.inp15.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp15.value)
    dut.sel.value=0b10000
    dut.inp16.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp16.value)
    dut.sel.value=0b10001
    dut.inp17.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp17.value)
    dut.sel.value=0b10010
    dut.inp18.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp18.value)
    dut.sel.value=0b10011
    dut.inp19.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp19.value) 
    dut.sel.value=0b10100
    dut.inp20.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp20.value)
    dut.sel.value=0b10101
    dut.inp21.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp21.value)
    dut.sel.value=0b10110
    dut.inp22.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp22.value)
    dut.sel.value=0b10111
    dut.inp23.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp23.value) 
    dut.sel.value=0b11000
    dut.inp24.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp24.value)
    dut.sel.value=0b11001
    dut.inp25.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp25.value)
    dut.sel.value=0b11010
    dut.inp26.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp26.value)
    dut.sel.value=0b11011
    dut.inp27.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp27.value) 
    dut.sel.value=0b11100
    dut.inp28.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp28.value)
    dut.sel.value=0b11101
    dut.inp29.value=0b00
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp29.value) 
    dut.sel.value=0b11110
    dut.inp30.value=0b11
    await Timer(2, units='ns')
    call(dut.sel.value,dut.inp30.value)
    

