import collections
import json
import matplotlib.pyplot as plt


filename = "test.json"
f = open(filename, 'r')
data = json.load(f)
f.close()

ndata = collections.OrderedDict(sorted(data['n'].items()))

n_vals = ndata.keys()
t_vals = []
temp_tvals = []


for key in n_vals:
    for element in ndata[key]:
        temp_tvals.append(element)
    t_vals.append(sum(temp_tvals)/len(temp_tvals)) 
    
    
#x axis: n_vals
#y_axis: t_vals

plt.plot(n_vals, t_vals)
plt.xlabel("n")
plt.ylabel("t")
plt.title("scaling: n vs t")
plt.savefig("graph.png") 
plt.show()   
