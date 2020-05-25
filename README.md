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
