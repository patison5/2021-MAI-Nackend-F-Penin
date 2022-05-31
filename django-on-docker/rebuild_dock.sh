sudo docker rm test
variable=`sudo docker build . | (tail -n1) | awk 'NF>1{print $NF}' `
sudo docker run --name test $variable