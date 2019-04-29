import sys
sys.path.append('..')

from config import Config as env

routes = {
    '/api/v{0}/get_mongo'.format(env.APP_VERSION) :{
        env.SHELL_PREFIX_PATH : 'install-MongoDB.sh'
    },
    '/api/v{0}/get_rabbit'.format(env.APP_VERSION) : {
        env.SHELL_PREFIX_PATH : 'install-RabbitMQ.sh'
    }
}
