import configparser

instance = None

def get_instance():
    global instance
    if instance is None:
        instance = BotConfig()
    return instance

class BotConfig:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        
        self.db_url = config.get("database", "db_url", fallback="sqlite:///tfm_bot.db")
        self.log_file_path = config.get("logging", "log_file_path", fallback="discord.log")
        self.log_level = config.get("logging", "log_level", fallback="DEBUG")
        self.stream_logging_enabled = config.getboolean("logging", "stream_logging_enabled", fallback=True)
        self.file_logging_enabled = config.getboolean("logging", "file_logging_enabled", fallback=True)
