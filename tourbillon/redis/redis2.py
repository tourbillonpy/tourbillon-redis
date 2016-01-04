import logging
import time

import redis


logger = logging.getLogger(__name__)


def get_redis_stats(agent):
    agent.run_event.wait()
    config = agent.config['redis']
    db_config = config['database']
    agent.create_database(**db_config)
    connection = redis.StrictRedis(**config['connection'])
    while agent.run_event.is_set():
        time.sleep(config['frequency'])
        try:
            info = connection.info('all')
            points = [{
                'measurement': 'redis_stats',
                'tags': {
                    'host': config['connection']['host'],
                },
                'fields': {
                    'mem_fragmentation_ratio': info['mem_fragmentation_ratio'],
                    'used_memory': info['used_memory'],
                    'used_memory_lua': info['used_memory_lua'],
                    'used_memory_peak': info['used_memory_peak'],
                    'used_memory_rss': info['used_memory_rss'],
                    'used_cpu_sys': info['used_cpu_sys'],
                    'used_cpu_sys_children': info['used_cpu_sys_children'],
                    'used_cpu_user': info['used_cpu_user'],
                    'used_cpu_user_children': info['used_cpu_user_children']
                }
            }]
            points[0]['fields'].update(connection.info('stats'))
            points[0]['fields'].update(connection.info('clients'))
            logger.debug('points: %s', points)
            agent.push(points, db_config['name'])
        except:
            logger.exception('cannot gather stats from redis')
