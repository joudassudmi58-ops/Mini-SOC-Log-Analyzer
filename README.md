# Mini SOC Log Analyzer

A Python-based log analysis tool that simulates real SOC operations by detecting brute force attacks using time-based detection logic.

This project demonstrates practical Security Operations Center (SOC) concepts including log parsing, threat detection, reporting, and automated response generation.

---

## Features

- Detects failed login attempts  
- Time-based brute force detection  
- Configurable detection threshold  
- Generates CSV security report  
- Automatically creates blocklist file  
- Handles malformed log entries safely  
- Sorts and analyzes timestamps per IP  

---

## Detection Logic

An IP is flagged as suspicious if:

- It performs **3 or more failed login attempts**
- Within a **60-second time window**

These values can be configured inside the script:

THRESHOLD = 3  
TIME_WINDOW_SECONDS = 60  

---

## Project Structure

Mini-SOC-Log-Analyzer/

- log_analyzer.py  
- sample_log.txt  
- report.csv (generated)  
- blocklist.txt (generated)  
- README.md  

---

## Output Files

### report.csv
Contains all IP addresses and total failed login attempts.

Example:

IP Address,Total Failed Attempts  
192.168.1.10,4  
192.168.1.20,1  

---

### blocklist.txt
Contains only suspicious IPs detected as brute force attackers.

Example:

192.168.1.10  

---

## Technologies Used

- Python 3  
- datetime module  
- CSV handling  
- Log parsing techniques  
- Time-based detection logic  
- Security monitoring concepts  

---

## How to Run

Run the script using:

python log_analyzer.py  

Make sure sample_log.txt exists in the same directory.

---

## Skills Demonstrated

- Log analysis  
- Brute force detection logic  
- Time-window correlation  
- File handling  
- CSV reporting  
- Basic defensive automation  
- Git version control  

---

## Author

Developed as a SOC portfolio project to demonstrate hands-on cybersecurity and security monitoring capabilities.
