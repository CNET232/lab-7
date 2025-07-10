#!/usr/bin/env python3

import subprocess

def test_lab7a():
    # Run the script and capture the output   
    p = subprocess.Popen(['python3', 'lab7a.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Provide the input
    p.stdin.write(b'3\n')
    p.stdin.flush()

    output = p.stdout.read().decode()

    # Check if the output is correct
    assert "Shiny" or "Rusty" or "Broken" or "Mighty" or "Cursed" or "Blessed" or "Enchanted" or "Mysterious" or "Ancient" or "Fragile" in output
    assert "Sword" or "Shield" or "Dagger" or "Staff" or "Bow" or "Axe" or "Mace" or "Spear" or "Wand" or "Orb" in output
    assert "Edinburgh" or "Glasgow" or "Aberdeen" or "Dundee" or "Inverness" or "Stirling" or "Perth" or "St. Andrews" or "Fort William" or "Oban" in output
test_lab7a()