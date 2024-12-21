up: build
	sudo docker run --name c_selly-user -p 8080:8000 selly-user

build:
	sudo docker build -t selly-user api/user

down:
	sudo docker compose down

clean:
	sudo docker rmi selly-user -f
	sudo docker rm c_selly-user
	sudo docker volume rm selly_postgres_data


