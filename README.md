git clone 
cd Eksperimentalni
docker compose build --no-cache
docker compose up
docker exec ab ab -n 1000 -c 10 http://localhost:5000/
