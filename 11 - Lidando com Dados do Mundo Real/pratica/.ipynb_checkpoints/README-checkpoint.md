
# Prática 11 - Lidando com Dados do Mundo Real 

Grande parte dos arquivos gerados são gerados na pasta `dados` e depois movidos para pastas de versão (`path-versao`) para que os dados gerados em testes não sejam sobreescritos ou perdidos durante o desenvolvimento do `notebook`. Os dados podem ter sido copiados ao invés de movidos para não influenciar a execução do `DataFrame` dependendo o caso.

**Segue o resumo, ordem que foi executado e criado os _notebooks_:**
- `extrair_dados_kworb_pratica`: Extrai os dados do site do Kworb, arquivos movidos para o diretório `dados/<path-versao>/kworb`.
- `transformar_dados_kworb_pratica`: Transforma os dados extraídos do site do Kworb para o diretório `dados/<path-versao>/kworb/transformacao`.
- `extrair_dados_musicbrainz_pratica`: Extrai os dados do banco de dados da musicbrainz que foi baixado, os dados são buscados através de uma consulta no banco de dados, os arquivos desse são copiados para o diretório `dados/<path-versao>/muscibrainz`. O arquivo `dados/musicas_generos` é um dos arquivos compiados, ele não foi movido pois as consultas ficam em andamento, por conta disso ele é utilizado como ponto de parada (_checkpoint_) para que continue de onde parou, dessa forma não é necessário buscar os arquivos novamente e _notebooks_ que leem este arquivo podem usar sua cópia.
- `transformar_dados_musicbrainz_pratica`: Transforma os dados extraídos criando um vetor para representar os gêneros catalogados.
- `agrupar_dados_transformados_para_modelo_pratica`: Agrupa os dados transformados resultando em um `DataFrame` com as informações necessárias para o modelo de recomendação, nele consta as métricas de pontuação e o vetor de genêros.
- `recomendacao_musicas`: Cria o modelo de recomendação utilizando KNN, normalizando os dados de pontuação e calculando a distância dos vetores de gêneros, esses dados são utilizados para recomendar músicas com base na música escolhida com a opção de repetir o artista ou não.

Muitas das músicas não possuem o genêro catalogado no banco de dados da musicbrainz por isso elas não são considerados na recomndação apesar de não ser a melhor prática quando se trata de dados nulos. Para popular os dados seria interessante um modelo que faz o cátalogo desses itens mas esse modelo não foi abordado nessa prática, talvez possa ser feito em uma prática futura de acordo com o aprendizado do treinamento.

**Dos _notebooks_ que podem ou foram reexecutados**

Os seguintes _notebooks_ foram reexecutados na seguinte ordem conforme os dados do arquivo `musicas_generos.csv` eram atualizados:

- `transformar_dados_musicbrainz_pratica`.
- `agrupar_dados_transformados_para_modelo_pratica`.
- `recomendacao_musicas`.

Os _notebooks_ foram atualizados conforme anova pasta de versão, por fim foi utilizado a versão `dados/final`. Demais notebooks não foram executados novamente pois a execução altera o `uuid` utilizado para identificar os registros tratados e os vínculos realizados.
