Bandwidth=int(input("enter a the bandwidth in mhz:- "))
mimo=int(input("enter a the bandwidth in mhz:- "))
mcs=int(input("enter the Qam use :-"))

rb= (Bandwidth*5)*12*7*2
print(rb)
maxthroughput=(rb*mcs)

print(maxthroughput)
th=maxthroughput/1000
print(th)
overload=th-25.00

print(overload)
