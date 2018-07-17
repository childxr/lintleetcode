import Queue

class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating 
    @return: the top k largest rating moive which contact with S
    """
    def topKMovie(self, rating, G, S, K):
        # Write your code here
        if not rating:
            return []
        
        n = len(rating)
        
        g = [set([]) for _ in xrange(n)]
        for i in xrange(len(G)):
            for m in G[i]:
                g[i].add(m)
                g[m].add(i)
        
        visited = set([])
        queue = Queue.Queue()
        queue.put(S)
        visited.add(S)
        
        while not queue.empty():
            cur = queue.get()
            for n in g[cur]:
                if n not in visited:
                    visited.add(n)
                    queue.put(n)
        
        visited.remove(S)
        candidate = [(rating[n], n) for n in visited]
        
        candidate.sort(cmp=lambda a, b: b[0] - a[0])
        
        #print candidate
        #print "***"
        
        if len(candidate) >= K:
            return [candidate[i][1] for i in xrange(K)]
        else:
            return [candidate[i][i] for i in xrange(len(candidate))]
        

