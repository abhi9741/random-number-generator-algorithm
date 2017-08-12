#Author : Abhinav Reddy Nimma (16XJ1A0504)
import random
from random import randint as r      #random library has an easy partern of showing random integers that can be easily cracked, so we just use it in solving  our algorith
l=1
print "enter an upperbound from (5,7,11,17,23,53,61,71,101,503), upperbound U gerates a random no. from first U-1 integers "
h=input("enter the UPPER bound of the range in which you want to generate a random no.")

list=[5,7,11,17,23,53,61,71,101,503] #these are the predefined upper bounds


if(h==5) : 		   #this checks if h matches with any predefined upper bound
	 k=r(l,h)
	 z=(2*k)%5         #random ibrary is used to generate a random no. which inturn is used in our formula to generate a random integer , this makes the pattern of showing random no. more efficient
	 print z	   #this prints the random no. generated

elif (h==7) :
	k=r(l,h)
	z=(2*k)%7
	print z

elif (h==11) :
	k=r(l,h)
	z=(7*k)%11
	print z

elif (h==17) :
	k=r(l,h)
	z=(7*k)%17
	print z

elif (h==23) :
	k=r(l,h)
	z=(5*k)%23
	print z
elif (h==53) :
	k=r(l,h)
	z=(5*k)%53
	print z

elif (h==61) :
	k=r(l,h)
	z=(7*k)%63
	print z

elif (h==71) :
	k=r(l,h)
	z=(13*k)%71
	print z

elif (h==101) :
	k=r(l,h)
	z=(11*k)%101
	print z
elif (h==503) :
	k=r(l,h)
	z=(17*k)%503
	print z
else :
	print"given number doesnot exist in the predefined upper bounds , please try again"
