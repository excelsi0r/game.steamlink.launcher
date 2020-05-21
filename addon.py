import subprocess

steamLink = "/usr/bin/steamlink %U"

process = subprocess.Popen(steamLink, stdout=subprocess.PIPE)
output, error = process = process.communicate()