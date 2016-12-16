#!/usr/bin/python
# coding: utf-8

import os

#########################################################
### Escolha qual rede será testada                    ###
rede = "10"
### Essa opção é para somente utilizar os IPs padrões ###
#########################################################

def imprimeCabecalho():
	print "################ Rastreio de Problemas de Rede Interno ###################"
	print "##                                                                      ##"
	print "## Autor: Luis Gustavo                                                  ##"
	print "##                                                                      ##"
	print "##   A intenção deste script é tentar descobrir em qual switch ou       ##"
	print "## dispositivo central a comunicação não está passando.                 ##"
	print "##                                                                      ##"
	print "##   Os arquivos de configuração são os comandos.txt e o listaips.txt   ##"
	print "## que estão na mesma pasta raiz do script. Caso queira passar uma outra##"
	print "## lista de IPs, sinta-se a vontade. Basta seguir a sintaxe abaixo:     ##"
	print "##                                                                      ##"
	print "##   Ex: ./script <comando> <listaIPS>                                  ##"
	print "##   Ex: ./script ping 10.10.100.10,10.10.100.2,10.10.200.1,10.10.0.1   ##"
	print "\n"

def testeIP(comando,IP,redirecionamento):
	# Aqui ele deve realizar testes predefinidos para o IP passado
	# Ele vai realizar os testes adquiridos pelo testeDB
	saidacomando = os.system(comando+IP+redirecionamento)	
	if int(saidacomando) == 0:
		print IP+": OK"
	else:
		print IP+": Sem resposta"


def testeManager(comando, listaIPs,redirecionamento):
	print "Testando..."
	comando = ''.join(comando)
	# Ele vai receber um array contendo todos os argumentos passados.
	for ip in listaIPs:
		testeIP(comando, ip,redirecionamento) 


def getCommandList():
	with open("comandos.txt") as f:
		# Vai pegar o primeiro comando do arquivo
		return f.readline().splitlines()

def getIPList():
	with open("listaips"+rede+".txt") as f:
		return f.read().splitlines()

def chooseDefaultOrNotList(argumento=None):
	if argumento is None:
		return getIPList()
	else:
		return argumento

def chooseDefaultOrNotCommand(argumento=None):
	if argumento is None:
		return getCommandList()
	else:
		return argumento


if __name__ == "__main__":
	imprimeCabecalho()

	# Vinda por argumentos
	# listaInicial = ['10.10.0.1','10.10.0.2','10.10.0.3']
	listaInicial = None
	redirecionamento = " > arquivosaida.txt"
	
	# Aqui ele irá verificar se ele usará a lista default do arquivo ou não
	# Isso dependerá se o usuário passou uma lista no argumento ou não
	listaReal = chooseDefaultOrNotList(listaInicial)
	
	# Verificar se o usuário passou argumento ou não para comandos
	# Se não ele usará o default do arquivo
	# A intenção e deixar uma lista de comandos pronta para o usuário mais pra frente
	comando = chooseDefaultOrNotCommand()
	
	# Aqui ele chama o gerenciador com a lista de ips dos switches
	testeManager(comando,listaReal,redirecionamento)
