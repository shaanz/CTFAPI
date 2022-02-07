# Normal config 
#docker build -t sbacker/witcherportal2 .
#docker run -it -d --name witcher10 -p80:80 -e PYTHONUNBUFFERED=1  sbacker/witcherportal2 
#docker push sbacker/witcherportal2

#Volterra RE Config
docker build -t sbacker/witcher_re .
docker run -it -d --name witcher10 -p8080:8080 -e PYTHONUNBUFFERED=1  sbacker/witcher_re
docker push sbacker/witcher_re