import datetime

class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque = 500.00
        self.saque_diario = 3
        self.saque_realizado = 0
        self.data_atual = datetime.date.today()

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito. Por favor, deposite apenas valores positivos.")
            return # fará o retorno de volta as opções, caso o valor inserido seja inválido.
        
        self.saldo += valor
        self.extrato.append(f"Depósito: +R$ {valor:,.2f}")
        print(f"Depósito de R$ {valor:,.2f} realizado com sucesso!")
        print("===============================\n")

    def sacar(self, valor):
        if datetime.date.today() != self.data_atual:
            self.saque_realizado = 0
            self.data_atual = datetime.date.today()
        
        if self.saque_realizado >= self.saque_diario:
            print("Limite de saques diários atingido.")
            return False # retornará para as opções quando o limite for atingido.
        
        if valor <= 0:
            print("Valor inválido para saque. Por favor, deposite apenas valores positivos.")
            return False # 
        
        if valor > self.limite_saque:
            print(f"O limite máximo por saque é de R$ {self.limite_saque:,.2f}.")
            return False # não aceita saques superior a R$ 500.
        
        if valor > self.saldo:
            print("Saldo insuficiente para saque.") 
            return False # caso não tenha saldo, retornará para as opções.
        
        self.saldo -= valor
        self.extrato.append(f"Saque: -R$ {valor:,.2f}")
        self.saque_realizado += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print("===============================\n")
        return True

    def visualizar_extrato(self):
        print("\n======= EXTRATO BANCÁRIO =======")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for movimentacao in self.extrato:
                print(movimentacao)
        print(f"Saldo atual: R$ {self.saldo:,.2f}")
        print("===============================\n")

def app():
    conta = SistemaBancario()
    while True:
        print("\n$$ Sistema Bancário $$")
        print("O que deseja?")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato Bancário")
        print("4 - Sair.")
        print("===============================\n")
    
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            valor = float(input("Qual o valor do depósito? "))
            conta.depositar(valor)
        
        elif opcao == '2':
            while True:
                valor = float(input("Qual valor deseja sacar? "))
                saldo_anterior = conta.saldo
                conta.sacar(valor)
                if saldo_anterior != conta.saldo:
                    break
                else:
                    break # caso não tenha saldo, retornará para as opções.
        
        elif opcao == '3':
            conta.visualizar_extrato()
        
        elif opcao == '4':
            print("Saindo do Sistema Bancário. Até logo!")
            break
        
        else:
            print("Opção Inválida. Tente novamente.")
        
if __name__ == "__main__":
    app()