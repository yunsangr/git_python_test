from git import Repo
import os
PATH_OF_GIT_REPO = os.getcwd()  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script 1'



def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add("*")
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
