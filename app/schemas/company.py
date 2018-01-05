from . import ma

class CompanySchema(ma.Schema):
    """ Company JSON schema """

    class Meta:
        fields = [
            'id',
            'name',
            'description',
            'start_date',
            'created_at'
        ]
