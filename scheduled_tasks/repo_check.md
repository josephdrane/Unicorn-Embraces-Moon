# git repo check script

## Manual process

```
pi@rebooter:~/Unicorn-Embraces-Moon $ git remote -v
origin	git@github.com:josephdrane/Unicorn-Embraces-Moon.git (fetch)
origin	git@github.com:josephdrane/Unicorn-Embraces-Moon.git (push)

pi@rebooter:~/Unicorn-Embraces-Moon $ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

pi@rebooter:~/Unicorn-Embraces-Moon $ git fetch
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0
Unpacking objects: 100% (4/4), done.
From github.com:josephdrane/Unicorn-Embraces-Moon
   22b81a3..70d0470  master     -> origin/master

pi@rebooter:~/Unicorn-Embraces-Moon $ git status
On branch master
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

pi@rebooter:~/Unicorn-Embraces-Moon $
```
