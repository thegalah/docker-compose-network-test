import os
import subprocess
cmd = ["docker", "run", "curl-test"]
output = subprocess.check_output(cmd)
check_maintenance(self, output)