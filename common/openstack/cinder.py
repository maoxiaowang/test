from .base import OpenStackRequest


class CinderRequest(OpenStackRequest):

    def __init__(self):
        super().__init__('cinder')

    def get_volume_detail(self, request, project_id, volume_id):
        """
        Show volume  details
        /v3/{project_id}/volumes/{volume_id}
        """
        return self.get(request, '/v3/%s/volumes/%s' % (project_id, volume_id))

    def list_volumes(self, request, project_id, detail=False, params=None, **kwargs):
        """
        List accessible volumes
        /v3/{project_id}/volumes
        """
        url = '/v3/%s/volumes' % project_id
        if detail:
            url += '/detail'
        return self.get(request, url, params=params, **kwargs)

    def create_volumes(self, request, project_id, volume_body, **kwargs):
        """
        Create a volume
        /v3/{project_id}/volumes
        """
        url = '/v3/%s/volumes' % project_id
        return self.post(request, url, data=volume_body)

    def create_volume_type(self, request, project_id, **kwargs):
        """
        Create a volume type
        /v3/{project_id}/types
        """
        return self.post(request, '/v3/%s/types' % project_id, data=None)

