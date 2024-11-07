programa {

    inclua biblioteca Util --> ut

    const inteiro TAMANHO_MAXIMO = 20 //tamanho máximo dos vetores utilizados abaixo
    cadeia materiais[TAMANHO_MAXIMO]// Para armazenar o nome de cada material
    caracter tipos[TAMANHO_MAXIMO] // Para armazenar o tipo de cada material
    inteiro indicesMatUsados[3] //índices do vetor de materiais que vai servir para tirar o material do compartimento
    
    //Menu amigável para o usuário escolher a opção na forja

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
 
  funcao inicio() {
      inteiro op = 0, op_TipoMin, op_NomeMin
      caracter tipoMin
      cadeia nomeMin

      inicializar()
      enquanto (op != 3){
    
      op = menuPrincipal()

      escolha(op){
        caso 1: {
          limpa()
          logoDaForja()
          
          escreva("\nQue tipo de item você deseja adicionar??")
          escreva("\n1 - Minério bruto\n2 - Minério Derretido\n3 - Lingote")
          escreva("\nOpção: ")
          leia(op_TipoMin)
          //a partir da seleção do menu, a função abaixo retorna o caracter referente ao tipo do minério
          tipoMin = selecionaTipoMinerio(op_TipoMin)
          limpa()
          logoDaForja() 
          escreva("\nQue minério deseja adicionar??")
          escreva("\n1 - Ferro\n2 - Cobre\n3 - Estanho\n4 - Carvão")
          escreva("\nOpção: ")
          leia(op_NomeMin)
          //a partir da seleção do menu, a função abaixo retorna o nome em extenso referente ao tipo do minério
          nomeMin = selecionaNomeMinerio(op_NomeMin)

          adicionarMaterial(nomeMin, tipoMin) // Adiciona um minério ao vetor do compartimento da forja
          pare
          
        }

        caso 2:{

          escreva("\nQue tipo de item você deseja FABRICAR??")
          escreva("\n1 - Minério Derretido\n2 - Lingote\n3 - Essência\n")
          escreva("\nOpção: ")
          leia(op_TipoMin)
          escreva("\nQue minério deseja FABRICAR??")
          escreva("\n1 - Ferro\n2 - Cobre\n3 - Estanho\n4 - Carvão")
          escreva("\nOpção: ")
          leia(op_NomeMin)

          //a forja vai fabricar o minério pedido de acordo com as informações solicitadas
          fabricar(selecionaNomeMinerio(op_NomeMin), selecionaTipoMinerio(op_TipoMin))
          pare
        }

        caso 3:{

          escreva("\nEsfriando a forja ...")
          ut.aguarde(2000)
          escreva("\nArmazenando os materiais não utilizados ...")
          ut.aguarde(2000)
          escreva("\nGuardando as ferramentas ...")
          ut.aguarde(2000)
          escreva("\nTudo finalizado. Os anões aguardam a sua volta!")
          ut.aguarde(2000)
          pare
        }

        caso contrario:{
          escreva("Opção inválida. Voltando ao menu inicial...")

        }
      }
     }
  }
}

