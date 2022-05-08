def numberGenerator(lowerLim= 100, upperLim= 200):
    for number in range(lowerLim, upperLim+1):
        yield number

    print("Function Terminated")

lowerLim= 10; upperLim= 20
numGen= numberGenerator(lowerLim, upperLim) # numberGenerator returns a Generator Object
print(numGen)

for _ in range(lowerLim, upperLim+1):
    print( next(numGen) )

print( next(numGen) )

