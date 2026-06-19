# """
# FatherTimeSDKP Unified Framework — Model Context Protocol (MCP) Server
#
# Author:     Donald Paul Smith (Father Time)
# ORCID:      0009-0003-7925-1653
# Module:     mcp_kapnack_server.py
# Protocol:   Model Context Protocol Infrastructure Mapping
# License:    CC BY 4.0
# """

import json
import sys
from typing import List, Dict, Any

# Ensure standard mcp dependencies are available via environment pip routing
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Error: The 'mcp' Python package is required. Run 'pip install mcp'", file=sys.stderr)
    sys.exit(1)

# Import the existing foundational modules
try:
    from kapnack_multibody_engine import BodySDVR, KapnackEngine
    from kapnack_integrator import KapnackIntegrator
except ImportError:
    print("Error: Foundations 'kapnack_multibody_engine.py' and 'kapnack_integrator.py' must be present in the execution path.", file=sys.stderr)
    sys.exit(1)

# Initialize the FastMCP instance container
app = FastMCP("FatherTimeSDKP-Core")

def _parse_bodies_payload(bodies_data: List[Dict[str, Any]]) -> List[BodySDVR]:
    """
    Helper parsing loop to process raw context payloads from the agent
    into rigidly formatted physical state nodes.
    """
    parsed_nodes = []
    for item in bodies_data:
        node = BodySDVR(
            body_id=str(item.get("body_id", "Unnamed_Node")),
            size=float(item.get("size", 1.0)),
            density=float(item.get("density", 1.0)),
            velocity=float(item.get("velocity", 0.0)),
            rotation=float(item.get("rotation", 0.0)),
            solid=str(item.get("solid", "cube")),
            position=tuple(item.get("position", (0.0, 0.0, 0.0)))
        )
        parsed_nodes.append(node)
    return parsed_nodes

@app.tool()
def evaluate_coherence(bodies_json: str, harmonic_order: int = 9) -> str:
    """
    Evaluates the current physical state of a system against Amiyah's Law and returns a coherence score.
    
    Arguments:
        bodies_json: A serialized JSON string containing an array of body nodes with SDVR vectors.
        harmonic_order: The resolution level for the 3-6-9 vortex cascade (3, 6, 9, or 12).
    """
    try:
        data = json.loads(bodies_json)
        nodes = _parse_bodies_payload(data)
        
        # Instantiate the solver using selected parameters
        engine = KapnackEngine(harmonic_order=harmonic_order)
        report = engine.system_coherence(nodes)
        
        # Format the processed diagnostics as text readable by the agent context window
        output_lines = [
            "=== FATHERTIMESDKP INTEGRATED FRAMEWORK COHERENCE DIAGNOSTIC ===",
            f"Calculated Coherence State C: {report['coherence']:.8f}",
            f"Active Resonance Mode       : Level {report['harmonic_order']} ({report['harmonic_description']})",
            f"Total System Interaction Sum: {report['psi_total']:.6e}",
            f"Coherence Band Margins      : {report['coherence_range_low']:.8f} — {report['coherence_range_high']:.8f}",
            "================================================================"
        ]
        return "\n".join(output_lines)
        
    except Exception as e:
        return f"Execution Failure during system coherence analysis: {str(e)}"

@app.tool()
def simulate_time_evolution(bodies_json: str, total_time: float, steps: int, harmonic_order: int = 9) -> str:
    """
    Simulates consecutive step intervals to compute discrete orbital updates over time.
    
    Arguments:
        bodies_json: A serialized JSON string containing an array of body nodes with SDVR vectors.
        total_time: The complete duration of the tracking window in seconds.
        steps: Total quantity of discrete steps to execute.
        harmonic_order: The target harmonic resolution cascade level (3, 6, 9, or 12).
    """
    try:
        data = json.loads(bodies_json)
        nodes = _parse_bodies_payload(data)
        
        # Bind the core components together
        engine = KapnackEngine(harmonic_order=harmonic_order)
        integrator = KapnackIntegrator(engine)
        
        # Execute the epoch step tracking sequence
        history_log = integrator.run_simulation(nodes, total_time=total_time, steps=steps)
        
        # Structure clear execution summaries for text parsing windows
        summary_lines = [
            f"=== DISCRETE ACCELERATION TIME-SERIES LOG ARRAY ===",
            f"Total Epochs Tracked: {len(history_log)} | Step Duration (dt): {total_time / steps:.4f}s\n"
        ]
        
        for entry in history_log:
            summary_lines.append(f"Epoch {entry['epoch'] + 1} | Elapse: {entry['elapsed_time_seconds']:.2f}s | Coherence: {entry['system_coherence']:.8f}")
            for s in entry['states']:
                pos_str = f"({s['pos'][0]:.2f}, {s['pos'][1]:.2f}, {s['pos'][2]:.2f})"
                summary_lines.append(f"  Node [{s['id']}] -> Position: {pos_str} | Vel: {s['v']:.2f} m/s")
                
        summary_lines.append("\n====================================================")
        return "\n".join(summary_lines)
        
    except Exception as e:
        return f"Execution Failure during dynamic simulation run: {str(e)}"

if __name__ == "__main__":
    # Launch the server instance using standard command-line pipes
    app.run()
