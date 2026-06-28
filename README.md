# 🔍 Log Analyzer — Automated Security Tool

> A Python-based cybersecurity tool designed to simulate real-world SOC (Security Operations Center) workflows. It analyzes system logs, detects threats, identifies brute-force attacks, flags suspicious IP addresses, and generates detailed security reports — just like a real SOC L1 Analyst would do.

## 🎯 Why This Project?
In a real SOC environment, analysts review thousands of log lines daily to detect threats. This tool automates that process — saving time, reducing human error, and demonstrating core Blue Team skills including log analysis, threat detection, and incident reporting.

## ⚡ Key Features
- Detects failed login attempts in real-time
- Identifies brute-force attacks (3+ attempts from same IP)
- Extracts and flags suspicious IP addresses automatically
- Detects critical system errors and anomalies
- Generates a comprehensive security report saved as `.txt`
- Simulates real SIEM log analysis workflows

## 🚨 Threat Detection Engine
| Threat Type | Detection Method | Severity |
|-------------|-----------------|----------|
| Brute Force Attack | 3+ failed logins from same IP | CRITICAL |
| Failed Login | Keywords: failed, invalid | HIGH |
| Critical Error | Keywords: error, critical | MEDIUM |
| Suspicious IP | Auto-extracted via Regex | HIGH |

## 🛠️ Tools & Technologies
- Python 3
- Regex (re module) — pattern matching for threat detection
- Collections (Counter) — IP frequency analysis
- Datetime module — timestamp generation

## 🚀 How To Run

### 1. Clone the repository
```bash
git clone https://github.com/sousou1999406/log-analyzer
cd log-analyzer
```

### 2. Run the tool
```bash
py log_analyzer.py
```

### 3. Check the report
```bash
cat security_report.txt
```

## 📸 Screenshots

### Security Report Output

<img width="438" height="237" alt="image" src="https://github.com/user-attachments/assets/59ab6f7c-217d-44ee-9cf3-09872c5a8db4" />

## 📊 Example Output
```
============================================================
LOG ANALYZER - Security Report

Generated: 2026-06-28 19:57:50
[!] Failed Logins:      6

[+] Successful Logins:  2

[!] Errors Found:       2
[ALERT] Possible Brute Force Detected!

-> IP: 192.168.1.100 | Attempts: 4
[+] Report saved: security_report.txt
```
## 🔗 Related Skills (on CV)
- SIEM Log Analysis (Wazuh)
- Threat Detection & Investigation
- Incident Response Documentation
- Python Scripting for Security Automation

## 📁 Project Structure
log-analyzer/

├── log_analyzer.py       # Main detection engine

├── security_report.txt   # Auto-generated security report

└── README.md             # Project documentation
## ⚠️ Disclaimer
This tool is for **educational purposes only**.  
Built to simulate real SOC analyst workflows and demonstrate defensive cybersecurity skills.  
Do not use on systems without explicit permission.

## 👩‍💻 Author

**Soukaina Douazi** — Cybersecurity Student | SOC Analyst in Training  
📍 Casablanca, Morocco  
🔗 [LinkedIn](https://linkedin.com/in/soukaina-douazi)  
🔗 [GitHub](https://github.com/sousou1999406)
