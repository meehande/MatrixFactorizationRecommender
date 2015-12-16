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

n = 150
m = 300
d = 10
rho = 1

filename = "test_recorder.json"

f = open(filename, 'r')
data = json.load(f)
print data
f.close()

f = open(filename, 'w+')
f.write(json.dumps(data))
f.close   
tuple_key = str((m,d))
while (n < 500):
    
    R = blc.createR(n,m,d)
    W = blc.sampleR(R)   
    start_time = timeit.default_timer()
    (U,V) = blc.ls(R,W,d)
    run_time = timeit.default_timer()-start_time
    if(data['n'].has_key(tuple_key) and data['n'][tuple_key].has_key(str(n))):#add time - m,d,n combo already present
        data['n'][tuple_key][str(n)].append(run_time)
    elif (data['n'].has_key(tuple_key)):#add m&time - d,n already present
	data['n'][tuple_key].update({str(n):[run_time]})
    else:#add n,d,m,time
        data['n'].update({tuple_key:{str(n):[run_time]}})
    n = n + 100
#print data    
f = open(filename, 'w+')
f.write(json.dumps(data))
f.close() 
    
#f.close()
    
    
    
    
    
    
