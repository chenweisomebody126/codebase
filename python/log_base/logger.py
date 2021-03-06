import os
import logging
import logging.config
import yaml


def get_debug_level(debug_level):
    """Transform debug level from string to logging flags.
    Parameters:
        debug_level (str): Debug level as string.
    Returns:
        debug (int): Debug level as logging flag.

    """
    if debug_level == 'INFO':
        return logging.INFO
    elif debug_level == 'DEBUG':
        return logging.DEBUG
    elif debug_level == 'WARNING':
        return logging.WARNING
    elif debug_level == 'ERROR':
        return logging.ERROR
    elif debug_level == 'CRITICAL':
        return logging.CRITICAL
    else:
        return None


def setup_logger(debug_level='ERROR', config_file=''):
    """Setup logging configuration.
    Parameters:
        debug_level (str): Debug level as string.
        config_file (str): Yaml configuration file.
    Returns:
        log (object): Logging object.
    Examples:
        >>> log = setup_logger(debug_level='DEBUG')
        >>> log.debug("Debug log_base")
        2017-01-29 23:15:45,551 -- logger.py:78 -- DEBUG: Debug log_base
        >>> log = setup_logger(debug_level='INFO', config_file='logging.yaml')
        >>> log.error("Error log_base")
        2017-01-29 23:16:34,671 -- logger.py:88 -- ERROR: Error log_base
        >>> os.environ['DEBUG_LEVEL'] = "DEBUG"
        >>> log = setup_logger(debug_level='INFO')
        >>> log.debug("Debug log_base")
        2017-01-29 23:17:24,582 -- logger.py:94 -- DEBUG: Debug log_base

    """
    level = get_debug_level(debug_level)

    # Get environment debug level if it is defined (overwrite level in code)
    env_debug_level = 'DEBUG_LEVEL'
    env_level = os.getenv(env_debug_level, None)
    if env_level and get_debug_level(env_level) is not None:
        level = get_debug_level(env_level)

    # Get logger
    log = logging.getLogger()
    log.setLevel(level)

    # Format logger
    if os.path.exists(config_file):
        with open(config_file, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        console = logging.StreamHandler()
        format_str = '%(asctime)s -- %(filename)s:%(lineno)s -- %(levelname)s: %(message)s'
        console.setFormatter(logging.Formatter(format_str))
        log.addHandler(console)

    return log

