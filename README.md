# Flask/Nameko microservice template

Template to use Flask with Nameko for microservices

# RUN RABBITMQ

> docker run -d --hostname rabbitmq -p 15672:15672 -p 5672:5672 --name rabbit rabbitmq:3-management

# RUN NAMEKO SERVICE

> nameko run service --broker amqp://guest:guest@localhost

# RUN NAMEKO SHELL

> nameko shell --broker amqp://guest:guest@localhost
