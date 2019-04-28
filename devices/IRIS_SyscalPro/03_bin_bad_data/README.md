This Syscal data set has the following properties:

* 40 electrodes, spacing 0.2 m
* data_normal.bin:
	* normal data, skip 0 measurements
	* the first measurement belongs to an old measurement (zero-index user
	  error when downloading)
	* the last measurement belong to another data set (also index user error)
* data_reciprocal.bin:
	* this is the reciprocal measurement for the first one. Note that the
	  cables were switched, leading to the first four electrodes not being
	  connected.
