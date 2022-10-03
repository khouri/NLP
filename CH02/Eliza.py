import re


# estilo um help desk...
class Eliza():

	def __init__(self, sentence):
		print("Eliza")
		self.sentence = sentence
	pass

	def internet_helper(self):
		p = re.compile(r"\bBom dia! Eu preciso de ajuda com a internet+\b.*")
		result = p.search(self.sentence)

		if result is not None:
			print("Qual seu problema com a internet?")

	pass

	def senha_helper(self):
		p = re.compile(r"\bMinha senha não funciona+\b.*")
		result = p.search(self.sentence)

		if result is not None:
			print("Vou te enviar o link para resetar sua senha <LINK>")
	pass

	def parse_sentence(self):

		self.internet_helper()
		self.senha_helper()

	pass

pass