"""1. Use zip para juntar os dados em uma lista chamada 'relatorio'

2. Use filter para criar uma lista só com os alunos que foram mais de 10 vezes no mês.
   Chame essa lista de 'frequentes' e mostre só o nome deles.

3. Use map para criar uma nova lista com os valores das mensalidades com 5% de desconto.
   Chame essa lista de 'descontos'.

4. Use sum para calcular o faturamento total do mês.

5. Use all para verificar se todos pagaram mais de R$80.
   Use any para verificar se algum pagou mais de R$400.

6. Use sorted para ordenar a lista 'relatorio' pela frequência mensal (do maior para o menor).

7. Use max e min para mostrar:
   - Quem pagou mais e quanto.
   - Quem pagou menos e quanto."""

alunos = ['Bruno', 'Camila', 'Diego', 'Larissa']
planos = ['Mensal', 'Trimestral', 'Mensal', 'Semestral']
mensalidades = [89.90, 240.00, 89.90, 420.00]
frequencia_mensal = [4, 12, 2, 18]  # quantas vezes o aluno foi na academia no mês

relatorio = zip([alunos, planos, mensalidades, frequencia_mensal])

