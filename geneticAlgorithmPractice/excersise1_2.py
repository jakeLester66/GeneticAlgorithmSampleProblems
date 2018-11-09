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
		self.runs = 20		#number of iterations
		self.pop = []		#poplulation list
		experiments = 5
		scoresum = 0
		for experiment in range(experiments):
			scoresum += self.run()
		print("average iterations required was ",scoresum/experiments)
		print("p_c == ", self.p_c, "AND p_m ==", self.p_m)

	def run(self):
		self.generate()
		for iterations in range(self.runs):
			self.selection()
			for x in range(self.n):
				if self.f(self.pop[x]) == 11111111111111111111:
					return iterations
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