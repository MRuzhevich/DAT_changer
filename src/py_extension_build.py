from cffi import FFI

C_MODULE_NAME = "c_formulas"

ffibuilder = FFI()

ffibuilder.cdef("float pi_approx(int n);")
ffibuilder.cdef("uint64_t simple_sum(uint64_t a, uint64_t b);")

ffibuilder.set_source(
    f"_{C_MODULE_NAME}",  # name of the output C extension
    source=f'#include "c_src/{C_MODULE_NAME}.h"',
    sources=[f"c_src/{C_MODULE_NAME}.c"],  # includes pi.c as additional sources
    # libraries=["m"],
)  # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(
        # target=f"_{C_MODULE_NAME}.*",
        verbose=True,
        tmpdir="./src/cfiles",
    )
