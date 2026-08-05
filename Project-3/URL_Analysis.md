# URL Analysis

The project analyzes URLs found in simulated phishing emails to identify suspicious patterns that may indicate malicious intent. Each URL is evaluated based on its domain name, wording, and the use of security-related terms such as **secure**, **login**, **verify**, and **account**. These indicators help users recognize potentially unsafe links before clicking them.

|    URL      | Observation | Security Concern |
|-------------|-------------|------------------|
| `http://secure-bank-login.example/verify` | Contains banking and login-related keywords but uses an untrusted example domain. | Could imitate a legitimate banking website to steal user credentials. |
| `http://claim-reward.example/prize` | Uses reward-related wording to encourage users to claim a prize. | Could redirect users to a fraudulent or phishing website. |
| `http://account-check.example/login` | Uses account verification and login-related terms to request user confirmation. | Could be used to collect usernames, passwords, or other sensitive information. |
| `http://delivery-update.example/address` | Requests delivery information through an unfamiliar domain. | Could be used to collect personal information or redirect users to a malicious page. |
