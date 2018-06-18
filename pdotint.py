from __future__ import print_function
import math


def Pdotintcal(Ex_pl, Ex_z, Ex_shk):
   a = Ex_pl
   b = Ex_z
   c = Ex_shk
   inp = raw_input("Do you want (1)- Only intrinsic spin period derivative, (2)- Only intrinsic orbital period decay, or, (3)- Both? Choose 1, 2, or 3: ")
   if inp == "1":
       Ps = float(input("Ps_obs(s)= "))
       Psdot_obs = float(input("Psdot_obs(x10^-20)= "))/pow(10.0,20.0)
       psdyn = a+b+c
       Psdotint = Psdot_obs-(psdyn*Ps)

       print ("Psdot_Expl= ", a*Ps)
       print ("Psdot_Exz= ", b*Ps)
       print ("Psdot_gal= ", (psdyn-c)*Ps)
       print ("Psdot_Shk= ", c*Ps)
       print ("Psdot_int= ", Psdotint)
      
   elif inp == "2":
       Pbdot_obs = float(input("Pbdot_obs= "))
       Pbd = float(input("Pb_obs(days)= "))
       Pbs = Pbd*24.0*3600.0
       pbdyn = a+b+c
       Pbdotint = Pbdot_obs-(pbdyn*Pbs)

       print ("Pbdot_Expl= ", a*Pbs)
       print ("Pbdot_Exz= ", b*Pbs) 
       print ("Pbdot_gal= ", (pbdyn-c)*Pbs)
       print ("Pbdot_Shk= ", c*Pbs)
       print ("Pbdot_int= ", Pbdotint)

   elif inp == "3":
       Pbdot_obs = float(input("Pbdot_obs= "))
       Pbd = float(input("Pb_obs(days)= "))
       Pbs = Pbd*24.0*3600.0
       pbdyn = a+b+c
       Pbdotint = Pbdot_obs-(pbdyn*Pbs)


       Ps = float(input("Ps_obs(s)= "))
       Psdot_obs = float(input("Psdot_obs(x10^-20)= "))/pow(10.0,20.0)
       psdyn = a+b+c
       Psdotint = Psdot_obs-(psdyn*Ps)
   
       print ("Pbdot_Expl= ", a*Pbs)
       print ("Pbdot_Exz= ", b*Pbs)
       print ("Pbdot_gal= ", (pbdyn-c)*Pbs)
       print ("Pbdot_Shk= ", c*Pbs)
       print ("Pbdot_int= ", Pbdotint)

       print ("Psdot_Expl= ", a*Ps)
       print ("Psdot_Exz= ", b*Ps)
       print ("Psdot_gal= ", (psdyn-c)*Ps)
       print ("Psdot_Shk= ", c*Ps)
       print ("Psdot_int= ", Psdotint)

   else:
       print ("Invalid Input") 


   return None;
