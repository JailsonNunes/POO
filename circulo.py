class Circulo:
	
	def __init__(self, raio, area, perimetro, pi):
		self.raio = raio;
		self.area = area;
		self.perimetro = perimetro;
		self.pi = pi;

	def calculaArea(self):
		resultado = self.pi * self.raio * self.raio
		self.area = resultado
		return self.area

	def calculaPerimetto(self):
		valor = 2 * self.pi * self.raio
		self.perimetro = valor
		return self.perimetro
		
	def imprimir(self):
		print("Area do Circulo é: {:.2f} ".format(self.area))
		print("Perimento do Circulo é: {:.2f}".format(self.perimetro))