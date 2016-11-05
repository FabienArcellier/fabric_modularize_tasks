from fabric.api import run
from fabric.api import task

@task
def host_type():
    run('uname -s')
