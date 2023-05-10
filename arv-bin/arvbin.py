from no import NO
from collections import deque

class ArvBin:
    def __init__(self):
        self.__raiz = None

    def vazia(self):
        if(self.__raiz == None):
            return True
        else:
            return False

    def totalNO(self):
        if(self.__raiz == None):
            return 0
        else:
            return self._totalNO(self.__raiz)

    def _totalNO(self, raiz):
        if(raiz == None):
            return 0
        
        total_esq = self._totalNO(raiz.esq)
        total_dir = self._totalNO(raiz.dir)
        return (total_esq + total_dir + 1)

    def altura(self):
        if(self.__raiz == None):
            return 0
        else:
            return self.__altura(self.__raiz)

    def __altura(self, raiz):
        if(raiz == None):
            return 0
        
        alt_esq = self.__altura(raiz.esq)
        alt_dir = self.__altura(raiz.dir)
        if(alt_esq > alt_dir):
            return alt_esq + 1
        else:
            return alt_dir + 1
    
    def insere(self, valor):
        novo = NO(valor)        

        if(self.__raiz == None):
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while(atual != None):
                ant = atual
                if(valor == atual.info):
                    return False # elemento jÃ¡ existe

                if(valor > atual.info):
                    atual = atual.dir
                else:
                    atual = atual.esq
            
            if(valor > ant.info):
                ant.dir = novo
            else:
                ant.esq = novo
        
        return True

    def busca(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                return True
            
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        
        return False
    

    def remove(self, valor):
        if(self.__raiz == None):
            return False
        
        ant = None
        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                if(atual == self.__raiz):
                    self.__raiz = self.__remove_atual(atual)
                else:
                    if(ant.dir == atual):
                        ant.dir = self.__remove_atual(atual)
                    else:
                        ant.esq = self.__remove_atual(atual)
                
                return True
            
            ant = atual
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        
        return False
    
    def __remove_atual(self, atual):

        if(atual.esq == None):
            return atual.dir
        
        no1 = atual
        no2 = atual.esq
        while(no2.dir != None):
            no1 = no2
            no2 = no2.dir
        
        # no2 Ã© o nÃ³ anterior a r na ordem e-r-d
        # no1 Ã© o pai de no2
        if(no1 != atual):
            no1.dir = no2.esq
            no2.esq = atual.esq
        
        no2.dir = atual.dir
        return no2

    def __preOrdem(self,raiz):
        if(raiz != None):
            print(raiz.info)
            self.__preOrdem(raiz.esq)
            self.__preOrdem(raiz.dir)
            

    def preOrdem(self):
        if(self.__raiz != None):
            self.__preOrdem(self.__raiz)

    def __emOrdem(self,raiz):
        if(raiz != None):            
            self.__emOrdem(raiz.esq)
            print(raiz.info)
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self.__emOrdem(self.__raiz)
        
    def __posOrdem(self,raiz):
        if(raiz != None):            
            self.__posOrdem(raiz.esq)            
            self.__posOrdem(raiz.dir)
            print(raiz.info)

    def posOrdem(self):
        if(self.__raiz != None):
            self.__posOrdem(self.__raiz)
            
    def __buscaLargura(self,raiz):
        if(raiz != None):
            fila = deque()
            fila.append(raiz)
            while fila:
                no = fila.popleft()
                print(no.info)
                if(no.esq != None):
                    fila.append(no.esq)
                if(no.dir != None):
                    fila.append(no.dir)    
        
    def buscaLargura(self):
        if(self.__raiz == None):
            return False
        else:
            self.__buscaLargura(self.__raiz)
            
    def __quaseCompleta(self,raiz):
        if(raiz == None):
            return 0
        
        completo_esq,alt_esq = self.__quaseCompleta(raiz.esq)
        completo_dir,alt_dir = self.__quaseCompleta(raiz.dir)
        
        if(completo_esq and completo_dir and abs(alt_esq-alt_dir)<=1):
            if(alt_esq == alt_dir):
                return alt_esq+1
            elif(alt_esq == alt_dir-1):
                completo,alt= self.__quaseCompleta(raiz.dir)
                if(completo and alt == alt_dir):
                    return alt_esq+1
            elif(alt_esq-1 == alt_dir):
                completo,alt= self.__quaseCompleta(raiz.esq)
                if(completo and alt == alt_esq):
                    return alt_dir+1
        
    def quaseCompleta(self):
        if(self.__raiz==None):
            self.__quaseCompleta(self)
            
    def __profundidade(self,raiz,valor_no):
        if(raiz == None):
            return -1
        elif(raiz==valor_no):
            return 0
        
        else:
            prof_esq = self.__profundidade(raiz.esq,valor_no)
            prof_dir = self.__profundidade(raiz.dir,valor_no)
            if(prof_esq == -1 and prof_dir == -1):
                return -1
            elif(prof_esq != -1):
                return prof_esq+1
            else:
                return prof_dir+1
                    
            
    def profundidade(self,valor_no,):
        if(self.__raiz == None):
            return False
        else:
            return self.__profundidade(self.__raiz,valor_no)
        
    def __arvoreBinaria(self,raiz):
        if(raiz == None):
            return True

        pilha=[]
        atual=raiz
        ult_visitado=None
        while True:
            if(atual != None):
                pilha.append(atual)
                atual=atual.esq
            
            elif pilha:
                atual=pilha.pop()
                if(ult_visitado != None and atual.info <= ult_visitado):
                    return False
                ult_visitado=atual.info
                atual=atual.dir
            else:
                break
            
        return True     
            
    
    def arvoreBinaria(self):
        if(self.__raiz == None):
            return False
        else:
            return self.__arvoreBinaria(self.__raiz)
    