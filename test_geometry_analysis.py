"""
Tests for geometry_analysis.py
"""
import geometry_analysis as ga
import pytest

def test_calculate_distance():
	coord1 = [0, 0, 2]
	coord2 = [0, 0, 0]
	observed = ga.calculate_distance(coord1, coord2)

	assert observed == 2

def test_bond_check_true():
	minval = 0.3
	maxval = 1.8
	bondlength = 1.6
	observed = ga.bond_check(bondlength, minval, maxval)

	assert observed == True

def test_bond_check_false():
	bondlength = 1.9
	observed = ga.bond_check(bondlength) 

	assert observed == False

def test_bond_check_type():
	bondlength = 'a'
	
	with pytest.raises(TypeError):
		observed = ga.bond_check(bondlength)	
