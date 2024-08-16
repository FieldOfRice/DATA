
### Notes ###

#### Windows ####

To remove files which are "Access denied" use an elevated CMD and type  
  <code>sc config TrustedInstaller binPath= "cmd.exe /C del path/to/file"</code>  
  <code>sc start TrustedInstaller</code>  
  <code>sc config TrustedInstaller binPath= "C:\Windows\servicing\TrustedInstaller.exe"</code>  
Or with Powershell type  
  <code>sc.exe start TrustedInstaller</code>  
  <code>$p = Get-NtProcess -Name TrustedInstaller</code>  
  <code>$proc = New-Win32Process cmd.exe -CreationFlags NewConsole -ParentProcess $p</code>  

To access all files of the WSL2 filesystem from W11 use Explorer e.g. <code>\\wsl$\Ubuntu-20.04\</code>

#### Linux ####

Luks related commands:
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

#### Abbreviations ####

|Abbr|Description|URLs|
|-----|-----------|----|
AES    | Advanced Encryption Standard||
AI     | Artificial Intelligence||
AMOLED | Active Matrix Organic Light Emitting Diode||
ARP    | Address Resolution Protocol||
ASM    | Attack Surface Management||
ATM    | Automated Teller Machine||
AV     | Antivirus||
BU     | Backup||
CA     | Configuration Assessment, Compliance and Auditing||
CIS    | Center for Internet Security | https://de.wikipedia.org/wiki/Center_for_Internet_Security https://www.cisecurity.org/|
CRTP   | Certified Red Team Professional||
CS     | Cloud Security / Container Security||
CSF    | Cyber Security Framework||
CVE    | Common Vulnerabilities and Exposures | https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures|
DHCP   | Dynamic Host Configuration Protocol (Port Server 67, Client 68)||
DID    | Defense In Depth||
DLNA   | Digital Living Network Alliance||
DNS    | Domain Naming System (Port 53)||
DTP    | Desktop Publishing||
DVD    | Digital Video Disc||
E6     | Ethernet Globalization Protocols||
EAN    | Enterprise Area Network||
EDGE   | Enhanced Data Rates For Global Evolution||
EDR    | Endpoint Detection and Response||
ESN    | Electronic Serial Number||
FIM    | File Integrity Monitoring||
FOAK   | First Of A Kind||
FSSAI  | Food Safety & Standards Authority Of India||
FTP    | File Transfer Protocol (Port 21)||
GGP    | Gateway To Gateway Protocol||
GOOGLE | Global Organization Of Oriented Group Language Of Earth||
GPRS   | General Packet Radio Service||
GPS    | Global Positioning System||
HDMI   | High Definition Multimedia Interface||
HIDS   | Host based Intrusion Detection System||
HTTP   | Hypertext Transfer Protocol (Port 80)||
HTTPS  | HTTP Secure (Port 443)||
HS     | Hotspot||
HSDPA  | High Speed Downlink Packet Access||
HSPA   | High Speed Packet Access||
HSUPA  | High Speed Uplink Packet Access||
ICMP   | Internet Control Message Protocol||
ID     | Intrusion Detection||
IDS    | Intrusion Detection System||
IFSC   | Indian Financial System Code||
IGMP   | Internet Group Management Protocol||
IMAP   | Internet Message Access Protocol (Port 143)||
IMEI   | International Mobile Equipment Identity||
IPS    | Intrusion Prevention System||
IR     | Incident Response||
KISS   | Keep It Simple Stupid||
LAN    | Local Area Network||
LCD    | Liquid Crystal Display||
LDA    | Log Data Analysis||
LED    | Light Emitting Diode||
LLM    | Large Language Model||
MAN    | Metropolitan Area Network||
MFA    | Multifactor Authentication||
MGMT   | Management||
MIT    | Mitigation||
MOTW   | Mark Of The Web (M$ Windows)||
MTP    | Media Transfer Protocol||
MTTD   | Mean Time To Detect||
MTTR   | Mean Time To Resolution||
NDR    | Network Detection Response||
NFC    | Near Field Communication||
NIST   | US National Institute of Standards and Technology | https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology|
NNTP   | Network News Transfer Protocol||
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
PK     | Passkeys||
POI    | Point Of Interest||
POLAN  | Passive Optical Local Area Network||
POLP   | Principle Of Least Privilege||
POP3   | Post Office Protocol (Port 110)||
PPI    | Pixels Per Inch||
PPP    | Point To Point Protocol | https://en.wikipedia.org/wiki/Point-to-Point_Protocol|
QOTD   | Quote of The Day (Port 17) | https://en.wikipedia.org/wiki/QOTD|
QVGA   | Quarter VGA||
RA     | Risk Analysis||
RAG    | Retrieval Augmented Generation||
RAM    | Random Access Memory||
RARP   | Reverse ARP | https://en.wikipedia.org/wiki/Reverse_Address_Resolution_Protocol|
RC     | Regulatory Compliance|||
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
SMTP   | Simple Mail Transfer Protocol (Port 25)||
SNS    | Social Network Service||
SOAR   | Security Orchestration, Automation and Response||
SPOC   | Single Point Of Control||
SPOF   | Single Point Of Failure||
SSH    | Secure Shell (Port 22)||
SSL    | Secure Socket Layer||
SWIFT  | Society For Worldwide Interbank Financial Telecommunication||
TCP    | Transmission Control Protocol||
TELNET | Teletype Network (Port 23) | https://en.wikipedia.org/wiki/Telnet|
TI     | Threat Intelligence||
TLS    | Transport Layer Security||
UAC    | User Account Control||
UDP    | User Datagram Protocol||
UMTS   | Universal Mobile Telecommunications System||
UPS    | Uninterruptible Power Supply||
USB    | Universal Serial Bus||
UTC    | Coordinated Universal Time | https://en.wikipedia.org/wiki/Coordinated_Universal_Time|
VD     | Vulnerability Detection||
VGA    | Video Graphics Array/Adapter||
VM     | Vulnerability Management||
VPN    | Virtual Private Network||
WAN    | Wide Area Network||
WIFI   | Wireless Fidelity||
WLAN   | Wireless Local Area Network||
WVGA   | Wide VGA||
WXGA   | Widescreen Extended Graphics Array||
XDR    | Extended Detection and Response System||
YAHOO  | Yet Another Hierarchical Officious Oracle | https://en.wikipedia.org/wiki/Yahoo!|
