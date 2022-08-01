# Seq_detect_1011 Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![image](https://user-images.githubusercontent.com/109664284/182092227-f7b15b25-06d5-44b5-a450-817094690cbf.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test(DUT - seq_detect_1011 module) which takes 1 bit input *inp_bit* at every negetive edge of the clock *clk* and the corresponding current state output *current_state* is observed in positive edge of clock. The whole operation carried out with active low *reset*.

The values are assigned to the input port using 
```
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.reset.value = 0
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1

```
The assert statement is used for comparing the mux's output to the expected value i.e. given input.

The following error is seen:
```
 assert dut.current_state.value == 0b001, "State Transition not working"
                     AssertionError: State Transition not working
```
```
assert dut.seq_seen.value == 0, "Design not proper"
                     AssertionError: Design not proper
```
## Failed Scenarios


## Test Scenario_01
- Test Inputs: reset=0 inp_bit=0,1,1
- Expected Output: seq_seen = 0, next_state = 001 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000

## Test Scenario_02
- Test Inputs: reset=0 inp_bit=0,1,0,0,1,0,1,0
- Expected Output: seq_seen = 0, next_state = 010 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000

## Test Scenario_03
- Test Inputs: reset=0 inp_bit=0,1,0,0,1,0,1,1,1
- Expected Output: seq_seen = 0, next_state = 001 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   === BUG
        else
          next_state = SEQ_10;
      end
 ....
 ....
 SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;  === BUG
      end
  ....
  ....
  SEQ_1011:
      begin
        next_state = IDLE;   === BUG
      end
 
```
In the always block of sequence detector design, three invalid transition of states are identified. 
1. In the state *SEQ_1* if we give input bit again as "1" then the next state moved to *IDLE* but it as per expected it should remains in the same state i.e. *SEQ_1*.
2. In the state *SEQ_101* if we give input bit again as "0" then the next state moved to *IDLE* but it as per expected it should moved to *SEQ_10*.
3. In the state *SEQ_1011* for both the give input state moved to *IDLE* which is invalid. for input "1" it has to move to *SEQ_1* state and for "0" move to *IDLE* state.

## Design Fix

Failed design file seq_detect_1011.v

![image](https://user-images.githubusercontent.com/109664284/182150696-e80c5250-bbb5-45c9-a5e4-75d8cf72f1da.png)

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109664284/182150623-efc79284-55c8-4e95-9d8b-8317edd4649c.png)

The updated design is checked in as seq_detect_1011_pass.v
