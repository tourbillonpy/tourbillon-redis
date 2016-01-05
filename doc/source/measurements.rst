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

The collected fields depends on the Redis version.

In the following tables there are the fields for each section that are collected if they exist.


**clients**

	* connected_clients
	* client_longest_output_list
	* client_biggest_input_buf
	* blocked_clients

**memory**

	* used_memory
	* used_memory_rss
	* used_memory_peak
	* used_memory_lua
	* mem_fragmentation_ratio

**persistence**

	* rdb_changes_since_last_save
	* rdb_bgsave_in_progress
	* aof_rewrite_in_progress
	* aof_rewrite_scheduled

**stats**

	* total_connections_received
	* total_commands_processed
	* instantaneous_ops_per_sec
	* total_net_input_bytes
	* total_net_output_bytes
	* instantaneous_input_kbps
	* instantaneous_output_kbps
	* rejected_connections
	* sync_full
	* sync_partial_ok
	* sync_partial_err
	* expired_keys
	* evicted_keys
	* keyspace_hits
	* keyspace_misses
	* pubsub_channels
	* pubsub_patterns
	* latest_fork_usec
	* migrate_cached_sockets

**replication**

	* connected_slaves
	* master_repl_offset
	* repl_backlog_active
	* repl_backlog_size
	* repl_backlog_first_byte_offset
	* repl_backlog_histlen

**cpu**
	
	* used_cpu_sys
	* used_cpu_user
	* used_cpu_sys_children
	* used_cpu_user_children

tourbillon-redis also collects the number of keys and expires for the database
specified in the redis connection parameters.

