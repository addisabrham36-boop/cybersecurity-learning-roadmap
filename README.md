# 🛡️ Personal Cybersecurity Learning Roadmap

> A structured, progressive study library organized from Foundations → Advanced Specialization.
> Check off each resource as you complete it to track your journey.

---

## 📁 Repository Structure

```
Books/
├── README.md                                  ← You are here (Master Roadmap)
│
├── 01-foundations/                            ← Start here: Core skills
│   ├── networking/                            (Protocols, TCP/IP, DNS)
│   ├── linux-and-shell/                       (Linux Bible, Bash scripting, Kali basics)
│   └── programming/
│       ├── python/                            (Python for hackers)
│       ├── bash/                              (Black Hat Bash, shell scripting)
│       └── other-languages/                   (Go, Rust, Violent Python)
│
├── 02-core-security/                          ← Core security concepts & tools
│   ├── web-security/                          (OWASP, XSS, SQLi, API security)
│   ├── network-security/                      (WiFi, packet analysis, protocols)
│   ├── cryptography/                          (Crypto fundamentals)
│   └── tools/                                (Kali Linux, Metasploit, Nmap)
│
├── 03-intermediate-labs/                      ← Hands-on practice
│   ├── penetration-testing/                   (Full pentest methodology, OSCP prep)
│   ├── bug-bounty/                            (Bug bounty hunting methodology)
│   ├── osint/                                 (Reconnaissance & OSINT)
│   └── wireless-and-social-engineering/       (Human hacking, WiFi attacks)
│
├── 04-advanced-specialization/                ← Deep expertise tracks
│   ├── malware-and-reverse-engineering/       (Malware dev, RE, forensics)
│   ├── exploit-development/                   (Binary exploitation, shellcode)
│   ├── cloud-and-mobile/                      (AWS, Android, iOS, AD attacks)
│   └── threat-hunting-and-incident-response/  (Blue team, IR, forensics)
│
├── 05-cheatsheets-and-reference/              ← Quick reference material
│   ├── tools/                                 (Cheatsheets for tools)
│   ├── interview-prep/                        (CISSP, CEH, INSA exam notes)
│   └── methodology/                           (Pentest checklists, OWASP guides)
│
├── Linux-Books-master/                        ← 36 Linux reference books
├── My-CyberSecurity-Store-main/               ← Notes, writeups, programming refs
├── awesome-pentest-cheat-sheets-main/         ← Pentest cheatsheet collection
└── misc/                                      ← Non-cyber / unclassified
```

---


---

## 🌐 Quick Access: External Portals & Practice Labs

| Platform | Domain / Focus | URL |
|---|---|---|
| **PortSwigger Web Security Academy** | Interactive Web Security & Burp Labs (Free labs & certifications) | [portswigger.net/web-security](https://portswigger.net/web-security) |
| **TryHackMe** | Gamified, guided hands-on security rooms & pathways | [tryhackme.com](https://tryhackme.com/) |
| **HackTheBox Academy** | Hands-on offensive security modules & skill tiers | [academy.hackthebox.com](https://academy.hackthebox.com/) |
| **picoCTF** | Beginner-to-intermediate jeopardy-style CTF wargames (CMU) | [picoctf.org](https://picoctf.org/) |
| **OverTheWire Bandit** | Command line, Linux navigation, and shell security wargames | [overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit/) |
| **GTFOBins** | Curated Unix binaries used to bypass local security restrictions | [gtfobins.github.io](https://gtfobins.github.io/) |
| **OWASP Top 10 Project** | The global standard for web application risk awareness | [owasp.org/www-project-top-ten](https://owasp.org/www-project-top-ten/) |
| **IppSec Search** | Searchable database of machine walkthrough videos & tools | [ippsec.rocks](https://ippsec.rocks/) |

---

## 🎓 Free Academic Lectures, Courses & Training

| Resource | Specialty / Curriculum | URL |
|---|---|---|
| **OpenSecurityTraining2 (OST2)** | World-class free reverse engineering, x86/x64 assembly, vulnerability hunting | [ost2.fyi](https://ost2.fyi/) |
| **Professor Messer** | Complete free video training courses for CompTIA Security+, Network+, and A+ | [professormesser.com](https://www.professormesser.com/) |
| **SEED Labs (Syracuse University)** | University-level hands-on security labs (Crypto, Web, Network, Linux) | [seedsecuritylabs.org](https://seedsecuritylabs.org/) |
| **pwn.college (Arizona State University)** | Full-credit university course on binary exploitation, shellcoding, & memory errors | [pwn.college](https://pwn.college/) |
| **Antisyphon Free Training (BHIS)** | Regular live, hands-on pay-what-you-can & free workshops from Black Hills InfoSec | [antisyphontraining.com](https://www.antisyphontraining.com/) |
| **SANS Cyber Aces Online** | Foundational self-paced courses in operating systems, networking, and security | [cyberaces.org](http://www.cyberaces.org/) |
| **Cybrary (Free Tier)** | Introductory courses on SOC analysis, penetration testing, and compliance | [cybrary.it](https://www.cybrary.it/) |
| **Cryptopals Crypto Challenges** | Progressive real-world cryptography breaking challenges | [cryptopals.com](https://cryptopals.com/) |

---

## 📺 Recommended YouTube Channels

| Channel | Focus Area | Link |
|---|---|---|
| **IppSec** | HackTheBox walkthroughs, methodical enumeration, exploit methodology | [youtube.com/@IppSec](https://www.youtube.com/@IppSec) |
| **LiveOverflow** | Binary exploitation, hardware hacking, CTF breakdowns, reverse engineering | [youtube.com/@LiveOverflow](https://www.youtube.com/@LiveOverflow) |
| **John Hammond** | CTF walkthroughs, malware analysis, incident response, security news | [youtube.com/@JohnHammondAudio](https://www.youtube.com/@JohnHammondAudio) |
| **PwnFunction** | Visual, animated web vulnerability explanations (XSS, CSRF, SSRF) | [youtube.com/@PwnFunction](https://www.youtube.com/@PwnFunction) |
| **NetworkChuck** | High-energy networking, Linux fundamentals, and hands-on tool intros | [youtube.com/@NetworkChuck](https://www.youtube.com/@NetworkChuck) |
| **David Bombal** | Networking, Python automation, Wireshark, hardware and interview talks | [youtube.com/@DavidBombal](https://www.youtube.com/@DavidBombal) |
| **InsiderPhD** | Bug bounty methodology, API security, web application recon | [youtube.com/@InsiderPhD](https://www.youtube.com/@InsiderPhD) |
| **Computerphile** | Academic CS fundamentals, cryptography, hashing, and protocol logic | [youtube.com/@Computerphile](https://www.youtube.com/@Computerphile) |

---

## 🗺️ Learning Roadmap

Follow the phases in order. Each phase builds on the previous.

---

## 📗 Phase 1 — Foundations

> **Goal:** Build the core technical literacy every security professional needs before touching hacking tools.

---

### 🌐 Networking

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Data Communication & Computer Networks Tutorial](./01-foundations/networking/data_communication_computer_network_tutorial.pdf) | Covers OSI model, TCP/IP, routing, switching — the essential network knowledge for any security role. |
| `[ ]` | [Linux Networking 101](./01-foundations/networking/Linux%20Networking%20101.pdf) | Practical Linux-side networking: interfaces, routing tables, netstat, ss, and packet inspection. |
| `[ ]` | [DNS Security Guide](./01-foundations/networking/DNS%20Security%20Guide.pdf) | Deep dive into DNS architecture, common DNS attacks (poisoning, hijacking), and defenses. |
| `[ ]` | [Handbook of Computer Networks and Cyber Security](./01-foundations/networking/Gupta%20B%20Handbook%20of%20Computer%20Networks%20and%20Cyber%20Security%202020.pdf) | Comprehensive reference covering network architectures, protocols, and cyber threats in one volume. |

---

### 🐧 Linux & Shell Scripting

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Linux Bible, 9th Edition](./01-foundations/linux-and-shell/Linux%20Bible%2C%209th%20Edition.pdf) | The definitive Linux reference covering system administration, file management, services, and networking. |
| `[ ]` | [Linux for Beginners](./01-foundations/linux-and-shell/Linux%20for%20Beginners.pdf) | Gentle introduction to the Linux command line and filesystem — start here if you're new to Linux. |
| `[ ]` | [Kali Linux Tutorial](./01-foundations/linux-and-shell/kali_linux_tutorial.pdf) | Focused tutorial on navigating and using Kali Linux specifically for security work. |
| `[ ]` | [Linux Admin Tutorial](./01-foundations/linux-and-shell/linux_admin_tutorial.pdf) | System administration fundamentals: user management, permissions, services, and log analysis. |
| `[ ]` | [Linux Basics for Hackers](./01-foundations/linux-and-shell/Linux%20Basics%20for%20Hackers_%20Getting%20Started%20with%20Networking%2C%20Scripting%2C%20and%20Security%20in%20Kali.pdf) | Covers Linux skills specifically from a hacker's perspective — networking, scripting, and Kali tools. |
| `[ ]` | [Linux Command Line and Shell Scripting Bible, 3rd Ed.](./01-foundations/linux-and-shell/Linux%20Command%20Line%20and%20Shell%20Scripting%20Bible%2C%203rd%20Edition.pdf) | Exhaustive coverage of bash scripting, shell utilities, and automation for power users. |
| `[ ]` | [Linux Shell Scripting with Bash](./01-foundations/linux-and-shell/Ken%20O.%20Burtch%20-%20Linux%20Shell%20Scripting%20with%20Bash-Sams%20%282004%29.pdf) | Classic hands-on bash scripting guide covering control flow, functions, and real-world script patterns. |
| `[ ]` | [Bash Cookbook](./01-foundations/linux-and-shell/Bash%20Cookbook_%20Solutions%20and%20Examples%20for%20Bash%20Users%20-%20Carl%20Albing%20%26%20Jp%20Vossen.pdf) | Solutions-oriented cookbook for everyday bash tasks, string manipulation, file processing, and automation. |
| `[ ]` | [Learning the Bash Shell, 2nd Edition](./01-foundations/linux-and-shell/Learning%20the%20Bash%20Shell%2C%202nd%20Edition%20-%20Cameron%20Newham%20%26%20Bill%20Rosenblatt.pdf) | O'Reilly classic — comprehensive bash from basic syntax through advanced job control and scripting. |
| `[ ]` | [Linux Bible by Christopher Negus](./01-foundations/linux-and-shell/linux-bible-by-christopher-negus.pdf) | Full-spectrum Linux reference with real-world sysadmin and security use cases. |
| `[ ]` | [Linux For Hackers](./01-foundations/linux-and-shell/Linux%20For%20Hackers.pdf) | Targeted guide focusing on the Linux tools and techniques most relevant to penetration testers. |
| `[ ]` | [Pro Bash Programming](./01-foundations/linux-and-shell/Pro%20Bash%20Programming_%20Scripting%20the%20Linux%20Shell%20-%20Chris%20Johnson%20-%20Google%20Books.pdf) | Advanced bash programming patterns for building robust, reusable shell scripts. |

---

### 🐍 Programming — Python

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [A Smarter Way to Learn Python](./01-foundations/programming/python/A%20Smarter%20Way%20to%20Learn%20Python%20-%20Learn%20it%20faster.%20Remember%20it%20longer.%20by%20Mark%20Myers.pdf) | Memory-friendly beginner Python course using active recall and exercises — ideal if Python is new to you. |
| `[ ]` | [Python Data Structures and Algorithms](./01-foundations/programming/python/Python%20Data%20Structures%20and%20Algorithms.pdf) | Covers essential CS fundamentals in Python — lists, trees, graphs, sorting — needed for writing security tools. |
| `[ ]` | [Python Web Penetration Testing Cookbook](./01-foundations/programming/python/Python%20Web%20Penetration%20Testing%20Cookbook%20by%20Cameron%20Buchanan.pdf) | Recipe-style book for automating web pentesting tasks with Python — fuzzing, scraping, and attacking APIs. |
| `[ ]` | [Gray Hat Python](./01-foundations/programming/python/Gray%20Hat%20Python.pdf) | Python for security researchers: debuggers, fuzzers, and Windows internals exploits using Python. |
| `[ ]` | [Black Hat Python](./01-foundations/programming/python/Black%20Hat%20Python%20-%20Python%20Programming%20for%20Hackers%20and%20Pentesters%20by%20Justin%20Seitz.pdf) | Classic offensive Python: network sniffers, trojans, keyloggers, and C2 tools from scratch. |

---

### 💻 Programming — Bash & Other Languages

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Black Hat Bash](./01-foundations/programming/bash/Black-Hat-Bash.pdf) | Offensive bash scripting for red teamers — post-exploitation automation, evasion, and tool building. |
| `[ ]` | [Penetration Testing with the Bash Shell](./01-foundations/programming/bash/Penetration%20Testing%20with%20the%20Bash%20shell.pdf) | Using bash as a penetration testing platform — recon, exploitation, and reporting via shell scripts. |
| `[ ]` | [Rust Tutorial](./01-foundations/programming/other-languages/rust_tutorial.pdf) | Introduction to Rust programming — useful for writing high-performance, memory-safe security tools. |
| `[ ]` | [Black Hat Go](./01-foundations/programming/other-languages/Black-Hat-Go_Go-Programming-For-Hackers-and-Pentesters.pdf) | Using Go for offensive security: network scanners, proxy tools, C2 frameworks, and post-exploitation. |

---

## 📘 Phase 2 — Core Security

> **Goal:** Understand fundamental security concepts, attacks, and industry-standard tools.

---

### 🌍 Web Security

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [OWASP Top 10 — 2017](./02-core-security/web-security/OWASP%20Top%2010-2017%20%28en%29.pdf) | The definitive list of the 10 most critical web application security risks with examples and mitigations. |
| `[ ]` | [OWASP API Security Top 10](./02-core-security/web-security/owasp-api-security-top-10.pdf) | Modern API-specific security risks — authentication flaws, excessive data exposure, and injection in REST/GraphQL. |
| `[ ]` | [OWASP Testing Guide v4 (OTGv4)](./02-core-security/web-security/OTGv4.pdf) | Comprehensive web application penetration testing methodology from OWASP — the industry standard test guide. |
| `[ ]` | [SQL Injection](./02-core-security/web-security/SQL.INJECTION.pdf) | Deep technical coverage of SQL injection — in-band, blind, time-based, and union-based exploitation. |
| `[ ]` | [MSSQL Injection Cheat Sheet](./02-core-security/web-security/MSSQL%20Injection%20Cheat%20Sheet%20_%20pentestmonkey.pdf) | Pentestmonkey's famous MSSQL-specific injection payloads and techniques for database enumeration. |
| `[ ]` | [PortSwigger XSS Cheat Sheet](./02-core-security/web-security/PortSwigger%20Cross-site%20scripting%20%28XSS%29%20cheat%20sheet.pdf) | PortSwigger's comprehensive XSS payload reference — context-specific bypasses and filter evasions. |
| `[ ]` | [IDOR and HTTP Security Headers](./02-core-security/web-security/IDOR%20and%20HTTP%20Security%20Headers.pdf) | Covers IDOR vulnerabilities with real examples and HTTP security headers that prevent common attacks. |
| `[ ]` | [Hacking Web Applications — Hacking Exposed](./02-core-security/web-security/19.%20Hacking%20Web%20Applications%20-%20Hacking%20Exposed.pdf) | Classic Hacking Exposed chapter covering web attack patterns and countermeasures. |
| `[ ]` | [Application Security Awareness](./02-core-security/web-security/APPLICATION%20SECURITY%20AWARENESS.pdf) | Broad application security overview — threat modeling, SDLC security, and common vulnerability classes. |

---

### 🔒 Network Security

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [WiFi Hack-Proof Your Wireless Network](./02-core-security/network-security/WiFi.HackProofYourWirelessNetwork.pdf) | Practical guide to securing wireless networks — WPA2, rogue APs, monitoring, and defenses. |
| `[ ]` | [WiFi Hacking for Beginners](./02-core-security/network-security/WiFi_Hacking_for_Beginners_Learn.1.pdf) | Introductory wireless hacking: WEP/WPA cracking, handshake captures, and deauth attacks. |
| `[ ]` | [Attacking Network Protocols](./02-core-security/network-security/Attacking-Network-Protocols-A-Hacker-s-Guide-to-Capture-Analysis-and-Exploitation.pdf) | James Forshaw's deep dive into network protocol analysis, fuzzing, and exploitation techniques. |
| `[ ]` | [Network Security Checklists](./02-core-security/network-security/Network%20Security%20Checklists.pdf) | Practical checklists for network hardening, firewall rules, and security assessments. |
| `[ ]` | [Network Security Musts](./02-core-security/network-security/Network%20Security%20Musts.pdf) | Key must-do network security controls and configurations for defending infrastructure. |
| `[ ]` | [Hacking Exposed Network Security](./02-core-security/network-security/Hacking%20Exposed%20Network%20Securi%20-%20Unknown_1243.pdf) | Network-layer attacks — scanning, sniffing, and spoofing from the Hacking Exposed series. |

---

### 🔧 Security Tools (Kali, Metasploit, and More)

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Kali Linux Revealed 2021 Edition](./02-core-security/tools/Kali-Linux-Revealed-2021-edition.pdf) | The official Kali Linux book — installation, configuration, tools overview, and custom builds. |
| `[ ]` | [20 Fantastic Kali Linux Tools](./02-core-security/tools/20FantasticKaliLinuxTools-1.pdf) | Curated walkthrough of 20 essential Kali tools with usage examples for each. |
| `[ ]` | [All Kali Linux Commands](./02-core-security/tools/All%20Kali%20Linux%20Commands.pdf) | Quick command reference for the full Kali Linux toolset — great desk reference. |
| `[ ]` | [Metasploit Framework](./02-core-security/tools/005Metasploit.Framework.pdf) | Core Metasploit concepts: modules, payloads, sessions, and the msfconsole workflow. |
| `[ ]` | [Metasploit — The Penetration Tester's Guide](./02-core-security/tools/Metasploit%20-%20The%20Penetration%20Tester%27s%20Guide%20by%20David%20Kennedy.pdf) | The definitive Metasploit book by David Kennedy — from exploitation to advanced post-exploitation. |
| `[ ]` | [Metasploit Unleashed](./02-core-security/tools/Metasploit%20Unleashed.pdf) | Offensive Security's free Metasploit course in PDF — comprehensive practical coverage. |
| `[ ]` | [The Easiest Metasploit Guide](./02-core-security/tools/44040-the-easiest-metasploit-guide-you%E2%80%99ll-ever-read.pdf) | Beginner-friendly Metasploit walkthrough — ideal for first-time users of the framework. |
| `[ ]` | [Inside Metasploit — Automating Meterpreter](./02-core-security/tools/Inside%20Metasploit.%20Automating%20meterpreter.pdf) | Advanced Meterpreter automation, scripting, and building custom post-exploitation modules. |
| `[ ]` | [Beginning Ethical Hacking with Kali Linux](./02-core-security/tools/Beginning%20Ethical%20Hacking%20with%20Kali%20Linux_%20Computational%20Techniques%20for%20Resolving%20Security%20Issues.pdf) | Entry-level Kali guide bridging theory and practice for beginners entering ethical hacking. |
| `[ ]` | [Mastering Kali Linux for Advanced Penetration Testing](./02-core-security/tools/Mastering%20Kali%20Linux%20for%20Advanced%20Penetration%20Testing%20by%20Robert%20W.%20Beggs.pdf) | Packt's advanced Kali book — covers sophisticated attack chains, custom tools, and evasion. |

---

## 📙 Phase 3 — Intermediate Labs & Practice

> **Goal:** Apply your knowledge with real hands-on pentest methodology, bug bounty hunting, and reconnaissance.

> 🎯 **Hands-On Lab Portals & Search Tools:**
> - [picoCTF Portal](https://picoctf.org/) (CMU beginner-to-intermediate jeopardy wargames)
> - [TryHackMe Labs](https://tryhackme.com/) & [HackTheBox](https://hackthebox.com/)
> - [IppSec Rocks Search Engine](https://ippsec.rocks/) (Search machine walkthroughs by vulnerability/tool)
> - [GTFOBins](https://gtfobins.github.io/) (Privilege escalation via Unix binaries)

---

### 💥 Penetration Testing

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Introduction to Ethical Hacking](./03-intermediate-labs/penetration-testing/001Introduction.To.Ethical.Hacking.pdf) | Foundation course covering the ethical hacking lifecycle, phases, and legal considerations. |
| `[ ]` | [System Hacking Lab](./03-intermediate-labs/penetration-testing/005System.Hacking.LAB.pdf) | Hands-on lab guide for system hacking — password cracking, privilege escalation, and covering tracks. |
| `[ ]` | [DOS Lab](./03-intermediate-labs/penetration-testing/009DOS.LAB.pdf) | Denial-of-service attack lab covering flood attacks, amplification, and countermeasures. |
| `[ ]` | [OSSTMM 3](./03-intermediate-labs/penetration-testing/OSSTMM.3.pdf) | The Open Source Security Testing Methodology Manual — the authoritative industry pentest methodology. |
| `[ ]` | [Basic Knowledge of Pentesting](./03-intermediate-labs/penetration-testing/Basic.knowldges.of.Pentesting.1.pdf) | Broad pentesting primer covering enumeration, exploitation, and reporting for beginners. |
| `[ ]` | [Red Teaming Fundamentals — Codelivly Day 01](./03-intermediate-labs/penetration-testing/Codelivly%20-%20Day%2001%20-%20Red%20Teaming%20Fundamentals.pdf) | Introduction to red team operations — adversary simulation, TTPs, and team structure. |
| `[ ]` | [Penetration Testing: Hands-On Introduction](./03-intermediate-labs/penetration-testing/Penetration%20Testing%20A%20Hands-On%20Introduction%20to%20Hacking%20by%20Georgia%20Weidman.pdf) | Georgia Weidman's celebrated pentesting textbook — lab setup through exploitation and reporting. |
| `[ ]` | [Advanced Penetration Testing](./03-intermediate-labs/penetration-testing/advancedpenetrationtesting.pdf) | Advanced techniques: custom exploits, lateral movement, and complex attack chains against hardened targets. |
| `[ ]` | [OSCP Preparation Material](./03-intermediate-labs/penetration-testing/oscpmain.pdf) | OSCP-prep material covering the full Offensive Security certification exam scope. |
| `[ ]` | [The Basics of Hacking and Penetration Testing](./03-intermediate-labs/penetration-testing/Patrick%2BEngebretson%2BThe%2BBasics%2Bof%2BHacking%2Band%2BPenetration%2BTesting%2C%2BSecond%2BEdition%2B%282013%29.pdf) | Patrick Engebretson's accessible step-by-step hacking methodology — great for structured learners. |
| `[ ]` | [BackTrack Lab Guide v3.2](./03-intermediate-labs/penetration-testing/Penetration%20Testing%20with%20BackTrack%20%28Lab%20Guide%29%20v3.2%20-%20Offensive%20Security.pdf) | Offensive Security's original lab guide — foundational hands-on exercises still relevant today. |
| `[ ]` | [Post-Exploitation — Ethical Hacking](./03-intermediate-labs/penetration-testing/Ethickal-haking-postexploitation.pdf) | Covers post-exploitation phases: persistence, lateral movement, data exfiltration, and cleanup. |
| `[ ]` | [Penetration Testing Report Sample](./03-intermediate-labs/penetration-testing/Penetration%20testing%20Report%20of%20company%20xyz.pdf) | Real-world sample pentest report — use as a template when writing professional reports. |
| `[ ]` | [Infrastructure Pentest Checklist](./03-intermediate-labs/penetration-testing/Infrastructure%20Penetration%20Testing%20Checklist.pdf) | Structured checklist for methodical infrastructure assessments — never miss a test category. |
| `[ ]` | [The Pentester Blueprint](./03-intermediate-labs/penetration-testing/pdfcoffee.com_the-pentester-blueprint-pdf-free.pdf) | Career and skill development roadmap for breaking into professional penetration testing. |
| `[ ]` | [Ethical Hacker's Playbook](./03-intermediate-labs/penetration-testing/Ethical%20Hacker%E2%80%99s%20Playbook_%20Supercharging%20Your%20Approach%20to%20Ethical%20Hacking%20_%20by%20CyberObito%20_%20Nov%2C%202023%20_%20Medium.pdf) | Modern ethical hacking strategies with up-to-date toolchains, methodology, and mindset advice. |

---

### 🏆 Bug Bounty Hunting

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Bug Bounty Bootcamp](./03-intermediate-labs/bug-bounty/Bug%20Bounty%20Bootcamp%20The%20Guide%20to%20Finding%20and%20Reporting%20Web%20Vulnerabilities%20by%20Vickie%20Li.pdf) | Vickie Li's comprehensive bug bounty guide — recon, enumeration, vulnerability classes, and report writing. |
| `[ ]` | [Bug Bounty Playbook V2](./03-intermediate-labs/bug-bounty/Bug-Bounty-Playbook-V2.pdf) | Advanced playbook with detailed attack patterns, tooling setups, and target selection strategies. |
| `[ ]` | [Bug Bounty Hunting Essentials](./03-intermediate-labs/bug-bounty/bug-bounty-hunting-essentials-p2p.pdf) | Core skills for bug bounty hunters: scope reading, HTTP analysis, subdomain enumeration, and triage. |
| `[ ]` | [BUG BOUNTY HUNTING — Methodology, Toolkit, Tips](./03-intermediate-labs/bug-bounty/BUG%20BOUNTY%20HUNTING%20%28METHODOLOGY%20%2C%20TOOLKIT%20%2C%20TIPS%20%26%20TRICKS%20%2C%20Blogs%29%20_%20by%20Sanyam%20Chawla%20_%20InfoSec%20Write-ups.pdf) | Community-compiled bug bounty methodology with toolkit recommendations and tips. |
| `[ ]` | [A Bug Hunter's Diary](./03-intermediate-labs/bug-bounty/A%20Bug%20Hunter%20%20039%20s%20Diary%20%20A%20Guided%20Tour%20Through%20the%20Wilds%20of%20Software%20Security.pdf) | Real-world bug hunting narratives — follow along as the author discovers and exploits real vulnerabilities. |
| `[ ]` | [Complete Bug Bounty Recon Fundamentals](./03-intermediate-labs/bug-bounty/Complete%20Bug%20Bounty%20Recon%20Fundamentals.%20_%20by%20Sagar%20Shewale%20_%20Medium.pdf) | Detailed reconnaissance methodology — asset discovery, subdomain enumeration, and fingerprinting. |
| `[ ]` | [Hacking APIs — Early Access](./03-intermediate-labs/bug-bounty/Hacking%20APIs%20-%20Early%20Access.pdf) | API security testing — authentication bypass, BOLA, mass assignment, and GraphQL attacks. |
| `[ ]` | [Bug Bounty Training Program](./03-intermediate-labs/bug-bounty/Bug%20Bounty%20Training%20Program%20%28Online%29.pdf) | Structured training curriculum for becoming a professional bug bounty hunter. |
| `[ ]` | [Bug Bounty Cheat Sheet Complete](./03-intermediate-labs/bug-bounty/Bug%20bounty%20cheat%20sheet%20complete.pdf) | Quick-reference payload lists and methodology reminders for active bug hunting sessions. |
| `[ ]` | [Breaking Into Information Security](./03-intermediate-labs/bug-bounty/Breaking_into_Information_Security_Learn.pdf) | Career guide for transitioning into infosec — certifications, labs, networking, and job search. |

---

### 🕵️ OSINT & Reconnaissance

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [OSINT Handbook](./03-intermediate-labs/osint/OSINT_Handbook_June-2018_Final.pdf) | Comprehensive OSINT methodology covering social media, public records, dark web, and investigative techniques. |
| `[ ]` | [21 OSINT Research Tools for Threat Intelligence](./03-intermediate-labs/osint/21%20OSINT%20RESEARCH%20TOOLS%20FOR%20THREAT%20INTELLIGENCE.pdf) | Curated toolkit of 21 OSINT tools with use cases for threat intelligence workflows. |
| `[ ]` | [A Methodical Framework for Reconnaissance](./03-intermediate-labs/osint/A_Methodical_Framework_for_Conducting_Reconnaissan.pdf) | Structured recon framework covering passive and active information gathering phases. |
| `[ ]` | [Dangerous Google Searching](./03-intermediate-labs/osint/Micha%C5%82%20%20Piotrowski%20-%20Dangerous%20Google%20Searching.pdf) | Google dorking techniques for finding exposed credentials, directories, configs, and sensitive data. |
| `[ ]` | [Extreme Privacy — Mobile Devices](./03-intermediate-labs/osint/Extreme%20Privacy%20-%20Mobile%20Devices%20%40redbluehit.pdf) | Mobile OSINT and privacy — how attackers track mobile devices and how to counter surveillance. |

---

### 📡 Wireless & Social Engineering

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Hacking the Human — Social Engineering](./03-intermediate-labs/wireless-and-social-engineering/Ian_Mann_Hacking_the_human_social_engineering_techniques_and_security.pdf) | Ian Mann's authoritative book on social engineering psychology, tactics, and organizational defenses. |
| `[ ]` | [The Art of Intrusion — Kevin Mitnick](./03-intermediate-labs/wireless-and-social-engineering/Kevin_Mitnick_-_The_Art_of_Intrusion.pdf) | Mitnick's real break-in stories revealing how attackers combine technical and social methods. |
| `[ ]` | [Computer Hacking Beginners Guide — Wireless](./03-intermediate-labs/wireless-and-social-engineering/Computer%20Hacking%20Beginners%20Guide%20How%20to%20Hack%20Wireless%20Network%2C%20Basic.pdf) | Beginner intro to wireless network hacking covering WEP/WPA attacks and basic exploitation. |
| `[ ]` | [Executive Guide to Human Security Testing](./03-intermediate-labs/wireless-and-social-engineering/executive-guide-to-human-security-testing-ebook.pdf) | How organizations test their human attack surface — phishing simulations and tabletop exercises. |

---

## 📕 Phase 4 — Advanced Specialization

> **Goal:** Deep expertise in specialist tracks. Pick the track(s) matching your career direction.

---

### 🦠 Malware Analysis & Reverse Engineering

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Malware Development for Ethical Hackers](./04-advanced-specialization/malware-and-reverse-engineering/Zhassulan_Zhussupov_Malware_Development_for_Ethical_Hackers_Learn.pdf) | Build real malware samples ethically — keyloggers, RATs, evasion techniques, and C2 comms. |
| `[ ]` | [Mastering Reverse Engineering](./04-advanced-specialization/malware-and-reverse-engineering/Mastering%20Reverse%20Engineering%20Re-engineer%20your%20ethical%20hacking%20skills%20by%20Reginald%20Wong%20%28z-lib.org%29.pdf) | Comprehensive RE guide — disassembly, debugging, binary analysis, and defeating anti-RE techniques. |
| `[ ]` | [Practical Malware Analysis](./04-advanced-specialization/malware-and-reverse-engineering/Practical%20Malware%20Analysis.pdf) | The essential malware analysis textbook — static/dynamic analysis, unpacking, and documenting behavior. |
| `[ ]` | [Introduction to Malware Analysis](./04-advanced-specialization/malware-and-reverse-engineering/INTRODUCTION%20TO%20MALWARE%20ANALYSIS.pdf) | Entry-level guide covering analysis environments, basic static analysis, and behavioral monitoring. |
| `[ ]` | [Malware Reverse Engineering Handbook](./04-advanced-specialization/malware-and-reverse-engineering/Malware%20Reverse%20Engineering%20Handbook.pdf) | Hands-on handbook for reversing malware binaries — IDA Pro/Ghidra workflows and real sample walkthroughs. |
| `[ ]` | [Malware Sandboxing](./04-advanced-specialization/malware-and-reverse-engineering/Malware%20Sandboxing.pdf) | Safely detonate and analyze malware in isolated sandboxes — Cuckoo and commercial platform techniques. |
| `[ ]` | [Malware Analysis 101](./04-advanced-specialization/malware-and-reverse-engineering/Malware%20Analysis%20101.pdf) | Quick-start guide for first-time analysts — tools, environment setup, and first analysis workflow. |
| `[ ]` | [Antivirus Hackers Handbook](./04-advanced-specialization/malware-and-reverse-engineering/Antivirus%20hackers%20handbook.pdf) | How AV works internally and how attackers bypass signatures, heuristics, and sandboxes. |
| `[ ]` | [Practical Forensic Imaging](./04-advanced-specialization/malware-and-reverse-engineering/practicalforensicimaging.pdf) | Forensically sound disk imaging — acquisition, verification, and chain of custody procedures. |
| `[ ]` | [Cyber Forensics](./04-advanced-specialization/malware-and-reverse-engineering/cyberforensics.pdf) | End-to-end digital forensics — evidence handling, memory analysis, and incident reconstruction. |

---

### 💣 Exploit Development

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Hacking: The Art of Exploitation, 2nd Edition](./04-advanced-specialization/exploit-development/Hacking%20-%20The%20Art%20of%20Exploitation%2C%202nd%20Edition%20by%20Jon%20Erickson.pdf) | Jon Erickson's classic — C programming, assembly, buffer overflows, and shellcode writing from scratch. |
| `[ ]` | [Penetration Testing with Shellcode](./04-advanced-specialization/exploit-development/Penetration%20Testing%20with%20Shellcode%20-%20Detect%2C%20exploit%2C%20and%20secure%20network-level%20and%20operating%20system%20vulnerabilities%20by%20Hamza%20Megahed.pdf) | Writing, encoding, and deploying shellcode for OS and network-level exploitation scenarios. |
| `[ ]` | [Gray Hat C#](./04-advanced-specialization/exploit-development/grayhatcsharp.pdf) | Using C# for offensive security — automation, network attacks, and Windows exploit development. |

---

### ☁️ Cloud & Mobile Security

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [AWS Security](./04-advanced-specialization/cloud-and-mobile/AWS%20SECURITY.pdf) | AWS cloud security fundamentals — IAM misconfigurations, S3 exposure, CloudTrail, and attack surface mapping. |
| `[ ]` | [Hands on AWS Penetration Testing](./04-advanced-specialization/cloud-and-mobile/Hands%20on%20AWS%20Penetration%20Testing.pdf) | Practical AWS pentest techniques — attacking cloud services and privilege escalation in AWS environments. |
| `[ ]` | [Android Hacker's Handbook](./04-advanced-specialization/cloud-and-mobile/Android%20Hacker%27s%20Handbook%20by%20Joshua%20J.%20Drake%2C%20Zach%20Lanier%2C%20Collin%20Mulliner%2C%20Pau%20Oliva%20Fora%2C%20Stephen%20A.%20Ridley%20and%20Georg%20Wicherski.pdf) | Deep Android security research — platform internals, vulnerability discovery, and exploitation. |
| `[ ]` | [Android Security Internals](./04-advanced-specialization/cloud-and-mobile/androidsecurityinternals.pdf) | Under-the-hood Android security — permissions model, Binder IPC, and security subsystems. |
| `[ ]` | [iOS Application Security](./04-advanced-specialization/cloud-and-mobile/iosapplicationsecurity.pdf) | iOS app security testing — data storage, transport security, authentication, and jailbreak analysis. |
| `[ ]` | [Attacking Active Directory](./04-advanced-specialization/cloud-and-mobile/ATTACKING%20ACTIVE%20DIRECTORY.pdf) | Real-world AD attacks — Kerberoasting, Pass-the-Hash, DCSync, and domain privilege escalation. |

---

### 🔵 Threat Hunting & Incident Response

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [Incident Response with Threat Intelligence](./04-advanced-specialization/threat-hunting-and-incident-response/incidentresponsewiththreatintelligence.pdf) | Integrating CTI into IR workflows — threat actor profiling, indicator enrichment, and faster response. |
| `[ ]` | [Cybersecurity Attack and Defense Strategies](./04-advanced-specialization/threat-hunting-and-incident-response/Cybersecurity_._Attack_and_Defense_Strategies_Infrastructure_security.pdf) | Infrastructure security from attacker and defender perspectives — covers kill chain and Zero Trust. |
| `[ ]` | [Cisco CyberOps Associate 200-201 Guide](./04-advanced-specialization/threat-hunting-and-incident-response/Cisco_Certified_CyberOps_Associate_200_201_Certification_Guide.pdf) | Full study guide for Cisco CyberOps cert — SOC operations, monitoring, analysis, and response. |
| `[ ]` | [ChatGPT for Cybersecurity Cookbook](./04-advanced-specialization/threat-hunting-and-incident-response/chatgptforcybersecuritycookbook.pdf) | Using AI/LLMs for security tasks — threat analysis, report generation, and automation with ChatGPT. |
| `[ ]` | [Cyber Incident Response Plan Guide](./04-advanced-specialization/threat-hunting-and-incident-response/CYBER%20INCIDENT%20RESPONSE%20PLAN%20GUIDE.pdf) | Building and executing an organizational incident response plan — detection, containment, eradication. |
| `[ ]` | [Cybersecurity Incident & Vulnerability Response Playbooks](./04-advanced-specialization/threat-hunting-and-incident-response/Cybersecurity%20Incident%20%26%20Vulnerability%20Response%20Playbooks.pdf) | Ready-to-use IR playbooks for phishing, ransomware, data breach, and DDoS incidents. |
| `[ ]` | [Maltego Handbook for Incident Response](./04-advanced-specialization/threat-hunting-and-incident-response/MALTEGO%20HANDBOOK%20FOR%20INCIDENT%20RESPONSE.pdf) | Using Maltego for IR — graph-based attack path reconstruction and threat actor attribution. |
| `[ ]` | [Intrusion Detection Guide](./04-advanced-specialization/threat-hunting-and-incident-response/Intrusion%20Detection%20Guide.pdf) | IDS/IPS concepts, signature writing, anomaly detection, and tuning to reduce false positives. |
| `[ ]` | [Incident Response Playbook — Phishing](./04-advanced-specialization/threat-hunting-and-incident-response/Incident%20response%20playbook%20-%20Phising%20Investigation%20part-1.pdf) | Step-by-step phishing investigation — header analysis, IOC extraction, and user remediation. |
| `[ ]` | [Guide to Vulnerability Management](./04-advanced-specialization/threat-hunting-and-incident-response/GUIDE%20TO%20VULNERABILITY%20MANAGEMENT%20WHITE%20PAPER.pdf) | Enterprise vuln management program design — scanning, prioritization, SLA tracking, and reporting. |

---

## 📓 Phase 5 — Cheatsheets & Reference

> **Use any time:** Quick lookups, exam prep, and methodology reminders during active work.

---

### 🗂️ Tool Cheatsheets

> See also: [`awesome-pentest-cheat-sheets-main/docs/`](./awesome-pentest-cheat-sheets-main/docs/) for Nmap, SQLMap, Metasploit, Wireshark, and PowerShell cheatsheets.

| Status | Resource | Description |
|--------|----------|-------------|
|  | [The Definitive Cybersecurity Tools Roadmap (Beginner → Elite PDF)](./05-cheatsheets-and-reference/tools/The_Cybersecurity_Tools_Roadmap_Beginner_to_Advanced.pdf) | Comprehensive 7-page tiered guide covering 25 essential security tools from Level 1 (Nmap/Wireshark) to Level 5 (WinDbg/Frida/JTAG) with commands and use cases. |
| `[ ]` | [Master Cheat Sheet](./05-cheatsheets-and-reference/tools/cheat-sheet.pdf) | General cybersecurity cheat sheet with commands, payloads, and tool syntax for quick reference. |
| `[ ]` | [Nmap Cheatsheet](./awesome-pentest-cheat-sheets-main/docs/nmap.md) | Nmap scan types, timing options, output formats, and scripting engine usage. |
| `[ ]` | [Metasploit Cheatsheet](./awesome-pentest-cheat-sheets-main/docs/Metasploit-CheatSheet.pdf) | Metasploit module navigation, handler setup, payload generation, and session management. |
| `[ ]` | [Wireshark Display Filters](./awesome-pentest-cheat-sheets-main/docs/Wireshark_Display_Filters.pdf) | Essential Wireshark filter syntax for isolating protocols, IPs, and suspicious traffic. |
| `[ ]` | [SQLMap Cheatsheet](./awesome-pentest-cheat-sheets-main/docs/sqlmap-cheatsheet-1.0-SDB.pdf) | SQLMap flags, tamper scripts, database enumeration, and OS command injection via SQLi. |
| `[ ]` | [PowerShell Cheatsheet v4.1](./awesome-pentest-cheat-sheets-main/docs/PowerShellCheatSheet_v41.pdf) | PowerShell for attackers and defenders — cmdlets, remoting, bypass techniques, and logging. |
| `[ ]` | [Shodan Cheatsheet](./awesome-pentest-cheat-sheets-main/docs/shodan.md) | Shodan search operators, filters, and API usage for Internet-facing asset discovery. |

---

### 📝 Interview & Certification Prep

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [200 IT Security Job Interview Questions](./05-cheatsheets-and-reference/interview-prep/200%20IT%20Security%20Job%20Interview%20Questions.pdf) | Comprehensive interview Q&A covering technical, behavioral, and scenario-based security questions. |
| `[ ]` | [CISSP Official Study Guide](./05-cheatsheets-and-reference/interview-prep/CISSP%20Official%20Study%20Guide.pdf) | Official ISC² CISSP guide — covers all 8 domains of the Common Body of Knowledge. |
| `[ ]` | [CEH Exam Blueprint v4.0](./03-intermediate-labs/bug-bounty/CEH-Exam-Blueprint-v4.0.pdf) | EC-Council's official CEH exam blueprint — topic weights, domain breakdown, and exam objectives. |
| `[ ]` | [Interview Q&A — Domain Wise](./My-CyberSecurity-Store-main/InterviewQuestion/Domain_Wise_Question.md) | Domain-organized interview questions: web security, Linux, crypto, networking, RE, and Windows. |

---

### 📋 Methodology & Checklists

| Status | Resource | Description |
|--------|----------|-------------|
| `[ ]` | [ANDS Roadmap](./05-cheatsheets-and-reference/methodology/ANDS_Roadmap.pdf) | Personal learning roadmap and goal-setting framework for structured skill development. |
| `[ ]` | [ANDS Reference](./05-cheatsheets-and-reference/methodology/ANDS_Reference.pdf) | Reference material companion to the ANDS methodology and curriculum. |
| `[ ]` | [OWASP Web App Penetration Checklist](./05-cheatsheets-and-reference/methodology/OWASP_Web_Application_Penetration_Checklist_v1_1.pdf) | OWASP's official web app pentest checklist — use during every web assessment for full coverage. |
| `[ ]` | [21-Day Program](./05-cheatsheets-and-reference/methodology/Combined_21_Day_Program_Bold_Large.pdf) | Structured 21-day learning sprint plan — use to create a focused study block for any topic. |

---

## 🗃️ Existing Resource Collections

These directories have their own internal organization and are kept intact. Browse them directly:

### 🐧 [Linux Books Master](./Linux-Books-master/)
36 Linux reference books (indexed in the folder's own [README](./Linux-Books-master/README.md)). Covers Linux administration, shell scripting, system programming, and Linux internals.

### 🔐 [My CyberSecurity Store](./My-CyberSecurity-Store-main/)
A rich personal knowledge store including:
- 📒 [Basic Of CyberSec/](./My-CyberSecurity-Store-main/Basic%20Of%20CyberSec/) — Beginner orientation materials
- 📖 [Books/](./My-CyberSecurity-Store-main/Books/) — 65+ curated books: Web App Hacker's Handbook, Real-World Bug Hunting, Blue Team Field Manual, Hacking APIs, Wireshark Practical Packet Analysis, and more
- 🛣️ [Roadmap/](./My-CyberSecurity-Store-main/Roadmap/) — CompTIA certifications map and learning path
- 💬 [InterviewQuestion/](./My-CyberSecurity-Store-main/InterviewQuestion/) — 11 domain-specific interview Q&A markdown files
- 💻 [Learn Programming/](./My-CyberSecurity-Store-main/Learn%20Programming/) — Notes for Python, Bash, JavaScript, C#, PHP, TypeScript, Go, Ruby, Rust, Perl, PowerShell
- 🌐 [Linux & Window Commands/](./My-CyberSecurity-Store-main/Linux%20%26%20Window%20Commands/) — Command reference README

### 📋 [Awesome Pentest Cheat Sheets](./awesome-pentest-cheat-sheets-main/)
Community cheatsheet collection with Nmap, Metasploit, Wireshark, SQLMap, PowerShell, Docker, and Shodan cheatsheets plus Python/JavaScript visual reference cards.

---

## 📊 Progress Tracker

| Phase | Topic | Resources |
|-------|-------|-----------|
| ✅ Phase 1 | Foundations (Networking, Linux, Programming) | 21 resources |
| 📘 Phase 2 | Core Security (Web, Network, Tools) | 25 resources |
| 📙 Phase 3 | Intermediate Labs (Pentest, Bug Bounty, OSINT) | 34 resources |
| 📕 Phase 4 | Advanced Specialization (Malware, Exploits, Cloud, IR) | 28 resources |
| 📓 Phase 5 | Cheatsheets & Reference | 18 resources |
| **🏁 Total** | | **126 resources** |

---

*Last updated: 2026-10-10 · Generated by Antigravity Cybersecurity Curriculum Designer*
