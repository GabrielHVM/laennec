# $PH^2$ Dataset

**Selecione a linguagem:**
- [English](README.md)
- [Português](README-pt.md)

$PH²$ é uma base de dados de imagens dermatoscópicas adquirida no Serviço de Dermatologia do Hospital Pedro Hispano, Matosinhos, Portugal.


## Descrição Sucinta
Este banco de imagens contém um total de 200 imagens dermatoscópicas de lesões melanocíticas, incluindo 80 nevos comuns, 80 nevos atípicos e 40 melanomas. A base de dados PH² inclui anotação médica de todas as imagens nomeadamente segmentação médica da lesão, diagnóstico clínico e histológico e avaliação de vários critérios dermatoscópicos (cores; rede pigmentar; pontos/glóbulos; estrias; áreas de regressão; véu azul-esbranquiçado).

## Conteúdo do banco de imagens
File organization
- ```PH2 Dataset images/```

    Dentro desta pasta existe uma pasta dedicada para cada imagem do banco de dados, que contém a imagem dermatoscópica original, a máscara binária da lesão segmentada bem como a máscara binária das classes de cores apresentadas na lesão cutânea.
- ```PH2_dataset.txt```

    Este arquivo contém a classificação de todas as imagens em um arquivo ".txt" de acordo com os critérios dermatoscópicos avaliados no banco de dados $PH^2$.
- ```PH2_dataset.xlsx```

    Este arquivo contém a classificação de todas as imagens em um arquivo ".xlsx" de acordo com os critérios dermatoscópicos avaliados no banco de dados $PH^2$.


## Referência
1. Teresa Mendonça, Pedro M. Ferreira, Jorge Marques, Andre R. S. Marcal, Jorge Rozeira. PH² - A dermoscopic image database for research and benchmarking, 35th International Conference of the IEEE Engineering in Medicine and Biology Society, July 3-7, 2013, Osaka, Japan. 