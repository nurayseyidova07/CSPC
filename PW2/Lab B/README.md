## PW1 — Lab B

The observed data show an exponential decrease and closely follow
the analytical model N(t) = N0 * exp(-0.3 * t).
The observed points have small fluctuations, while the analytical
curve is smooth.

The Snakefile uses decay_observed.csv and plot.py as inputs
and generates figure.png by running python plot.py.
It rebuilds the figure when an input changes or the output is missing.
If everything is up to date, Snakemake reports "Nothing to be done".

To run the workflow, activate the cspc environment, open PW1/Lab B,
and run:

    snakemake --cores 1 figure.png