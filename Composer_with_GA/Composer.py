from pygene3.gene import *
from pygene3.population import *
from pygene3.organism import *
from Composer_with_GA.Otherutils.fitness_calc import *
from pygame import *
refmel = [88,88,88,88,88,81,84,88,86,86,86,86,91,91,91,91,86,86,86,95,93,93,93,92,93,93,93,93,100,100,100,100,93,93,93,93,\
          100,100,100,100,98,98,100,98,95,95,91,91,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93]
chords = [[41,45,48,52],[43,47,50,55],[40,43,47,50],[45,48,52,57],[41,45,48,52],[43,47,50,55],[45,48,52,57],[45,48,52,57]]
class melodymaker(CharGeneExchange) :
    mutProb = 0.01
    mutAmt = (ord('x')-ord('!'))/2
    randMax = 'x'
    randMin = '!'
    def __repr__(self):
        return self.value

genome = {}
for i in range(0,64):
    genome[str(i)] = melodymaker

class melodygenes(Organism):
    genome = genome
    def __repr__(self):
        chars = [self[str(i)] for i in range(self.numgenes)]
        return str(''.join(chars))
    def fitness(self):
        mels = str(self)
        mel1 = []
        for mel in mels:
            mel1.append(mel)
        base_diffs = 10
        j = 0
        k = 0
        for i in range(len(mel1)):
            if j>=8:
                k+=1
                j=0
            j+=1
            base_diffs = calculate_fitness(chords[k],mels[i],mels[i-1],chr(refmel[i]),base_diffs)
        return base_diffs

class melodygenespopulation (Population) :
    species = melodygenes
    initPopulation = 128
    childCull = 32
    childCount = 64
    mutants = 32
def main() :
    from time import time
    world = melodygenespopulation()
    i=0
    started = time()
    while True:
        b = world.best()
        reprb = repr(b)
        mels = []
        for x in reprb:
            x = notecalc(x)
            mels.append(x.AscToNote())
        print("Generation %02d :" %i , mels,"best=%s average=%s" % (b.get_fitness(), world.fitness()))
        if b.get_fitness() <=0.5:
            print(i, "generations and after", time() - started, "seconds")
            break
        i+=1
        world.gen()

if __name__ == '__main__':
    main()