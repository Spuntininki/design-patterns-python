#Open closed Principle
#Uma classe deve estar aberta para extensão, mas não para modificação.
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name: str, Color: Color, Size: Size) -> None:
        self.name = name
        self.color = Color
        self.size = Size

#O problema da abordagem adotada na criação da classe abaixo é que sempre que for necessário colocar um novo filtro, será necessário criar um novo metodo.
#O que viola o principio postulado.
class ProductFilter:
    def filter_by_color(self, products: list, color):
        for product in products:
            if product.color == color:
                return product
    #ad infinitum



#Uma solução seria a criação de classes abstratas, onde para implementar o filtro desejado é utilizado do padrão specification (Enterprise design patterns).
class Specification:
    def is_satisfied(self):
        pass

class betterFilter:
    pass

if __name__ == '__main__':
    abacate = Product('Abacate', Color.GREEN, Size.SMALL)
    alface = Product('Alface', Color.GREEN, Size.SMALL)
    pano = Product('Pano', Color.RED, Size.SMALL)
    guarda_chuva = Product('Guarda Chuva', Color.BLUE, Size.MEDIUM)

    produtos = [abacate, alface, pano, guarda_chuva]
    pf = ProductFilter()

    resultado = pf.filter_by_color(produtos, Color.GREEN)

    print(resultado.color)