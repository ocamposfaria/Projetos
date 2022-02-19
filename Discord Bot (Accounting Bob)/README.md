# Discord Bot - Accounting Bob

Criei um bot no Discord para que eu possa registrar facilmente meus gastos pessoais. 

O bot recebe uma mensagem de uma compra realizada, e registra a informação, com a data do registro e com a categoria da compra, num .csv em uma máquina EC2 na AWS. Por exemplo, se gastei 20 reais com um pedido na cafeteria The Coffee, posso dizer "!credit 20 The Coffee restaurantes" (ou !debit, se paguei no débito) e o registro (da categoria restaurantes) irá para esse .csv. Em seguida, posso usar o comando !sendtosql para converter o .csv e fazer o upload dos dados para uma tabela numa base salva em um RDS da AWS. Assim, posso apontar uma planilha para essa base e consumir os dados que estou mandando para o bot.
