# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    dut._log.info(f'clk={dut.clk.value}')
    dut._log.info(f'rst={dut.reset.value}')

    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}") 

    

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    dut._log.info(f"seq seen at i/p 1={dut.seq_seen.value}")
    assert dut.current_state.value == dut.SEQ_1.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_1.value}"
    
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    dut._log.info(f"seq seen at i/p 10={dut.seq_seen.value}")
    assert dut.current_state.value == dut.SEQ_10.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_10.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    dut._log.info(f"seq seen at i/p101={dut.seq_seen.value}")
    assert dut.current_state.value == dut.SEQ_101.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_101.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    dut._log.info(f"seq seen at i/p1011={dut.seq_seen.value}")
    assert dut.current_state.value == dut.SEQ_1011.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_1011.value}"


    
