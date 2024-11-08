
### Notes ###

#### Windows ####

* To remove files which are "Access denied" use an elevated CMD and type  
  <code>sc config TrustedInstaller binPath= "cmd.exe /C del path/to/file"</code>  
  <code>sc start TrustedInstaller</code>  
  <code>sc config TrustedInstaller binPath= "C:\Windows\servicing\TrustedInstaller.exe"</code>  
* Or with Powershell type  
  <code>sc.exe start TrustedInstaller</code>  
  <code>$p = Get-NtProcess -Name TrustedInstaller</code>  
  <code>$proc = New-Win32Process cmd.exe -CreationFlags NewConsole -ParentProcess $p</code>  

* Interesting Metadata at downloaded files  
  <code>cd C:\Users\\...\Downloads</code>  
  <code>DIR /R</code>  
  <code>notepad ...:Zone.Identifier:$DATA</code>  
    reveals download URL and Referrer URL  

* To access all files of the WSL2 filesystem from W11 use Explorer e.g. `\\wsl$\Ubuntu-20.04\` or `wsl.localhost\Ubuntu-20.04\`

* list proxies: netsh interface portproxy show all

* Add the openSSH Feature  
* tunnel using rdp A: ssh -L 10000:localhost:3389 username@192.168.16.8 # login with username and password and keep shell open (do NOT use keys, use your brain)  
* tunnel using rdp B: mstsc /v:localhost:10000 # initiate the rdp session to the rdp server running at the remote(rdp server listens on localhost only)

* admin Powershell: (Get-MpPreference).ExclusionPath
* user  Powershell: & 'C:\Program Files\Windows Defender\MpCmdRun.exe' -Scan -ScanType 3 -File "C:\<path to check>|*" # would print "Scanning … was skipped"

#### Linux ####
##### Luks related commands
~~~
# create
dd if=/dev/urandom of=special.img bs=1M count=1024
cryptsetup --verify-passphrase luksFormat special.img
sudo cryptsetup open --type luks special.img myspecial
ls /dev/mapper/myspecial
sudo mkfs.ext4 -L myspecial /dev/mapper/myspecial
sudo cryptsetup close myspecial
sudo mkdir /myspecial
sudo chmod a+rwx /myspecial
# open
sudo cryptsetup open --type luks special.img myspecial
ls /dev/mapper/myspecial
sudo mount /dev/mapper/myspecial /myspecial
ls -alL /myspecial/
# close (don't forget it...)
sudo umount /myspecial
sudo cryptsetup close myspecial
~~~
#### debian 12 bookworm unable to install openssh-server, needed commands are:
~~~
mv -i /var/lib/apt/lists/deb.debian.org_debian_dists_bookworm_InRelease /root/
apt-get update
apt-get install openssh-server
~~~

#### Abbreviations ####

|Abbr|Description|URLs|
|-----|-----------|----|
ADS    | Alternate Data Streams (DIR /R)||
AES    | Advanced Encryption Standard||
AI     | Artificial Intelligence||
AMOLED | Active Matrix Organic LED||
API    | Application Programming Interface||
APK    | Android Package||
AR     | Augmented Reality||
ARP    | Address Resolution Protocol (IPv4) | https://en.wikipedia.org/wiki/Address_Resolution_Protocol|
ASM    | Attack Surface Management||
ATM    | Automated Teller Machine||
AV     | Antivirus||
BFS    | Breadth First Search (Queue)||
BU     | Backup||
CA     | Configuration Assessment, Compliance and Auditing||
CFG    | Classifier Free Guidance||
CFOR   | Cross Fork Object Reference||
CIS    | Center for Internet Security | https://de.wikipedia.org/wiki/Center_for_Internet_Security https://www.cisecurity.org/|
CKPT   | Checkpoint||
CNAME  | Canonical Name Record (see DNS)||
CNCF   | Cloud Native Computing Foundation||
CNF    | Conjunctive Normal Form||
CRTP   | Certified Red Team Professional||
CS     | Cloud Security / Container Security||
CSF    | Cyber Security Framework||
CSP    | Constraint Satisfaction Problem||
CTF    | Capture The Flag||
CVE    | Common Vulnerabilities and Exposures | https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures|
DDD    | Domain Driven Design||
DEFCON | Defense Condition | https://en.wikipedia.org/wiki/DEFCON https://defcon.org/ |
DFIR   | Digital Forensics and Incident Response||
DFS    | Depth First Search (Stack)||
DHCP   | Dynamic Host Configuration Protocol (Port Server 67, Client 68)||
DID    | Defense In Depth||
DLNA   | Digital Living Network Alliance||
DNS    | Domain Name System (Port 53)||
DOH    | DNS Over HTTPS||
DTP    | Desktop Publishing||
DVD    | Digital Video Disc||
E6     | Ethernet Globalization Protocols||
EAN    | Enterprise Area Network||
EDGE   | Enhanced Data Rates For Global Evolution||
EDR    | Endpoint Detection and Response||
ELK    | Elasticsearch, Logstash, Kibana||
ESN    | Electronic Serial Number||
ETL    | Extract, Transform, Load||
FIM    | File Integrity Monitoring||
FOAK   | First Of A Kind||
FP     | False Positive||
FSSAI  | Food Safety & Standards Authority Of India||
FTP    | File Transfer Protocol (Port 21)||
GBFS   | Greedy Best First Search||
GGP    | Gateway To Gateway Protocol||
GOOGLE | Global Organization Of Oriented Group Language Of Earth||
GPRS   | General Packet Radio Service||
GPS    | Global Positioning System||
GT     | Global Titles||
HDMI   | High Definition Multimedia Interface||
HIDS   | Host based Intrusion Detection System||
HTTP   | Hypertext Transfer Protocol (Port 80)||
HTTPS  | HTTP Secure (Port 443)||
HS     | Hotspot||
HSDPA  | High Speed Downlink Packet Access||
HSPA   | High Speed Packet Access||
HSUPA  | High Speed Uplink Packet Access||
ICANN  | Internet Corporation for Assigned Names and Numbers||
ICMP   | Internet Control Message Protocol||
ID     | Intrusion Detection||
IDS    | Intrusion Detection System||
IFSC   | Indian Financial System Code||
IGMP   | Internet Group Management Protocol||
IMAP   | Internet Message Access Protocol (Port 143)||
IMEI   | International Mobile Equipment Identity||
IMSI   | International Mobile Subscriber Identity||
IP     | Internet Protocol||
IPS    | Intrusion Prevention System||
IR     | Incident Response||
ISP    | Internet Service Provider||
JSON   | Java Script Object Notation
KE     | Knowledge Engineering||
KISS   | Keep It Simple Stupid||
LAN    | Local Area Network||
LCD    | Liquid Crystal Display||
LDA    | Log Data Analysis||
LED    | Light Emitting Diode||
LGTM   | Looks Good To Me||
LLM    | Large Language Model||
LOLBAS | Living Off The Land Binaries and Scripts (and Libraries) | https://github.com/LOLBAS-Project/LOLBAS/blob/master/README.md|
LORA   | Low Rank Adaptation||
MAN    | Metropolitan Area Network||
MD     | Manhattan Distance||
MFA    | Multifactor Authentication||
MGMT   | Management||
MIT    | Mitigation||
MOTW   | Mark Of The Web (M$ Windows)||
MTP    | Media Transfer Protocol||
MTTD   | Mean Time To Detect||
MTTR   | Mean Time To Resolution||
NDP    | Neighbor Discovery Protocol (IPv6)||
NDR    | Network Detection Response||
NF     | Normalized Float||
NFC    | Near Field Communication||
NIST   | US National Institute of Standards and Technology | https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology|
NMOT   | Nominal Module Operating Temperature||
NNTP   | Network News Transfer Protocol||
NOCT   | Normal Operating Cell Temperature||
NTP    | Network Time Protocol||
OLED   | Organic Light Emitting Diode||
OOTB   | Out Of The Box||
OS     | Operating System||
OSI    | Open Systems Interconnection||
OSSEC  | Open Source HIDS Security | https://en.wikipedia.org/wiki/OSSEC https://www.ossec.net/|
OTG    | On The Go||
PAN    | Personal Area Network||
PAN    | Permanent Account Number||
PDF    | Portable Document Format||
PE     | Portable Executable||
PK     | Passkeys||
PKI    | Public Key Infrastruture||
POI    | Point Of Interest||
POLAN  | Passive Optical Local Area Network||
POLP   | Principle Of Least Privilege||
POP3   | Post Office Protocol (Port 110)||
PPA    | Post Privacy Age||
PPI    | Pixels Per Inch||
PPP    | Point To Point Protocol | https://en.wikipedia.org/wiki/Point-to-Point_Protocol|
PTR    | Pointer Resource Record (see DNS)||
QOTD   | Quote of The Day (Port 17) | https://en.wikipedia.org/wiki/QOTD|
QVGA   | Quarter VGA||
RA     | Risk Analysis||
RAG    | Retrieval Augmented Generation||
RAM    | Random Access Memory||
RARP   | Reverse ARP | https://en.wikipedia.org/wiki/Reverse_Address_Resolution_Protocol|
RAT    | Remote Access Trojan||
RC     | Regulatory Compliance|||
RCE    | Remote Code Execution||
RDP    | Remote Desktop Protocol (Port 3389)||
ROM    | Read Only Memory||
RSA    | Rivest–Shamir–Adleman||
SAN    | Storage/System Area Network||
SCA    | Security Configuration Assessment||
SEM    | Security Event Management||
SFTP   | Secure file Transfer Protocol||
SIEM   | Security Information and Event Management aka SEM + SIM | https://en.wikipedia.org/wiki/Security_information_and_event_management|
SIM    | Security Information Management||
SIM    | Subscriber Identity Module||
SLCD   | Super Liquid Crystal Display||
SMB    | Server Message Block||
SMTP   | Simple Mail Transfer Protocol (Port 25)||
SNS    | Social Network Service||
SOA    | Start Of Authority||
SOAR   | Security Orchestration, Automation and Response||
SPI    | Serial Peripherial Interface||
SPOC   | Single Point Of Control||
SPOF   | Single Point Of Failure||
SS7    | Signaling System No. 7||
SSH    | Secure Shell (Port 22)||
SSL    | Secure Socket Layer||
STC    | Standard Test Conditions||
SWIFT  | Society For Worldwide Interbank Financial Telecommunication||
TCP    | Transmission Control Protocol||
TELNET | Teletype Network (Port 23) | https://en.wikipedia.org/wiki/Telnet|
TI     | Threat Intelligence||
TLS    | Transport Layer Security | https://en.wikipedia.org/wiki/Transport_Layer_Security|
UAC    | User Account Control||
UDP    | User Datagram Protocol||
UMTS   | Universal Mobile Telecommunications System||
UPS    | Uninterruptible Power Supply||
URL    | Uniform Resource Locator||
USB    | Universal Serial Bus||
USO    | Update Session Orchestrator||
UTC    | Coordinated Universal Time | https://en.wikipedia.org/wiki/Coordinated_Universal_Time|
VD     | Vulnerability Detection||
VGA    | Video Graphics Array/Adapter||
VM     | Vulnerability Management||
VPN    | Virtual Private Network||
VR     | Virtual Relity||
WAN    | Wide Area Network||
WIFI   | Wireless Fidelity||
WLAN   | Wireless Local Area Network||
WVGA   | Wide VGA||
WXGA   | Widescreen Extended Graphics Array||
XDR    | Extended Detection and Response System||
YAHOO  | Yet Another Hierarchical Officious Oracle | https://en.wikipedia.org/wiki/Yahoo!|
