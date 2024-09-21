'''' Apache Kafka

Quando se fala de Kafka em relação a "localização", pode-se estar se referindo ao Apache Kafka em um contexto de sistemas distribuídos, onde ele é utilizado para gerenciar e processar fluxos de dados em tempo real, frequentemente em arquiteturas de microserviços.

Em sistemas de localização, Kafka pode ser usado para:

Coleta de dados: Receber dados de sensores ou dispositivos móveis que coletam informações de localização.
Processamento em tempo real: Analisar esses dados em tempo real para tomar decisões imediatas (como em aplicativos de navegação).
Integração de dados: Facilitar a comunicação entre diferentes serviços que precisam compartilhar informações de localização.
Se precisar de mais detalhes ou um exemplo específico, é só avisar!
apache kafka é um Broker um intermediario do servidor até o cliente

Conceitos kafka

Quando um consumidor consome o seu dado ao invés do dado for apagada ela fica armazenada em um banco de dados do apache kafka
ele funciona de forma distrubuida 
Cada vez que você cria um tópico ele consegue dividir esse topico em até 3 gavetas,  em até 3 maquinas se caso uma
parar, outra irá começar a mandar os dados replicados.
Certo mas o pc que apagou vai perder as informações?
Não,porque ele tem umreplication factory


'''