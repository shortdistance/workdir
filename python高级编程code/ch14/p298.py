#!/usr/bin/python
# page 298

ubuntu_iso = Url('http://ubuntu.mirrors.proxad.net/hardy/ubuntu-8.04-desktop-i386.iso')
print ubuntu_iso.headers['last-modified']
