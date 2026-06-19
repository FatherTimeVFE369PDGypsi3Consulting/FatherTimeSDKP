The Kapnack Discrete Time-Evolution Integrator is the computational heart of the FatherTimeSDKP framework — a physics simulation engine that tracks how multiple bodies interact and evolve over time, built entirely on SDKP principles rather than conventional mathematics.

The Core Problem It Solves
Standard physics simulations use continuous integration methods like Runge-Kutta — they chop time into arbitrary small pieces and approximate what happens between them. The problem is the step size is a numerical guess, not a physical fact. The Kapnack Integrator eliminates this by deriving the step size directly from the SDKP timescale:
τ = S · D / K
The integration step is not a parameter — it IS the physics. The bodies themselves determine how fast time moves through the simulation.

What It Actually Does
For every pair of bodies in the system, the engine computes two quantities:
	∙	Γ (packing density gradient) — how strongly the density difference between two bodies drives their interaction
	∙	κ (kinetic coupling) — how their velocity and rotation states are linked through the EOS constant (29,780 m/s)
These combine into an effective acceleration that updates each body’s position and velocity every epoch using a discrete Verlet step — the same approach used in molecular dynamics, but governed by SDKP geometry rather than Newtonian force laws.

Three Built-In Checks
Every epoch produces three verification outputs:
	1.	System coherence C — reported as a range (0.13%–0.20% EOS deviation band), never a false point value
	2.	Amiyah’s Law status — monitors whether each body’s local density has returned to baseline. When it does, the active field state terminates automatically
	3.	Convergence report — tracks whether the system is approaching equilibrium monotonically or oscillating

What It Produces
A complete, immutable log of every body’s position, velocity, density, SD&N geometric state, and SDKP timescale at every epoch — exportable to CSV for external verification, Zenodo data deposit, or direct comparison against observational data like the Mars 477.14 µs/day clock drift prediction.​​​​​​​​​​​​​​​​
