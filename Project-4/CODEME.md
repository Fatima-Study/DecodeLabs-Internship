# DecodeLabs-Internship

# Project 4

# 🛡️ Modern Web Application Security Audit Report

> A comprehensive security assessment of the OWASP Juice Shop web application using industry-standard penetration testing tools to identify security vulnerabilities and recommend mitigation strategies.

---

# 📑 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Tools and Technologies](#tools-and-technologies)
- [Methodology](#methodology)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [Output](#output)
- [How to Run This Project](#how-to-run-this-project)
- [Future Work](#future-work)
- [Author & Contact](#author--contact)

---

# Overview

This project presents a **security assessment of the OWASP Juice Shop** web application conducted in a controlled laboratory environment using **Kali Linux**. The assessment focuses on identifying security vulnerabilities through network reconnaissance, web vulnerability scanning, and HTTP traffic analysis. Industry-standard security tools including **Nmap**, **Nikto**, and **Burp Suite** were used to evaluate the application's security posture and document findings with appropriate remediation recommendations.

---

# Problem Statement

Modern web applications are frequently exposed to security threats caused by insecure configurations and vulnerable services. This project aims to identify common web application security weaknesses within the OWASP Juice Shop application, assess their potential impact, and provide practical recommendations to improve overall security.

---

# Tools and Technologies

| Tool | Purpose |
|------|---------|
| Kali Linux | Security testing operating system |
| Oracle VirtualBox | Virtualization platform |
| Docker | Deploy OWASP Juice Shop |
| OWASP Juice Shop | Target web application |
| Nmap | Network scanning and service detection |
| Nikto | Web vulnerability scanning |
| Burp Suite Community | HTTP traffic interception and analysis |
| Firefox | Accessing the target application |

---

# Methodology

The assessment was performed in four phases:

1. **Environment Setup**
   - Configured Kali Linux virtual machine.
   - Verified Docker service.
   - Deployed the OWASP Juice Shop application.
   - Accessed the application through a web browser.

2. **Network Scanning**
   - Performed port scanning using Nmap.
   - Identified open services and running ports.
   - Verified the exposed application service.

3. **Vulnerability Assessment**
   - Conducted vulnerability scanning using Nikto.
   - Identified missing HTTP security headers and configuration weaknesses.
   - Evaluated potential security risks.

4. **HTTP Traffic Analysis**
   - Intercepted HTTP requests and responses using Burp Suite.
   - Captured user registration and login traffic.
   - Analyzed communication between the client and server.

---

# Key Insights

- Successfully deployed OWASP Juice Shop using Docker.
- Identified TCP Port **3000** as publicly accessible.
- Detected multiple missing HTTP security headers, including:
  - Content Security Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - Referrer Policy
- Identified a permissive **CORS** configuration (`Access-Control-Allow-Origin: *`).
- Successfully captured and analyzed HTTP requests using Burp Suite.
- Provided security recommendations to mitigate identified vulnerabilities.

---

# Project Structure

```text
DecodeLabs-Internship/
│
├── Project-4/
│   ├── README.md
│   ├── Security_Audit_Report.pdf
│   │   ├── figure1.png   (OWASP Juice Shop Home Page)
│   │   ├── figure2.png   (Nmap Network Scan Results)
│   │   ├── figure3.png   (Nikto Vulnerability Scan Results)
│   │   ├── figure4.png   (User Registration and Login in OWASP Juice Shop)
│   │   └── figure5.png   (Burp Suite HTTP Traffic Analysis)
│   ├── LICENSE
│   └── .gitignore
│
└── README.md
```

# Output

The project includes:

- OWASP Juice Shop deployment verification
- Nmap network scan results
- Nikto vulnerability scan results
- Burp Suite HTTP traffic analysis
- Vulnerability assessment report
- Risk analysis and remediation recommendations

---

# How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/Fatima-Study/DecodeLabs-Internship.git
```

### 2. Open the project folder

Navigate to the **Web Application Security Audit** project directory.

### 3. Deploy OWASP Juice Shop

Run the Docker container and verify that the application is accessible on:

```text
http://127.0.0.1:3000
```

### 4. Perform Security Assessment

Execute the following tools:

- Nmap for network scanning
- Nikto for vulnerability assessment
- Burp Suite for HTTP traffic analysis

### 5. Review the Report

Open the project report to review:

- Methodology
- Scan results
- Identified vulnerabilities
- Security recommendations

---

# Future Work

- Perform authenticated vulnerability assessments.
- Integrate automated security scanning into CI/CD pipelines.
- Conduct advanced penetration testing using additional security tools.
- Evaluate compliance with the OWASP Top 10 security risks.
- Reassess the application after implementing recommended security controls.

---

# Author & Contact

**Author:** Fatima

**Project:** Modern Web Application Security Audit Report

**Internship:** Cybersecurity Internship

**LinkedIn:** linkedin.com/in/fatima-taufique-1313b633b
