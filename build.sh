docker stop fmp-serving
docker rm fmp-serving
docker rmi hhkim940/fmp-serving:latest

docker build -t hhkim940/fmp-serving:latest .
docker push hhkim940/fmp-serving:latest

docker run --name fmp-serving -d -p 8000:8000 hhkim940/fmp-serving
