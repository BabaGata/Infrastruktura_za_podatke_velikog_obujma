git clone\n
cd Eksperimentalni\n
docker compose build --no-cache\n
docker compose up\
docker exec ab ab -n 1000 -c 10 http://localhost:5000/
