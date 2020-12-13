.PHONY: build
APP_VERSION=$$(git-version show)

# Make content for developer
help:
	@echo "dev			Create docker image for dev"
	@echo "qas			Create docker image for qas"
	@echo "prod			Create docker image for prod"
	@echo "run-service			Start Nameko RPC service"
	@echo "version			Show version"


build = echo "$(APP_VERSION)" > version.txt && docker-compose build && docker-compose push

dev:
	export ENVIRONMENT=dev && $(build)

qas:
	export ENVIRONMENT=qas && $(build)

prod:
	export ENVIRONMENT=prod && $(build)

version:
	echo $(APP_VERSION)

run-service:
	nameko run service_loader --broker amqp://guest:guest@localhost