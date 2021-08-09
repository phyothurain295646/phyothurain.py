Haccker Mi
	# 05 - Password Attacks
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		print("\n    [01] Hydra: Network logon cracker supporting different services")
		print("    [02] FMBrute: Facebook Multi Brute Force")
		print("    [03] HashID: Software to identify the different types of hashes")
		print("    [04] Facebook Brute Force 3")
		print("    [05] Black Hydra: A small program to shorten brute force sessions on hydra")
		print("    [06] Hash Buster: Crack hashes in seconds")
		print("    [07] FBBrute: Facebook Brute Force")
		print("    [08] Cupp: Common User Passwords Profiler")
		print("    [09] InstaHack: Instagram Brute Force")
		print("    [10] Indonesian Wordlist")
		print("    [11] Xshell")
		print("    [12] Aircrack-ng: WiFi security auditing tools suite")
		print("    [13] BlackBox: A Penetration Testing Framework")
		print("    [14] Katak: An open source software login brute-forcer toolkit and hash decrypter")
		print("    [15] Hasher: Hash cracker with auto detect hash")
		print("    [16] Hash-Generator: Beautiful Hash Generator")
		print("    [17] nk26: Nkosec Encode")
		print("    [18] Hasherdotid: A tool for find an encrypted text")
		print("    [19] Crunch: Highly customizable wordlist generator")
		print("    [20] Hashcat: World's fastest and most advanced password recovery utility")
		print("    [21] ASU: Facebook Hacking ToolKit")
		print("    [22] Credmap: An open source tool that was created to bring awareness to the dangers of credential reuse")
		print("    [23] BruteX: Automatically brute force all services running on a target")
		print("    [24] Gemail-Hack: python script for Hack gmail account brute force")
		print("    [25] GoblinWordGenerator: Python wordlist generator")
		print("\n    [00] Back to main menu\n")
		passtak = input("lzmx > set_install ")
		if passtak == "@":
			passtak = ""
			for x in range(1,201):
				passtak += f"{x} "
		if len(passtak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for passx in passtak.split():
			if passx.strip() == "01" or passx.strip() == "1": hydra()
			elif passx.strip() == "02" or passx.strip() == "2": fmbrute()
			elif passx.strip() == "03" or passx.strip() == "3": hashid()
			elif passx.strip() == "04" or passx.strip() == "4": fbBrute()
			elif passx.strip() == "05" or passx.strip() == "5": black_hydra()
			elif passx.strip() == "06" or passx.strip() == "6": hash_buster()
			elif passx.strip() == "07" or passx.strip() == "7": fbbrutex()
			elif passx.strip() == "08" or passx.strip() == "8": cupp()
			elif passx.strip() == "09" or passx.strip() == "9": instaHack()
			elif passx.strip() == "10": indonesian_wordlist()
			elif passx.strip() == "11": xshell()
			elif passx.strip() == "12": aircrackng()
			elif passx.strip() == "13": blackbox()
			elif passx.strip() == "14": katak()
			elif passx.strip() == "15": hasher()
			elif passx.strip() == "16": hashgenerator()
			elif passx.strip() == "17": nk26()
			elif passx.strip() == "18": hasherdotid()
			elif passx.strip() == "19": crunch()
			elif passx.strip() == "20": hashcat()
			elif passx.strip() == "21": asu()
			elif passx.strip() == "22": credmap()
			elif passx.strip() == "23": brutex()
			elif passx.strip() == "24": gemailhack()
			elif passx.strip() == "25": goblinwordgenerator()
			elif passx.strip() == "00" or passx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 06 - Wireless Attacks
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		print("\n    [01] Aircrack-ng: WiFi security auditing tools suite")
		print("    [02] Wifite: An automated wireless attack tool")
		print("    [03] Wifiphisher: The Rogue Access Point Framework")
		print("    [04] Routersploit: Exploitation Framework for Embedded Devices")
		print("\n    [00] Back to main menu\n")
		wiretak = input("lzmx > set_install ")
		if wiretak == "@":
			wiretak = ""
			for x in range(1,201):
				wiretak += f"{x} "
		if len(wiretak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for wirex in wiretak.split():
			if wirex.strip() == "01" or wirex.strip() == "1": aircrackng()
			elif wirex.strip() == "02" or wirex.strip() == "2": wifite()
			elif wirex.strip() == "03" or wirex.strip() == "3": wifiphisher()
			elif wirex.strip() == "04" or wirex.strip() == "4": routersploit()
			elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 07 - Reverse Engineering
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		print("\n    [01] Binary Exploitation")
		print("    [02] jadx: DEX to JAVA Decompiler")
		print("    [03] apktool: A utility that can be used for reverse engineering Android applications")
		print("    [04] uncompyle6: Python cross-version byte-code decompiler")
		print("    [05] ddcrypt: DroidScript APK Deobfuscator")
		print("    [06] CFR: Yet another java decompiler")
		print("    [07] UPX: Ultimate Packer for eXecutables")
		print("    [08] pyinstxtractor: PyInstaller Extractor")
		print("    [09] innoextract: A tool to unpack installers created by Inno Setup")
		print("\n    [00] Back to main menu\n")
		reversi = input("lzmx > set_install ")
		if reversi == "@":
			reversi = ""
			for x in range(1,201):
				reversi += f"{x} "
		if len(reversi.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for revex in reversi.split():
			if revex.strip() == "01" or revex.strip() == "1": binploit()
			elif revex.strip() == "02" or revex.strip() == "2": jadx()
			elif revex.strip() == "03" or revex.strip() == "3": apktool()
			elif revex.strip() == "04" or revex.strip() == "4": uncompyle()
			elif revex.strip() == "05" or revex.strip() == "5": ddcrypt()
			elif revex.strip() == "06" or revex.strip() == "6": cfr()
			elif revex.strip() == "07" or revex.strip() == "7": upx()
			elif revex.strip() == "08" or revex.strip() == "8": pyinstxtractor()
			elif revex.strip() == "09" or revex.strip() == "9": innoextract()
			elif revex.strip() == "00" or revex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 08 - Exploitation Tools
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		print("\n    [01] Metasploit: Advanced open-source platform for developing, testing and using exploit code")
		print("    [02] commix: Automated All-in-One OS Command Injection and Exploitation Tool")
		print("    [03] BlackBox: A Penetration Testing Framework")
		print("    [04] Brutal: Payload for teensy like a rubber ducky but the syntax is different")
		print("    [05] TXTool: An easy pentesting tool")
		print("    [06] XAttacker: Website Vulnerability Scanner & Auto Exploiter")  
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [09] A-Rat: Remote Administration Tool")
		print("    [10] BAF: Blind Attacking Framework")
		print("\n    [00] Back to main menu\n")
		exploitool = input("lzmx > set_install ")
		if exploitool == "@":
			exploitool = ""
			for x in range(1,201):
				exploitool += f"{x} "
		if len(exploitool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for explx in exploitool.split():
			if explx.strip() == "01" or explx.strip() == "1": metasploit()
			elif explx.strip() == "02" or explx.strip() == "2": commix()
			elif explx.strip() == "03" or explx.strip() == "3": blackbox()
			elif explx.strip() == "04" or explx.strip() == "4": brutal()
			elif explx.strip() == "05" or explx.strip() == "5": txtool()
			elif explx.strip() == "06" or explx.strip() == "6": xattacker()
			elif explx.strip() == "07" or explx.strip() == "7": websploit()
			elif explx.strip() == "08" or explx.strip() == "8": routersploit()
			elif explx.strip() == "09" or explx.strip() == "9": arat()
			elif explx.strip() == "10": baf()
			elif explx.strip() == "00" or explx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 09 - Sniffing and Spoofing
	elif lazymux.strip() == "9" or lazymux.strip() == "09":
		print("\n    [01] KnockMail: Verify if Email Exists")
		print("    [02] tcpdump: A powerful command-line packet analyzer")
		print("    [03] Ettercap: Comprehensive suite for MITM attacks, can sniff live connections, do content filtering on the fly and much more")
		print("    [04] hping3: hping is a command-line oriented TCP/IP packet assembler/analyzer")
		print("    [05] tshark: Network protocol analyzer and sniffer")
		print("\n    [00] Back to main menu\n")
		sspoof = input("lzmx > set_install ")
		if sspoof == "@":
			sspoof = ""
			for x in range(1,201):
				sspoof += f"{x} "
		if len(sspoof.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for sspx in sspoof.split():
			if sspx.strip() == "01" or sspx.strip() == "1": knockmail()
			elif sspx.strip() == "02" or sspx.strip() == "2": tcpdump()
			elif sspx.strip() == "03" or sspx.strip() == "3": ettercap()
			elif sspx.strip() == "04" or sspx.strip() == "4": hping3()
			elif sspx.strip() == "05" or sspx.strip() == "5": tshark()
			elif sspx.strip() == "00" or sspx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 10 - Reporting Tools
	elif lazymux.strip() == "10":
		print("\n    [01] dos2unix: Converts between DOS and Unix text files")
		print("    [02] exiftool: Utility for reading, writing and editing meta information in a wide variety of files")
		print("    [03] iconv: Utility converting between different character encodings")
		print("    [04] mediainfo: Command-line utility for reading information from media files")
		print("    [05] pdfinfo: PDF document information extractor")
		print("\n    [00] Back to main menu\n")
		reportls = input("lzmx > set_install ")
		if reportls == "@":
			reportls = ""
			for x in range(1,201):
				reportls += f"{x} "
		if len(reportls.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for reportx in reportls.split():
			if reportx.strip() == "01" or reportx.strip() == "1": dos2unix()
			elif reportx.strip() == "02" or reportx.strip() == "2": exiftool()
			elif reportx.strip() == "03" or reportx.strip() == "3": iconv()
			elif reportx.strip() == "04" or reportx.strip() == "4": mediainfo()
			elif reportx.strip() == "05" or reportx.strip() == "5": pdfinfo()
			elif reportx.strip() == "00" or reportx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 11 - Forensic Tools
	elif lazymux.strip() == "11":
		print("\n    [01] steghide: Embeds a message in a file by replacing some of the least significant bits")
		print("    [02] tesseract: Tesseract is probably the most accurate open source OCR engine available")
		print("    [03] sleuthkit: The Sleuth Kit (TSK) is a library for digital forensics tools")
		print("    [04] CyberScan: Network's Forensics ToolKit")
		print("    [05] binwalk: Firmware analysis tool")
		print("\n    [00] Back to main menu\n")
		forensc = input("lzmx > set_install ")
		if forensc == "@":
			forensc = ""
			for x in range(1,201):
				forensc += f"{x} "
		if len(forensc.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for forenx in forensc.split():
			if forenx.strip() == "01" or forenx.strip() == "1": steghide()
			elif forenx.strip() == "02" or forenx.strip() == "2": tesseract()
			elif forenx.strip() == "03" or forenx.strip() == "3": sleuthkit()
			elif forenx.strip() == "04" or forenx.strip() == "4": cyberscan()
			elif forenx.strip() == "05" or forenx.strip() == "5": binwalk()
			elif forenx.strip() == "00" or forenx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 12 - Stress Testing
	elif lazymux.strip() == "12":
		print("\n    [01] Torshammer: Slow post DDOS tool")
		print("    [02] Slowloris: Low bandwidth DoS tool")
		print("    [03] Fl00d & Fl00d2: UDP Flood tool")
		print("    [04] GoldenEye: GoldenEye Layer 7 (KeepAlive+NoCache) DoS test tool")
		print("    [05] Xerxes: The most powerful DoS tool")
		print("    [06] Planetwork-DDOS")
		print("    [07] Xshell")
		print("    [08] santet-online: Social Engineering Tool")
		print("    [09] dost-attack: WebServer Attacking Tools")
		print("    [10] DHCPig: DHCP exhaustion script written in python using scapy network library")
		print("\n    [00] Back to main menu\n")
		stresstest = input("lzmx > set_install ")
		if stresstest == "@":
			stresstest = ""
			for x in range(1,201):
				stresstest += f"{x} "
		if len(stresstest.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for stressx in stresstest.split():
			if stressx.strip() == "01" or stressx.strip() == "1": torshammer()
			elif stressx.strip() == "02" or stressx.strip() == "2": slowloris()
			elif stressx.strip() == "03" or stressx.strip() == "3": fl00d12()
			elif stressx.strip() == "04" or stressx.strip() == "4": goldeneye()
			elif stressx.strip() == "05" or stressx.strip() == "5": xerxes()
			elif stressx.strip() == "06" or stressx.strip() == "6": planetwork_ddos()
			elif stressx.strip() == "07" or stressx.strip() == "7": xshell()
			elif stressx.strip() == "08" or stressx.strip() == "8": sanlen()
			elif stressx.strip() == "09" or stressx.strip() == "9": dostattack()
			elif stressx.strip() == "10": dhcpig()
			elif stressx.strip() == "00" or stressx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 13 - Install Linux Distro
	elif lazymux.strip() == "13":
		print("\n    [01] Ubuntu")
		print("    [02] Fedora")
		print("    [03] Kali Nethunter")
		print("    [04] Parrot")
		print("    [05] Arch Linux")
		print("\n    [00] Back to main menu\n")
		innudis = input("lzmx > set_install ")
		if innudis == "@":
			innudis = ""
			for x in range(1,201):
				innudis += f"{x} "
		if len(innudis.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for innux in innudis.split():
			if innux.strip() == "01" or innux.strip() == "1": ubuntu()
			elif innux.strip() == "02" or innux.strip() == "2": fedora()
			elif innux.strip() == "03" or innux.strip() == "3": nethunter()
			elif innux.strip() == "04" or innux.strip() == "4": parrot()
			elif innux.strip() == "05" or innux.strip() == "5": archlinux()
			elif innux.strip() == "00" or innux.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 14 - Termux Utility
	elif lazymux.strip() == "14":
		print("\n    [01] SpiderBot: Curl website using random proxy and user agent")
		print("    [02] Ngrok: tunnel local ports to public URLs and inspect traffic")
		print("    [03] Sudo: sudo installer for Android")
		print("    [04] google: Python bindings to the Google search engine")
		print("    [05] kojawafft")
		print("    [06] ccgen: Credit Card Generator")
		print("    [07] VCRT: Virus Creator")
		print("    [08] E-Code: PHP Script Encoder")
		print("    [09] Termux-Styling")
		print("    [11] xl-py: XL Direct Purchase Package")
		print("    [12] BeanShell: A small, free, embeddable Java source interpreter with object scripting language features, written in Java")
		print("    [13] vbug: Virus Maker")
		print("    [14] Crunch: Highly customizable wordlist generator")
		print("    [15] Textr: Simple tool for running text")
		print("    [16] heroku: CLI to interact with Heroku")
		print("    [17] RShell: Reverse shell for single listening")
		print("    [18] TermPyter: Fix all error Jupyter installation on termux")
		print("    [19] Numpy: The fundamental package for scientific computing with Python")
		print("    [20] BTC-to-IDR-checker: Check the exchange rate virtual money currency to Indonesia Rupiah from Bitcoin.co.id API")
		print("    [21] ClickBot: Earn money using telegram bot")
		print("\n    [00] Back to main menu\n")
		moretool = input("lzmx > set_install ")
		if moretool == "@":
			moretool = ""
			for x in range(1,201):
				moretool += f"{x} "
		if len(moretool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for moret in moretool.split():
			if moret.strip() == "01" or moret.strip() == "1": spiderbot()
			elif moret.strip() == "02" or moret.strip() == "2": ngrok()
			elif moret.strip() == "03" or moret.strip() == "3": sudo()
			elif moret.strip() == "04" or moret.strip() == "4": google()
			elif moret.strip() == "05" or moret.strip() == "5": kojawafft()
			elif moret.strip() == "06" or moret.strip() == "6": ccgen()
			elif moret.strip() == "07" or moret.strip() == "7": vcrt()
			elif moret.strip() == "08" or moret.strip() == "8": ecode()
			elif moret.strip() == "09" or moret.strip() == "9": stylemux()
			elif moret.strip() == "10": passgencvar()
			elif moret.strip() == "11": xlPy()
			elif moret.strip() == "12": beanshell()
			elif moret.strip() == "13": vbug()
			elif moret.strip() == "14": crunch()
			elif moret.strip() == "15": textr()
			elif moret.strip() == "16": heroku()
			elif moret.strip() == "17": rshell()
			elif moret.strip() == "18": termpyter()
			elif moret.strip() == "19": numpy()
			elif moret.strip() == "20": btc2idr()
			elif moret.strip() == "21": clickbot()
			elif moret.strip() == "00" or moret.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 15 - Shell Function [.bashrc]
	elif lazymux.strip() == "15":
		print("\n    [01] FBVid (FB Video Downloader)")
		print("    [02] cast2video (Asciinema Cast Converter)")
		print("    [03] iconset (AIDE App Icon)")
		print("    [04] readme (GitHub README.md)")
		print("    [05] makedeb (DEB Package Builder)")
		print("    [06] quikfind (Search Files)")
		print("    [07] pranayama (4-7-8 Relax Breathing)")
		print("    [08] sqlc (SQLite Query Processor)")
		print("\n    [00] Back to main menu\n")
		myshf = input("lzmx > set_install ")
		if myshf == "@":
			myshf = ""
			for x in range(1,201):
				myshf += f"{x} "
		if len(myshf.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for mysh in myshf.split():
			if mysh.strip() == "01" or mysh.strip() == "1": fbvid()
			elif mysh.strip() == "02" or mysh.strip() == "2": cast2video()
			elif mysh.strip() == "03" or mysh.strip() == "3": iconset()
			elif mysh.strip() == "04" or mysh.strip() == "4": readme()
			elif mysh.strip() == "05" or mysh.strip() == "5": makedeb()
			elif mysh.strip() == "06" or mysh.strip() == "6": quikfind()
			elif mysh.strip() == "07" or mysh.strip() == "7": pranayama()
			elif mysh.strip() == "08" or mysh.strip() == "8": sqlc()
			elif mysh.strip() == "00" or mysh.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 16 - Install CLI Games
	elif lazymux.strip() == "16":
		print("\n    [01] Flappy Bird")
		print("    [02] Street Car")
		print("    [03] Speed Typing")
		print("    [04] NSnake: The classic snake game with textual interface")
		print("    [05] Moon buggy: Simple game where you drive a car across the moon's surface")
		print("    [06] Nudoku: ncurses based sudoku game")
		print("    [07] tty-solitaire")
		print("    [08] Pacman4Console")
		print("\n    [00] Back to main menu\n")
		cligam = input("lzmx > set_install ")
		if cligam == "@":
			cligam = ""
			for x in range(1,201):
				cligam += f"{x} "
		if len(cligam.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for clig in cligam.split():
			if clig.strip() == "01" or clig.strip() == "1": flappy_bird()
			elif clig.strip() == "02" or clig.strip() == "2": street_car()
			elif clig.strip() == "03" or clig.strip() == "3": speed_typing()
			elif clig.strip() == "04" or clig.strip() == "4": nsnake()
			elif clig.strip() == "05" or clig.strip() == "5": moon_buggy()
			elif clig.strip() == "06" or clig.strip() == "6": nudoku()
			elif clig.strip() == "07" or clig.strip() == "7": ttysolitaire()
			elif clig.strip() == "08" or clig.strip() == "8": pacman4console()
			elif clig.strip() == "00" or clig.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 17 - Malware Analysis
	elif lazymux.strip() == "17":
		print("\n    [01] Lynis: Security Auditing and Rootkit Scanner")
		print("    [02] Chkrootkit: A Linux Rootkit Scanners")
		print("    [03] ClamAV: Antivirus Software Toolkit")
		print("    [04] Yara: Tool aimed at helping malware researchers to identify and classify malware samples")
		print("    [05] VirusTotal-CLI: Command line interface for VirusTotal")
		print("    [06] avpass: Tool for leaking and bypassing Android malware detection system")
		print("    [07] DKMC: Dont kill my cat - Malicious payload evasion tool")
		print("\n    [00] Back to main menu\n")
		malsys = input("lzmx > set_install ")
		if malsys == "@":
			malsys = ""
			for x in range(1,201):
				malsys += f"{x} "
		if len(malsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for malx in malsys.split():
			if malx.strip() == "01" or malx.strip() == "1": lynis()
			elif malx.strip() == "02" or malx.strip() == "2": chkrootkit()
			elif malx.strip() == "03" or malx.strip() == "3": clamav()
			elif malx.strip() == "04" or malx.strip() == "4": yara()
			elif malx.strip() == "05" or malx.strip() == "5": virustotal()
			elif malx.strip() == "06" or malx.strip() == "6": avpass()
			elif malx.strip() == "07" or malx.strip() == "7": dkmc()
			elif malx.strip() == "00" or malx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 18 - Compiler/Interpreter
	elif lazymux.strip() == "18":
		print("\n    [01] Python2: Python 2 programming language intended to enable clear programs")
		print("    [02] ecj: Eclipse Compiler for Java")
		print("    [03] Golang: Go programming language compiler")
		print("    [04] ldc: D programming language compiler, built with LLVM")
		print("    [05] Nim: Nim programming language compiler")
		print("    [06] shc: Shell script compiler")
		print("    [07] TCC: Tiny C Compiler")
		print("    [08] PHP: Server-side, HTML-embedded scripting language")
		print("    [09] Ruby: Dynamic programming language with a focus on simplicity and productivity")
		print("    [10] Perl: Capable, feature-rich programming language")
		print("    [11] Vlang: Simple, fast, safe, compiled language for developing maintainable software")
		print("    [12] BeanShell: Small, free, embeddable, source level Java interpreter with object based scripting language features written in Java")
		print("    [13] fp-compiler: Free Pascal is a 32, 64 and 16 bit professional Pascal compiler")
		print("    [14] Octave: Scientific Programming Language")
		print("    [15] BlogC: A blog compiler")
		print("    [16] Dart: General-purpose programming language")
		print("    [17] Yasm: Assembler supporting the x86 and AMD64 instruction sets")
		print("    [18] Nasm: A cross-platform x86 assembler with an Intel-like syntax.")
		print("\n    [00] Back to main menu\n")
		compter = input("lzmx > set_install ")
		if compter == "@":
			compter = ""
			for x in range(1,201):
				compter += f"{x} "
		if len(compter.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for compt in compter.split():
			if compt.strip() == "01" or compt.strip() == "1": python2()
			elif compt.strip() == "02" or compt.strip() == "2": ecj()
			elif compt.strip() == "03" or compt.strip() == "3": golang()
			elif compt.strip() == "04" or compt.strip() == "4": ldc()
			elif compt.strip() == "05" or compt.strip() == "5": nim()
			elif compt.strip() == "06" or compt.strip() == "6": shc()
			elif compt.strip() == "07" or compt.strip() == "7": tcc()
			elif compt.strip() == "08" or compt.strip() == "8": php()
			elif compt.strip() == "09" or compt.strip() == "9": ruby()
			elif compt.strip() == "10": perl()
			elif compt.strip() == "11": vlang()
			elif compt.strip() == "12": beanshell()
			elif compt.strip() == "13": fpcompiler()
			elif compt.strip() == "14": octave()
			elif compt.strip() == "15": blogc()
			elif compt.strip() == "16": dart()
			elif compt.strip() == "17": yasm()
			elif compt.strip() == "18": nasm()
			elif compt.strip() == "00" or compt.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 19 - Social Engineering Tools
	elif lazymux.strip() == "19":
		print("\n    [01] weeman: HTTP server for phishing in python")
		print("    [02] SocialFish: Educational Phishing Tool & Information Collector")
		print("    [03] santet-online: Social Engineering Tool")
		print("    [04] SpazSMS: Send unsolicited messages repeatedly on the same phone number")
		print("    [05] LiteOTP: Multi Spam SMS OTP")
		print("    [06] F4K3: Fake User Data Generator")
		print("    [07] Hac")
		print("    [08] Cookie-stealer: Crappy cookie stealer")
		print("\n    [00] Back to main menu\n")
		soceng = input("lzmx > set_install ")
		if soceng == "@":
			soceng = ""
			for x in range(1,201):
				soceng += f"{x} "
		if len(soceng.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for socng in soceng.split():
			if socng.strip() == "01" or socng.strip() == "1": weeman()
			elif socng.strip() == "02" or socng.strip() == "2": socfish()
			elif socng.strip() == "03" or socng.strip() == "3": sanlen()
			elif socng.strip() == "04" or socng.strip() == "4": spazsms()
			elif socng.strip() == "05" or socng.strip() == "5": liteotp()
			elif socng.strip() == "06" or socng.strip() == "6": f4k3()
			elif socng.strip() == "07" or socng.strip() == "7": hac()
			elif socng.strip() == "08" or socng.strip() == "8": cookiestealer()
			elif socng.strip() == "00" or socng.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	elif lazymux.strip() == "00":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(1)
		restart_program()

if __name__ == "__main__":
	os.system("clear")
	main()
© 2021 GitHub, Inc.
