import subprocess
import logging
import os
import json
from typing import List, Dict, Any, Optional

class Engine:
    def __init__(self, config_path: str = "config/config.json"):
        self.config = self._load_json(config_path)
        self._setup_logging()

    def _load_json(self, path: str) -> Dict:
        with open(path, 'r') as f:
            return json.load(f)

    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, self.config['settings']['log_level']),
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def execute(self, cmd: str, shell: bool = True) -> subprocess.CompletedProcess:
        """
        The primary execution engine. Handles command routing
        and process management.
        """
        logging.info(f"Executing: {cmd}")
        try:
            # Using subprocess.run for synchronous execution of tools
            result = subprocess.run(
                cmd,
                shell=shell,
                text=True,
                capture_output=False # We want the tool output to go straight to the TUI
            )
            return result
        except Exception as e:
            logging.error(f"Execution error: {e}")
            raise e

import subprocess
import logging
import os
import json
from typing import List, Dict, Any, Optional

class Engine:
    def __init__(self, config_path: str = "config/config.json"):
        self.config = self._load_json(config_path)
        self._setup_logging()

    def _load_json(self, path: str) -> Dict:
        with open(path, 'r') as f:
            return json.load(f)

    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, self.config['settings']['log_level']),
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def execute(self, cmd: str, shell: bool = True) -> subprocess.CompletedProcess:
        """
        The primary execution engine. Handles command routing
        and process management.
        """
        logging.info(f"Executing: {cmd}")
        try:
            # Using subprocess.run for synchronous execution of tools
            result = subprocess.run(
                cmd,
                shell=shell,
                text=True,
                capture_output=False # We want the tool output to go straight to the TUI
            )
            return result
        except Exception as e:
            logging.error(f"Execution error: {e}")
            raise e

    def run_bash_module(self, module_path: str, args: List[str] = []):
        """
        Runs a bash script from the modules directory.
        """
        full_cmd = f"bash {module_path} {' '.join(args)}"
        return self.execute(full_cmd)

    def smart_install(self, tool_id: str):
        """
        Tries to install a tool using APT, and if that fails,
        attempts to find it on GitHub.
        """
        import subprocess
        print(f"\n[*] Attempting to install {tool_id}...")

        # Try APT first
        try:
            subprocess.run(['sudo', 'apt-get', 'update'], check=True, stdout=subprocess.DEVNULL)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', tool_id], check=True)
            print(f"[+] {tool_id} installed successfully via APT!")
            return True
        except subprocess.CalledProcessError:
            print(f"[-] APT installation failed for {tool_id}. Trying GitHub...")

        # Try GitHub (Simplified: search for the tool name in a common format)
        # In a real scenario, we'd use the GitHub API, but for a script:
        try:
            repo_url = f"https://github.com/{tool_id}"
            subprocess.run(['git', 'clone', repo_url], check=True)
            print(f"[+] {tool_id} cloned from GitHub successfully!")
            return True
        except subprocess.CalledProcessError:
            print(f"[!] Could not find {tool_id} on APT or GitHub.")
            return False
