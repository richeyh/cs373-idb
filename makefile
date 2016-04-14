IMAGE_NAME_APP := cs373idb_app
IMAGE_NAME_DB := cs373idb_db
IMAGE_NAME_LB := cs373idb_lb
DOCKER_HUB_USERNAME := rychoi

FILES :=                         \
    .travis.yml                  \
    .gitignore                   \
	  makefile                     \
    apiary.apib                  \
    IDB2.log                     \
    models.html                  \
    app/models.py                    \
    app/tests.py                     \
    UML.pdf

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

models.html: models.py
	pydoc3 -w models

IDB2.log:
	git log > IDB2.log

db-init:
	docker-compose run --rm --no-deps app make init

db-update:
	docker-compose run --rm --no-deps app make upgrade
	docker-compose run --rm --no-deps app make migrate

fetch:
	docker-compose run --rm --no-deps app make fetch

docker-build:
	@if [ -z "$$CONTINUE" ]; then \
		read -r -p "Have you sourced the docker.env file for our Carina cluster? (y/n): " CONTINUE; \
	fi ; \
	[ $$CONTINUE = "y" ] || [ $$CONTINUE = "Y" ] || (echo "Exiting."; exit 1;)
	@echo "Building the images..."
	docker login

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_APP} app
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_APP}

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_DB} db
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_DB}

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_LB} lb
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_NAME_LB}

docker-push:
	docker-compose --file docker-compose-prod.yml up -d

docker-db:
	docker-compose --file docker-compose-prod.yml run -d --rm --no-deps app make init

docker-db-update:
	docker-compose --file docker-compose-prod.yml run -d --rm --no-deps app make upgrade
	docker-compose --file docker-compose-prod.yml run -d --rm --no-deps app make migrate

docker-db-fetch:
	docker-compose --file docker-compose-prod.yml run --rm --no-deps app make fetch

docker-proxy:
	docker run -it --rm \
	--name temp-proxy \
	--net cs373idb_backend \
	--publish 3306:3306 \
	--env PROTOCOL=TCP \
	--env UPSTREAM=cs373idb_db \
	--env UPSTREAM_PORT=3306 \
	carinamarina/nginx-proxy
