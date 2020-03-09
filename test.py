from git import Repo
import os
PATH_OF_GIT_REPO = os.getcwd()  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script 1'


def git_push(files_to_add, commit_message):
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(files_to_add)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push('*', 'adding hello, bye')
