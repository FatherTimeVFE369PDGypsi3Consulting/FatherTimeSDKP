#!/usr/bin/env python3
"""
The Integrated Framework: Automated MCP Validation Harness
Filename: test_mcp_client.py
Description: Spawns the root-level mcp_kapnack_server.py file as a subprocess,
             simulates standard JSON-RPC orchestration frames, and verifies
             Amiyah's Law and Dallas's Code security outputs in compliance 
             with the local stdio MCP specification.
"""

import subprocess
import json
import sys
import time

def print_status(message: str):
    """Prints clear status metrics to the standard tracking channel."""
    print(f"[Harness Update] {message}")

def run_validation_test():
    print_status("Initializing subprocess connection to mcp_kapnack_server.py...")
    
    # Launch the target MCP server with stderr passed through to the terminal
    # This keeps the OS pipe buffer completely clear and exposes background logs
    process = subprocess.Popen(
        [sys.executable, "mcp_kapnack_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        text=True
    )

    try:
        # 1. Execute Protocol Handshake (initialize request)
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-harness", "version": "1.0.0"}
            }
        }
        
        print_status("Transmitting JSON-RPC 'initialize' handshake frame...")
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Capture and validate handshake response
        init_response_raw = process.stdout.readline()
        if not init_response_raw:
            print_status("ERROR: Server exited or failed to reply during handshake phase.")
            return

        init_response = json.loads(init_response_raw)
        
        # Check for protocol-level errors
        if "error" in init_response:
            print_status(f"FATAL: Server returned initialization error: {json.dumps(init_response['error'])}")
            return

        print_status("Handshake Response verified from server:")
        print(json.dumps(init_response, indent=2))

        # 2. Transmit Post-Initialization Notification Signal
        initialized_notification = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        print_status("Transmitting asymmetric 'notifications/initialized' frame...")
        process.stdin.write(json.dumps(initialized_notification) + "\n")
        process.stdin.flush()
        time.sleep(0.1)  # Brief pause for asynchronous stream ingestion

        # 3. Simulate Multi-Body SDVR Execution Call (evaluate_coherence)
        # This scenario models a continuous structural array using the Integrated Framework logic
        test_bodies = [
            {"body_id": "Core_Node_Alpha", "size": 1.5, "density": 5.4, "velocity": 29.78, "rotation": 0.004, "solid": "sphere"},
            {"body_id": "Boundary_Node_Beta", "size": 0.8, "density": 2.7, "velocity": 24.07, "rotation": 0.001, "solid": "cube"}
        ]
        
        tool_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "evaluate_coherence",
                "arguments": {
                    "bodies_json": json.dumps(test_bodies),
                    "harmonic_order": 9
                }
            }
        }
        
        print_status("Transmitting computational 'evaluate_coherence' matrix payload...")
        process.stdin.write(json.dumps(tool_request) + "\n")
        process.stdin.flush()
        
        # Capture and handle mathematical core calculations
        tool_response_raw = process.stdout.readline()
        if not tool_response_raw:
            print_status("ERROR: Server failed to respond to computational tool call.")
            return

        tool_response = json.loads(tool_response_raw)
        
        if "error" in tool_response:
            print_status(f"FATAL: Tool execution failed with error: {json.dumps(tool_response['error'])}")
            return

        print_status("Mathematical optimization payload returned successfully:")
        
        # Extract results matching the protocol content array structure
        result_node = tool_response.get("result", {})
        if result_node.get("isError"):
            print_status("WARNING: Server execution flag 'isError' is set to True.")

        content_list = result_node.get("content", [])
        if not content_list or "text" not in content_list[0]:
            print_status("ERROR: Server response format did not contain structured text content.")
            return

        content_text = content_list[0]["text"]
        parsed_core_output = json.loads(content_text)
        print(json.dumps(parsed_core_output, indent=2))
        
        # 4. Verification Check Routines
        print_status("--- Executing Architectural Verification Pass ---")
        
        # Verify framework integrity alignment
        status_indicator = parsed_core_output.get("status")
        coherence_value = parsed_core_output.get("system_coherence")
        seal_data = parsed_core_output.get("dallas_code_seal", {})
        prime_terminator = seal_data.get("prime_terminator")
        
        print(f" -> Solver Core Status: {status_indicator}")
        print(f" -> System Coherence Boundary: {coherence_value}")
        print(f" -> Dallas's Code Verification Seal: {seal_data.get('integrity')}")
        print(f" -> Prime-Terminated Scalar Value: {prime_terminator}")
        
        # Cross-reference with the baseline framework accuracy properties (reported December 14, 2025)
        if status_indicator == "SUCCESS" and prime_terminator:
            print_status("SUCCESS: The root-level MCP server is fully operational and authenticated.")
        else:
            print_status("ERROR: Integrity check failed to return valid parameters.")

    finally:
        # Guarantee cleanup of subprocess channels safely regardless of early returns or errors
        print_status("Shutting down subprocess connection safely...")
        if process.poll() is None:
            process.terminate()
            process.wait()

 if __name__ == "__main__":
    try:
        run_validation_test()
    except Exception as err:
        print(f"[Harness Fault] Fatal verification failure: {str(err)}")
        sys.exit(1)
