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
    print "the cost for section "+str(section)+ " is:"+ str(np.sum(c))

def section_cost(Q,section):
    for j in range(0,section):
		median = np.median(Q[j])
		calc_cost(Q[j],median,j)

def make_section(Q):
    Q = sorted(Q)
    for j in range (1,5):
        n = (len(Q)/j)
        f = lambda Q, n: [Q[i:i+n] for i in range(0, len(Q), n)]
        section_cost(f(Q,n),j)
        print "------ "+ str(j) + "number of cuts -----"
        
        # section_cost(Q,sections,n)
def plot_queries(Q):
    pyplot.figure()
    pyplot.plot(Q, np.zeros(Q.shape), '*')
    pyplot.savefig('queries.png')

queries = make_queries()
# print queries
plot_queries(queries)
sections = make_section(queries)
plot_queries(queries)