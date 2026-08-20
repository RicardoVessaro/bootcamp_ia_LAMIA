#!/bin/bash

set -e # Para caso de erro para a execução

export PATH="/opt/mbslave-venv/bin:$PATH" # Encontra o comando no venv criado antes

# Configurações postgres para apenas iniciar
export PGHOST="/var/run/postgresql"
export PGUSER="postgres"

# Inicia de fato o mbslave com configuracao inicial usando o usario default 
# do posgres
mbslave -c /usr/src/app/mbslave.conf init --create-user --create-database 
