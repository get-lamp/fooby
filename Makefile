up:
	cd banky/api && sudo docker compose up -d ; cd -
	cd selly/api/user && sudo docker compose up -d ; cd -

down:
	cd selly/api/user && sudo docker compose down ; cd -
	cd banky/api && sudo docker compose down ; cd -
