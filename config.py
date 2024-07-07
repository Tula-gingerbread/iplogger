debug = False
port = 80

loggers = {
    'how_to_bake_a_cake': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}

# --- Check --- #
assert isinstance(debug, bool), 'debug var must be bool!'
assert isinstance(port, int), 'port var must be int!'
assert isinstance(loggers, dict), 'loggers must be dict!'
assert (len(loggers) != 0), 'loggers must be not empty!'