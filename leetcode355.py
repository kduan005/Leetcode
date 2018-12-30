import collections, heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followship = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweet, heap = [], []
        tweet.extend(self.tweets[userId])
        for followee in self.followship[userId]:
            tweet.extend(self.tweets[followee])
        heapq.heapify(heap)
        for i in range(len(tweet)):
            if len(heap) < 10:
                heapq.heappush(heap, tweet[i])
            else:
                if tweet[i] > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, tweet[i])
        return [heapq.heappop(heap)[1] for i in range(len(heap))][::-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.followship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followship[followerId]:
            self.followship[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
