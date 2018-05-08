from .base import OpenStackRequest


class CinderRequest(OpenStackRequest):

    def get_volume_detail(self, request, project_id, volume_id):
        return self.get(request, '/v3/%s/volumes/%s' % (project_id, volume_id))

    def list_volumes(self, request, project_id, detail=False, params=None, **kwargs):
        url = '/v3/%s/volumes' % project_id
        if detail:
            url += '/detail'
        return self.get(request, url, params=params, **kwargs)

    def create_volumes(self):
        pass
