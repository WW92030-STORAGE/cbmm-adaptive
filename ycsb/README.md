# ebpf4379

```
sudo chmod -R 777 . && sudo ./install_modules.sh && ./mongo_install.sh && ./mongobench_setup.sh && ./mongo_run.sh

sudo ./install_damo.sh
```

```
cd ycsb

sudo ./install_python.sh && ./install_mongo4.sh && ./install_ycsb.sh

echo 'export PATH="/usr/local/python2.7/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

./run_mongo4.sh
```

## RUN TESTS

For CBMM:

```

cd ycsb
sudo echo 0 > /proc/force_init
# change UPDATE_HISTOS in ../profile/histograms.py to False
./run_tests.sh

```

For custom:

```

cd profile
# change the BUCKET_ORDER in CONSTANTS.py as needed
# change UPDATE_HISTOS in histograms.py to True
sudo python3 init_values.py
cd ../ycsb
./run_tests.sh

```