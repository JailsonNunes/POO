class Quadrado:
	def __init__(self,lado, area, perimetro):
		self.lado = lado;
		self.area = area;
		self.perimetro = perimetro;

	def calcularPerimetro(self):
		resultado = 4 * self.lado
		self.perimetro = resultado

	def calcularArea(self):
		valor = self.lado * self.lado
		self.area = valor
	
	def imprimir(self):
		print("Perimetro e: ", self.perimetro)
		print("Area e: ", self.area)