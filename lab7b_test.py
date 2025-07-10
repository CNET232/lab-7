#!/usr/bin/env python3

import subprocess

def test_lab7b():
    # Run the script and capture the output   
    p = subprocess.Popen(['python3', 'lab7b.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Provide the input
    p.stdin.write(b'3\n')
    p.stdin.flush()

    output = p.stdout.read().decode()
    assert "Sir" or "Lady" or "Lord" or "Dame" or "Master" or "Mistress" or "King" or "Queen" or "Prince" or "Princess" in output
    assert "Camelot" or "Ealdor" or "Essetir" or "Gorlois" or "Merlin's Cave" or "Tintagel" or "Avalon" or "Albion" or "Caerleon" or "Cadbury" in output

test_lab7b()
