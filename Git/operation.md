## Initial
git init
git add .
git commit -m "Initial commit"

git remote add origin https://github.com/${GITHUB_USERNAME}/{REPONSITORY_NAME}.git
git branch -M main
git push -u origin main


## Branch
### Create and switch to a new branch
```git checkout -b ${BRANCH_NAME}```
### Set projection from local branch to remote branch
```git branch -u origin/${BRANCH_NAME}```
### See projection relationship
```git branch -vv```