'''Connection pool with Redis'''
import redis


connections_pool = {}


def connect(**redis_settings):
    '''Get Redis connection'''
    conn_key = ';'.join(['{}:{}'.format(k, str(v)) for k, v in redis_settings.items()])
    if conn_key not in connections_pool:
        redis_settings = redis_settings.copy()
        connections_pool[conn_key] = redis.StrictRedis(**redis_settings)
    return connections_pool[conn_key]
