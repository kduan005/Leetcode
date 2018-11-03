class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(room, l):
            if l[room]:
                return
            else:
                l[room] = 1
                for nei in rooms[room]:
                    dfs(nei, l)

        l = [0 for i in range(len(rooms))]
        dfs(0, l)
        for truth in l:
            if not truth:
                return False
        return True
        
