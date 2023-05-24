import random
import argparse
import os

from os import system
from argparse import ArgumentParser
from random import choices

def clear():
	system("clear")

def banner():
	print("""\033[1;33m
 *******     **    *     *          ****   ****  ****     **
/**////**   */*  ***** *****       */// * */// */**/**   /**
/**   /**  * /* /*/*/ /*/*/       /*   / /    /*/**//**  /**
/*******  ******/*****/***** *****/*****    *** /** //** /**
/**////  /////* ///*/*///*/*///// /*/// *  /// */**  //**/**
/**          /*  ***** *****      /*   /* *   /*/**   //****
/**          /* ///*/ ///*/       / **** / **** /**    //***
//           /    /     /          ////   ////  //      ///\033[0m
\033[41m Password Generator | https://github.com/t0mxplo1t \033[0m""")

pass_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","q","y","z","1","2","3","4","5","6","7","8","9","0","!","@","$","%","#","*","?","&"]

clear()
p = ArgumentParser(description=banner())
p.add_argument("-l","--length",help="panjang kata",required=True,type=int)
argument = p.parse_args()

kata_sandi = argument.length

if kata_sandi:
	passwd = ""

	for i in range(kata_sandi):
		passwd += choices(pass_list)[0]

	print("\033[1;32mYour new password : \033[0m{}".format(passwd))
