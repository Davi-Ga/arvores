import copy
import math
from arvbin import ArvBin

if __name__=="_main_":
    arv = ArvBin()
    print(arv.altura())

    arv.insere(50)
    arv.insere(100)
    arv.insere(30)
    arv.insere(20)
    arv.insere(40)
    arv.insere(45)
    arv.insere(35)
    arv.insere(37)

    print(arv.altura())
    #arv.preOrdem()
    #arv.emOrdem()
    #arv.posOrdem()

    print("busca: ",arv.busca(41))
    arv.remove(40)
    arv.remove(100)
    arv.remove(10)
    arv.emOrdem()