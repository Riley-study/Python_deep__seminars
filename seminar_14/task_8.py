import json
import os

import pytest

from project import User, ProjectException, AccessError, LevelError, Project


@pytest.fixture
def authenticated_project(request):
    file = 'test_users.json'
    data = {"5": {"12345656": "Alex"}, "7": {"12345657": "Ben"}}
    with open(file, 'w') as f:
        json.dump(data, f)
    p = Project(file)
    p.authorization("12345656", "Alex")
    def delete_project():
        os.remove(file)
    request.addfinalizer(delete_project) # выполняется после завершения работы теста, к которому приделана фикстура
    return p

@pytest.fixture
def authenticated_user():
    return User("12345656", "5", "Alex")


def test_user_authed(authenticated_project, authenticated_user):
    assert authenticated_project.admin is not None
    assert authenticated_project.admin == authenticated_user


if __name__ == '__main__':
    pytest.main(['-v'])


