import pytz

def utc_to_local(utc_dt):
    _local_tz = pytz.timezone('Europe/Moscow')
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(_local_tz)
    return _local_tz.normalize(local_dt)


def pluralize(name):
    """ Выполняем изменение слова по формам  """
    if name.endswith('y') and name[-2] not in 'aeiou':
        return name[:-1] + 'ies'
    elif name.endswith('s') or name.endswith('x') or name.endswith('z') or name.endswith('sh') or name.endswith('ch'):
        return name + 'es'
    else:
        return name + 's'
