# Zero-game
Game that adds random zero´s to 2 numbers and evaluate which resulting number is greater
Description: 
Given two natural numbers: A and B. A > B.
What is the probability of Bn  > An if we multiply A and B by a different power of 10.


Formula for the probability

A = bigger number
B = smaller number
n = Upper limit of the Power of 10n to multiply each of both numbers
j = Log(A/B)
k = ⌊j⌋  floor number of j (round down of j)
n-k = substraction of n minus k (if negative assign zero)
alfa = ⌊k/j⌋
beta=Boolean value: if n/j is greater than 1 then 1 else zero  

(((n-k)*(n-k+1))/2)/(〖(n+1)〗^2-(n-k+1)*alfa*beta)

Additional documents: 
	Zero test.xlsx : First test to see the values 
	Zero.py: Returns the probability given the values A, B and the number of zeros (n)
	Zero2.py Test all numbers from 0 to A, B and n and returns the number of good and bad cases and the resulting error if the formula doesn´t apply
	Zero2.1.py better version of zero2.py
	Zero3.py Given A, B and n. It test a random sample (sample to be defined by user) to see the good and correct cases (Lean version of zero2.py)
