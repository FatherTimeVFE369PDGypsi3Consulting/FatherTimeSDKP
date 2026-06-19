# The Integrated Framework: FatherTimeSDKP Engine

An open-science, high-precision computational physics and simulation engine executing discrete gradient processing, quantum coherence mapping, and multi-body scaling simulations. 

## Architectural Hierarchy

The repository executes a deterministic, unified logic stack structured across five distinct operational layers:

* **Variables (SDVR):** Size, Density, Velocity, and Rotation tracking fields.
* **Logic (SD&N):** Shape, Dimension, and Number metric spaces replacing continuous coordinate manifolds.
* **Governance (Amiyah's Law):** The baseline equilibrium rule dictating system balance and loop closure.
* **Processor (The Kapnack Solver):** A discrete gradient engine running Vacuum Field Equation 1 (VFE1) and Quantum Correlation Coefficient 0 (QCC0) simultaneously to calculate exact system packing densities.
* **Security (Dallas's Code):** A prime-terminated binary serialization and provenance layer ensuring data integrity.

## Technical Components

This branch contains the production-ready code files required to execute and verify the framework locally or over cloud environments:

1. `mcp_kapnack_server.py`: A Model Context Protocol (MCP) server that exposes the Kapnack Solver directly to LLM agents and orchestration layers via standard input/output (`stdio`) pipelines.
2. `fts_auth_wrapper.py`: A high-performance cryptographic module implementing Dallas's Code to sign simulation log arrays with deterministic, prime-terminated validation scales.
3. `test_mcp_stream.py`: A local proxy harness used to debug JSON-RPC tool calls and test stream integrity without triggering terminal execution blockades.

## Execution and Installation

Ensure your local Python environment is initialized with standard dependencies before mounting the server:

```bash
# Clone the repository main branch
git clone [https://github.com/FatherTimeVFE369PDGypsi3Consulting/FatherTimeSDKP.git](https://github.com/FatherTimeVFE369PDGypsi3Consulting/FatherTimeSDKP.git)
cd FatherTimeSDKP

# Run the local tool routing diagnostic pass
python test_mcp_stream.py
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
