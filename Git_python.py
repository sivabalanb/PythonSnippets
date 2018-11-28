import os
import datetime
import git

repo = git.Repo(os.getcwd())

master = repo.head.reference

print(master.name)

print(master.commit.message)

print(datetime.datetime.fromtimestamp(master.commit.committed_date))

#repo = Repo(path)
from git import Repo, Commit

repo = git.Repo(os.getcwd())

for commit in repo.iter_commits():
    print("Author: ", commit.author)
    print("Summary: ", commit.message)