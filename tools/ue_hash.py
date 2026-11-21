"""Unreal's text hash for locres version 3: CityHash64 over the UTF-16LE bytes, folded to 32 bits
(GetTypeHash(uint64) = low + high * 23). Checked against the game's own Game.locres in build_locres.py."""
M = (1 << 64) - 1
K0, K1, K2 = 0xc3a5c85c97cb3127, 0xb492b66fbe98f273, 0x9ae16a3b2f90404f
KMUL = 0x9ddfea08eb382d69


def _f64(s, i): return int.from_bytes(s[i:i + 8], "little")
def _f32(s, i): return int.from_bytes(s[i:i + 4], "little")
def _rot(v, n): return v if n == 0 else ((v >> n) | (v << (64 - n))) & M
def _smix(v): return v ^ (v >> 47)
def _bswap(v): return int.from_bytes(v.to_bytes(8, "little"), "big")


def _h16(u, v, mul=KMUL):
    a = ((u ^ v) * mul) & M
    a ^= a >> 47
    b = ((v ^ a) * mul) & M
    b ^= b >> 47
    return (b * mul) & M


def _len0to16(s, n):
    if n >= 8:
        mul = (K2 + n * 2) & M
        a = (_f64(s, 0) + K2) & M
        b = _f64(s, n - 8)
        c = (_rot(b, 37) * mul + a) & M
        d = ((_rot(a, 25) + b) * mul) & M
        return _h16(c, d, mul)
    if n >= 4:
        mul = (K2 + n * 2) & M
        a = _f32(s, 0)
        return _h16((n + (a << 3)) & M, _f32(s, n - 4), mul)
    if n > 0:
        a, b, c = s[0], s[n >> 1], s[n - 1]
        y = (a + (b << 8)) & 0xFFFFFFFF
        z = (n + (c << 2)) & 0xFFFFFFFF
        return (_smix(((y * K2) ^ (z * K0)) & M) * K2) & M
    return K2


def _len17to32(s, n):
    mul = (K2 + n * 2) & M
    a = (_f64(s, 0) * K1) & M
    b = _f64(s, 8)
    c = (_f64(s, n - 8) * mul) & M
    d = (_f64(s, n - 16) * K2) & M
    return _h16((_rot((a + b) & M, 43) + _rot(c, 30) + d) & M, (a + _rot((b + K2) & M, 18) + c) & M, mul)


def _len33to64(s, n):
    mul = (K2 + n * 2) & M
    a = (_f64(s, 0) * K2) & M
    b = _f64(s, 8)
    c = _f64(s, n - 24)
    d = _f64(s, n - 32)
    e = (_f64(s, 16) * K2) & M
    f = (_f64(s, 24) * 9) & M
    g = _f64(s, n - 8)
    h = (_f64(s, n - 16) * mul) & M
    u = (_rot((a + g) & M, 43) + (_rot(b, 30) + c) * 9) & M
    v = (((a + g) & M ^ d) + f + 1) & M
    w = (_bswap(((u + v) * mul) & M) + h) & M
    x = (_rot((e + f) & M, 42) + c) & M
    y = ((_bswap(((v + w) * mul) & M) + g) * mul) & M
    z = (e + f + c) & M
    a = (_bswap(((x + z) * mul + y) & M) + b) & M
    b = (_smix(((z + a) * mul + d + h) & M) * mul) & M
    return (b + x) & M


def _weak(w, x, y, z, a, b):
    a = (a + w) & M
    b = _rot((b + a + z) & M, 21)
    c = a
    a = (a + x) & M
    a = (a + y) & M
    b = (b + _rot(a, 44)) & M
    return (a + z) & M, (b + c) & M


def _weak_s(s, i, a, b):
    return _weak(_f64(s, i), _f64(s, i + 8), _f64(s, i + 16), _f64(s, i + 24), a, b)


def city64(s: bytes) -> int:
    n = len(s)
    if n <= 32:
        return _len0to16(s, n) if n <= 16 else _len17to32(s, n)
    if n <= 64:
        return _len33to64(s, n)
    x = _f64(s, n - 40)
    y = (_f64(s, n - 16) + _f64(s, n - 56)) & M
    z = _h16((_f64(s, n - 48) + n) & M, _f64(s, n - 24))
    v = _weak_s(s, n - 64, n, z)
    w = _weak_s(s, n - 32, (y + K1) & M, x)
    x = (x * K1 + _f64(s, 0)) & M
    left = (n - 1) & ~63
    pos = 0
    while True:
        x = (_rot((x + y + v[0] + _f64(s, pos + 8)) & M, 37) * K1) & M
        y = (_rot((y + v[1] + _f64(s, pos + 48)) & M, 42) * K1) & M
        x ^= w[1]
        y = (y + v[0] + _f64(s, pos + 40)) & M
        z = (_rot((z + w[0]) & M, 33) * K1) & M
        v = _weak_s(s, pos, (v[1] * K1) & M, (x + w[0]) & M)
        w = _weak_s(s, pos + 32, (z + w[1]) & M, (y + _f64(s, pos + 16)) & M)
        z, x = x, z
        pos += 64
        left -= 64
        if left == 0:
            break
    return _h16((_h16(v[0], w[0]) + _smix(y) * K1 + z) & M, (_h16(v[1], w[1]) + x) & M)


def text_hash(s: str) -> int:
    h = city64(s.encode("utf-16-le"))
    return ((h & 0xFFFFFFFF) + (h >> 32) * 23) & 0xFFFFFFFF
