class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson]) 
        time_map={}
        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)
        for t in sorted(time_map.keys()):
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])
        return list(secrets)
      
            
#         graph = defaultdict(list)

#         for x,y,t in meetings:
#             graph[x].append((y,t))
#             graph[y].append((x,t))

#         heap = [(0,firstPerson)] #time,person
#         for nei,time in graph[0]:
#             heapq.heappush(heap,(time,nei))
        
#         visited = set([0])

#         while heap:
#             time,person = heapq.heappop(heap)

#             if person in visited:
#                 continue

#             visited.add(person)

#             for nei,t in graph[person]:
#                 if t>=time:
#                     heapq.heappush(heap,(t,nei))
# return visited
    