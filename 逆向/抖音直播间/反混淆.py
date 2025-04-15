import re
import subprocess

def exec_value(hex_string):
    res =subprocess.check_output(f"node part.js {hex_string}")
    char_string =res.strip()
    return char_string
def run():
    with open("f1.js", mode='r', encoding='utf-8') as f1, open("f2.js", mode='w', encoding='utf-8') as f2:
        for line in f1:
            if not line:
                f2.write(line)
                continue
            match_list =re.findall(r"(_0x2145df\((.*?)\))",line)
            for total, arg in match_list:
                real_value =exec_value(arg)
                line = line.replace(total, f'"{real_value}"')
                f2.write(line)

run()