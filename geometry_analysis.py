# This is my geometry analysis code
import numpy
import os
import sys

# Best practice: put in function definitions after importing libraries

def bond_check(bond_distance, minimum_value=0, maximum_value=1.5):
	"""
	Check if the bond distance is within the specified length.

	Parameters
	----------
	bond_distance: float
		The distance between atoms
	minimum_value: float, optional
		The minimum distance expected for a bond
	maximum_value: float, optional
		The maximum distance expected for a bond

	Returns
	-------
	True: Boolean operator
		The value is between the minimum and maximum
	False: Boolean operator
		The value is not between the minimum and maximum

	Examples
	--------
	>>> bond_check(0.8)
	True
	>>> bond_check(2.3)
	False
	>>> bond_check(1.6, minimum_value=0.4, maximum_value=2.0)
	True 

	"""
	
	# Check that bond_distance is a float

	if not isinstance(bond_distance, float): # if bond_distance is not a float
		given_type = type(bond_distance)
		raise TypeError(F'bond_distance must be type float. given: {bond_distance} is {given_type}')
	if bond_distance>minimum_value and bond_distance<maximum_value:
		return True
	else:
		return False


def calculate_distance(atom1, atom2): # variables that can be used in code
	"""
	Calculate the distance between two atoms.
	
	Parameters  
	----------
	atom1: list
		A list of coordinates [x, y, z]
	atom2: list
		A list of coordinates [x, y, z]

	Returns
	-------
	bond_length: float
		The distance between atoms
	
	
	Examples
	--------
	>>> caclulate_distance([0, 0, 0],[0, 0, 1])
	1.0

	"""
	x_distance = atom1[0]-atom2[0]
	y_distance = atom1[1]-atom2[1]
	z_distance = atom1[2]-atom2[2]
	distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
	return distance

# User specifies where the file is 


if __name__== "__main__": # "_ _name_ _" needs two underscores, watch indentation 
	
	if len(sys.argv) < 2:
		raise IndexError('No file name given. Script requires an xyz file.')

	xyz_file = sys.argv[1]

# Loading in the data

	distances = numpy.genfromtxt(fname=xyz_file,dtype='unicode',skip_header=2)
	headers = distances[:,0]
	data = distances[:,1:]
	data = data.astype(numpy.float)

# Print the bond lengths for any bondds

	for numA, atomA in enumerate(data):
		for numB, atomB in enumerate(data):
			if numB<numA:
				distance_AB = calculate_distance(atomA, atomB)
				if bond_check(distance_AB)==True:
					print(F'{headers[numA]} to {headers[numB]} : {distance_AB:.3f}')
