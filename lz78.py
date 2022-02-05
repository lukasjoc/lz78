"""
LZ78 compression (Simplified)

"""

from dataclasses import dataclass
import sys

# The `Chunk` Type for a given pair


@dataclass
class Chunk:
    ref: int
    frag: str
    index: int


def encoder(phrase):
    index = 0
    dd = {"": Chunk(ref=0, frag="", index=index)}
    o = ""
    temp = ""
    mem = ""

    for l in phrase:
        temp += l
        ddk = list(dd.keys())
        if not temp in ddk:
            index += 1
            c = Chunk(ref=ddk.index(mem),
                    frag=temp[len(temp) - 1],
                    index=index)

            dd[temp] = c
            o += str(c.ref) + c.frag

            temp, mem = "", ""

        mem = temp

    if len(temp) > 0:
        o += str(dd[temp].index)

    return o


def decoder(phrase):
    index = 0
    dd = {"": Chunk(ref=0, frag="", index=index)}
    o = ""
    ap = ""
    ip = ""

    for l in phrase:
        ddk = list(dd.keys())
        if l.isnumeric():
            ip += l
            # print(ip)
        else:
            # print(ap)
            index += 1
            ap += l

            if len(ip) > 0:
                if int(ip) > 0:
                    ap = str(ddk[int(ip)]) + ap

                c = Chunk(ref=int(ip),
                        frag=str(ap),
                        index=index)

                dd[ap] = c
                o += ap
            ip = ""
            ap = ""

    if(len(ip) > 0):
        o += ddk[int(ip)]

    return o

