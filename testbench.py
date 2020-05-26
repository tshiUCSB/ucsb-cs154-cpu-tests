# Import the pyrtl hardware description language
import pyrtl

# Import extra parsing libraries for tester
from json import loads
from base64 import b64decode

# Import extra library for handling binary data
from struct import pack, unpack

# Attempt to import the cpu implementation
from cpu import i_mem, d_mem, rf

def start_test_group(name):
    print("\n--------------{}--------------".format(name))

def assert_equals(expected, actual, message):
    if expected == actual:
        print("PASSED: {}".format(message))
    else:
        print("FAILED: {}".format(message))
        print("   Expected:")
        print("     {}".format(expected))
        print("   Actual:")
        print("     {}".format(actual))

def init_sim(testname):
    file = open("tests/{}.s".format(testname), 'r')
    enc_asm = file.readlines()[0][1:].strip()
    asm = loads(b64decode(enc_asm).decode("UTF-8"))
    i_mem_init = {int(k): v for k, v in asm.items()}
    sim_trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=sim_trace, memory_value_map={
        i_mem : i_mem_init
    })
    return sim, sim_trace

def print_trace_result(sim, sim_trace):
    print("+++++++++++++start_of_trace+++++++++++++")
    print("data memory:", sim.inspect_mem(d_mem))
    print("register file:", sim.inspect_mem(rf))
    sim_trace.render_trace()
    print("++++++++++++++end_of_trace++++++++++++++")

def test_lui(enable_trace=False):
    sim, sim_trace = init_sim("test_lui")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(1798635520, sim.inspect_mem(rf)[9], "[test_lui] $t1 == 1798635520")

def test_ori(enable_trace=False):
    sim, sim_trace = init_sim("test_ori")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(6573, sim.inspect_mem(rf)[2], "[test_ori] $v0 == 6573")

def test_addi(enable_trace=False):
    sim, sim_trace = init_sim("test_addi")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(6573, sim.inspect_mem(rf)[2], "[test_addi] $v0 == 6573")

def test_ori_negative(enable_trace=False):
    sim, sim_trace = init_sim("test_ori_negative")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(55117, sim.inspect_mem(rf)[21], "[test_ori_negative] $s5 == 55117")

def test_addi_negative(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_negative")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[21]))[0]
    assert_equals(-10419, actual, "[test_addi_negative] $s5 == -10419")

def test_ori_lui(enable_trace=False):
    sim, sim_trace = init_sim("test_ori_lui")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(3546218496, sim.inspect_mem(rf)[17], "[test_ori_lui] $s1 == 3546218496")

def test_lui_ori(enable_trace=False):
    sim, sim_trace = init_sim("test_lui_ori")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(3546228915, sim.inspect_mem(rf)[17], "[test_lui_ori] $s1 == 3546228915")

def test_add_pp(enable_trace=False):
    sim, sim_trace = init_sim("test_add_pp")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(318, sim.inspect_mem(rf)[2], "[test_add_pp] $v0 == 318")

def test_add_same(enable_trace=False):
    sim, sim_trace = init_sim("test_add_same")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_add_same] $v0 == 0")

def test_add_nn(enable_trace=False):
    sim, sim_trace = init_sim("test_add_nn")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-318, actual, "[test_add_nn] $v0 == -318")

def test_add_np(enable_trace=False):
    sim, sim_trace = init_sim("test_add_np")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-110, actual, "[test_add_np] $v0 == -110")

def test_add_pn(enable_trace=False):
    sim, sim_trace = init_sim("test_add_pn")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(110, sim.inspect_mem(rf)[2], "[test_add_pn] $v0 == 110")

def test_addi_pp(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_pp")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(32, sim.inspect_mem(rf)[2], "[test_addi_pp] $v0 == 32")

def test_addi_same(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_same")
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_addi_same] $v0 == 0")

def test_addi_nn(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_nn")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-32, actual, "[test_addi_nn] $v0 == -32")

def test_addi_np(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_np")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(2, sim.inspect_mem(rf)[2], "[test_addi_np] $v0 == 2")

def test_addi_pn(enable_trace=False):
    sim, sim_trace = init_sim("test_addi_pn")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-2, actual, "[test_addi_pn] $v0 == -2")

def test_slt_pp_1(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_pp_1")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(1, sim.inspect_mem(rf)[4], "[test_slt_pp_1] (254 < 10419) == 1")

def test_slt_pp_2(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_pp_2")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[4], "[test_slt_pp_2] (10419 < 254) == 0")

def test_slt_same(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_same")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[5], "[test_slt_same] (0 < 0) == 0")

def test_slt_nn_1(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_nn_1")
    for _ in range(5):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_slt_nn_1] (-1 < -2) == 0")


def test_slt_nn_2(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_nn_2")
    for _ in range(5):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(1, sim.inspect_mem(rf)[2], "[test_slt_nn_2] (-2 < -1) == 1")

def test_slt_np(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_np")
    for _ in range(4):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(1, sim.inspect_mem(rf)[15], "[test_slt_np] (-10419 < 10419) == 1")

def test_slt_pn(enable_trace=False):
    sim, sim_trace = init_sim("test_slt_pn")
    for _ in range(4):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[15], "[test_slt_pn] (10419 < -10419) == 0")

def test_sw(enable_trace=False):
    sim, sim_trace = init_sim("test_sw")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(9, sim.inspect_mem(d_mem)[0x68], "[test_sw] *(0x68) == 9")

def test_sw_offset_n(enable_trace=False):
    sim, sim_trace = init_sim("test_sw_offset_n")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(d_mem)[0x66]))[0]
    assert_equals(-9, actual, "[test_sw_offset_n] *(0x66) == -9")

def test_sw_offset_p(enable_trace=False):
    sim, sim_trace = init_sim("test_sw_offset_p")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(9, sim.inspect_mem(d_mem)[0x6A], "[test_sw_offset_p] *(0x6A) == 9")

def test_lw(enable_trace=False):
    sim, sim_trace = init_sim("test_lw")
    for _ in range(4):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(17, sim.inspect_mem(rf)[2], "[test_lw] $v0 == 17")

def test_lw_offset_n(enable_trace=False):
    sim, sim_trace = init_sim("test_lw_offset_n")
    for _ in range(5):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-17, actual, "[test_lw_offset_n] $v0 == -17")

def test_lw_offset_p(enable_trace=False):
    sim, sim_trace = init_sim("test_lw_offset_p")
    for _ in range(5):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(17, sim.inspect_mem(rf)[2], "[test_lw_offset_p] $v0 == 17")

def test_and(enable_trace=False):
    sim, sim_trace = init_sim("test_and")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(5, actual, "[test_and_ones] $v0 == 5")

def test_and_zeroes(enable_trace=False):
    sim, sim_trace = init_sim("test_and_zeroes")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_and_zeroes] $v0 == 0")

def test_and_ones(enable_trace=False):
    sim, sim_trace = init_sim("test_and_ones")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    actual = unpack('<i', pack('<I', sim.inspect_mem(rf)[2]))[0]
    assert_equals(-214, actual, "[test_and_ones] $v0 == -214")

def test_beq_backward_eq(enable_trace=False):
    sim, sim_trace = init_sim("test_beq_backward_eq")
    for _ in range(10):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(104, sim.inspect_mem(rf)[4], "[test_beq_backward_eq] $a0 == 104")

def test_beq_backward_neq(enable_trace=False):
    sim, sim_trace = init_sim("test_beq_backward_neq")
    for _ in range(10):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(214, sim.inspect_mem(rf)[4], "[test_beq_forward_neq] $a0 == 214")

def test_beq_forward_eq(enable_trace=False):
    sim, sim_trace = init_sim("test_beq_forward_eq")
    for _ in range(10):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(1, sim.inspect_mem(rf)[4], "[test_beq_forward_eq] $a0 == 1")
    assert_equals(2, sim.inspect_mem(rf)[5], "[test_beq_forward_eq] $a1 == 2")

def test_beq_forward_neq(enable_trace=False):
    sim, sim_trace = init_sim("test_beq_forward_neq")
    for _ in range(10):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(2, sim.inspect_mem(rf)[4], "[test_beq_forward_neq] $a0 == 2")
    assert_equals(2, sim.inspect_mem(rf)[5], "[test_beq_forward_neq] $a1 == 2")

def test_zero_lui(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_lui")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_lui] $v0 == 0")

def test_zero_ori(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_ori")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_ori] $v0 == 0")

def test_zero_addi(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_addi")
    sim.step({})
    sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_addi] $v0 == 0")

def test_zero_add(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_add")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_add] $v0 == 0")

def test_zero_and(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_and")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_and] $v0 == 0")

def test_zero_slt(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_slt")
    for _ in range(3):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_slt] $v0 == 0")

def test_zero_lw(enable_trace=False):
    sim, sim_trace = init_sim("test_zero_lw")
    for _ in range(4):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(0, sim.inspect_mem(rf)[2], "[test_zero_lw] $v0 == 0")

def test_instructor(enable_trace=False):
    sim, sim_trace = init_sim("test_instructor")
    
    for cycle in range(500):
        sim.step({})

    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(10, sim.inspect_mem(d_mem)[0], "[test_instructor] *(0x0) == 10")
    assert_equals(10, sim.inspect_mem(rf)[8], "[test_instructor] $t0 == 10")

def test_fibonacci(enable_trace=False):
    sim, sim_trace = init_sim("test_fibonacci")
    for cycle in range(500):
        sim.step({})
    if enable_trace:
        print_trace_result(sim, sim_trace)
    assert_equals(987, sim.inspect_mem(rf)[2], "[test_fibonacci] $v0 == 987")
    assert_equals(0, sim.inspect_mem(rf)[16], "[test_fibonacci] $s0 == 0")
    assert_equals(1, sim.inspect_mem(rf)[17], "[test_fibonacci] $s1 == 1")
    assert_equals(0, sim.inspect_mem(rf)[18], "[test_fibonacci] $s2 == 0")
    assert_equals(10419, sim.inspect_mem(rf)[10], "[test_fibonacci] $t2 == 10419")

if __name__ == "__main__":
    # Pass in True for any test function to enable trace
    start_test_group("LOAD_IMMEDIATE_VALUE")
    test_lui()
    test_ori()
    test_addi()
    test_ori_negative()
    test_addi_negative()
    test_ori_lui()
    test_lui_ori()

    start_test_group("ADD_IMMEDIATE")
    test_addi_pp()
    test_addi_same()
    test_addi_nn()
    test_addi_np()
    test_addi_pn()

    start_test_group("ADD_REGISTERS")
    test_add_pp()
    test_add_same()
    test_add_nn()
    test_add_np()
    test_add_pn()

    start_test_group("SET_LESS_THAN")
    test_slt_pp_1()
    test_slt_pp_2()
    test_slt_same()
    test_slt_nn_1()
    test_slt_nn_2()
    test_slt_np()
    test_slt_pn()

    start_test_group("STORE_WORD")
    test_sw()
    test_sw_offset_n()
    test_sw_offset_p()

    start_test_group("LOAD_WORD")
    test_lw()
    test_lw_offset_n()
    test_lw_offset_p()

    start_test_group("AND_BITMASKING")
    test_and()
    test_and_zeroes()
    test_and_ones()

    start_test_group("BRANCH_ON_EQUAL")
    test_beq_backward_eq()
    test_beq_backward_neq()
    test_beq_forward_eq()
    test_beq_forward_neq()
    
    start_test_group("ZERO_READ_ONLY")
    test_zero_lui()
    test_zero_ori()
    test_zero_addi()
    test_zero_add()
    test_zero_and()
    test_zero_slt()
    test_zero_lw()

    start_test_group("INSTRUCTOR_PROVIDED_TEST")
    test_instructor()
    
    start_test_group("FIBONACCI_SEQUENCE")
    test_fibonacci()
