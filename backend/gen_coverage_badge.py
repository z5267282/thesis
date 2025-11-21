import sys

percent = sys.argv[1]
color = "red"
try:
    p = float(percent)
    if p >= 90: color = "green"
    elif p >= 75: color = "yellow"
    elif p >= 50: color = "orange"
except Exception: pass

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
    <rect width="70" height="20" fill="#555"/>
    <rect x="70" width="50" height="20" fill="{color}"/>
    <text x="35" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">coverage</text>
    <text x="95" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{percent}%</text>
</svg>
'''

with open("coverage-badge.svg", "w") as f:
    f.write(svg)
