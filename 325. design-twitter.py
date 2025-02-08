from collections import defaultdict,deque

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.out = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.out.appendleft((userId,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
            return [tweetId for user, tweetId in self.out if userId == user or user in self.followers[userId]][:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)