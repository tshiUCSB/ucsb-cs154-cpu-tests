# CMPSC 154: PyRTL CPU Unit Tests
A unit testing framework for guaranteeing correctness of the CMPSC 154 PyRTL CPU implementation
## Using the Framework
- Download the unit testing framework to your computer
- Copy your `cpu.py` file to the root directory (alongside `testbench.py`)
- Run `testbench.py` with python3
```
python3 testbench.py
```
## The /tests/ Directory
- Every test in `testbench.py` has a corresponding test in `/tests/` called `testname.s`
- Every `*.s` file has a first (commented) line which encodes the instructions in base64, serialized with JSON
- The assembly code used for every test will follow after that initial line
- NOTE: Some of the assembly instructions were assembled by hand, since some assemblers don't like negatives or `lui`

## Testing Methodology
The tests are structured in such a way that passing earlier tests are preconditions for the later tests. If you fail
a test that comes sooner, several of the following tests might fail or be inaccurate. The immediate instructions,
for instance, are vital for the rest of the tester suite, so if those tests don't pass, the rest of the tests are 
compromised.

## Edge Cases
The following are edge cases that can be found with the framework
- `slt` is a signed operation, so `0xFFFFFFFF < 0x00000000`
- `ori` is zero-extended, so immediate `0xFFFF` should yield `0x0000FFFF`
- `$zero` is a read-only register, so it should never change even when it's the write destination

## Sample Output
```
--------------LOAD_IMMEDIATE_VALUE--------------
PASSED: [test_lui] $t1 == 1798635520
PASSED: [test_ori] $v0 == 6573
PASSED: [test_addi] $v0 == 6573
PASSED: [test_ori_negative] $s5 == 55117
PASSED: [test_addi_negative] $s5 == -10419
PASSED: [test_ori_lui] $s1 == 3546218496
PASSED: [test_lui_ori] $s1 == 3546228915

--------------ADD_IMMEDIATE--------------
PASSED: [test_addi_pp] $v0 == 32
PASSED: [test_addi_same] $v0 == 0
PASSED: [test_addi_nn] $v0 == -32
PASSED: [test_addi_np] $v0 == 2
PASSED: [test_addi_pn] $v0 == -2

--------------ADD_REGISTERS--------------
PASSED: [test_add_pp] $v0 == 318
PASSED: [test_add_same] $v0 == 0
PASSED: [test_add_nn] $v0 == -318
PASSED: [test_add_np] $v0 == -110
PASSED: [test_add_pn] $v0 == 110

--------------SET_LESS_THAN--------------
PASSED: [test_slt_pp_1] (254 < 10419) == 1
PASSED: [test_slt_pp_2] (10419 < 254) == 0
PASSED: [test_slt_same] (0 < 0) == 0
PASSED: [test_slt_nn_1] (-1 < -2) == 0
PASSED: [test_slt_nn_2] (-2 < -1) == 1
PASSED: [test_slt_np] (-10419 < 10419) == 1
PASSED: [test_slt_pn] (10419 < -10419) == 0

--------------STORE_WORD--------------
PASSED: [test_sw] *(0x68) == 9
PASSED: [test_sw_offset_n] *(0x66) == -9
PASSED: [test_sw_offset_p] *(0x6A) == 9

--------------LOAD_WORD--------------
PASSED: [test_lw] $v0 == 17
PASSED: [test_lw_offset_n] $v0 == -17
PASSED: [test_lw_offset_p] $v0 == 17

--------------AND_BITMASKING--------------
PASSED: [test_and_ones] $v0 == 5
PASSED: [test_and_zeroes] $v0 == 0
PASSED: [test_and_ones] $v0 == -214

--------------BRANCH_ON_EQUAL--------------
PASSED: [test_beq_backward_eq] $a0 == 104
PASSED: [test_beq_forward_neq] $a0 == 214
PASSED: [test_beq_forward_eq] $a0 == 1
PASSED: [test_beq_forward_eq] $a1 == 2
PASSED: [test_beq_forward_neq] $a0 == 2
PASSED: [test_beq_forward_neq] $a1 == 2

--------------ZERO_READ_ONLY--------------
PASSED: [test_zero_lui] $v0 == 0
PASSED: [test_zero_ori] $v0 == 0
PASSED: [test_zero_addi] $v0 == 0
PASSED: [test_zero_add] $v0 == 0
PASSED: [test_zero_and] $v0 == 0
PASSED: [test_zero_slt] $v0 == 0
PASSED: [test_zero_lw] $v0 == 0

--------------INSTRUCTOR_PROVIDED_TEST--------------
PASSED: [test_instructor] *(0x0) == 10
PASSED: [test_instructor] $t0 == 10

--------------FIBONACCI_SEQUENCE--------------
PASSED: [test_fibonacci] $v0 == 987
PASSED: [test_fibonacci] $s0 == 0
PASSED: [test_fibonacci] $s1 == 1
PASSED: [test_fibonacci] $s2 == 0
PASSED: [test_fibonacci] $t2 == 10419
```
