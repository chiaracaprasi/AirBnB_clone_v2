#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder
sing the function do_pack. """

from fabric.api import *
from datetime import datetime
from os import path

env.user = 'ubuntu'
env.hosts = ['52.23.231.242', '34.229.134.248']


def do_pack():
    """
        Generates a .tgz archine from contents of web_static
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{date}.tgz"
    local("mkdir -p versions")
    archive_file = local(f"tar -czvf {filename} web_static")
    if archive_file:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """
        Distributes an archive to your web servers
        Returns False if archive_path doesn’t exist
    """

    if path.exists(archive_path) is False:
        return False

    else:
        # Upload the archive to the /tmp/ directory of the web server
        path = '/data/web_static/releases/'
        f_name = archive_path.split("/")[-1]
        f_name_no_ext = f_name.split(".")[0]

        put(archive_path, '/tmp')
        run(f'mkdir -p /data/web_static/releases/{f_name}')
        run(f'tar -xzf /tmp/{f_name} -C {path}{f_name_no_ext}/')
        run(f'rm /tmp/{f_name}')
        run(f'mv {path}{f_name_no_ext}/web_static/* {path}{f_name_no_ext}/')
        run(f'rm -rf {path}{f_name_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -sf {path}{f_name_no_ext} /data/web_static/current')