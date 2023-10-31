salary = float(input('Qual é o salario do funcionario?'))
newSalary = salary / 100 * 115
print('Um Funcionario que ganhava R${}, com 15% de aumento, agora vai receber R${:.2f}'. format(salary, newSalary))