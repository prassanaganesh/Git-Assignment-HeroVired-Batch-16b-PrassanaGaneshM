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


