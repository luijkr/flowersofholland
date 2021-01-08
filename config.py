import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  NAVBAR = [
    {
      "name": "Home",
      "url": "/"
    },
    {
      "name": "About",
      "url": "/about"
    }
  ]