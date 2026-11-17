# PW2 – Lab B: Optimization in Chemistry

## Part 2 – Optimization Methods

We compared three optimization methods:
Gradient Descent, Newton's Method, and SLSQP.

For the simple function, all three methods converged to x = 3.

For the more complicated function, the results
depended on the starting point.

Newton's Method sometimes found a maximum
instead of a minimum.

This shows that the starting point and the
optimization method can affect the result.

## Part 3 – Reaction Kinetics

We studied a first-order chemical reaction.

The initial concentration was 104.082.

Using the SLSQP optimization method,
we obtained:

Fitted rate constant: k = 0.26176

The fitted curve closely follows the
experimental data.

The graph was saved as kinetics.png.

## Part 4 – Chemical Equilibrium

We studied the reaction:

H2 + I2 <=> 2HI

We used Newton's Method and SLSQP.

Newton's Method: x = 0.663848

SLSQP Method: x = 0.663847

Both methods gave almost identical results.

At equilibrium:

H2 = 0.336 mol
I2 = 0.336 mol
HI = 1.328 mol

The graph was saved as equilibrium.png.

## Part 5 – Titration (Bonus)

We analyzed the titration curve using
the numerical gradient.

The equivalence point was found at:

Volume = 50.0

The graph was saved as titration.png.

## Conclusion

Optimization methods are useful for solving
mathematical and chemical problems.

Newton's Method and SLSQP gave similar results
for the chemical equilibrium problem.

We also used optimization to estimate
a reaction rate constant and numerical
differentiation to find the titration
equivalence point.