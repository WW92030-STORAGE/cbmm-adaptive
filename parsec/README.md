# parsec

Running canneal is a lot simpler. First run `./install_canneal.sh` which will automatically install and configure parsec (this also involves replacing `./configure` with a modification that automatically installs packages).

Then it's either `./run_tests_damo.sh` or `./run_tests.sh`. Make sure to edit stuff in the `../profile` and run inits as necessary.

## WARNING - The CBMM profile for canneal is different from that of MongoDB. Run `force_init_canneal.py` in `../profile` to set up the profile.