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
    temp = ""

    def get_frag_by_ref(ref, f=""):
        for _, value in dd.items():
            if str(value.index) == str(ref):
                f = value.frag + f
                if (len(str(value.ref)) > 0
                        and int(value.ref) > 0):
                    return get_frag_by_ref(str(value.ref), f)
        return f

    for l in phrase:
        temp += l
        ddk = (list(dd.keys()) + [str(c.ref) for c in dd.values()]
               + [str(c.index) for c in dd.values()])
        if not temp in ddk:
            index += 1
            index_len = len(str(index))
            if index_len >= len(temp):
                index_len = len(temp) - 1
            c = Chunk(ref=temp[:index_len],
                      frag=temp[len(temp) - 1],
                      index=index)
            dd[temp] = c
            o += get_frag_by_ref(c.ref) + c.frag
            temp = ""

    if len(temp) > 0:
        a = get_frag_by_ref("3")
        for _, value in dd.items():
            if str(value.index) == str(temp):
                o += get_frag_by_ref(value.index)
    return o
