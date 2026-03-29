# Git-Assignment-HeroVired-Batch-16b-PrassanaGaneshM
Git_assignment_HeroVired


This repository demonstrates multiple Git workflows while building simple Python utilities. The assignment includes the following tasks:

* Q1 – Calculator Plus Application (branching, PR, tagging)
* Q2 – Git Large File Storage (LFS)
* Q3 – Geometry Calculator using Git Stash

All steps below include the actual commands and outputs captured during execution.

# Q1 – Calculator Plus Application

## a. Create Repository
       
       Repository named git_assignment_HeroVired was created in the GitHub account prassanaganesh-repo and set as a private repository.

## b. Clone Repository to Local Machine
       git clone https://github.com/prassanaganesh/Git-Assignment-HeroVired-Batch-16b-owned-by-Prassana-Ganesh-M.git

## c. Create and Switch to dev Branch

       git branch dev
       git checkout dev

## d. Added Provided Calculator Application Code

```Python
import math
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
```
## e. Commit 
       git add .
       git commit -m "Add base calculator"

   Push branch:
         
          git push origin dev

## f.Merge dev → main and Create Release v1
       
       git checkout main
       git merge dev
       git tag v1.0
       git push origin v1.0

<img width="947" height="492" alt="image" src="https://github.com/user-attachments/assets/b0b4fd06-db73-4ca6-b212-c8b0d50d985f" />

## g. Create Feature Branch feature/sqrt

       git checkout main
       git branch feature/sqrt
       git checkout feature/sqrt

<img width="937" height="208" alt="image" src="https://github.com/user-attachments/assets/cc31ed46-dfbc-42bc-b00c-39793b2e0d3b" />

## i. Implement Square Root Feature

       git add .
       git commit -m "Added square root feature"
       git push origin feature/sqrt

## j. Fix Critical Bug in dev
       
- Updated divide function:

 ```python
      def divide(self, a, b):
           if b == 0:
         raise ValueError("Cannot divide by zero.")
           return a / b
```
- Commit fix:
  
         git checkout dev
         git add .
         git commit -m "Fix division by zero bug"
         git push origin dev

<img width="1332" height="912" alt="image" src="https://github.com/user-attachments/assets/e7c4ec09-f4b2-4f88-9004-1e341ab9a4ef" />

## Pull Request & Review

       - PR from feature/sqrt → main.
       - Merge feature/sqrt → dev
       - Merge dev → main.

<img width="1327" height="786" alt="image" src="https://github.com/user-attachments/assets/edbc10df-2f67-4a96-8224-b4d4630eb42e" />


# Q2 – Git Large File Storage (LFS)

a.Create lfs Branch

       git lfs install --> Install Git LFS
       git branch lfs
       git checkout lfs
       
b. Verify Git LFS Installation
       git lfs status
       
-Output:

       On branch lfs

Objects to be committed:

       Objects not staged for commit:
       This confirms Git LFS is installed.-Track Large Files

       
c. Track Large Files

       git lfs track "*.zip" --> Track large files

       git branch lfs       
       
<img width="1202" height="330" alt="image" src="https://github.com/user-attachments/assets/924104d3-50a7-49d6-a84a-965deb74d7c1" />

d. Commit .gitattributes
       git add .gitattributes
       git commit -m "Configure Git LFS tracking"
       
<img width="1482" height="717" alt="image" src="https://github.com/user-attachments/assets/42ce0bed-8356-4e7b-9085-a812a64d1536" />

e. Add Large Binary File

       Rawdata.zip
       git add Rawdata.zip
       git commit -m "Add large file using Git LFS"

<img width="946" height="170" alt="image" src="https://github.com/user-attachments/assets/0df1aff6-2e9b-41bb-91e8-7ce14a40f679" />

f. Push Branch

       git push origin lfs       

g. Verify LFS Tracking

       git lfs ls-files
       
<img width="1385" height="912" alt="image" src="https://github.com/user-attachments/assets/1ffd6cb1-7c13-4198-91f3-51ecdf048d33" />
