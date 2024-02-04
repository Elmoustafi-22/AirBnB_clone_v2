#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of
    the web_static folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """pack web_static contents into a .tgz archive"""
    if not os.path.exists("versions"):
        local("mkdir versions")
    created = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(created))
    task = "tar -cvzf {} web_static".format(name)
    result = local(task)
    if not result.failed:
        return name


