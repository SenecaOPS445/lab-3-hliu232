#!/usr/bin/env python3

# Author ID: hliu232

import subprocess

def free_space():

        space_p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        space_output = space_p.communicate()
        # Convert space_output to a string and strip off the newline characters
        space_size = space_output[0].decode('utf-8').strip()
        return space_size


#main block


if __name__ == "__main__":
    print(free_space())