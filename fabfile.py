from fabric.api import run
from fabric.api import task

from subproject1 import fabfile as subproject1

@task
def host_type():
    local('uname -s')
