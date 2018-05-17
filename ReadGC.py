from __future__ import print_function
import math
import numpy as np
import parameters as par
from AllCal import allcal

def readGCfunc():
   global n1,dat,name,aname,gl,gb,dd,b1,dkpc1,zkpc1,bdeg,ldeg
   dat = []
   name = []
   aname = []
   gl = []
   gb = []
   dd = []
   b1 = []
   dkpc1 = [] 
   zkpc1 = []
   f1 = open('GC_harris.txt','r')
   n1 = 0
   for line in f1:
      s = line.split()
      dat.append(s)
      n1 = n1 +1  

   for j in range(0,n1):
      name.append(dat[j][0])
      aname.append(dat[j][1])
      gl.append(float(dat[j][2]))
      gb.append(float(dat[j][3])) 
      dd.append(float(dat[j][4]))
      b1=gb[j]*par.degtorad
      dkpc1=dd[j]
      zkpc1=dkpc1*math.sin(b1)
     
   f1.close()
   return None;


def gcinp():
    ans = raw_input("Cluster Name(Case Sensitive): ")
    global flag, bdeg, ldeg, dkpc, Har
    Har = 1
    flag = 0
    for i in range(0,n1):
      if ans == dat[i][0] or ans == dat[i][1] and ans != 'NA':
         flag = 1
         print ("Found !")
         print (dat[i][0], dat[i][1])
         ldeg = float(dat[i][2])
         bdeg = float(dat[i][3])
         dkpc = float(dat[i][4])
        
         allcal(bdeg,0,ldeg,0,dkpc,0,Har)

         

      elif i==156 and flag ==0:
         print ("Cluster Not Found. Check name again")
    return None;

def GCrepeat():
    if flag == 0:
       print ("Here is the list of clusters. Choose your cluster and type the name correctly.")
       for j in range(0,n1):
          print (name[j], aname[j])
       gcinp()
    return None;










