class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points):
            return points
        dist = {}
        point = {}
        m = 0
        for i in range(len(points)):
            point[i] = points[i]
        for i in points:
            dist[m] = (((i[0])**2) + ((i[1])**2))**0.5
            m += 1
        dd = defaultdict(list)
        for d in (dist, point):
            for key, value in d.items(): 
                dd[key].append(value) 
        res = [[k,v] for k,v in dd.items()]
        res.sort(key = lambda x: x[1][0])
        result = []
        for i in range(k):
            result.append(res[i][1][1])
        return result