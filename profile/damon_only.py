from bcc import BPF
from time import sleep
import time
import argparse, subprocess, atexit
from execute import exec_
import math
import concurrent.futures as CF
import cbmm_modules as cbmm
import threading
from damon_utils import impart_workflow_pid_to_kdamonds

NUM_BUCKETS = 256

DAMO_REC = True
DAMO_UPDATE = True

# Runner -- periodically procure a histogram and do updates
if __name__ == "__main__":
    """

    Period = seconds per iteration

    """
    PERIOD = 4

    parser = argparse.ArgumentParser(description = "put pid here")
    parser.add_argument('--workflow', type=str, default = "")

    args = parser.parse_args()
    workflow_pid = args.workflow

    print("PID:", workflow_pid)

    impart_workflow_pid_to_kdamonds(workflow_pid, NUM_BUCKETS)

    if DAMO_REC:
        subprocess.run("sudo ../damo/damo start --kdamonds kdamonds.json".split())
    print("DAMO PROC OPENED")
    while True:
        # Begoin damo record

        try:

            damo_record_proc = None

            if DAMO_REC:
                damo_record = "sudo ../damo/damo record"
                damo_record_proc = subprocess.Popen(damo_record.split())

            sleep(PERIOD)

            if DAMO_REC:
                damo_record_proc.terminate()
                damo_record_proc.wait()
                if DAMO_UPDATE:
                    subprocess.Popen("./damon_report_only.sh".split())
            
            print("PERIOD HIT")
        
        except Exception as e:
            print("SOMETHING BAD REALLY HAPPENED :(", e)

        # End damo record

"""
"""

def goodbye():
    print("HISTOGRAM TERMINATED")

    if DAMO_PROC is not None:
        subprocess.run("sudo ../damo/damo stop")
        print("DAMO_PROC TERMINATED")
def exit_handler():
    goodbye()