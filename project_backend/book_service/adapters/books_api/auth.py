from classic.http_auth import Group, Permission, strategies


class Permissions:
    FULL_CONTROL = Permission('full_control')


class Groups:
    ADMINS = Group('admins', permissions=(Permissions.FULL_CONTROL,))


jwt_strategy = strategies.JWT(secret_key='kerim_project')

ALL_GROUPS = (Groups.ADMINS,)
