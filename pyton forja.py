##CONSTANTES

import time as ti

TAMANHO_MAXIMO = 10


material    = []
tipo        = []


##menu da forja
def logoDaForja():
    print('''
        ---------------------------------------
        --------- BEM-VINDO À FORJA!! ---------
        ---------------------------------------
        ''')

def menuPrincipal():

        ##colcar um limpa aqui dps
    logoDaForja()
    mostrarElementosNaForja()
    opcao=int(input('''
        O que você deseja fazer na nossa fornalha?
        1 - Adicionar Material
        2 - Fabricar Item
        3 - Sair da Fornalha
        Opção:'''))
    return opcao

def inicializar():
  for i in range(0,TAMANHO_MAXIMO):
    materiais[i]=""
    tipos[i]=''
  
def mostrarElementosNaForja():
    global materiais, tipos
    print("Elementos presentes na forja")
    print(" | ")
    for i in range (TAMANHO_MAXIMO):
        if(materiais[i] == " "):
            print("  | ")
        else:
            print(f"  {materiais[i]} [{tipos[i]} |")
			
           #função para adicionar um determinado minério de tipo definido pelo usuário no compartimento da forja em um espaço vazio

def adicionarMaterial():
    global material, tipos, tipo, TAMANHO_MAXIMO
    for i in range (TAMANHO_MAXIMO):
        if(materiais[i] == " " or tipos[i] == ' '):
            materiais[i] = material
            tipos[i] = tipo
            print("Você adicionou um "+informaTipoMinerio(tipo)+" de "+material+" no compartimento da forja")
            ti.sleep(4)
        if (i==TAMANHO_MAXIMO):
          print("Não há espaço para mais materiais.")
          ti.sleep(4)   

def adicionarMaterial(materialX,tipoY):
    global material 
    global tipo

    material.apend(materialX)
    tipo.append(tipoY)
    print(f"Você adicionou um {informaTipoMinerio(tipo)} de {material} no compartimento da forja")
    ti.sleep(4)

def  selecionaTipoMinerio(tipo):
        match (tipo):
            case 1:
                return('B') #caracter que refere-se ao minério Bruto

            case 2:
              return('D') #caracter que refere-se ao minério Derretido
           
            case 3:
                return('L') #caracter que refere-se ao Lingote
            
            case (_): 
                    return "Erro minerio indefinido"

def selecionaNomeMinerio(tipo):
    match(tipo):
        case 1:
            return "Ferro"
        case 2:
            return "Cobre"
        case 3:
            return "Estanho"
        case 4:
            return "Carvão"
        case(_):
            return "Erro minerio indefinido"

def informaNomeMinerioFabricado(tipo):
    
    if (tipo == 'B'): return "Minério Derretido"
    if (tipo == 'D'): return "Lingote"
    if (tipo == 'L'):  return "Essência"

def informaTipoMinerioFabricado(tipo):
    if (tipo == 'B'): return 'D'
    if (tipo == 'D'): return 'L'
    if (tipo == 'L'): return 'E'

def informaTipoMinerio(tipo):
    if (tipo == 'B'): return "Minério Bruto"
    if (tipo == 'D'): return "Minério Derretido"
    if (tipo == 'L'): return "Lingote"

def fabricar(material, tipo):

    contagem =0
    j = 0
    nomeMatFeito ##vai receber o nome do mateiral que foi fabricado

    for inc in range(0, TAMANHO_MAXIMO):
        if ((materiais[inc] == material) and (tipos[inc] == tipo)):
            print(f"Encontrei um dos minérios na {inc+1}° parte do compartimento da forja")
            ti.sleep(1,5)
'''
        funcao fabricar(cadeia material, caracter tipo){
        // Lógica simplificada para encontrar os materiais necessários e realizar a fabricação
          inteiro contagem = 0, j = 0
          cadeia nomeMatFeito // vai receber o nome do mateiral que foi fabricado
          
        
        para (inteiro inc = 0;inc<TAMANHO_MAXIMO;inc++){
            se ((materiais[inc] == material) e (tipos[inc] == tipo)){
              escreva("Encontrei um dos minérios na ",inc+1,"° parte do compartimento da forja\n")
              ut.aguarde(1500)
              
              //guarde os índices no vetor de 'materiais' onde os dois minérios a serem usados estão localizados
              se (j == 0){
                //coloca no primeiro espaço do vetor o índice onde está localizado o primeiro mínero usado
                indicesMatUsados[j] = inc 
           
                j++
                  }
                  senao {
                    //coloca no primeiro espaço do vetor o índice onde está localizado o primeiro mínero usado
                    indicesMatUsados[j] = inc 
                                  
                  }
                contagem ++
            }
            se (contagem == 2){
              pare //ele vai parar de fazer a busca dos materiais no compartimento da forja (o loop PARA)
            }
        }
        se (contagem < 2){ //não achou a quantidade suficiente
          escreva("Não foram achados materiais suficientes para a fabricação")
          ut.aguarde(4000)
        }
        senao {
          nomeMatFeito = informaNomeMinerioFabricado(tipo) //diz qual o tipo do minério foi fabricado
          escreva("Você acabou de criar um(a) "+nomeMatFeito+" de "+material)
          ut.aguarde(4000)

          //substitui um dos minérios usados pelo item resultante 
          materiais[indicesMatUsados[0]] = material
          tipos[indicesMatUsados[0]] = informaTipoMinerioFabricado(tipo)

          //elimina o segundo minério usado, deixando o espaço vago
          materiais[indicesMatUsados[1]] = " "          
          tipos[indicesMatUsados[1]] = ' '
        }
      }
 '''
