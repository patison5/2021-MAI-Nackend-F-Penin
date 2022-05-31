docker rm -f $(docker ps -a -q)
docker volume prune
# docker rmi $(docker images -a -q)
# docker-compose down -v 
