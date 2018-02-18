from . import abort

ERROR_404 = 'Object does not exist'

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
            abort(404, ERROR_404)
    except:
        abort(404, ERROR_404)
