'''import requests
from git import Repo
#from os import getcwd


		
url = "https://raw.githubusercontent.com/farmanAbbasi/helloWorldJenkins/master/folder1/f1_text2.txt"
#directory = getcwd()
filename = 'C:/Users/moabbasi/Desktop/gitFiles/Test1.txt'
r = requests.get(url)
content=r.content.decode('ascii')

f = open(filename,'w')
f.write(content)
print(r.content)'''

import os
from git import Repo


COMMITS_TO_PRINT = 3


def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    t=repo.head.commit
    print("hello")
    my_string=str(repo.git.diff(t))
    temp=my_string.split("a",1)[1]
    temp2=temp.split(" ",1)[0]
    print(temp2)
    #print(str(repo.git.diff(t)))
    print("hello2")
    #print("\"{}\" by {} ({})".format(commit.summary,commit.author.name,commit.author.email))
    print(str(commit.authored_datetime))
    #print(str("count: {} and size: {}".format(commit.count(),commit.size)))
											 


def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


if __name__ == "__main__":
    repo_path = os.getenv('https://github.com/farmanAbbasi/helloWorldJenkins')
    #repo = git.Repo(os.path.dirname())
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path,search_parent_directories=True)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))
