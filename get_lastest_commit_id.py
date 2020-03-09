from git import Repo
import os

def get_lastest_commit():
    repo = Repo(os.getcwd())
    lastest_commit = repo.head.commit
    return lastest_commit


if __name__ == '__main__':
    print(get_lastest_commit())
