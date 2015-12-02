""" 
Use this to test how function scales
JSON file is updated with the key value pairs
n:time
d:time
m:time
so that most current results are always recorded. 

"""

import blc
import timeit
import json

n = 500
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

while (n < 600):
    
    R = blc.createR(n,m,d)
    W = blc.sampleR(R)   
    start_time = timeit.default_timer()
    (U,V) = blc.ls(R,W,d)
    if(data['n'].has_key(str(n))):
        data['n'][str(n)].append(timeit.default_timer()-start_time)
    else:
        data['n'].update({str(n):[timeit.default_timer()-start_time]})
    #f.write(str(timeit.default_timer()-start_time)+ "\n")    
  #  print data
    n = n + 10
#print data    
f = open(filename, 'w+')
f.write(json.dumps(data))
f.close 
    
#f.close()