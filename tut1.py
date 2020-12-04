#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pygmyhdl import *clk = Wire(name='clk')  # This is a single-bit signal that carries the clock input.
led = Wire(name='led')  # This is another single-bit signal that receives the LED output.


# In[2]:


initialize()


# In[3]:


# The following function will define a chunk of logic, hence the @chunk decorator precedes it.
# The blinker logic takes three inputs:
#   clk_i:  This is a clock signal input.
#   led_o:  This is an output signal that drives an LED on and off.
#   length: This is the number of bits in the counter that generates the led_o output.
@chunk
def blinker(clk_i, led_o, length):
    
    # Define a multi-bit signal (or bus) with length bits.
    # Assign it a display name of 'cnt' for use during simulation.
    cnt = Bus(length, name='cnt')
    
    # Define a piece of sequential logic. Every time there is a positive
    # edge on the clock input (i.e., it goes from 0 -> 1), the value of
    # cnt is increased by 1. So over a sequence of clock pulses, the
    # cnt value will progress 0, 1, 2, 3, ...
    @seq_logic(clk_i.posedge)
    def counter_logic():
        cnt.next = cnt + 1

    # This is a piece of simple combinational logic. It just connects the
    # most significant bit (MSB) of the counter to the LED output.
    @comb_logic
    def output_logic():
        led_o.next = cnt[length-1]


# In[4]:


clk = Wire(name='clk')  # This is a single-bit signal that carries the clock input.
led = Wire(name='led')  # This is another single-bit signal that receives the LED output.


# In[5]:


blinker(clk_i=clk, led_o=led, length=3);  # Attach the clock and LED signals to a 3-bit blinker circuit.


# In[6]:


clk_sim(clk, num_cycles=16)  # Pulse the clock input 16 times.


# In[7]:


show_waveforms()


# In[8]:


show_text_table()


# In[9]:


toVerilog(blinker, clk_i=clk, led_o=led, length=22) # Give it the function name, signal connections, and counter size.


# In[10]:


print(open('blinker.v').read())


# In[11]:


with open('blinker.pcf', 'w') as pcf:
    pcf.write(
'''
set_io led_o 99
set_io clk_i 21
'''
    )


# In[12]:


get_ipython().system('yosys -q -p "synth_ice40 -blif blinker.blif" blinker.v')


# In[13]:


get_ipython().system('arachne-pnr -q -d 1k -p blinker.pcf blinker.blif -o blinker.asc')


# In[14]:


get_ipython().system('icepack blinker.asc blinker.bin')


# In[ ]:




