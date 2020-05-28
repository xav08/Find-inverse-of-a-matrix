import random


#pretty prints the matrix
def pretty_print(mat1, r):
	for i in range(r):
		for j in range(r):
	
			print(str(round(mat1[i][j],2))+"\t", end ='')
		print()

#swaps the matrices by rows given the matrix and the 2 rows 
def swap(mat1, i, j):
	for k in range(r):
		mat1[i][k], mat1[j][k] = mat1[j][k], mat1[i][k]



#to check if any of the diagonal elements is 0 and to swap it
def check(mat1, mat2):
	flag = 1
	for i in range(r):
		if(mat1[i][i] == 0):
			flag = -1
			for j in range(r):
				if(j == i):
					continue
				if(mat1[j][i] != 0 and mat1[i][j] != 0):
					swap(mat1, i, j)
					swap(mat2, i, j)
					flag = 1
	if(flag == -1):
		print("issue cannot be resolved: singular matrix or zero matrix")
		exit()



#converts the diagonal element to one and divides all the respective row ele with the same that is used to divide the diagonal ele
def ones(mat1, mat2, i, r):
	ele = mat1[i][i]
	for j in range(r):
		mat1[i][j] = mat1[i][j] / ele
		mat2[i][j] = mat2[i][j] / ele


#convert all the ele on the current column to 0 along with their connected column elements
def zeros(mat1, mat2, i, r):
	for j in range(r):
		if(j == i):
			continue
		ele = mat1[j][i]
		for k in range(r):
			mat1[j][k] = mat1[j][k] - ele * mat1[i][k]
			mat2[j][k] = mat2[j][k] - ele * mat2[i][k]

			
#finds the inverse of 2 matrix 
def inverse(mat3, mat2):	
	for i in range(r):
		check(mat3, mat2)
		ones(mat3, mat2, i, r)
		zeros(mat3, mat2, i, r)


		
#finds the product of 2 matrices		
def product_mat(mat1, mat2):
	product = []
	for i in range(r):
		temp = []
		for j in range(r):
			s = 0
			for k in range(r):
				s += mat1[i][k] * mat2[k][j]
			if(s <= 0.0001):
				s = 0
			temp.append(s)	
		product.append(temp)
	return product	


	
#creates the identity matrix of specified r	
def id_mat(r):
	mat2 = []
	for i in range(r):
		col = []
		for j in range(r):
			if(i == j):
				col.append(1)
			else:
				col.append(0)
		mat2.append(col)
	return mat2
	
	
#creates  square matrix of specified length and returns it along with a hard copy of it
def create_mat(r):
	mat1 = []
	mat3 = []
	for i in range(r):
		col = []
		for j in range(r):
			temp = random.randint(0, 10)
			print(temp)
			#temp = float(input())    #uncomment this for user input matrix
			col.append(temp)
		mat1.append(col)
		mat3.append(col[:])
	return mat1, mat3

		




r = int(input())
c = int(input())
if(r != c):
	print("the matrix is not a square matrix\nthe inverse cannot be found")
	exit()

mat1, mat3 = create_mat(r)
mat2 = id_mat(r)
inverse(mat3, mat2)
product = product_mat(mat1, mat2)
print("inputed matrix is :\n")
pretty_print(mat1, r)
print("inverse matrix is:\n")
pretty_print(mat2, r)
print("product matrix is:\n")
pretty_print(product, r)




