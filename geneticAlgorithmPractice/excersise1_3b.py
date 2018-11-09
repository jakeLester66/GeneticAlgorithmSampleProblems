#July 3rd 2018
#Jake L
#GA ch.1 ce.3(on ce.1)

import random
import math

class GA():
	"""Genetic Algorithm Class to operate on Chapter 1
	Excersise 3 of Genetic Algrotihms: An overview."""

	def __init__(self):
		self.n = 100		#population size
		self.p_c = .7		#crossover rate
		self.p_m = 0.001		#mutation rate
		self.l = 20			#length of chromosone
		self.runs = 20		#20 iterations
		self.pop = []		#poplulation list
		experiments = 5
		scoresum = 0
		self.schemaMakeHelper()
		self.run()

	def run(self):
		"""Calls the initial generation function
		and then maintains future iterations of
		selection, crossover, and mutation.
		Special helper functions have been added
		to test the validity of a predictive schema theorem."""
		self.generate()
		for iterations in range(self.runs):
			self.iterations = iterations
			self.schemaMeasure()
			self.selection()

	def generate(self):
		"""Generates population of self.n size.
		Each chromosone, referred to as x, is an instance of
		self.l alleles of binary nature. Each chromosone is
		generated randomly"""
		for x in range(self.n):
			chromosone = ""
			for bit in range(self.l):
				bit = str(random.randint(0,1))
				chromosone += bit
			self.pop.append(chromosone)
		
	def f(self, x):
		"""Fitness funtion... fitness = number of 1's in chromosone x.
		As such, the possible fittness values of any given organism in
		self.pop is an integer open-bounded by 0 and 20."""
		fitness = 0
		for i in range(self.l):
			if x[i] == '1':
				fitness += 1
		return fitness

	def selection(self):
		"""Selction performed using proportionate
		roulette wheel sampling. It is to be noted that
		this particular form of roulette wheel sampling
		works only with integer fittness of low variety,
		as a high variety would cause memory overflow
		and non integer values would not be iterated in NOTE** below"""
		
		roulette = []
		fitsum = 0
		for x in range(self.n):
			for fitness in range(self.f(self.pop[x])): #NOTE**
				roulette.append(self.pop[x])
				fitsum += 1
		newPopulation = []
		for mating in range(50):
			mate1 = roulette[random.randint(0,fitsum-1)]
			mate2 = roulette[random.randint(0,fitsum-1)]
			children = self.crossover(mate1,mate2)
			for child in range(2):
				newPopulation.append(children[child])
		self.pop=newPopulation

	def crossover(self, mate1, mate2):
		"""Randomly selects a locus and splices two chromosones,
		mate1 and mate2. The probability of crossover threshold, self.p_c
		must be met in order for this to take place.
		Otherwise, the crossover function returns the original parents."""
		if random.random() > self.p_c:
			return self.mutation(mate1,mate2)
		locus = random.randint(1,self.l)
		child1 = mate1[0:locus] + mate2[locus:self.l]
		child2 = mate2[0:locus] + mate1[locus:self.l]
		return self.mutation(child1,child2)

	def mutation(self,child1,child2):
		"""for each gene in the chromosone,
		if the random number generator breaks the mutation rate
		threshold, self.p_m, the gene will flip to its opposite binary allele."""
		children = [child1, child2]
		for child in range(len(children)):
			for bit in range(self.l):
				if random.random() < self.p_m:
					if children[child][bit] == '0':
						children[child] = children[child][0:bit] + '1' + children[child][bit+1:self.l]
					else:
						children[child] = children[child][0:bit] + '0' + children[child][bit+1:self.l]
		return children

	def avgFit(self):
		"""returns the average fitness of the population
		at a given time, t"""
		fitsum = 0
		for x in range(self.n):
			fitsum += self.f(self.pop[x])
		return fitsum/self.n

	def schemaMakeHelper(self):
		"""iniializes schema definition
		and creates 3 key lists as commented below."""

		s0 = "1*******************"
		s1 = "10******************"
		s2 = "111*****************"
		s3 = "1111****************"
		s4 = "11111***************"
		s5 = "0*******************"
		s6 = "01******************"
		s7 = "000*****************"
		s8 = "0000****************"
		s9 = "00000***************"
		self.schemaList = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9] #holds each schema for reference
		self.schemaCounter = []	#keeps count of the quanity of chromosones that are a member of each given schema... refreshed each iteration
		self.schemaFitSum = [] #keeps count of the average fittness of every organism in a each schema
		for i in range(10):
			self.schemaCounter.append(0)
			self.schemaFitSum.append(0)

	def schemaMeasure(self):
		"""This funciton is the main frame for testing the schema theorem.
		it includes print functions to show the user how the predicted results compare with the actual
		results"""
		for x in range(len(self.pop)):
			chromosone = self.pop[x]
			for schema in range(10):
				match = True
				for allele in range(20):
					if chromosone[allele] != self.schemaList[schema][allele]:
						if self.schemaList[schema][allele] == "*":
							match = True
						else:
							match = False
							break
					
				if match:
					self.schemaCounter[schema] += 1
					self.schemaFitSum[schema] += self.f(chromosone) 
		print()
		print("ITERATION #", self.iterations)
		print("Avg Fitness: ", self.avgFit())
		#print("_____________________ | m(H,t) | E(m(H, t+1))")
		for schema in range(10):
			print(self.schemaList[schema], " : ", self.schemaCounter[schema], " | ", self.schemaTheorem(schema))
		
		self.schemaCounter = []
		self.schemaFitSum = []
		for i in range(10):
			self.schemaCounter.append(0)
			self.schemaFitSum.append(0)


	def u(self, H):
		"""helper function to find avg fitness of schema H at time t"""
		if self.schemaCounter[H] == 0:
			return 0
		return self.schemaFitSum[H] / self.schemaCounter[H]

	def schemaTheorem(self, H):
		"""predictive formula to estimate the number
		of organisms a schema, H, will posses at the end of the next iteration.
		Ignores the effects of crossover"""
		return ( self.u(H) / self.avgFit() ) * (self.schemaCounter[H])




def main():
	GA()


if __name__ == "__main__":
	main()