# Definição do Método Analítico para Análise de Sentimentos em Companhias Aéreas

### Sumário
- [Introdução](#introdução)
- [Metadados](#metadados)
- [Metadatas](#Metadata)
- [Colaboradores](#colaboradores)

---

### Introdução

No cenário atual, onde a jornada de migração internacional exige cada vez mais planejamento e decisões bem informadas, o uso da análise de sentimentos tem se consolidado como uma estratégia eficaz para compreender a percepção dos consumidores em tempo real. As redes sociais, especialmente o X (antigo Twitter), tornaram-se espaços essenciais para que os usuários compartilhem suas experiências, elogios e frustrações — oferecendo, assim, um valioso repositório de dados sobre empresas e serviços.

Neste contexto, o presente projeto tem como objetivo aplicar técnicas de processamento de linguagem natural (NLP) e aprendizado de máquina para analisar as opiniões de brasileiros sobre diferentes companhias aéreas, com foco na experiência de voos entre o Brasil e os Estados Unidos. A iniciativa será conduzida pela Decolar, uma das maiores empresas de viagens da América Latina, fundada em 1999 e com presença em mais de 20 países. Reconhecida por seu papel inovador no turismo digital, a Decolar oferece uma ampla gama de serviços, incluindo passagens aéreas, hospedagens, pacotes de viagem e suporte personalizado ao cliente.

Com base em dados coletados diretamente do X, este estudo pretende identificar sentimentos positivos, negativos e neutros em relação às principais companhias aéreas utilizadas por brasileiros, fornecendo insights relevantes para orientar futuras decisões de viagem. A partir da análise desses sentimentos, será possível detectar padrões de preferência, pontos críticos na experiência dos passageiros e sugestões de melhorias que podem ser integradas aos serviços da Decolar.

Dessa forma, a proposta não apenas reforça o compromisso da empresa com a excelência no atendimento e a personalização da jornada do cliente, mas também evidencia como a inteligência artificial pode ser uma poderosa aliada na construção de soluções mais humanas, eficientes e alinhadas às reais necessidades de quem deseja realizar o sonho de migrar para os Estados Unidos com segurança e tranquilidade.


---

### Metadados

Fonte dos Dados

Os dados foram obtidos do conjunto ["Twitter US Airline Sentiment"](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) disponível no Kaggle.

Método de Coleta

Os tweets foram coletados em fevereiro de 2015 e classificados manualmente por sentimento (positivo, neutro ou negativo) em relação às principais companhias aéreas dos EUA.

Formato do Arquivo

- **Tipo de Arquivo**: CSV (Comma-Separated Values).

Licença de Uso

Os dados são disponibilizados no Kaggle para fins de pesquisa, análise e desenvolvimento, sendo permitida sua utilização para esses propósitos. No entanto, o uso comercial ou a redistribuição sem autorização expressa pode estar sujeito a restrições.

Contato

Para mais informações ou dúvidas sobre o uso dos dados, consulte a [página do conjunto de dados no Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) ou utilize os canais de comunicação da plataforma.

---

### Metadata

| Nome da Coluna                 | Tipo    | Descrição                                                                                                                                         |
|--------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **tweet_id**                   | int64   | Identificador único do tweet.                                                                                                                     |
| **airline_sentiment**          | object  | Classificação do sentimento do tweet (por exemplo, positivo, negativo ou neutro).                                                                |
| **airline_sentiment_confidence** | float64 | Nível de confiança associado à classificação do sentimento.                                                                                     |
| **negativereason**             | object  | Motivo associado à classificação negativa, quando aplicável (nem todos os tweets possuem esse valor).                                             |
| **negativereason_confidence**  | float64 | Nível de confiança na identificação do motivo negativo.                                                                                         |
| **airline**                  | object  | Nome da companhia aérea mencionada no tweet.                                                                                                      |
| **airline_sentiment_gold**   | object  | Anotação de sentimento padrão (gold standard) para validação, disponível para uma amostra restrita.                                                 |
| **name**                     | object  | Nome ou identificador do usuário que postou o tweet.                                                                                              |
| **negativereason_gold**      | object  | Anotação gold do motivo negativo, usada para validação, disponível em poucos casos.                                                               |
| **retweet_count**            | int64   | Número de vezes que o tweet foi retweetado.                                                                                                       |
| **text**                     | object  | Conteúdo textual completo do tweet.                                                                                                               |
| **tweet_coord**              | object  | Coordenadas geográficas (latitude e longitude) do tweet, quando disponíveis.                                                                      |
| **tweet_created**            | object  | Data e hora em que o tweet foi criado.                                                                                                            |
| **tweet_location**           | object  | Localização informada no tweet, quando disponível.                                                                                              |
| **user_timezone**            | object  | Fuso horário do usuário que postou o tweet, quando disponível.                                                                                    |

---

### Colaboradores

**Alunos**  
- Felipe Fagion Longarini  
- Lucas Oliveira  
- Gleider Mackedanz de Campos  
- Gabriel Henrique Titanegro Zanelatto  

**Professor**  
- Felipe Albino Dos Santos


<br>

