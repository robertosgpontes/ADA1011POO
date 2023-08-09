class Fracao:
    
    def __init__(self, numerador:int, denominador:int) -> None:
        """_summary_

        Args:
            numerador (int): _description_
            denominador (int): _description_
        """
        self.numerador = numerador
        self.denominador = denominador
        
    def soma(self, fracao):
        """_summary_

        Args:
            fracao (Fracao): _description_

        Returns:
            Fracao: _description_
        """
        numerador =  fracao.denominador*self.numerador + fracao.numerador*self.denominador
        denominador = fracao.denominador*self.denominador
        
        return Fracao(numerador, denominador)
    
    def subtracao(self, fracao):
        
        numerador =  fracao.denominador*self.numerador - fracao.numerador*self.denominador
        denominador = fracao.denominador*self.denominador
        
        return Fracao(numerador, denominador)
    
    def multiplicacao(self, fracao):
        
        numerador =  self.numerador * fracao.numerador
        denominador = fracao.denominador * self.denominador
        
        return Fracao(numerador, denominador)
    
    def divisao(self, fracao):
        
        numerador =  self.numerador * fracao.denominador
        denominador = fracao.numerador * self.denominador
        
        return Fracao(numerador, denominador)
    
    def apresenta(self):
        return f"{self.numerador}/{self.denominador}"   