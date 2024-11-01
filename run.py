from app import app
from app.utils import server_logger, config


if __name__ == '__main__':
    server_logger.info('--------------------------------------')
    server_logger.info('Starting server...')
    server_logger.info('Server started at http://{}:{}'.format(config.get('server', 'host'), config.get('server', 'port')))
    app.run(debug=True, host=config.get('server', 'host'), port=config.get('server', 'port'))
    server_logger.info('Server stopped')