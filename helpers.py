#input helpers
def cast_input(prompt, castto=float, default=None, allowed_values = None):
    while True:
        response = raw_input('%s %s (default: %s)' % (prompt, str(allowed_values), default) )
        if default and response=='':
            number = castto(default)
        try:
            number = castto(response)
        except ValueError:
            print "The value you entered was not of type %s.\n" % castto.__name__
        if allowed_values == None or (number in allowed_values):
            return number

def bool_input(prompt, default=True):
    if default == False:
        hint = ' [yN]'
    else:
        hint = ' [Yn]'
    while True:
       response = raw_input(prompt + hint)
       if response in ('y', 'yes'):
            return True
       else if response in ('n', 'no'):
            return False
       else if response == '':
            return default
