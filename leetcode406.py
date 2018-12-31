class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda k: (k[0], -k[1]), reverse = True)
        n = len(people)
        for i in range(1, n):
            if people[i][1] < i:
                tmp = people[i]
                for j in range(i, tmp[1], -1):
                    people[j] = people[j-1]
                people[tmp[1]] = tmp
        return people
        
