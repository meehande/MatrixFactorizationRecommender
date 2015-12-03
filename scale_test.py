""" 
Use this to test how function scales
JSON file is updated with the key value pairs
n:time
d:time
m:time
so that most current results are always recorded. 

"""
#JSON format - to implement:
#    {n: 
#	{(m,d):
#		{n1:	[t], n2: [t],   },
#	 (m2,d2):
#		{n1:	[t], n2: [t],   }
#	}
#	
#}
#	{3:[]},
#d: {}
#
#}
#n: dict{tuple(md) : dict{n:[t]}}




import blc
import timeit
import json

n = 400
m = 100
d = 10

filename = "test.json"

f = open(filename, 'r')
data = json.load(f)
print data
f.close()

#data['n'].update({"0":"0"})
#print data
#print type(data)
#print type(data['n'])

f = open(filename, 'w+')
f.write(json.dumps(data))
f.close   
#f = open(filename, 'a')

#data = {'n':[{}],"m":[{}], "d":[{}]}

while (m < 500):
    
    R = blc.createR(n,m,d)
    W = blc.sampleR(R)   
    start_time = timeit.default_timer()
    (U,V) = blc.ls(R,W,d)
    if(data['m'].has_key(str(m))):
        data['m'][str(m)].append(timeit.default_timer()-start_time)
    else:
        data['m'].update({str(m):[timeit.default_timer()-start_time]})
    m = m + 100
#print data    
f = open(filename, 'w+')
f.write(json.dumps(data))
f.close 
    
#f.close()
    
    
    
    
    
    