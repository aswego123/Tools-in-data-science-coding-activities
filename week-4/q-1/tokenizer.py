import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

user_input = "List only the valid English words from these: j, QGA, aqTb3ya, O0xo, Oy2tNI, c4FkLEheO, NIDOQ, HZMfM, gj6p, mmsVFa2s, QxS7, GAC, Nlk2T, nVGCq, 1R, X, Wowm60l, ub6IxABJDo, 9uHgRkV, I6WJk, f24Yc6HGFL, fz0Af2, 7oF, JU2ta, xX, HbfotIuhl, j9ObEDSdQ, XEh, ls1j8c0eXc, hspNvtv6j, KKQiFbN, TF, M5E4VRx, 4RS, w89EpUZ, lVe7nKbA, KEpux, 331J, 0HTMORYw, nTjASo, R8m, 7gZN, rdySf9qF, fyFt, CvS, B, Bunx"
tokens = encoding.encode(user_input)
print(f"Tokens -{len(tokens)}")
