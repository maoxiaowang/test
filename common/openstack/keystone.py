# coding=utf-8
from .base import OpenStackRequest
from ..models.utils import get_project_model

Project = get_project_model()


class IdentityRequest(OpenStackRequest):

    v3_project_pre = '/v3/projects'
    v3_user_pre = '/v3/users'

    def __init__(self):
        super().__init__('keystone')

    def auth_token(self, username, password, version=3):
        """
        Login to OpenStack.
        We don't use keystone system, so hard code here
        :param username:
        :param password:
        :param version:
        :return:
        """
        pass

    def create_project(self, request, name, is_domain=False, description=None,
                       domain_id='default', enabled=True):
        data = {
            "project": {
                "description": description,
                "domain_id": domain_id,
                "enabled": enabled,
                "is_domain": is_domain,
                "name": name
            }
        }
        result = self.post(request, self.v3_project_pre, data=data)

        # create a project model object
        project_id = result['project']['id']
        Project.objects.create(id=project_id, user__id=request.user.id)

        return result

    def list_project(self, request, name=None, enabled=True):
        result = self.get(request, self.v3_project_pre,
                          {'name': name, 'enabled': enabled})
        return result

    def delete_project(self, request, project_id):
        self.delete(request, self.v3_project_pre + '/' + project_id)
