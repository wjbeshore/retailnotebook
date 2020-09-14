SELECT 
	d.nonfood + d.meat + d.produce + d.dairy + d.mix AS total,
	d.month,
	s.ceres_id




 FROM stores s
INNER JOIN donation d ON d.ceres_id = s.ceres_id;