#!/usr/bin/env python3
from bcc import BPF
import ctypes
import time
import os

# Configuration
ORDER = 8
N_BUCKETS = 1 << ORDER
ADDR_SPACE = 1 << 48
BUCKET_SIZE = ADDR_SPACE // N_BUCKETS

print(f"Using {N_BUCKETS} buckets, bucket size = {hex(BUCKET_SIZE)}")

# BPF program: increment histogram based on memory address
bpf_text = f"""
#include <uapi/linux/ptrace.h>
#include <uapi/linux/bpf_perf_event.h>

#define N_BUCKETS {N_BUCKETS}
#define BUCKET_SIZE {BUCKET_SIZE}

BPF_ARRAY(hist, u64, N_BUCKETS);

// This function will be called on each perf event sample
int on_sample(struct bpf_perf_event_data *ctx) {{
    u64 addr = ctx->addr;
    if (addr != 0) {{
        // bpf_trace_printk(\"Hello, World! \%lu\\n\", addr);
    }}
    u64 bucket = addr / BUCKET_SIZE;
    if (bucket >= N_BUCKETS)
        bucket = N_BUCKETS - 1;

    u64 *val = hist.lookup(&bucket);
    if (val) {{
        __sync_fetch_and_add(val, 1);
    }}
    return 0;
}}
"""

b = BPF(text=bpf_text)

# Hardware or raw perf type constants
PERF_TYPE_HARDWARE = 0
PERF_TYPE_SOFTWARE = 1
PERF_TYPE_TRACEPOINT = 2
PERF_TYPE_HW_CACHE = 3
PERF_TYPE_RAW = 4
PERF_TYPE_BREAKPOINT = 5

# Attach to hardware perf event: MEM_INST_RETIRED.ALL_LOADS
# ev_type = PERF_TYPE_RAW, ev_config = 0x1D1 for ALL_LOADS on Intel (adjust for your CPU)
b.attach_perf_event(ev_type=PERF_TYPE_RAW,
                    ev_config=0x1D1,
                    fn_name="on_sample",
                    sample_period=1000)  # sample every 1000 events

hist = b.get_table("hist")

print("Tracing memory load events... Ctrl-C to end.")

try:
    while True:
        # b.trace_print()
        os.system("clear")
        print("Bucket\tCount")
        for i in range(N_BUCKETS):
            count = hist[ctypes.c_int(i)].value
            if count > 0:
                print(f"{i}\t{count}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Detaching...")

print("Final histogram:")
for i in range(N_BUCKETS):
    count = hist[ctypes.c_int(i)].value
    if count > 0:
        print(f"{i}\t{count}")