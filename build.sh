docker build -t sbacker/witchermesgserver .
docker run -it -d --name mesg_server -p 8080:8080 sbacker/witchermesgserver
docker push sbacker/witchermesgserver