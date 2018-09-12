import praw
import pdb
import re
import json

# create Reddit instance
reddit = praw.Reddit("bot1")

#select subreddit
subreddit = reddit.subreddit("jokes")

'''repliedTitles = []
repliedTexts = []

with open("topPosts.json") as json_file:
    topPosts = json.load(json_file)


for post in subreddit.top(limit=1000):
    if post.id not in topPosts["posts"]:
        topPosts["posts"].append({
            "id": post.id,
            "title": post.title,
            "text": post.selftext
        })

with open('topPosts.json', 'w') as outfile:
    json.dump(topPosts, outfile)

with open("post_ids_replied_to.txt", "r") as f:
   post_ids_replied_to = f.read()
   post_ids_replied_to = post_ids_replied_to.split("\n")
   post_ids_replied_to = list(filter(None, post_ids_replied_to))'''

for submission in subreddit.new(limit=10):
    '''if submission.id not in post_ids_replied_to:
        for post in topPosts["posts"]:
            if post.title == submission.title and post.selftext == submission.selftext:
                repostID = post.id
                repostTopComment = submission.comments.sort(top)'''
    for comment in submission.comments.sort(new):
        print(comment.body)

