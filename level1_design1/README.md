# Multiplexer 31:1 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![image](https://user-images.githubusercontent.com/109664284/182092227-f7b15b25-06d5-44b5-a450-817094690cbf.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test(DUT - mux module) which takes in 5-bit selection line *sel* and 2-bit input lines *inp0-inp30* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.sel.value = 0b01101
dut.inp13.value = 0b11

```
The assert statement is used for comparing the mux's output to the expected value i.e. given input.

The following error is seen:
```
 assert dut.inp13.value == dut.out.value, f"Output and the Input doesn't matching for the same selection line . Sel = ({dut.sel.value}) Inp = {(dut.inp13.value)} Out = {(dut.out.value)}"
                     AssertionError: Output and the Input doesn't matching for the same selection line . Sel = (01101) Inp = 11 Out = 10
```
## Failed Scenarios


## Test Scenario_01
- Test Inputs: sel=0b01100, inp12=0b10
- Expected Output: out=0b10
- Observed Output in the DUT dut.out=0b00

## Test Scenario_02
- Test Inputs: sel=0b01101, inp13=0b11
- Expected Output: out=0b11
- Observed Output in the DUT dut.out=0b10

## Test Scenario_03
- Test Inputs: sel=0b11110, inp30=0b10
- Expected Output: out=0b10
- Observed Output in the DUT dut.out=0b00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      ...
      ...
      ...
      5'b01101: out = inp12           ====> BUG
      5'b01101: out = inp13           ====> BUG
      ...
      ...
      5'b11101: out = inp29;          ====> BUG
      default: out = 0;
    endcase
  end
  
```
In the always block of mux design, the selection line 5'b01101 is assigned with two input lines inp12 and inp13, full case description is not done in the design, selection line 5'b01100 and 5'b11110 are not defined.
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.

## Design Fix

Failed design file mux.v

![image](https://user-images.githubusercontent.com/109664284/182104544-fea20dcb-b844-4deb-ac7c-78c0140408b8.png)

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109664284/182103841-d29f30b6-d9c3-4b72-8b8f-336198846c16.png)

The updated design is checked in as mux_fixed.v
