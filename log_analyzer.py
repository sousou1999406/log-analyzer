import re
import datetime
from collections import Counter

def analyze_logs(log_content):
    failed_logins = []
    successful_logins = []
    suspicious_ips = []
    errors = []

    lines = log_content.strip().split('\n')
    
    for line in lines:
        # Detect failed logins
        if re.search(r'failed|Failed|FAILED|invalid|Invalid', line):
            failed_logins.append(line)
            ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip:
                suspicious_ips.append(ip.group())
        
        # Detect successful logins
        elif re.search(r'success|Success|SUCCESS|accepted|Accepted', line):
            successful_logins.append(line)
        
        # Detect errors
        elif re.search(r'error|Error|ERROR|critical|Critical', line):
            errors.append(line)

    # Count suspicious IPs
    ip_counts = Counter(suspicious_ips)
    brute_force = {ip: count for ip, count in ip_counts.items() if count >= 3}

    return failed_logins, successful_logins, brute_force, errors

def generate_report(failed, success, brute_force, errors):
    print("=" * 60)
    print("LOG ANALYZER - Security Report")
    print(f"Generated: {datetime.datetime.now()}")
    print("=" * 60)
    
    print(f"\n[!] Failed Logins: {len(failed)}")
    print(f"[+] Successful Logins: {len(success)}")
    print(f"[!] Errors Found: {len(errors)}")
    
    if brute_force:
        print(f"\n[ALERT] Possible Brute Force Detected!")
        for ip, count in brute_force.items():
            print(f"  -> IP: {ip} | Attempts: {count}")
    else:
        print("\n[OK] No Brute Force Detected")

    # Save report
    with open("security_report.txt", "w", encoding="utf-8") as f:
        f.write("LOG ANALYZER - Security Report\n")
        f.write(f"Generated: {datetime.datetime.now()}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Failed Logins: {len(failed)}\n")
        f.write(f"Successful Logins: {len(success)}\n")
        f.write(f"Errors: {len(errors)}\n")
        if brute_force:
            f.write("\nBRUTE FORCE DETECTED:\n")
            for ip, count in brute_force.items():
                f.write(f"  IP: {ip} | Attempts: {count}\n")
    
    print("\n[+] Report saved: security_report.txt")
    print("=" * 60)

# Sample logs for testing
sample_logs = """
2026-06-28 10:01:23 Failed login attempt from 192.168.1.100
2026-06-28 10:01:25 Failed login attempt from 192.168.1.100
2026-06-28 10:01:27 Failed login attempt from 192.168.1.100
2026-06-28 10:01:30 Failed login attempt from 192.168.1.100
2026-06-28 10:02:01 Successful login from 192.168.1.50
2026-06-28 10:03:15 Invalid password from 10.0.0.5
2026-06-28 10:04:22 Error: Connection timeout
2026-06-28 10:05:10 Accepted login from 192.168.1.75
2026-06-28 10:06:33 Failed login attempt from 172.16.0.1
2026-06-28 10:07:45 Critical error in authentication module
"""

print("Analyzing logs...")
failed, success, brute_force, errors = analyze_logs(sample_logs)
generate_report(failed, success, brute_force, errors)