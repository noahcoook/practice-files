import random

# Quiz data
questions = [
    {
        "question": "What should be the first step when implementing a comprehensive network security strategy?",
        "answers": [
            "Purchasing security tools",
            "Training employees",
            "Risk assessment and asset identification",
            "Installing security software"
        ],
        "correct": "Risk assessment and asset identification"
    },
    {
        "question": "What are the three main functional types of security controls?",
        "answers": [
            "Mandatory, Discretionary, Role-based",
            "Symmetric, Asymmetric, Hashing",
            "Physical, Technical, Administrative",
            "Preventive, Detective, Corrective"
        ],
        "correct": "Preventive, Detective, Corrective"
    },
    {
        "question": "True or False: Availability in the CIA Triad means that systems must be running 24/7 without any downtime.",
        "answers": ["False", "True"],
        "correct": "False"
    },
    {
        "question": "Which open source solution provides Security Information and Event Management (SIEM) capabilities in our course environment?",
        "answers": [
            "Splunk Enterprise",
            "ELK Stack (Elasticsearch, Logstash, Kibana)",
            "Microsoft SCOM",
            "IBM QRadar"
        ],
        "correct": "ELK Stack (Elasticsearch, Logstash, Kibana)"
    },
    {
        "question": "What is the primary open source alternative to Cisco ASA firewalls that we use in this course?",
        "answers": ["OpenWrt", "Smoothwall", "pfSense", "iptables"],
        "correct": "pfSense"
    },
    {
        "question": "True or False: Phishing is the most common type of social engineering attack used by cybercriminals today.",
        "answers": ["True", "False"],
        "correct": "True"
    },
    {
        "question": "Which attack involves injecting malicious scripts into web pages that are then executed by unsuspecting users' browsers?",
        "answers": [
            "Directory Traversal",
            "SQL Injection",
            "CSRF",
            "Cross-Site Scripting (XSS)"
        ],
        "correct": "Cross-Site Scripting (XSS)"
    },
    {
        "question": "In a typical cyber attack chain, what usually happens immediately after gaining initial access to a system?",
        "answers": [
            "Data exfiltration",
            "Network reconnaissance",
            "System destruction",
            "Privilege escalation"
        ],
        "correct": "Privilege escalation"
    },
    {
        "question": "What attack method involves using stolen username and password combinations from data breaches to access other accounts?",
        "answers": [
            "Brute force attack",
            "Social engineering",
            "Rainbow table attack",
            "Credential stuffing"
        ],
        "correct": "Credential stuffing"
    },
    {
        "question": "According to the NIST Cybersecurity Framework, what is the first step in developing an effective security strategy?",
        "answers": [
            "Training employees",
            "Risk assessment and asset identification",
            "Implementing firewalls",
            "Installing security software"
        ],
        "correct": "Risk assessment and asset identification"
    },
    {
        "question": "What are the five core functions of the NIST Cybersecurity Framework?",
        "answers": [
            "Assess, Design, Deploy, Operate, Maintain",
            "Plan, Implement, Monitor, Evaluate, Improve",
            "Prevent, Detect, Contain, Eradicate, Recover",
            "Identify, Protect, Detect, Respond, Recover"
        ],
        "correct": "Identify, Protect, Detect, Respond, Recover"
    },
    {
        "question": "Which type of security platform is specifically designed to automate incident response through playbooks and orchestration?",
        "answers": [
            "SOAR (Security Orchestration, Automation, and Response)",
            "DLP (Data Loss Prevention)",
            "IDS (Intrusion Detection System)",
            "SIEM (Security Information and Event Management)"
        ],
        "correct": "SOAR (Security Orchestration, Automation, and Response)"
    },
    {
        "question": "True or False: Detective security controls are designed to prevent security incidents before they occur.",
        "answers": ["False", "True"],
        "correct": "False"
    },
    {
        "question": "What is the standard formula for calculating cybersecurity risk?",
        "answers": [
            "Risk = Threat × Vulnerability × Impact",
            "Risk = Threat - Vulnerability + Impact",
            "Risk = Threat + Vulnerability + Impact",
            "Risk = Threat ÷ Vulnerability × Impact"
        ],
        "correct": "Risk = Threat × Vulnerability × Impact"
    },
    {
        "question": "True or False: The ELK Stack (Elasticsearch, Logstash, Kibana) can be used as an open source SIEM solution.",
        "answers": ["True", "False"],
        "correct": "True"
    },
    {
        "question": "What are the four main phases of the incident response lifecycle according to NIST?",
        "answers": [
            "Assess, Design, Implement, Monitor",
            "Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity",
            "Identify, Protect, Detect, Respond",
            "Plan, Do, Check, Act"
        ],
        "correct": "Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity"
    },
    {
        "question": "True or False: Corrective security controls are designed to prevent security incidents from occurring.",
        "answers": ["False", "True"],
        "correct": "False"
    },
    {
        "question": "Which open source vulnerability assessment tool is commonly used for network security scanning?",
        "answers": ["Rapid7 Nexpose", "OpenVAS", "Nessus", "Qualys"],
        "correct": "OpenVAS"
    },
    {
        "question": "Which security framework provides a prioritized set of actions for cybersecurity, focusing on the most effective security measures?",
        "answers": [
            "CIS Critical Security Controls",
            "ISO 27001",
            "ITIL",
            "COBIT"
        ],
        "correct": "CIS Critical Security Controls"
    },
    {
        "question": "Which open source tool is commonly used for file integrity monitoring on Linux systems?",
        "answers": [
            "Nmap",
            "Metasploit",
            "Wireshark",
            "AIDE (Advanced Intrusion Detection Environment)"
        ],
        "correct": "AIDE (Advanced Intrusion Detection Environment)"
    },
    {
        "question": "Which security solution specifically focuses on managing and controlling administrative and privileged user accounts?",
        "answers": [
            "Identity and Access Management (IAM)",
            "Multi-Factor Authentication (MFA)",
            "Single Sign-On (SSO)",
            "Privileged Access Management (PAM)"
        ],
        "correct": "Privileged Access Management (PAM)"
    },
    {
        "question": "Which metric measures the effectiveness of incident response teams in resolving security incidents?",
        "answers": [
            "Mean Time to Response (MTTR)",
            "Mean Time to Detection (MTTD)",
            "Recovery Time Objective (RTO)",
            "Service Level Agreement (SLA)"
        ],
        "correct": "Mean Time to Response (MTTR)"
    },
    {
        "question": "RADIUS uses TCP as its transport protocol.",
        "answers": ["True", "False"],
        "correct": "False"
    },
    {
        "question": "Which port does RADIUS use for authentication by default?",
        "answers": ["1813", "636", "389", "1812"],
        "correct": "1812"
    },
    {
        "question": "Multi-factor authentication requires at least three different authentication factors.",
        "answers": ["True", "False"],
        "correct": "False"
    },
    {
        "question": "Which FreeRADIUS configuration file defines RADIUS clients?",
        "answers": ["clients.conf", "users", "radiusd.conf", "eap.conf"],
        "correct": "clients.conf"
    },
    {
        "question": "Which command would generate the most secure SSH key pair for authentication?",
        "answers": [
            "ssh-keygen -t rsa -b 1024",
            "ssh-keygen -t rsa -b 2048",
            "ssh-keygen -t ed25519",
            "ssh-keygen -t dsa"
        ],
        "correct": "ssh-keygen -t ed25519"
    },
    {
        "question": "Which SSH configuration option represents a security best practice for production systems?",
        "answers": [
            "Port 22",
            "PasswordAuthentication yes",
            "AllowUsers *",
            "PermitRootLogin no"
        ],
        "correct": "PermitRootLogin no"
    },
    {
        "question": "What are the correct file permissions for the SSH authorized_keys file?",
        "answers": [
            "chmod 777 ~/.ssh/authorized_keys",
            "chmod 600 ~/.ssh/authorized_keys",
            "chmod 755 ~/.ssh/authorized_keys",
            "chmod 644 ~/.ssh/authorized_keys"
        ],
        "correct": "chmod 600 ~/.ssh/authorized_keys"
    },
    {
        "question": "What does CIS stand for in the context of security benchmarks?",
        "answers": [
            "Critical Infrastructure Security",
            "Cyber Intelligence Service",
            "Center for Internet Security",
            "Computer Information Systems"
        ],
        "correct": "Center for Internet Security"
    },
    {
        "question": "What should be the correct permissions for the /etc/shadow file?",
        "answers": ["755", "644", "777", "600"],
        "correct": "600"
    },
    {
        "question": "It's acceptable to leave unnecessary services running as long as they are properly configured.",
        "answers": ["True", "False"],
        "correct": "False"
    },
    {
        "question": "OpenSCAP can be used for automated security compliance scanning.",
        "answers": ["True", "False"],
        "correct": "True"
    },
    {
        "question": "Which iptables command would block all traffic from the network 192.168.100.0/24?",
        "answers": [
            "iptables -A INPUT -s 192.168.100.0/24 -j ACCEPT",
            "iptables -A INPUT -d 192.168.100.0/24 -j DROP",
            "iptables -A OUTPUT -s 192.168.100.0/24 -j DROP",
            "iptables -A INPUT -s 192.168.100.0/24 -j DROP"
        ],
        "correct": "iptables -A INPUT -s 192.168.100.0/24 -j DROP"
    },
    {
        "question": "A network administrator wants to create an ACL that allows HTTP and HTTPS traffic from any source but blocks all other traffic. Which approach is most secure?",
        "answers": [
            "Only create allow rules for ports 80 and 443 (implicit deny)",
            "Create a deny rule for all ports except 80 and 443",
            "Create allow rules for ports 80 and 443, then add an explicit deny-all rule",
            "Use a default allow policy with specific deny rules"
        ],
        "correct": "Create allow rules for ports 80 and 443, then add an explicit deny-all rule"
    },
    {
        "question": "Which type of firewall operates at Layer 7 of the OSI model and can perform deep packet inspection?",
        "answers": [
            "Next-Generation",
            "Stateful Inspection",
            "Application Layer",
            "Packet Filtering"
        ],
        "correct": "Application Layer"
    },
    {
        "question": "Which iptables target is commonly used for NAT when sharing internet access from an internal network?",
        "answers": ["MASQUERADE", "DNAT", "REDIRECT", "SNAT"],
        "correct": "MASQUERADE"
    },
    {
        "question": "Which iptables connection tracking states should be used to allow return traffic for established connections?",
        "answers": [
            "NEW,INVALID",
            "NEW,ESTABLISHED",
            "ESTABLISHED,RELATED",
            "INVALID,RELATED"
        ],
        "correct": "ESTABLISHED,RELATED"
    },
    {
        "question": "What is the default UDP port used by OpenVPN?",
        "answers": ["500", "1723", "443", "1194"],
        "correct": "1194"
    },
    {
        "question": "Which pfSense package is primarily used for threat intelligence feeds and geographic IP blocking?",
        "answers": ["Squid", "Suricata", "pfBlockerNG", "OpenVPN"],
        "correct": "pfBlockerNG"
    },
    {
        "question": "Which protocol does pfSense use for high availability and automatic failover?",
        "answers": [
            "GLBP (Gateway Load Balancing Protocol)",
            "VRRP (Virtual Router Redundancy Protocol)",
            "CARP (Common Address Redundancy Protocol)",
            "HSRP (Hot Standby Router Protocol)"
        ],
        "correct": "CARP (Common Address Redundancy Protocol)"
    }
]

def run_quiz():
    """Run the interactive quiz"""
    score = 0
    total = len(questions)
    
    print("=" * 70)
    print("NETWORK SECURITY QUIZ")
    print("=" * 70)
    print(f"\nTotal Questions: {total}\n")
    
    # Shuffle questions for variety
    quiz_questions = random.sample(questions, len(questions))
    
    for i, q in enumerate(quiz_questions, 1):
        print(f"\nQuestion {i}/{total}:")
        print("-" * 70)
        print(q["question"])
        print()
        
        # Shuffle answers
        shuffled_answers = q["answers"].copy()
        random.shuffle(shuffled_answers)
        
        # Display answers with letters
        for idx, answer in enumerate(shuffled_answers, 1):
            print(f"  {idx}. {answer}")
        
        # Get user input
        while True:
            try:
                user_answer = input("\nYour answer (enter number): ").strip()
                answer_num = int(user_answer)
                if 1 <= answer_num <= len(shuffled_answers):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(shuffled_answers)}")
            except ValueError:
                print("Please enter a valid number")
        
        # Check answer
        selected_answer = shuffled_answers[answer_num - 1]
        if selected_answer == q["correct"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. The correct answer is: {q['correct']}")
        
        print("-" * 70)
    
    # Display final score
    percentage = (score / total) * 100
    print("\n" + "=" * 70)
    print("QUIZ COMPLETED!")
    print("=" * 70)
    print(f"\nYour Score: {score}/{total} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("Grade: A - Excellent!")
    elif percentage >= 80:
        print("Grade: B - Good job!")
    elif percentage >= 70:
        print("Grade: C - Passing")
    elif percentage >= 60:
        print("Grade: D - Needs improvement")
    else:
        print("Grade: F - Study more and try again")
    
    print("=" * 70)

if __name__ == "__main__":
    run_quiz()
