class banco:
    def __init__(self,objPessoa):
        self.nome = objPessoa["nome"]
        self.idade = objPessoa["idade"]
        self.saldo = objPessoa["saldo"]
    
    def mostrarSaldo(self):
        print(f"Seu saldo é : R$ {self.saldo}")
        
    def deposito(self):
        self.saldo += float(input("Escreva o quanto você deseja depositar: R$ "))
    
    def saque(self):
        saque = float(input("Escreva o quanto você deseja sacar: R$"))
        if self.saldo < saque:
            print("Saldo insuficiente!")
        else:
            self.saldo -= saque
        