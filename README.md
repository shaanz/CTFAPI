# CTFAPI
The project consists of files used to build CTF version 2 
Details of version 1 : https://www.f5.com/labs/articles/education/demystifying-api-attacks-using-gamification
The files can be used to build and run docker containers 

Build the container using the build files in  source code provided or obtain  the images from docker hub (sbacker/witcherportal2 and sbacker/witchermesgserver) 

Steps to run the REST API server 
docker build -t sbacker/witcher_re .
docker run -it -d --name witcher10 -p8080:8080 -e PYTHONUNBUFFERED=1  sbacker/witcherportal2


Steps to run the websocket server 
docker build -t sbacker/witchermesgserver .
docker run -it -d --name mesg_server -p 8080:8080 sbacker/witchermesgserver


#### THE CTF Portal is built on CTFd.io   
Steps to pull down the container 
docker run --name ctfapi1 -p 8000:8000 -it -d sbacker/ctfapi2
