
 > Earlier, we took a look at the basic workflow for working with remotes when we want to fetch the changes manually, merge if necessary, and only then push any changes of our own. Since fetching and merging are so common, Git gives us the git pull command that does both for us. 
![imagen](https://user-images.githubusercontent.com/63612112/207994854-33028afd-013c-42e3-b822-a7f86ccbc73d.png)


Running git pull will fetch the remote copy of the current branch and automatically try to merge it into the current local branch. 


Let's check if our friend Blue Kalehas made any new changes to the repo. 
We'll run git pull and see what changes we get.
If you look closely at this output, you'll see that it includes the output of the fetch and merge commands that we saw earlier. 
![imagen](https://user-images.githubusercontent.com/63612112/207995408-9ed4e6f3-56c0-4351-8911-fcc5822675d3.png)
First, Git fetched the updated contents from the remote repository, including a new branch. And then it did a fast forward
merge to the local master branch. 

![imagen](https://user-images.githubusercontent.com/63612112/207995463-507ee148-f185-4e06-a372-6198da26364c.png)


We'll see that the all_checks file was updated as well. We can look at the changes by using git log -p -1. 
We see that our colleague added a check_disk_full function that includes the code from the other disk_usage py file that we saw earlier.

![imagen](https://user-images.githubusercontent.com/63612112/207995567-09ced7af-c4f3-486f-a000-b9a544163811.png)

So now I'll exit the editor with q. When we called git pull, we saw that there was also a new remote branch called experimental.
Our friend Blue Kale told us that they've started working on a new feature in that branch.


Let's check out the output of git remote show origin and see what it says about that new branch.
We see that there's a new remote branch called experimental, which we don't have a local branch for yet. 
To create a local branch for it, we can run git checkout experimental. 
When we checked out the experimental branch, Git automatically copied the contents of the remote branch into the local branch. 
The working tree has been updated to the contents of the experimental branch. 
Now we're all set to work on the experimental feature together with our colleague. 
In this last example, we got the contents of the experimental bunch together with those of the master branch when we called git pull, which also
merged new changes onto the master branch. 

![imagen](https://user-images.githubusercontent.com/63612112/207995890-4c0715ac-eff0-4ba6-a0dc-49101b43198f.png)

![imagen](https://user-images.githubusercontent.com/63612112/207996139-020ec726-1a53-44d5-9335-b38f3a256cd7.png)


If we want to get the contents of remote branches without automatically merging any contents into the local branches, we can call git remote update.
This will fetch the contents of all remote branches, so that we can just call checkout or merge as needed. 
We've now seen a bunch of different ways that we can use to interact with remote repositories. 
We've seen how to check their status, how to push and pull changes into repositories, and even how to get new branches out of them.

There's still more to come, but you're probably starting to see how useful this can be for collaborating with others. 
In our past examples, we've only looked at what happens with changes when they can be solved through fast forward. 
In upcoming videos, we'll look at what happens when we try to push changes, especially when our changes generate conflicts.
But before we do that, check out the reading for the list of all the commands involved, and then take the quiz to put this knowledge into practice.
