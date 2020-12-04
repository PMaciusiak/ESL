// File: pwm_simple.v
// Generated by MyHDL 0.11
// Date: Fri Dec  4 21:11:39 2020


`timescale 1ns/10ps

module pwm_simple (
    clk_i,
    pwm_o,
    threshold
);
// Inputs:
//     clk_i: PWM changes state on the rising edge of this clock input.
//     threshold: Bit-length determines counter width and value determines when output goes low.
// Outputs:
//     pwm_o: PWM output starts and stays high until counter > threshold and then output goes low.

input clk_i;
output pwm_o;
wire pwm_o;
input [7:0] threshold;

reg [7:0] cnt;




assign pwm_o = (cnt < threshold);


always @(posedge clk_i) begin: PWM_SIMPLE_LOC_INSTS_CHUNK_INSTS_K
    cnt <= (cnt + 1);
end

endmodule
