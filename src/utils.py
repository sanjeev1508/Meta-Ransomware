import os
import subprocess
import logging

logger = logging.getLogger(__name__)

def ping_target(target_ip: str):
    """
    Utility function to ping a suspected ransomware C2 server.
    
    SECURITY VULNERABILITY: OS Command Injection
    This function takes a target_ip directly from input and executes it
    in the shell. If target_ip is "8.8.8.8; rm -rf /", it will execute the rm command.
    """
    logger.info(f"Pinging target {target_ip} to check connectivity...")
    
    # OS Command Injection Vulnerability
    command = f"ping -c 4 {target_ip}"
    os.system(command)
    
def execute_analysis_script(script_path: str):
    """
    Executes a bash script for deeper analysis.
    
    SECURITY VULNERABILITY: Subprocess execution without sanitization
    """
    logger.info(f"Executing script at {script_path}")
    subprocess.call([script_path], shell=True)

if __name__ == "__main__":
    # Test execution
    ping_target("127.0.0.1")
