hosts = file('/etc/hosts')
try:
    for line in hosts:
        if line.startswith('#'):
            continue
        print line
finally:
    hosts.close()
