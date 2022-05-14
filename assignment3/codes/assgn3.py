from unittest import result


P_x0= 0.6 #Probability that first group wins
P_x1= 0.4 #Probability that second group wins
P_y0x1= 0.3 #Probability that second group introduces new product if it wins
P_y0x0= 0.7 #Probability that first group introduces new product if it wins
P_x1y0= result #Probability that new product is introduced by second group
result= P_y0x1*P_x1/(P_y0x0*P_x0 + P_y0x1*P_x1)
print(result)
