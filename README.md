# Git-Fundamentals

## 1. git clone : Creates a copy of an existing Git repository. 
- Syntax: **$git clone git_repository_name**
- Example : **$git clone https://www.github.com/KiranGaikwad2020/Git-Fundamentals.git**
- Here **https://www.github.com/KiranGaikwad2020/Git-Fundamentals.git** represents the repository name.


## 2. git add : Moves changes from the working directory to the staging area. 
- Syntax: **$git add filename_name or filenames**
- Example : **$git add test.py**
- Here **test.py** represents the file name which is to be added in git environment.
- Variant: if you have multiple files in current working directory to add in staging area use the command **$git add .**

## 3. git commit: Takes the staged snapshot and commits it to the project history. 
- Syntax: **$git commit -m "a sutaible commit message"**
- Example : **$git commit -m "New project file is created"**
- Here **-m** represents the sutiable messages to be used to commit.


## 4. git config: A convenient way to set configuration options for your Git installation. You’ll typically need to use this immediately after installing Git on a new development machine. 
- IMP: following git configurations is to be carried out to perofrm push operations with user identification.
- Syntax: **$git config --global user.email "mentionusermail"** and **$git config --global user.name "mention_username"**
- Example : **$git conig --global  user.email"abc@gmail.com"** and **$git config --global user.name "abc xyz"**

  
## 5. git push: It lets you move a local updates to remote github repository, which serves as a convenient way to publish data to remote github repository. 
- Syntax: **$git push**
- Here user will be directed to enter **user github credentails** to push the updates to remote github repository.

## 6. Personal Access Token Creation Process to use it as password while perofming github user authenitcation

- Go to Settings ---> Developer Settings ---> Personal Access Token
  
![Settings](images/passwordCreationProcess-1.png)

![Developer Settings](images/passwordCreationProcess-2.png)

![Personal Access Token](images/passwordCreationProcess-3.png)
  
- Click on Generate new token (classic)

![Token Create](images/passwordCreationProcess-4.png)

- Click on Generate Token Button present in bottom after filling all the required information.

## 7. Follow the following link to gain more expertise on Git commands
** https://atlassian.com/git/glossary#commands **
