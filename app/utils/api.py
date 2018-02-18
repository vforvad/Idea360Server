ERROR_404 = { 'error': 'Object does not exist' }, 404

def get_object_or_404(klass, id):
    """
    Return requested object or render 404 error
    :param klass: Class type
    :param id: Object's primary key
    :return Requested instance of klass
    """
    try:
        instance = klass.query.get(id)
        if instance:
            return instance
        else:
            return ERROR_404
    except:
        return ERROR_404
