import os
import sys
import subprocess
import time

# ANSI Styling Tokens
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[38;5;196m"
GREEN   = "\033[38;5;48m"
CYAN    = "\033[38;5;51m"
AMBER   = "\033[38;5;214m"
MAGENTA = "\033[38;5;201m"
GRAY    = "\033[38;5;242m"

BANNER = f"""{CYAN}{BOLD}
 ██████╗ ██╗     ██╗   ██╗███████╗    ████████╗███████╗ █████╗ ███╗   ███╗
 ██╔══██╗██║     ██║   ██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
 ██████╔╝██║     ██║   ██║█████╗         ██║   █████╗  ███████║██╔████╔██║
 ██╔══██╗██║     ██║   ██║██╔══╝         ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
 ██████╔╝███████╗╚██████╔╝███████╗       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
 ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
{RESET}{AMBER} » UNIFIED CYBERSECURITY & DEFENSIVE OPERATIONS MASTER CONSOLE «{RESET}
"""

MODULES = [
    ("1", "Aegis-SOC: Autonomous Incident Operations Console", "aegis-soc-console", "aegis_soc.py"),
    ("2", "Q-RAG-Guard: Quantum CBOM & LLM/RAG Injection Scanner", "q-rag-guard", "q_rag_guard.py"),
    ("3", "Vigil-Guard: Pre-Commit Secrets & Entropy Radar", "vigil-secrets-guard", "vigil_guard.py"),
    ("4", "Spectre-HoneyNet: Deception Trap & Keylogger", "spectre-honeynet", "spectre_honeypot.py"),
    ("5", "Vortex-C2-Hunter: C2 Beacon & Covert Channel Radar", "vortex-c2-hunter", "vortex_hunter.py"),
    ("6", "Krypton-EDR: Behavioral Sensor & Threat Neutralizer", "krypton-edr-sensor", "krypton_edr.py"),
    ("7", "Nova-CloudGuard: Multi-Cloud IAM & CSPM Auditor", "nova-cloudguard", "nova_cloudguard.py"),
    ("8", "Apex-WebAudit: OWASP Web Defense Posture Scanner", "apex-web-auditor", "apex_scanner.py"),
    ("9", "Nucleus-Bridge: Vulnerability Telemetry & SLA Correlator", "nucleus-bridge-correlator", "nucleus_engine.py"),
    ("10", "Chrono-Forensics: Live Volatile Memory Triage", "chrono-forensics-triage", "chrono_triage.py"),
    ("11", "Hydra-Forge: Password Policy Auditor & Hashcat Bridge", "hydra-forge-auditor", "hydra_forge.py"),
    ("12", "Docker Security Hardening Auditor", "docker-security-auditor", "auditor.py"),
    ("13", "Process Lineage Anomaly Detector", "process-lineage-detector", "process_tree_detector.py"),
    ("14", "SSL/TLS Cipher Suite Monitor", "ssl-cipher-monitor", "tls_monitor.py"),
    ("0", "Exit Master Console", None, None)
]

def main():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(BANNER)
        print(f"{BOLD}Select an active defensive module to launch:{RESET}\n")

        for key, name, _, _ in MODULES:
            if key == "0":
                print(f"  {RED}[{key}]{RESET} {DIM}{name}{RESET}")
            else:
                print(f"  {CYAN}[{key:>2}]{RESET} {BOLD}{name}{RESET}")

        print("\n" + "=" * 80)
        choice = input(f"{AMBER}Enter module number > {RESET}").strip()

        if choice == "0":
            print(f"\n{GREEN}[✓] Terminating Master Console session. Stay secure!{RESET}\n")
            break

        selected = next((m for m in MODULES if m[0] == choice), None)
        if selected and selected[2] and selected[3]:
            mod_dir, script = selected[2], selected[3]
            print(f"\n{GREEN}[+] Launching {selected[1]}...{RESET}\n")
            time.sleep(0.5)

            # Change to directory and run script
            original_dir = os.getcwd()
            try:
                if os.path.exists(mod_dir):
                    os.chdir(mod_dir)
                    subprocess.run([sys.executable, script])
                else:
                    print(f"{RED}[-] Error: Directory '{mod_dir}' not found.{RESET}")
            finally:
                os.chdir(original_dir)

            input(f"\n{GRAY}Press Enter to return to Master Menu...{RESET}")
        else:
            print(f"{RED}[!] Invalid selection. Try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
