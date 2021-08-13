def vectorCompare(matInf, matEst):
    print("Matriculados em Informatica Basica: " + str(len(matInf)))
    print("VetorA: " + str(matInf))
    print("")
    print("Matriculados em Estatistica: " + str(len(matEst)))
    print("VetorB: " + str(matEst))
    
    i = 0
    elemFound = 0
    matBoth = []
    
    for matInf_ in matInf:
        while elemFound == 0 and i < len(matEst):
            if matInf_ == matEst[i]:
                matBoth.append(matInf_)
                elemFound = 1
            else:    
                i += 1
            if i == len(matEst)+1:
                elemFound = 1
                
        elemFound = 0
        i = 0
        
    print("")
    print("R. Estudantes que cursam simultaneamente as duas disciplinas: \n" + str(matBoth))
    
matInf = [43540, 62143, 22456, 86109, 54324]
matEst = [54324, 13579, 43540, 76543, 62143, 56810]
vectorCompare(matInf, matEst)

print("\n-----------\n")

matInf = [54651, 33567, 97210, 65435, 67921, 73254, 87653]
matEst = [65435, 67921, 54651, 87654, 73254]
vectorCompare(matInf, matEst)
