Configure
*********


Create the tourbillon-redis configuration file
==============================================

You must create the tourbillon-redis configuration file in order to use tourbillon-redis.
By default, the configuration file must be placed in **/etc/tourbillon/conf.d** and its name
must be **redis.conf**.

The tourbillon-redis configuration file looks like: ::

	{
		"database": {
			"name": "redis",
			"duration": "365d",
			"replication": "1"
		},
		"connection": {
			"host": "localhost",
			"port": 6379,
			"db": 0
		},
		"frequency": 1
	}


You can customize the database name, the retencion policy and the redis connection parameters.


Enable the tourbillon-redis metrics collectors
==============================================

To enable the tourbillon-redis metrics collectors types the following command: ::

	$ sudo -i tourbillon enable tourbillon.redis=get_redis_stats
