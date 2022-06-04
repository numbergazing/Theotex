from logging import getLogger, DEBUG, StreamHandler, Formatter, WARNING

getLogger("urllib3").setLevel(WARNING)  # .propagate = False to deactivate completely

debug_log = getLogger("debug")
debug_log.setLevel(DEBUG)

debug_handler = StreamHandler()
debug_formatter = Formatter("%(asctime)s [%(name)s] %(message)s", "%Y-%m-%d %H:%M:%S")
debug_handler.setFormatter(debug_formatter)
debug_log.addHandler(debug_handler)
