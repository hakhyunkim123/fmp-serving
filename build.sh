docker rmi hhkim940/fmp-serving:latest
docker build -t hhkim940/fmp-serving:latest .
docker push hhkim940/fmp-serving:latest

docker run -d -p 8000:8000 hhkim940/fmp-serving
