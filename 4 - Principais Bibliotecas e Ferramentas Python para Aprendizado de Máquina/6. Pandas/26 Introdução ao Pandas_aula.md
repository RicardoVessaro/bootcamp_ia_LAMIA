# 26 Introdução ao Pandas_aula

Pandas é escrita sobre o NumPy.

Utilizada para visualização de dados e comparado sua semelhança ao excel.

Com Pandas você pode trabalhar com muito mais quantidades de dados como `strings` `classes`, etc.

Para instalar Pandas utilize:
```bash
conda install pandas
```

## Ambiente Virtual

Utilizado um novo ambiente virtual para o capítulo sobre Pandas.

Para criar o ambiente e adicioná-lo utilizou-se:
```bash
# Cria uma ambiente virtual do conda com python 3.14.6 e pandas
conda create -n env-6-pandas python=3.14.6 pandas

# Ativa o ambiente virtual criado
conda activate env-6-pandas  

## Adicionar no kernel do jupyter conforme [7]
# instala o ipykernel
conda install ipykernel  

# adiciona o ambiente virtual do conda ao kernel jupyter
python -m ipykernel install --user --name env-6-pandas --display-name "Python 3.14.6 (pandas)"
```
