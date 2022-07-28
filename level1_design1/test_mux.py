# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    inp_line=[]
    
    i0=dut.inp0.value=random.randint(0, 3)
    inp_line.append(i0)
    i1=dut.inp1.value=random.randint(0, 3)
    inp_line.append(i1)
    i2=dut.inp2.value=random.randint(0, 3)
    inp_line.append(i2)
    i3=dut.inp3.value=random.randint(0, 3)
    inp_line.append(i3)
    i4=dut.inp4.value=random.randint(0, 3)
    inp_line.append(i4)
    i5=dut.inp5.value=random.randint(0, 3)
    inp_line.append(i5)
    i6=dut.inp6.value=random.randint(0, 3)
    inp_line.append(i6)
    i7=dut.inp7.value=random.randint(0, 3)
    inp_line.append(i7)
    i8=dut.inp8.value=random.randint(0, 3)
    inp_line.append(i8)
    i9=dut.inp9.value=random.randint(0, 3)
    inp_line.append(i9)
    i10=dut.inp10.value=random.randint(0, 3)
    inp_line.append(i10)
    i11=dut.inp11.value=random.randint(0, 3)
    inp_line.append(i11)
    i12=dut.inp12.value=random.randint(0, 3)
    inp_line.append(i12)
    i13=dut.inp13.value=random.randint(0, 3)
    inp_line.append(i13)
    i14=dut.inp14.value=random.randint(0, 3)
    inp_line.append(i14)
    i15=dut.inp15.value=random.randint(0, 3)
    inp_line.append(i15)
    i16=dut.inp16.value=random.randint(0, 3)
    inp_line.append(i16)
    i17=dut.inp17.value=random.randint(0, 3)
    inp_line.append(i17)
    i18=dut.inp18.value=random.randint(0, 3)
    inp_line.append(i18)
    i19=dut.inp19.value=random.randint(0, 3)
    inp_line.append(i19)
    i20=dut.inp20.value=random.randint(0, 3)
    inp_line.append(i20)
    i21=dut.inp21.value=random.randint(0, 3)
    inp_line.append(i21)
    i22=dut.inp22.value=random.randint(0, 3)
    inp_line.append(i22)
    i23=dut.inp23.value=random.randint(0, 3)
    inp_line.append(i23)
    i24=dut.inp24.value=random.randint(0, 3)
    inp_line.append(i24)
    i25=dut.inp25.value=random.randint(0, 3)
    inp_line.append(i25)
    i26=dut.inp26.value=random.randint(0, 3)
    inp_line.append(i26)
    i27=dut.inp27.value=random.randint(0, 3)
    inp_line.append(i27)
    i28=dut.inp28.value=random.randint(0, 3)
    inp_line.append(i28)
    i29=dut.inp29.value=random.randint(0, 3)
    inp_line.append(i29)
    i30=dut.inp30.value=random.randint(0, 3)
    inp_line.append(i30)

    cocotb.log.info('##### CTB: Develop your test here ########')
    sel_line=[]

    for a in range(0,30):
        
        dut.sel.value = a
        
        await Timer(1, units='ns')
        
        dut._log.info(f'sel={dut.sel.value}')
        print("****************** input=",inp_line[a])
        dut._log.info(f'output = {dut.out.value}',)
        print("==============================================================================")
        count=a
        assert inp_line[a] == dut.out.value, "Test failed with: sel={SEL} ,input= {IN} ,output= {OUT} , In case statement line number ={C} ".format(
        SEL=dut.sel.value,IN=inp_line[a], OUT=dut.out.value,C=count+1)
    
        
    
       
        
       
       





