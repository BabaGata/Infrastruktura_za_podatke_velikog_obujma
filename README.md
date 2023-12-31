git clone<br>
cd Eksperimentalni<br>
docker compose build<br>
docker compose up<br>
docker exec ab ab -n 1000 -c 10 http://localhost:5000/
