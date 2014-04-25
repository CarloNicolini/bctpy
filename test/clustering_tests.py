from load_samples import *
import numpy as np
import bct
from scipy import io

def test_cluscoef_wu():
	x = load_sample(thres=.23)
	cc = bct.clustering_coef_wu(x)
	assert np.allclose(np.sum(cc), 187.95878414)

def test_transitivity_wu():
	x = load_sample(thres=.23)
	t = bct.transitivity_wu(x)
	assert np.allclose(t, 1.32927829)

#test signed clustering so that the cuberoot functionality is tested
#there is no equivalent matlab functionality
def test_cluscoef_signed():
	x = load_signed_sample(thres=.85)
	cc = bct.clustering_coef_wu(x)
	assert np.imag(np.sum(cc))==0	

def test_transitivity_signed():
	x = load_signed_sample(thres=.85)
	t = bct.transitivity_wu(x)
	assert np.imag(t)==0

#test functions dealing with components on very sparse dataset
def test_component():
	from scipy import stats
	x = load_sparse_sample()
	c1,cs1 = bct.get_components(x)

	assert np.max(c1) == 19
	assert np.max(cs1) == 72

	try:
		import networkx
		c2,cs2 = bct.get_components(x, no_depend=True)
		assert np.max(c2) == 19
		assert np.max(cs2) == 72

	except ImportError:
		pass

	assert bct.number_of_components(x) == 19

def test_consensus():
	pass

def test_cluscoef_wd():
	x = load_directed_sample(thres=.45)
	cc = bct.clustering_coef_wd(x)
	#FIXME
	print np.sum(cc), cc[-1]
	assert np.allclose(np.sum(cc), 298.30817908)

def test_transitivity_wd():
	x = load_directed_sample(thres=.45)
	t = bct.transitivity_wd(x)
	print t
	#FIXME
	assert np.allclose(t, 1.30727748)

def test_cluscoef_bu():
	x = bct.binarize(load_sample(thres=.17), copy=False)
	cc = bct.clustering_coef_bu(x)
	#FIXME
	print np.sum(cc)
	assert np.allclose(np.sum(cc), 60.10160458)

def test_transitivity_bu():
	x = bct.binarize(load_sample(thres=.17), copy=False)
	t = bct.transitivity_bu(x)
	assert np.allclose(t, 0.42763107)

def test_cluscoef_bd():
	x = bct.binarize(load_directed_sample(thres=.41), copy=False)
	cc = bct.clustering_coef_bd(x)
	assert np.allclose(np.sum(cc), 113.31145155)

def test_transitivity_bd():
	x = bct.binarize(load_directed_sample(thres=.41), copy=False)
	t = bct.transitivity_bd(x)
	assert np.allclose(t, 0.50919493)

def test_agreement_weighted():
	pass
