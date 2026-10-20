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
 ## Session 1 — Distribution Analysis

- Age: The distribution is slightly left-skewed, with most patients aged between 50 and 65.
- Cholesterol: The distribution is right-skewed, with a few unusually high values.
- Resting blood pressure: The distribution is right-skewed, with most values between 110 and 140.
- Maximum heart rate: The distribution is left-skewed, with most values between 140 and 180.   
## Session 1 — Normality Testing

The Shapiro-Wilk test was used to check whether the four
continuous variables follow a normal distribution.

Results:
- Age: p = 0.0061
- Cholesterol: p < 0.0001
- Resting blood pressure: p < 0.0001
- Maximum heart rate: p = 0.0001

All p-values are below 0.05, so we reject the null
hypothesis of normality for all four variables.

The histograms also show some skewness, supporting
the results of the Shapiro-Wilk test.
## Session 2 — Heart Rate Comparison

The Mann-Whitney U test was used to compare maximum
heart rates between healthy patients and patients
with heart disease.

Results:
- Healthy mean: 158.38 bpm
- Disease mean: 139.26 bpm
- Mann-Whitney U statistic: 16989.5
- P-value: 1.86e-13

The p-value is much smaller than 0.05, indicating
a statistically significant difference between
the two groups.

Healthy patients have a higher mean maximum
heart rate than patients with heart disease.
### Mean and Uncertainty

The mean maximum heart rate was calculated for both groups,
together with the standard error of the mean (SEM).

Results:
- Healthy: 158.38 ± 1.50 bpm
- Heart disease: 139.26 ± 1.92 bpm

The healthy group has a higher mean maximum heart rate.

The error bars represent the standard error of the mean.
The plot supports the conclusion that the groups differ,
consistent with the Mann-Whitney U test.
## Task 5 — Age and Maximum Heart Rate Correlation

Spearman correlation was used because the variables
did not follow a normal distribution.

Results:
- Spearman correlation coefficient: -0.3916
- P-value: < 0.0001

There is a moderate negative correlation between
age and maximum heart rate.

This means that as age increases, maximum heart
rate tends to decrease.

The relationship is statistically significant.
However, correlation does not prove causation.
## Task 6 and 7 — Correlation vs Causation

Initially, cadmium showed a stronger correlation
with malignancy (r = 0.8849) than benzene (r = 0.3765).

After restricting the pollution index to 40–60,
the results changed:

- Benzene: r = 0.7093
- Cadmium: r = 0.2972
- Number of patients: 199

The correlation between cadmium and malignancy
decreased significantly, while the correlation
between benzene and malignancy became stronger.

This suggests that pollution index acts as a
confounding variable.

In this synthetic dataset, benzene appears to be
the intended causal chemical, while cadmium's
initially strong association is largely explained
by confounding.

However, correlation alone cannot definitively
establish causation.