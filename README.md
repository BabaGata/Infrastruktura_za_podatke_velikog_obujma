git clone<br>
cd Infrastruktura_za_podatke_velikog_obujma<br>
docker compose build<br>
docker compose up<br>
docker exec ab ab -n 1000 -c 10 http://localhost:5000/
