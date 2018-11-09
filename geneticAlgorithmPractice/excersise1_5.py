#Aug 7th 2018
#Jake L
#GA ch.1 ce.5

import random
import math

class GA():
	"""docstring for ClassName"""

	def __init__(self):
		self.n = 20			#population size
		self.p_c = .7		#crossover rate
		self.p_m = 0.001	#mutation rate
		self.l = 541		#length of genome = (4**0)*((2*0)+1) + (4**1)*((2*1)+1) + (4**2)*((2*2)+1) + (4**3)*((2*3)+1)
		self.runs = 100		#20 iterations
		self.pop = []		#poplulation list
		self.run()

	def run(self):
		self.generate()
		for iteration in range(self.runs):
			self.scoreboard = self.dilema()
			print("Iteration", iteration, "|||", self.datafy())
			self.selection()

	def generate(self):
		for x in range(self.n):
			#~~~~~~~~~
			chromosone = str(random.randint(0,1))
			#~~~~~~~~~
			for i in range(2):
				for j in range(2):
					case = str(i) + str(j)
					response = str(random.randint(0,1))
					chromosone += case + response
			#~~~~~~~~~
			for a1 in range(2):
				for a2 in range(2):
					for a3 in range(2):
						for a4 in range(2):
							case = str(a1) + str(a2) + str(a3) + str(a4)
							response = str(random.randint(0,1))
							chromosone += case + response
			#~~~~~~~~~
			for a1 in range(2):
				for a2 in range(2):
					for a3 in range(2):
						for a4 in range(2):
							for a5 in range(2):
								for a6 in range(2):
									for a7 in range(2):
										for a8 in range(2):
											case = str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7) + str(a8)
											response = str(random.randint(0,1))
											chromosone += case + response
			#~~~~~~~~~
			self.pop.append(chromosone)

	def dilema(self):
		"""Each player plays against every other player once including themselves."""
		scoreboard=[]
		for i in range(self.n):
			scoreboard.append(0)
		for player in range(20):
			p1 = self.pop[player]
			for opponent in range(20-player):
				p2 = self.pop[opponent]
				(score1, score2) = self.play(p1,p2)
				scoreboard[player] += score1
				scoreboard[opponent] += score2
		for i in range(self.n):
			scoreboard[i] = 10000 - scoreboard[i]
		return scoreboard

	def play(self, p1,p2):
		score = [0,0]
		#~~~~~~~~~~~round 1
		r1 = p1[0] + p2[0]
		score = self.upkeep(r1, score)
		r1a = ""
		for i in range(len(r1)):
			r1a += r1[len(r1) - i - 1]
		#~~~~~~~~~~~round 2
		for gamete in range(4):
			gamete = gamete * 3
			gamete += 1
			if p1[gamete:gamete+2] == r1:
				move1 = p1[gamete+3]
				break
			if gamete == 10:
				#print("Check5a", r1)
				move1 = str(random.randint(0,1))
		for gamete in range(4):
			gamete = gamete * 3
			gamete += 1
			if p2[gamete:gamete+2] == r1a:
				move2 = p2[gamete+3]
				break
			if gamete == 10:
				#print("Check5b", r1a)
				move2 = str(random.randint(0,1))
		#print("check1", move1, move2)
		r2 = r1 + move1 + move2
		score = self.upkeep(move1 + move2,score)
		r2a = ""
		for i in range(len(r2)):
			r2a += r2[len(r2) - i - 1]
		#~~~~~~~~~~~round 3
		for gamete in range(16):
			gamete = gamete * 5
			gamete += 1+(3*4)
			if p1[gamete:gamete+4] == r2:
				move1 = p1[gamete+5]
				break
		for gamete in range(16):
			gamete = gamete * 5
			gamete += 1+(3*4)
			if p2[gamete:gamete+4] == r2a:
				move2 = p2[gamete+5]
				break
		#print("check2", move1, move2)
		r3 = r2 + move1 + move2
		score = self.upkeep(move1+move2, score)
		r3a = ""
		for i in range(len(r3)):
			r3a += r3[len(r3) - i - 1]
		#~~~~~~~~~~~round 4 thru 100
		r_new = r3
		ra_new = r3a
		for rounds in range(96):
			r_old = r_new
			ra_old = ra_new
			for gamete in range(64):
				gamete += 1+(3*4)+(5*16)
				if p1[gamete:gamete+6] == r_old:
					move1 = p1[gamete+7]
					break
			for gamete in range(16):
				gamete += 1+(3*4)+(5*16)
				if p2[gamete:gamete+6] == ra_old:
					move2 = p2[gamete+7]
					break
			r_new = r_old[2:6] + move1 + move2
			score = self.upkeep(move1+move2, score)
			ra_new = ""
			for i in range(len(r_new)):
				ra_new += r_new[len(r_new) - i - 1]
		#~~~~~~~~~~~Concluding
		return score

	def upkeep(self, case, score):
		if case == "00":
			#print("case1")
			score1 = 1
			score2 = 1 
		if case == "01":
			#print("case2")
			score1 = 5
			score2 = 0
		if case == "10":
			#print("case3")
			score1 = 0
			score2 = 5
		if case == "11":
			#print("case4")
			score1 = 3
			score2 = 3
		#else:
		#	print("check3", case)
		score[0] += score1
		score[1] += score2
		return score

	def f(self, x):
		return self.scoreboard[x]

	def selection(self):
		"""using roulette wheel sampling"""
		fitsum = 0
		newPopulation = []
		for x in range(self.n):
			fitsum += self.f(x)
		for mating in range(int((self.n)/2)):
			#random.shuffle(self.pop)
			for x1 in range(self.n):
				if random.random() < self.f(x)/fitsum:
					mate1 = self.pop[x1]
					break
				if x1==self.n-1:
					mate1 = self.pop[random.randint(0,self.n-1)]
			#random.shuffle(self.pop)
			for x2 in range(self.n):
				if random.random() < self.f(x)/fitsum:
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
		return self.mutation(child1,child2)#

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

	def datafy(self):
		scoresum = 0
		for x in range(self.n):
			scoresum += self.scoreboard[x]
		return "Average Fitness:  " + str(scoresum/self.n)


def main():
	GA()


if __name__ == "__main__":
	main()