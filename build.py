SchemeName = "Solarmodo"

def hexToBGR(val):
    if type(val) == int:
        return val

    val = val.lstrip('#')
    if len(val) == 3:
        val += val

    r,g,b = int(val[:2], 16), int(val[2:4], 16), int(val[4:], 16)
    color = r+g*256+b*256*256
    return color

Scheme = {}
execfile("%s.scheme" % SchemeName, Scheme)

file = open("%s.ksf" % SchemeName)
contents = file.read()
file.close()

import re
for k in Scheme["colors"]:
    color = hexToBGR(Scheme["colors"][k])
    contents = re.sub(r'\d+,\s#\s+:'+k+'(?:$|\n)', "%s, # :%s\n" % (color, k), contents)
    
file = open("%s.ksf" % SchemeName, "w")
file.write(contents)
file.close()
