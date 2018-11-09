#June 24th 2018
#Jake L
#GA ch.1 ce.2

import random
import math

class GA():
	"""docstring for ClassName"""

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
		"""for experiment in range(experiments):
			scoresum += self.run()
		print("average iterations required was ",scoresum/experiments)
		print("p_c == ", self.p_c, "AND p_m ==", self.p_m)
"""
	def schemaMakeHelper(self):
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
		self.schemaList = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
		self.schemaCounter = []
		self.schemaFitSum = []
		for i in range(10):
			self.schemaCounter.append(0)
			self.schemaFitSum.append(0)

	def schemaMeasure(self):
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
		#for 
		print()
		print("ITERATION #", self.iterations)
		print("Avg Fitness: ", self.avgFit())
		print("_____________________ | m(H,t) | E(m(H, t+1))")
		for schema in range(10):
			print(self.schemaList[schema], " : ", self.schemaCounter[schema], " | ", self.schemaTheorem(schema))
		
		self.schemaCounter = []
		for i in range(10):
			self.schemaCounter.append(0)


	def u(self, H):
		"""helper function to find avg fitness of schema H at time t"""
		if self.schemaCounter[H] == 0:
			return 0
		return self.schemaFitSum[H] / self.schemaCounter[H]

	def schemaTheorem(self, H)	:
		return ( self.u(H) / self.avgFit() ) * (self.schemaCounter[H])

	def run(self):
		self.generate()
		for iterations in range(self.runs):
			self.iterations = iterations
			self.schemaMeasure()
			self.selection()
			"""	for x in range(self.n):
				if self.f(self.pop[x]) == 11111111111111111111:
					return iterations"""
		return 100

	def generate(self):

		for x in range(self.n):
			chromosone = ""
			for bit in range(self.l):
				bit = str(random.randint(0,1))
				chromosone += bit
			self.pop.append(chromosone)
		
	def f(self, x):
		"""Fitness funtion... fitness = numerical representation of x"""
		return int(x)

	def selection(self):
		"""using roulette wheel sampling"""
		fitsum = 0
		newPopulation = []
		for x in range(self.n):
			fitsum += self.f(self.pop[x])
		for mating in range(50):
			random.shuffle(self.pop)
			for x1 in range(self.n):
				if random.random() < self.f(self.pop[x1])/fitsum:
					mate1 = self.pop[x1]
					break
				if x1==self.n-1:
					mate1 = self.pop[random.randint(0,self.n-1)]
			random.shuffle(self.pop)
			for x2 in range(self.n):
				if random.random() < self.f(self.pop[x2])/fitsum:
					mate2 = self.pop[x2]
					break
				if x2==self.n-1:
					mate2 = self.pop[random.randint(0,self.n-1)]
			children = self.crossover(mate1, mate2)
			for child in range(2):
				newPopulation.append(children[child])
		self.pop=newPopulation


	def crossover(self, mate1, mate2):
		if random.random() > self.p_c:
			return self.mutation(mate1,mate2)
		locus = random.randint(1,self.l)
		#print(mate2, "hi")
		child1 = mate1[0:locus] + mate2[locus:self.l]
		child2 = mate2[0:locus] + mate1[locus:self.l]
		return self.mutation(child1,child2)

	def mutation(self,child1,child2):
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
		fitsum = 0
		for x in range(self.n):
			fitsum += self.f(self.pop[x])
		return fitsum/self.n

def main():
	GA()


if __name__ == "__main__":
	main()