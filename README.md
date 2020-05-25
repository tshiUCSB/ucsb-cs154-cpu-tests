# CMPSC 154: PyRTL CPU Unit Tests
A unit testing framework for guaranteeing correctness of the CMPSC 154 PyRTL CPU implementation
## Usage
- Download the unit testing framework to your computer
- Copy your `cpu.py` file to the root directory (alongside `testbench.py`)
- Run `testbench.py` with python3
```
python3 testbench.py
```
## /tests/
- Every test in `testbench.py` has a corresponding test in `/tests/` called `testname.s`
- Every `*.s` file has a first (commented) line which encodes the instructions in base64, serialized with JSON
- The assembly code used for every test will follow after that initial line
- NOTE: Some of the assembly instructions were assembled by hand, since some assemblers don't like negatives or `lui`
