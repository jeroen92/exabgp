import os

release = "4.0.0-73e61fb3"
json = "4.0.0"
text = "4.0.0"
version = os.environ.get('EXABGP_VERSION',release)

# Do not change the first line as it is parsed by scripts

if __name__ == '__main__':
	import sys
	sys.stdout.write(version)
