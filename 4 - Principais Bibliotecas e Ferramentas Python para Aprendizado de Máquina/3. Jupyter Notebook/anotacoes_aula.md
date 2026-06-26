# Anotações

Anotações referentes as aulas 8 [1] e 9 [2] do capítulo 3. 

Instalado o conda através do miniconda [3] para lidar com diferentes versões de python para não conflitar com o python do sistema operacional e quando necessário utilizar outra versão de python com base no curso ou aula apresentada. 

## Utilizando `conda`
Para inicializar o conda utilize
```bash
conda activate
``` 

Para finalizar o conda utilize
```bash
conda deactivate
``` 

## Utilizando o `jupyter notebook`
Para a instalação do jupiter notebook foi utilziado o conda-forge [4]. 

Jupiter notebook instalando utilizando: 
```bash
conda install jupyter
``` 

Para inicializar o servidor do jupyter utilize (certifique-se que o conta está ativado):
```bash
jupyer notebook
``` 

## Utilizando ambientes virtuais

Para criar um ambiente virutal `conda` utilize:
```bash
conda create -n myenv python=3.9 scipy=1.12.0 numpy
```
`-n`: Para nomear o ambiente, ex: `myenv`.

`python=3.9`: Opcional para definir a versão do python que será utilizada.

Em seguida os pacotes que serão instalados no ambiente:

`scipy=1.12.0`: Instala o `scipy` na versão 1.12.0.

`numpy`: Instala o `numpy` na última versão estável disponível.

Para ativar o novo ambiente criado utilize: 
```bash
conda activate myenv
```
Lembrando que `myenv` é o nome do ambiente que deseja ativar.

Para desativar utilize:
```bash
conda deactivate
```

Para listar os ambientes criados utilize:
```bash
conda info --envs
```

Para remover um abiente criado utilize: 
```bash
conda env remove --name myenv
```

Demais informações sobre os ambientes virtuais do conda pode ser encontradas em [6].