import sys
import math

rd = sys.argv[1]
rdfile = ""
rdfile = rdfile + rd

print "Filename: ", rdfile

wname="position.dat"

r = open(rdfile,'r')
w = open(wname,'w')

tot = 0
it = 0

errx = 0.0
errv = 0.0
SS_tot = 0.0
SS_res = 0.0
SS_reg = 0.0

x = []
v = []
t = []

vmax = 0.0
xmax = 0.0
vsum = 0.0
xsum = 0.0

xa = []
va = []

Q=1.0
m=1.0
B0 = 2.0
Bs = 10.0
alpha = 8.0
v0 = math.sqrt(3.0)/2.0 
beta = Q*Q/(2.0*m*1.0*1.0*B0)
gamma = math.sqrt(beta*alpha)
x0 = -1.0
dt = 0.005

for line in r:
	vals = line.split()
        x.append(float(vals[0]))
        v.append(float(vals[2]))
        t.append(float(vals[8]))


	xa.append((v0/gamma)*math.sin(gamma*t[it])+(B0/alpha)*math.cos(gamma*t[it])+x0-(B0/alpha))
	va.append(v0*math.cos(gamma*(t[it]+dt/2.0))-B0*math.sqrt(beta/alpha)*math.sin(gamma*(t[it]+dt/2.0)))
        vsum += abs(float(va[it]))	
        xsum += abs(float(xa[it]))	

	if abs(float(va[it]))>vmax:
			vmax = abs(float(va[it]))
	if abs(float(xa[it]))>xmax:
			xmax = abs(float(xa[it]))

        errx +=  (x[it]-xa[it])**2
        errv +=  (v[it]-va[it])**2

        w.write(str(t[it])+'\t'+str(xa[it])+'\t'+str(va[it])+'\n')
        it = it +1

print "gamma: ", gamma
print "beta: ", beta
print "Error X: ", math.sqrt(errx/it)
print "Error V: ", math.sqrt(errv/it)
print "Normalized Max Error X: ", math.sqrt(errx/it)/xmax*100
print "Normalized Max Error V: ", math.sqrt(errv/it)/vmax*100
#print "Normalized Mean Error X: ", cnt1*math.sqrt(err/it)/xsum*100
#print "Normalized Mean Error V: ", cnt1*math.sqrt(err/it)/vsum*100
