#!/bin/bash

echo "Installing Erlang"

wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb

dpkg -i erlang-solutions_1.0_all.deb

echo "Installing Erlang binaries"
apt-get update
apt-get install erlang erlang-nox

echo "Installing RabbitMQ"

add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main'

wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

echo "Installing binaries"
apt-get update
apt-get install rabbitmq-server

echo "Complete"
