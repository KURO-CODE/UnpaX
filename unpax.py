#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                           
#          ~ UnpaX ~                            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# CoDeD: bY KURO-CODE
# DaTe: 12/12/2017
# Dev: Python
# Ver: 1
#
#~~~~~~~~~~~ INFO ~~~~~~~~~~~~
#
#   Cracker Zip & Rar files...
#
#     *** Requirements ***
#  - Zip
#  - Unrar
#
#*****************************

import os, time, sys, signal, subprocess
import itertools
import zipfile
import rarfile

#~~~~ Keybord interruption ~~~~
def signal_handler(signal, frame):
		KURO()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pResSEd Ctrl+C!')
		time.sleep(2)
		KURO()
		subprocess.call(['pkill', '-f', 'python'])
signal.signal(signal.SIGINT, signal_handler)

#~~~ Function KURO ~~~~
def KURO():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')

#~~~~ L O G O ~~~~
def LOGO():
	KURO()

	print """\033[1;34m
  ...    ::::::.    :::.::::::::::. :::.     \033[1;31m .,::      .:\033[1;34m
  ;;     ;;;`;;;;,  `;;; `;;;```.;;;;;`;;    \033[1;31m `;;;,  .,;; \033[1;34m
 [['     [[[  [[[[[. '[[  `]]nnn]]',[[ '[[,  \033[1;31m   '[[,,[['  \033[1;34m
 $$      $$$  $$$ "Y$c$$   $$$""  c$$$cc$$$c \033[1;31m    Y$$$P    \033[1;m
 88    .d888  888    Y88   888o    888   888,\033[1;31m  oP"``"Yo,  \033[1;m
  "YmmMMMM""  MMM     YM   YMMMb   YMM   ""`\033[1;31m,m"       "Mm,\033[0;32m
--------[\033[1;mUnpa\033[1;31mX\033[1;m ZIP\033[1;33m &\033[1;m R\033[1;34mA\033[1;mR CRACKER BY \033[1;34mK\033[1;mURO-COD\033[1;34mE\033[0;32m]\033[0;32m--------\033[1;m
"""


#~~~~ M E N U ~~~~
def MENU():
	KURO()
	LOGO()
	print """
	  +-\033[1;32m OpTiOnS\033[1;m ------------------+
	  |                            |
	  |    1)\033[0;30m...\033[1;mWorDlisT CreAtOr   |
	  |    2)\033[0;30m...\033[1;mCrAck Zip file     |
	  |    3)\033[0;30m...\033[1;mCrAck Rar fiLe     |
	  |\033[1;31m    0\033[1;m)\033[0;30m...\033[1;31mE\033[1;mxiT               |
	  |                            |
	  +----------------------------+
	"""
	unpax = raw_input(" SeLEcT: ")
	if unpax == '1':
		KURO()
		LOGO()
		print " *** WorLisT CreAtOr ***\n"
		time.sleep(1)
		print " ~ EnTer ChArs ~\n\033[1;32m-----------------\n\033[1;m"
		chrs=raw_input(' chArs: ')
		Min=int(raw_input(' Min: '))
		Max=int(raw_input(' Max: '))
		Name=raw_input(' NamE fiLe: ')
		print "\033[1;m File cReAteD..."
		KURO()
		LOGO()

		N_file=Name+'.txt'
		timer=time.asctime()
		start=time.time()
		end=time.time()
		time.x=end-start
		ln=len(chrs)
		TXT=[]

		file= open(N_file, 'a')
		for x in xrange(Min,Max+1):
			meta=ln**x
			TXT.append(meta)
			TXT_line=sum(TXT)
			for xs in itertools.product(chrs, repeat=x):
				file.write(''.join(xs)+'\n')
		file.close()
		KURO()
		LOGO()
		sys.stdout.write("\033[1;32m\r FiNisHEd\n")
		time.sleep(3)
		KURO()
		LOGO()
		print '\t\033[1;32m Name File   :',N_file
		print '\t\033[1;33m ChArs Min   :',Min
		print '\t\033[1;33m CHarS MAx   :',Max
		print '\t\033[1;m cHaRs       :',chrs
		print '\t\033[1;34m TotAl LiNEs :',TXT_line
		print '\t TimE        :',time.x
		print ""
		raw_input("\033[1;mPreSs Enter, rEtuRn TO mAiN MenU...")
		MENU()
	elif unpax == '2':
		KURO()
		LOGO()
		zipFile = raw_input(" ZipFilE: ")
		if os.path.isfile(zipFile):
			KURO()
			LOGO()
			print " File ExIsT!"
			time.sleep(2)
			KURO()
		else:
			KURO()
			LOGO()
			print " FilE nOt ExIsT!"
			time.sleep(2)
			MENU()
		LOGO()
		File = raw_input(" List: ")
		if os.path.isfile(File):
			KURO()
			LOGO()
			print " FiLe ExIsT!"
			time.sleep(2)
			KURO()
		else:
			KURO()
			LOGO()
			print " FilE nOt ExIsT!"
			time.sleep(2)
			MENU()

		zipFile = zipfile.ZipFile(zipFile)
		password = []
		LOGO()
		print " CrAcK... pLeAsE wAiT..."

		with open(File, 'r') as f:
			for line in f.readlines():
				password = line.strip('\n')

				try:
					zipFile.extractall(pwd=password)
					KURO()
					LOGO()
					print "[+]\033[1;m PAsswOrD FoUnD:\033[1;32m %s \033[1;m\n" % password
					raw_input(" PreSs Enter, rEtuRn TO mAiN MenU...")
					MENU()
				except:
					pass	

	elif unpax == '3':
		KURO()
		LOGO()
		rarFile = raw_input(" RarFilE: ")
		if os.path.isfile(rarFile):
			KURO()
			LOGO()
			print " FiLe ExIsT!"
			time.sleep(1)
			KURO()
		else:
			KURO()
			LOGO()
			print " FilE nOt ExIsT!"
			time.sleep(1)
			MENU()
		LOGO()
		File = raw_input(" List: ")
		if os.path.isfile(File):
			KURO()
			LOGO()
			print " FiLe ExIsT!"
			time.sleep(1)
			KURO()
		else:
			KURO()
			LOGO()
			print " FilE nOt ExIsT!"
			time.sleep(1)
			MENU()

		rarFile = rarfile.RarFile(rarFile)
		password = []
		KURO()
		LOGO()
		print " CrAcK... pLeAsE wAiT..."

		with open(File, 'r') as f:
			for line in f.readlines():
				password = line.strip('\n')
				try:
					rarFile.extractall(pwd=password)
					KURO()
					LOGO()
					print "[+]\033[1;m PAsswOrD FoUnD: \033[1;32m%s \033[1;m\n" % password
					raw_input(" PreSs Enter, rEtuRn TO mAiN MenU...")
					MENU()
				except:
					pass

	elif unpax == '0':
		KURO()
		LOGO()
		time.sleep(1)
		print "\033[1;m ThAnkS fOr UsiNg UnpaX\033[1;m"
		time.sleep(2)
		print
		print "\033[1;m[\033[1;31mX\033[1;m]...\033[1;32mClOsiNg"
		time.sleep(1)
		KURO()
		sys.exit()
	else:
		KURO()
		LOGO()
		print " [\033[1;33m***\033[1;31mERROR\033[1;33m***\033[1;m]"
		time.sleep(2)
		MENU()
	
MENU()
