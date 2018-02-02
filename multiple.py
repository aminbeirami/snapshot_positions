import numpy as np
import matplotlib.pyplot as pyplot

def make_queries():
    Q = np.vstack([
        np.random.normal(4, 4, (20, 1)),
        np.random.normal(40, 4, (20, 1))
        ])
    a, b = np.min(Q), np.max(Q)
    Q = np.vstack([Q, np.random.uniform(a, b, (10, 1))])
    Q = Q - np.min(Q)
    return np.squeeze(Q)

def plot_queries(Q):
    pyplot.figure()
    pyplot.plot(Q, np.zeros(Q.shape), '*')
    pyplot.savefig('multiple.png')

def calc_cost(queries,snapshot,section):
    queries = np.array(queries)
    nQ = queries.shape[0]
    # nS = snapshot.shape[0]
    d = np.zeros((nQ, snapshot))
    for i in range(nQ):
        q = queries[i]
        d[i, :] = np.abs(snapshot - q)
    c = np.min(d, axis=1)
    cost = np.sum(c)
    print "the cost of section "+ str(section)+" is "+ str(cost)

def section_cost(Q,sections,n):
	splited_sections = []
	for i in range(0,n):
	 	splited_sections.append([x for x in Q if (x >sections[i] and x < sections[i+1])])
	print "------- "+str(i+1)+" number of cuts ---------"
	for j in range(0,len(splited_sections)):
		median = np.median(splited_sections[j])
		calc_cost(splited_sections[j],median,j)

def make_section(Q):
	maxValue = np.ceil(np.max(queries))
	for n in range (1,5):
		sections = []
		division = maxValue/n
		sections.append(0)
		for i in range(1,n+1):
			sections.append(sections[i-1]+division)
		section_cost(Q,sections,n)
def plot_queries(Q):
    pyplot.figure()
    pyplot.plot(Q, np.zeros(Q.shape), '*')
    pyplot.savefig('queries.png')

queries = make_queries()
plot_queries(queries)
sections = make_section(queries)
plot_queries(queries)