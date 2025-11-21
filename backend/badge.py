import sys

percent = float(sys.argv[1])
color = (
    "brightgreen" if percent >= 90 else
    "yellow" if percent >= 75 else
    "orange" if percent >= 50 else
    "red"
)

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
  <rect width="70" height="20" fill="#555"/>
  <rect x="70" width="50" height="20" fill="{color}"/>
  <text x="35" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">coverage</text>
  <text x="95" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{percent:.1f}%</text>
</svg>
'''
with open("coverage-badge.svg", "w") as f:
    f.write(svg)
