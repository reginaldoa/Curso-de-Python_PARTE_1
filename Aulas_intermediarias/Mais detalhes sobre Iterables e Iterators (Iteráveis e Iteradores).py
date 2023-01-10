#Generator expression, iterables e iterators em Python

iterable =  ['Eu', 'tenho','_iter_']
iterator = iterable.__iter__() #tem_iter_e_next_

#O iteravel, você pode apresentar um valor seguido do outro.
#O iterator apresenta um valor de cada vez. Ele não entrega nada, apenas o próximo valor.

print(next(iterator))

iterator = iter(iterable) #Forma mais fácil de escrever
print(next(iterator))
print(next(iterator))
print(next(iterator))