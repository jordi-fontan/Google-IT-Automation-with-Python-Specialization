
## Skipping the Stage area

UC: We want to commit a small change without it having to be for long in stage area, or not want to write long commit messages
TRULY SMALL CHANGES THAN NO NEED FURTHER EXPLANATION



`git commit -a`

> be careful it doesn't add untracked files so it's not the same as git add + git commit

![imagen](https://user-images.githubusercontent.com/63612112/196896362-fc15a6fc-b21c-454b-a53d-df434486ab50.png)

![imagen](https://user-images.githubusercontent.com/63612112/196897244-bffc9e77-b7ac-4810-9ad0-c70adfb7dcef.png)

>Once commit we can't add anything more at stage area in that commit. careful then

# HEAD and MASTER

###  Git Log After last commit

![imagen](https://user-images.githubusercontent.com/63612112/196898128-727abda4-ae75-4c8a-83a8-c6cdeaa4b9f3.png)

#### MASTER? HEAD?

HEAD ---> WHere the current snapshop is it ( pointer to last snapshot)

![imagen](https://user-images.githubusercontent.com/63612112/196898585-a27d8f4f-a670-46cb-872b-d0847bf5527e.png)

### Git log -p (patch)

`Give us info about the specific changes ( as diff does)`

![imagen](https://user-images.githubusercontent.com/63612112/196903978-2760082d-ebc5-4bc3-a079-211c6e921479.png)

### git show *commitId*

### git log --stat

## Changes we still haven't commit

- For complex changes, before commit we need to test.

`git diff`
`git diff <filename>`

![imagen](https://user-images.githubusercontent.com/63612112/196906575-a06438e9-0a2b-4d53-9538-ebeab7220c59.png)


#### git add -p (aks interactively if we want to stage or not)
![imagen](https://user-images.githubusercontent.com/63612112/196907455-c31db396-0da9-4574-a298-a930cae6dad5.png)

git diff---> only commited
git diff --staged ---> staged

![imagen](https://user-images.githubusercontent.com/63612112/196907877-df2602ad-df51-49f1-b69d-ff5ceb5b54e4.png)

# Deleting Renaming

 `Git rm <filename>`
 
 
![removing a file](https://user-images.githubusercontent.com/63612112/196909064-44df1a38-c08d-46e3-820b-35ab576d4613.png)

And next, commit 

![imagen](https://user-images.githubusercontent.com/63612112/196909374-8383adb6-86df-48aa-afbb-7dacadc74ae3.png)


## Renaming 

 `Git mv <filename>`
 
 
## Git Ignore

![imagen](https://user-images.githubusercontent.com/63612112/196910324-7111bbd2-b355-4a04-98dc-0c8b7c6e3b56.png)

 
![imagen](https://user-images.githubusercontent.com/63612112/196909877-26ae266f-1aa3-47f2-bc69-d8889a66329e.png)


![imagen](https://user-images.githubusercontent.com/63612112/196910547-d8052c6c-df1c-4cdc-9c0f-054f7dc6378b.png)


Advanced Git Cheat Sheet

Command
	

Explanation & Link

git commit -a
	

Stages files automatically

git log -p
	

Produces patch text

git show
	

Shows various objects

git diff
	

Is similar to the Linux `diff` command, and can show the differences in various commits

git diff --staged
	

An alias to --cached, this will show all staged files compared to the named commit

git add -p
	

Allows a user to interactively review patches to add to the current commit

git mv
	

Similar to the Linux `mv` command, this moves a file

git rm
	

Similar to the Linux `rm` command, this deletes, or removes a file

There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as this one.
.gitignore files

.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

A few common examples of file patterns to exclude can be found here.
