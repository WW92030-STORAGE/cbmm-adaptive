import subprocess, math

VA_ORDER = 48       # How many bits does the address space occupy?

from execute import exec_
import CONSTANTS
import cbmm_modules as cbmm

if __name__ == "__main__":
    cbmm.SET_PROF_SIZE(1)
    cbmm.SET_STARTS(0, 0x7ff3d4200000)
    cbmm.SET_ENDS(0, 0x7ffec2600000)
    cbmm.SET_BENEFITS(0, 23262478)