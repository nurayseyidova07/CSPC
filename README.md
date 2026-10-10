# CSPC - Computer Science for Ph

Pysics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml

conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

* I created the CSPC repository, set up the Conda environment, added the decay simulation, tests, and speed comparison.

**Speed comparison (loop vs NumPy):**

* loop : 1.6616 s
* numpy : 0.0002 s
* speed-up: 7746.92 x faster

**Tests:** all passing? yes

**Conclusion:**

* I learned how to use Git, GitHub, Conda, pytest, and NumPy.
* The NumPy version was faster than the pure-Python loop.
**Reproducibility test:**
- The repository was cloned into a fresh test directory.
- The environment was recreated successfully from environment.yml.
- All 3 tests passed with no changes to the code.
- Result: reproducible on the test environment.

## Nuray's Lab A Verification

I activated the Conda environment and verified that all three tests pass.
I also ran the Python and NumPy speed comparison.



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

## PW2 — Lab A

Mean acceleration: -8.58 m/s².
Acceleration standard deviation: 28.72 m/s².

The mean is approximately -9.81 m/s², with a difference of
1.23 m/s². Differentiating the noisy position data twice
amplifies the noise, causing large acceleration fluctuations.

Integrating acceleration twice with the initial velocity and
position recovers the original position closely. The maximum
position difference is 0.785 m, less than 1 metre.

The three-panel plot is saved in PW2/Lab A/motion.png.

To run, activate the cspc environment, open PW2/Lab A,
and run: python analysis.py