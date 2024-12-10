#max_bitrate.py
# Written by Andres Sanchez

#package modules
import sys
import math

#constants used
SOL = 299792458 #speed of light

L_l = 10**(-1/10) # this is line loss
L_a = 10**(0/10)# this is atmospheric loss

#put all the float terms here, in order as seen on given print command
tx_w = float('nan') 
tx_gain_db = float('nan') 
freq_hz = float('nan') 
dist_km = float('nan')
rx_gain_db = float('nan') 
n0_j = float('nan') 
bw_hz = float('nan') 


if len(sys.argv)==8: #one more than num of arguments, arguments in order of print given
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
     'Usage: '\
     'max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()


#Calculations from class
wavelength = SOL/freq_hz
tx_gain = 10**(tx_gain_db/10)
rx_gain = 10**(rx_gain_db/10)
C = tx_w*L_l*tx_gain*L_a*rx_gain*(wavelength/(4*math.pi*dist_km))**2
N = n0_j*bw_hz


r_max = bw_hz*math.log(( 1+C/N),2)

print(math.floor(r_max)) #final answer
