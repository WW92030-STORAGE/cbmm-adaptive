import subprocess, math
import argparse

VA_ORDER = 48       # How many bits does the address space occupy?

from execute import exec_
import CONSTANTS
import cbmm_modules as cbmm

# chop off the lowest k
def construct_policy(k = 0):
	# get this by using read_csv.py
	POLICY = []
	POLICY.append((0x7fd6aa200000, 0x7fd71bc00000, 11966130))
	POLICY.append((0x7fd870a00000, 0x7fd8e2400000, 28249659))
	POLICY.append((0x7fddc4200000, 0x7fde35c00000, 64599085))
	POLICY.append((0x7fdffc400000, 0x7fe06de00000, 57317061))
	POLICY.append((0x7fe06de00000, 0x7fe0df800000, 46339825))
	POLICY.append((0x7fe2a6000000, 0x7fe317a00000, 165328064))
	POLICY.append((0x7fe5c1600000, 0x7fe633000000, 123882214))
	POLICY.append((0x7fe633000000, 0x7fe6a4a00000, 150004662))
	POLICY.append((0x7fe787e00000, 0x7fe7f9800000, 45074710))
	POLICY.append((0x7feb86800000, 0x7febf8200000, 201264))
	POLICY.append((0x7febf8200000, 0x7fec69c00000, 198482385))
	POLICY.append((0x7fed4d000000, 0x7fedbea00000, 171982115))
	POLICY.append((0x7fedbea00000, 0x7fee30400000, 76587744))
	POLICY.append((0x7fee30400000, 0x7feea1e00000, 213852544))
	POLICY.append((0x7feea1e00000, 0x7fef13800000, 131009019))
	POLICY.append((0x7fef13800000, 0x7fef85200000, 98395000))
	POLICY.append((0x7fef85200000, 0x7feff6c00000, 14437294))
	POLICY.append((0x7feff6c00000, 0x7ff068600000, 516825832))
	POLICY.append((0x7ff068600000, 0x7ff0da000000, 233620695))
	POLICY.append((0x7ff0da000000, 0x7ff14ba00000, 434616965))
	POLICY.append((0x7ff14ba00000, 0x7ff1bd400000, 578747766))
	POLICY.append((0x7ff1bd400000, 0x7ff22ee00000, 1125118556))
	POLICY.append((0x7ff22ee00000, 0x7ff2a0800000, 1726002787))
	POLICY.append((0x7ff2a0800000, 0x7ff312200000, 3837041315))
	POLICY.append((0x7ff312200000, 0x7ff383c00000, 396141855))
	POLICY.append((0x7ff383c00000, 0x7ff3f5600000, 744923537))
	POLICY.append((0x7ff3f5600000, 0x7ff467000000, 51261982))
	POLICY.append((0x7ff4d8a00000, 0x7ff54a400000, 44077970))
	POLICY.append((0x7ff54a400000, 0x7ff5bbe00000, 162323536))
	POLICY.append((0x7ff782600000, 0x7ff7f4000000, 173174373))
	POLICY.append((0x7ff865a00000, 0x7ff8d7400000, 125584889))
	POLICY.append((0x7ffa9dc00000, 0x7ffb0f600000, 93258346))
	POLICY.append((0x7ffb0f600000, 0x7ffb81000000, 8144140))
	POLICY.append((0x7ffe9c600000, 0x7fff0e000000, 65579280))

	# sort by benefit, then clip off the front
	arr = []
	for p in POLICY:
		arr.append((p[2], p[1], p[0]))

	arr.sort()
	
	res = []
	for i in range(k, len(arr)):
		res.append((arr[i][2], arr[i][1], arr[i][0]))
	return res



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "--x to chop off low ranked benefits")
	parser.add_argument('--x', type=str, default = "0")
	args = parser.parse_args()
	k = int(args.x)
	POLICY = construct_policy(k)
	POLICY.sort()

	cbmm.SET_PROF_SIZE(len(POLICY))
	for i in range(len(POLICY)):
		print(POLICY[i])
		cbmm.SET_STARTS(i, POLICY[i][0])
		cbmm.SET_ENDS(i, POLICY[i][1])
		cbmm.SET_BENEFITS(i, POLICY[i][2])
