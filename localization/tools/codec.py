"""Cosmobreeder Yiffai pack codec: Salsa20/20 keystream (key = last 32 bytes, nonce = first 8 bytes)."""
M = 0xffffffff
SIGMA = (0x61707865, 0x3320646e, 0x79622d32, 0x6b206574)

def _rotl(x, n):
    return ((x << n) | (x >> (32 - n))) & M

def _double_round(x):
    # column round
    x[4] ^= _rotl((x[0] + x[12]) & M, 7);  x[8] ^= _rotl((x[4] + x[0]) & M, 9)
    x[12] ^= _rotl((x[8] + x[4]) & M, 13); x[0] ^= _rotl((x[12] + x[8]) & M, 18)
    x[9] ^= _rotl((x[5] + x[1]) & M, 7);   x[13] ^= _rotl((x[9] + x[5]) & M, 9)
    x[1] ^= _rotl((x[13] + x[9]) & M, 13); x[5] ^= _rotl((x[1] + x[13]) & M, 18)
    x[14] ^= _rotl((x[10] + x[6]) & M, 7); x[2] ^= _rotl((x[14] + x[10]) & M, 9)
    x[6] ^= _rotl((x[2] + x[14]) & M, 13); x[10] ^= _rotl((x[6] + x[2]) & M, 18)
    x[3] ^= _rotl((x[15] + x[11]) & M, 7); x[7] ^= _rotl((x[3] + x[15]) & M, 9)
    x[11] ^= _rotl((x[7] + x[3]) & M, 13); x[15] ^= _rotl((x[11] + x[7]) & M, 18)
    # row round
    x[1] ^= _rotl((x[0] + x[3]) & M, 7);   x[2] ^= _rotl((x[1] + x[0]) & M, 9)
    x[3] ^= _rotl((x[2] + x[1]) & M, 13);  x[0] ^= _rotl((x[3] + x[2]) & M, 18)
    x[6] ^= _rotl((x[5] + x[4]) & M, 7);   x[7] ^= _rotl((x[6] + x[5]) & M, 9)
    x[4] ^= _rotl((x[7] + x[6]) & M, 13);  x[5] ^= _rotl((x[4] + x[7]) & M, 18)
    x[11] ^= _rotl((x[10] + x[9]) & M, 7); x[8] ^= _rotl((x[11] + x[10]) & M, 9)
    x[9] ^= _rotl((x[8] + x[11]) & M, 13); x[10] ^= _rotl((x[9] + x[8]) & M, 18)
    x[12] ^= _rotl((x[15] + x[14]) & M, 7); x[13] ^= _rotl((x[12] + x[15]) & M, 9)
    x[14] ^= _rotl((x[13] + x[12]) & M, 13); x[15] ^= _rotl((x[14] + x[13]) & M, 18)

def _block(state, counter):
    x = state[:]
    x[8] = counter & M
    x[9] = (counter >> 32) & M
    w = x[:]
    for _ in range(10):
        _double_round(w)
    out = bytearray(64)
    for i in range(16):
        v = (w[i] + x[i]) & M
        out[4*i:4*i+4] = v.to_bytes(4, 'little')
    return bytes(out)

def _state_from_key_nonce(key, nonce):
    """Mirrors PRG/adQ.e([B)[I : sigma + key(32) + nonce(8) layout."""
    kb = [int.from_bytes(key[4*i:4*i+4], 'little') for i in range(8)]
    nb = [int.from_bytes(nonce[4*i:4*i+4], 'little') for i in range(2)]
    s = [0] * 16
    s[0] = SIGMA[0]
    s[1:5] = kb[0:4]
    s[5] = SIGMA[1]
    s[10] = SIGMA[2]
    s[11:15] = kb[4:8]
    s[15] = SIGMA[3]
    s[6], s[7] = nb[0], nb[1]
    return s

def keystream(key, nonce, length, counter_start=1):
    st = _state_from_key_nonce(key, nonce)
    out = bytearray()
    c = counter_start
    while len(out) < length:
        out += _block(st, c)
        c += 1
    return bytes(out[:length])

def decrypt_file(blob):
    """blob layout: nonce(8) || ciphertext || key(32). Returns plaintext bytes."""
    if len(blob) < 40:
        raise ValueError('blob too short: %d' % len(blob))
    key = blob[-32:]
    body = blob[:-32]
    nonce, ct = body[:8], body[8:]
    ks = keystream(key, nonce, len(ct))
    return bytes(a ^ b for a, b in zip(ct, ks))

def encrypt_file(plain, key, nonce):
    """Inverse of decrypt_file (for repacking patches)."""
    ks = keystream(key, nonce, len(plain))
    ct = bytes(a ^ b for a, b in zip(plain, ks))
    return nonce + ct + key

if __name__ == '__main__':
    import sys, zipfile
    z = zipfile.ZipFile(sys.argv[1] if len(sys.argv) > 1 else
                        r'C:\SteamLibrary\steamapps\common\Cosmobreeder Yiffai\cosmobreeder-multi.jar')
    for n in sys.argv[2:]:
        pt = decrypt_file(z.read(n))
        print('===', n, len(pt))
        print(pt[:400])
