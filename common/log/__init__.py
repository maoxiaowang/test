import logging


__all__ = [
    'Logging'
]


class LoggingBase(object):

    @property
    def default_logger(self):
        return logging.getLogger('default')

    @property
    def scripts_logger(self):
        return logging.getLogger('scripts')

    @staticmethod
    def custom_logger(logger_name):
        """
        Should be added in settings.py
        :return:
        """
        return logging.getLogger(logger_name)


Logging = LoggingBase()
