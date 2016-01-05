import logging
import time

import redis


logger = logging.getLogger(__name__)


STATS_FIELDS = {
    'clients': ['connected_clients', 'client_longest_output_list',
                'client_biggest_input_buf', 'blocked_clients'],
    'memory': ['used_memory', 'used_memory_rss', 'used_memory_peak',
               'used_memory_lua', 'mem_fragmentation_ratio'],
    'persistence': ['rdb_changes_since_last_save', 'rdb_bgsave_in_progress',
                    'aof_rewrite_in_progress', 'aof_rewrite_scheduled'],
    'stats': ['total_connections_received', 'total_commands_processed',
              'instantaneous_ops_per_sec', 'total_net_input_bytes',
              'total_net_output_bytes', 'instantaneous_input_kbps',
              'instantaneous_output_kbps', 'rejected_connections',
              'sync_full', 'sync_partial_ok', 'sync_partial_err',
              'expired_keys', 'evicted_keys', 'keyspace_hits',
              'keyspace_misses', 'pubsub_channels', 'pubsub_patterns',
              'latest_fork_usec', 'migrate_cached_sockets'],
    'replication': ['connected_slaves', 'master_repl_offset',
                    'repl_backlog_active', 'repl_backlog_size',
                    'repl_backlog_first_byte_offset', 'repl_backlog_histlen'],
    'cpu': ['used_cpu_sys', 'used_cpu_user', 'used_cpu_sys_children',
            'used_cpu_user_children']
}


def get_redis_stats(agent):
    agent.run_event.wait()
    config = agent.config['redis']
    db_config = config['database']
    agent.create_database(**db_config)
    connection = redis.StrictRedis(**config['connection'])
    while agent.run_event.is_set():
        time.sleep(config['frequency'])
        try:
            info = connection.info()
            points = [{
                'measurement': 'redis_stats',
                'tags': {
                    'host': config['connection']['host'],
                },
                'fields': {
                }
            }]
            for group, fields in STATS_FIELDS.items():
                for f in fields:
                    if f in info:
                        points[0]['fields'][f] = info[f]
            db_name = 'db{}'.format(str(config['connection']['db']))
            if db_name in info:
                keys = '{}_keys'.format(db_name)
                expires = '{}_expires'.format(db_name)
                points[0]['fields'][keys] = info[db_name]['keys']
                points[0]['fields'][expires] = info[db_name]['expires']

            logger.debug('points: %s', points)
            agent.push(points, db_config['name'])
        except:
            logger.exception('cannot gather stats from redis')
