FROM postgres:16

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    postgresql-server-dev-16 \
    gcc \
    python3-dev \
    git \ 
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/mbslave-venv
ENV PATH="/opt/mbslave-venv/bin:$PATH"

# Instalando mbslave
RUN pip install --no-cache-dir 'mbslave'

WORKDIR /usr/src/app
COPY . .

# Torna o script executável
COPY init-mbslave.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-mbslave.sh

# Inicia o Banco e executa o script 
CMD ["postgres"]
