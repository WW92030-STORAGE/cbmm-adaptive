# ebpf4379

`sudo apt-get install python3-bpfcc linux-headers-$(uname -r)`

You must build [github.com/WW92030-STORAGE/scea_linux/](github.com/WW92030-STORAGE/scea_linux/) first! See `LINUX.md` for details.

NOTE - The following word salad is not a `bash` file. There are multiple branches as well as portions that you must do outside of running commands.

# SETUP (DO THIS ALWAYS)

```

# ENTER THIS FOLDER (e.g.)

cd ebpf4379

# SETUP MONGO

sudo chmod -R 777 . && sudo ./install_modules.sh && ./mongo_install.sh

# SETUP PERF/DAMO

sudo ./install_perf.sh && sudo ./install_damo.sh

# SETUP YCSB

cd ycsb
sudo ./install_python.sh && ./install_mongo4.sh && ./install_ycsb.sh
echo 'export PATH="/usr/local/python2.7/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

```

The rest of this details different workflows. For more information please see the relevant READMEs in the YCSB repo...

## MONGODB

```

# RUN MONGO (4.2) in a separate terminal

./run_mongo4.sh

# RUN TESTS
# 1. First, make sure mongo and modules are installed, and mongo 4.2 is running. Then, there are two branches:

# A. IF YOU ARE RUNNING CBMM:
cd ~/ebpf4379/profile
# change NO_UPDATES in damon_report_only.py to True
sudo echo 0 > /proc/force_init

# B. IF YOU ARE RUNNING AN ADAPTIVE POLICY (DAMO)
cd ~/ebpf4379/profile
# change NO_UPDATES in damon_report_only.py to False
# change the value in init_values.py and damon_report_only.py marked by CHANGE THE DEFAULT VALUE HERE to whatever is needed. 200000 and below is no promotions, anything above means promotions.
# EMPTY THE damo_report.txt FILE
sudo python3 init_values.py

# C. IF YOU RUNNING CBMM BUT EBPF (Slightly deprecated)
cd ~/ebpf4379/profile
# change UPDATE_HISTOS in histograms.py to False
sudo echo 0 > /proc/force_init

# D. IF YOU RUNNING AN ADAPTIVE POLICY (EBPF) (Slightly deprecated)
cd ~/ebpf4379/profile
# change UPDATE_HISTOS in histograms.py to True
# change the MODE in histograms.py to whatever is needed.
sudo echo 0 > /proc/force_init

# 2. Then, run the actual workload.
cd ../ycsb

# To set the workload, change the -P value in install_workload.sh and run_tests.sh to workloads/<workload> e.g. workloads/workloada. You can also customize the actual workload files. Alternatively, run ./install_workload.sh <workload> and ./run_tests_*.sh <workload>

# If you have not installed the workload.
./install_workload.sh

# Run the actual workload.
# For A and B
./run_tests_damo.sh 

# For C and D
./run_tests_histogram.sh


# alternatively: ./install_workload.sh workloadb
# etc.

# For shifting workloads, since each workload must be installed before it can be run, it's all packaged into one file:

./run_tests_shifting_*.sh <w1> <w2>

```

## REDIS

Deprecated

## NOTE - YOU MUST RUN `install_modules.sh` AND `run_mongo4.sh` ON EACH BOOT