Measurements
************

tourbillon-redis collects metrics about memory, cpu, clients and other statistics.

Please refers to  `http://redis.io/commands/info <http://redis.io/commands/info>`_ for more information.


Redis stats
===========

tourbillon-redis store metrics in the ``redis_stats`` series.
Each datapoint is tagged with the redis instance hostname and the values collected are:


Tags
----
	* **host**: redis instance hostname

Fields
------

	* **mem_fragmentation_ratio**: ratio between used_memory_rss and used_memory
	* **used_memory**: total number of bytes allocated by Redis using its allocator (either standard libc, jemalloc, or an alternative allocator such as tcmalloc
	* **used_memory_lua**: number of bytes used by the Lua engine
	* **used_memory_peak**: peak memory consumed by Redis (in bytes)
	* **used_memory_rss**: number of bytes that Redis allocated as seen by the operating system (a.k.a resident set size). This is the number reported by tools such as top(1) and ps(1)
	* **used_cpu_sys**: system CPU consumed by the Redis server
	* **used_cpu_sys_children**: system CPU consumed by the background processes
	* **used_cpu_user**: user CPU consumed by the Redis server
	* **used_cpu_user_children**: user CPU consumed by the background processes
	* **connected_clients**: number of client connections (excluding connections from slaves)
	* **client_longest_output_list**: longest output list among current client connections
	* **client_biggest_input_buf**: biggest input buffer among current client connections
	* **blocked_clients**: number of clients pending on a blocking call (BLPOP, BRPOP, BRPOPLPUSH)
	* **total_connections_received**: total number of connections accepted by the server
	* **total_commands_processed**: total number of commands processed by the server
	* **instantaneous_ops_per_sec**: number of commands processed per second
	* **rejected_connections**: number of connections rejected because of maxclients limit
	* **expired_keys**: total number of key expiration events
	* **evicted_keys**: number of evicted keys due to maxmemory limit
	* **keyspace_hits**: number of successful lookup of keys in the main dictionary
	* **keyspace_misses**: number of failed lookup of keys in the main dictionary
	* **pubsub_channels**: global number of pub/sub channels with client subscriptions
	* **pubsub_patterns**: global number of pub/sub pattern with client subscriptions
	* **latest_fork_usec**: duration of the latest fork operation in microseconds


