from PIL import Image
from functools import reduce
import numpy as jafdhjsfd
import time

class sdhfsdfsdfsdf():
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __mul__(self, other):
        return sdhfsdfsdfsdf(self.x * other, self.y * other, self.z * other)
    def __add__(self, other):
        return sdhfsdfsdfsdf(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return sdhfsdfsdfsdf(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def __abs__(self):
        return self.dot(self)
    def norm(self):
        sadfbsdfhsabdf = jafdhjsfd.sqrt(abs(self))
        return self * (1.0 / jafdhjsfd.where(sadfbsdfhsabdf == 0, 1, sadfbsdfhsabdf))
    def components(self):
        return (self.x, self.y, self.z)
dsflgmsdflg = sdhfsdfsdfsdf
(sahdbgfbsad, jkgjasgnja) = (128, 128)
slkdfjsddf = sdhfsdfsdfsdf(5, 5., -10)
fdgkdjsfs = sdhfsdfsdfsdf(0., 0, 0)
kafjgsdajsdaf = [-10, 2.5, 5] 
afsbgbjasdgj = 1.0e39
dfgjakjdglk = 0
def kfjdgjkagnaf(ljggjasgkjg, lkdsflklkdf, lngdlkadlf, ngndsglng = 0):
    kjdsfgjsdg = [s.kfjfdgjkagnaff(ljggjasgkjg, lkdsflklkdf) for s in lngdlkadlf]
    kafsddfsjkd = reduce(jafdhjsfd.minimum, kjdsfgjsdg)
    jashjsgjasddf = dsflgmsdflg(0, 0, 0)
    for (s, d) in zip(lngdlkadlf, kjdsfgjsdg):
        jsfgsd = s.kfjjfdgjkagnaf(ljggjasgkjg, lkdsflklkdf, d, lngdlkadlf, ngndsglng) * (kafsddfsjkd != afsbgbjasdgj) * (d == kafsddfsjkd)
        jashjsgjasddf += jsfgsd
        _rgb = [Image.fromarray((255 * jafdhjsfd.clip(jdfgjkdfasd, 0, 1).reshape((jkgjasgnja, sahdbgfbsad))).astype(jafdhjsfd.uint8), "L") for jdfgjkdfasd in jsfgsd.components()]
        global dfgjakjdglk
        dfgjakjdglk += 1
    return jashjsgjasddf
class kfjfdgjkagnaf:
    def __init__(self, fsdafasddfsadf, jsdfsa, sdfasdgsad, xdsafsdf = 0.5):
        self.c = fsdafasddfsadf
        self.r = jsdfsa
        self.diffuse = sdfasdgsad
        self.mirror = xdsafsdf
    def kfjfdgjkagnaff(self, jfdghdjfas, jgsdbfkjgsnd):
        dakjijassd = 2 * jgsdbfkjgsnd.dot(jfdghdjfas - self.c)
        sdbfkasjdf = abs(self.c) + abs(jfdghdjfas) - 2 * self.c.dot(jfdghdjfas) - (self.r * self.r)
        dfkbgsdsdf = (dakjijassd ** 2) - (4 * sdbfkasjdf)
        sdbfsdfssdf = jafdhjsfd.sqrt(jafdhjsfd.maximum(0, dfkbgsdsdf))
        sdnbsdksf = (-dakjijassd - sdbfsdfssdf) / 2
        lskdnglskdfs = (-dakjijassd + sdbfsdfssdf) / 2
        dfkngkdfg = jafdhjsfd.where((sdnbsdksf > 0) & (sdnbsdksf < lskdnglskdfs), sdnbsdksf, lskdnglskdfs)
        asdfkjnskdjf = (dfkbgsdsdf > 0) & (dfkngkdfg > 0)
        return jafdhjsfd.where(asdfkjnskdjf, dfkngkdfg, afsbgbjasdgj)
    def kfjfddgjkagnaf(self, sakdjjfsdfh):
        return self.diffuse
    def kfjjfdgjkagnaf(self, fsadfkksdfsd, fsdklfasdf, sdfsadfsadf, sddfsdlf, dsffjsdhhf):
        return self.diffuse
        ashdbvkdffas = (fsadfkksdfsd + fsdklfasdf * sdfsadfsadf)
        sdgfjasdfsfdsa = (ashdbvkdffas - self.c) * (1. / self.r)
        toL = (slkdfjsddf - ashdbvkdffas).norm()
        toO = (fdgkdjsfs - ashdbvkdffas).norm()
        nudged = ashdbvkdffas + sdgfjasdfsfdsa * .0001
        kfjjfdgjkagnaf_distances = [s.kfjfdgjkagnaff(nudged, toL) for s in sddfsdlf]
        kfjjfdgjkagnaf_nearest = reduce(jafdhjsfd.minimum, kfjjfdgjkagnaf_distances)
        seekfjjfdgjkagnaf = kfjjfdgjkagnaf_distances[sddfsdlf.index(self)] == kfjjfdgjkagnaf_nearest
        seekfjjfdgjkagnaf = 1
        dffgndfjgdf = dsflgmsdflg(0.05, 0.05, 0.05)
        lv = jafdhjsfd.maximum(sdgfjasdfsfdsa.dot(toL), 0)
        dffgndfjgdf += self.kfjfddgjkagnaf(ashdbvkdffas) * lv * seekfjjfdgjkagnaf
        if 0:
            dassdfsdfsfdsd = (fsdklfasdf - sdgfjasdfsfdsa * 2 * fsdklfasdf.dot(sdgfjasdfsfdsa)).norm()
            dffgndfjgdf += kfjdgjkagnaf(nudged, dassdfsdfsfdsd, sddfsdlf, dsffjsdhhf + 1) * self.mirror
        phong = sdgfjasdfsfdsa.dot((toL + toO).norm())
        dffgndfjgdf += dsflgmsdflg(1, 1, 1) * jafdhjsfd.power(jafdhjsfd.clip(phong, 0, 1), 50) * seekfjjfdgjkagnaf
        return dffgndfjgdf
class dflgdffadfsf(kfjfdgjkagnaf):
    def kfjfddgjkagnaf(self, kjasdfasdbf):
        lndfgjbfdg = ((kjasdfasdbf.x * 2).astype(int) % 2) == ((kjasdfasdbf.z * 2).astype(int) % 2)
        return self.diffuse * lndfgjbfdg
ggldfsjgjdfg = [kfjfdgjkagnaf(sdhfsdfsdfsdf(0, 0, 2), .6, dsflgmsdflg(0, 0, 1))]
dflgnjgsdf = float(sahdbgfbsad) / jkgjasgnja
dfskgnkdfjgn = (-1., 1., 1., -1.)
lkdfgldsfgs = jafdhjsfd.tile(jafdhjsfd.linspace(dfskgnkdfjgn[0], dfskgnkdfjgn[2], sahdbgfbsad), jkgjasgnja)
dfgmdsflgfdsg = jafdhjsfd.repeat(jafdhjsfd.linspace(dfskgnkdfjgn[1], dfskgnkdfjgn[3], jkgjasgnja), sahdbgfbsad)
dsfnkasddfnsdf = time.time()
sdlfasdjfsdaf = sdhfsdfsdfsdf(lkdfgldsfgs, dfgmdsflgfdsg, 1)
dffgndfjgdf = kfjdgjkagnaf(fdgkdjsfs, (sdlfasdjfsdaf - fdgkdjsfs).norm(), ggldfsjgjdfg)
dsflgmsdflg = [Image.fromarray((255 * jafdhjsfd.clip(c, 0, 1).reshape((jkgjasgnja, sahdbgfbsad))).astype(jafdhjsfd.uint8), "L") for c in dffgndfjgdf.components()]

sahdbgfbsad = 400
jkgjasgnja = 300
def ksdjfsadfsdf(ksjdfkjsdfs, sajdfjsadfnsd):
    ksjdfkjsdfs /= jafdhjsfd.linalg.norm(ksjdfkjsdfs)
    return ksjdfkjsdfs
def kfjfdgjkagnaff_plane(kdfjgkjdfg, sfsdfasdfsd, sdfsdfsddg, ladfkgdfk):
    dgdffdffggk = jafdhjsfd.dot(sfsdfasdfsd, ladfkgdfk)
    if jafdhjsfd.abs(dgdffdffggk) < 1e-6:
        return jafdhjsfd.inf
    dlfgjsfdgndf = jafdhjsfd.dot(sdfsdfsddg - kdfjgkjdfg, ladfkgdfk) / dgdffdffggk
    if dlfgjsfdgndf < 0:
        return jafdhjsfd.inf
    return dlfgjsfdgndf
def kfjfdgjkagnaff_sphere(sdfhsadgsag, sjkgnaskdjngsaj, sddklfkSJDF, sgjbdsgsag):
    fdagnkfajdgn = jafdhjsfd.dot(sjkgnaskdjngsaj, sjkgnaskdjngsaj)
    lldfngkjfdgnds = sdfhsadgsag - sddklfkSJDF
    gdfgjhfdgjds = 2 * jafdhjsfd.dot(sjkgnaskdjngsaj, lldfngkjfdgnds)
    dfgjafdjgd = jafdhjsfd.dot(lldfngkjfdgnds, lldfngkjfdgnds) - sgjbdsgsag * sgjbdsgsag
    dfjkgkfjdg = gdfgjhfdgjds * gdfgjhfdgjds - 4 * fdagnkfajdgn * dfgjafdjgd
    if dfjkgkfjdg > 0:
        distSqrt = jafdhjsfd.sqrt(dfjkgkfjdg)
        kjasdfksdbf = (-gdfgjhfdgjds - distSqrt) / 2.0 if gdfgjhfdgjds < 0 else (-gdfgjhfdgjds + distSqrt) / 2.0
        sdkfsdafbsddf = kjasdfksdbf / fdagnkfajdgn
        ksdbfjsddfssdfdsa = dfgjafdjgd / kjasdfksdbf
        sdkfsdafbsddf, ksdbfjsddfssdfdsa = min(sdkfsdafbsddf, ksdbfjsddfssdfdsa), max(sdkfsdafbsddf, ksdbfjsddfssdfdsa)
        if ksdbfjsddfssdfdsa >= 0:
            return ksdbfjsddfssdfdsa if sdkfsdafbsddf < 0 else sdkfsdafbsddf
    return jafdhjsfd.inf
def kfjfdgjkagnaff(dlffgndlangasdd, sdjfsdkfjs, skdjbsdjkaf, sdfsdkjfnsafsdf):
    if skdjbsdjkaf['type'] == 'plane':
        return kfjfdgjkagnaff_plane(dlffgndlangasdd, sdjfsdkfjs, skdjbsdjkaf['position'], skdjbsdjkaf['dfbgdfk'])
    elif skdjbsdjkaf['type'] == 'sphere':
        return kfjfdgjkagnaff_sphere(dlffgndlangasdd, sdjfsdkfjs, skdjbsdjkaf['position'], skdjbsdjkaf['radius'])
def fsdhfjsadbfsajdf(dsfsdfsdfa, M, sdjfbshadfbsad, sdkjfsadfs):
    asdfhiasdfhsdif = sdjfbshadfbsad
    skdfbsdjfbs = sdjfbshadfbsad[sdkjfsadfs % (len(sdjfbshadfbsad) - 1)]
    sdhfhbsdhbf = sdkjfsadfs % (len(sdjfbshadfbsad) - 1) - 1
    if dsfsdfsdfa['type'] == 'sphere':
        sddhfbsdfsfd = ksdjfsadfsdf(M - dsfsdfsdfa['position'], asdfhiasdfhsdif)
    elif dsfsdfsdfa['type'] == 'plane':
        sddhfbsdfsfd = dsfsdfsdfa['dfbgdfk']
    sdhfhbsdhbf = sdkjfsadfs % (len(sdjfbshadfbsad) - 1) - 1
    while sdhfhbsdhbf >= 0 and asdfhiasdfhsdif[sdhfhbsdhbf] < skdfbsdjfbs:
        asdfhiasdfhsdif[sdhfhbsdhbf + 1] = asdfhiasdfhsdif[sdhfhbsdhbf]
        sdhfhbsdhbf -= 1
        if dsfsdfsdfa['type'] == 'sphere':
            sddhfbsdfsfd = ksdjfsadfsdf(M - dsfsdfsdfa['position'], asdfhiasdfhsdif)
    asdfhiasdfhsdif[sdhfhbsdhbf + 1] = skdfbsdjfbs
    return sddhfbsdfsfd, asdfhiasdfhsdif
def dskjfhasidfhsd(sdffsdfsafwad, sdfsadfsdfsd, sdfsdfsdfs, sdafaseefssdf):
    asdawsdasdsaa = sdffsdfsafwad['djhbsdfjbsfbjfs']
    if not hasattr(asdawsdasdsaa, '__len__'):
        asdawsdasdsaa = asdawsdasdsaa(sdfsadfsdfsd)
    sdfsdfsdsdfsdf = sdafaseefssdf % (len(sdfsdfsdfs) - 1)
    if (sdfsdfsdfs[sdfsdfsdsdfsdf] != max(sdfsdfsdfs[sdfsdfsdsdfsdf], sdfsdfsdfs[sdfsdfsdsdfsdf+1])):
        sdfsdfsdfs[sdfsdfsdsdfsdf], sdfsdfsdfs[sdfsdfsdsdfsdf + 1] = max(sdfsdfsdfs[sdfsdfsdsdfsdf + 1],
        sdfsdfsdfs[sdfsdfsdsdfsdf]), min(sdfsdfsdfs[sdfsdfsdsdfsdf + 1], sdfsdfsdfs[sdfsdfsdsdfsdf])
        if not hasattr(asdawsdasdsaa, '__len__'):
            asdawsdasdsaa = asdawsdasdsaa(sdfsadfsdfsd)
    return asdawsdasdsaa, sdfsdfsdfs
def sdafsdfsdfsddf(sdfasdfsadfs, sadfsadfsadf, sadfsdfasefae, sadxcsdfzdfsdf):
    sdfeawfsdfsdf = jafdhjsfd.inf
    for sdfsefsdfsddfd, sdadfsdfsfse in enumerate(ggldfsjgjdfg):
        sdfefsdfsdfds = kfjfdgjkagnaff(sdfasdfsadfs, sadfsadfsadf, sdadfsdfsfse, sadfsdfasefae)
        if sdfefsdfsdfds < sdfeawfsdfsdf:
            sdfeawfsdfsdf, bsddjbfsadhdf = sdfefsdfsdfds, sdfsefsdfsddfd
    if sdfeawfsdfsdf == jafdhjsfd.inf:
        return 
    sdadfsdfsfse = ggldfsjgjdfg[bsddjbfsadhdf]
    sdasdasdasdsad = sadfsdfasefae
    sdsafsdfsdf = sdfasdfsadfs + sadfsadfsadf * sdfeawfsdfsdf
    sdfsdfsadfsdf, sdfsdfsdfsdfsa = fsdhfjsadbfsajdf(sdadfsdfsfse, sdsafsdfsdf, sadfsdfasefae, sadxcsdfzdfsdf)
    sdfsdfsdfsdf, sdfsdafsdfsaf = dskjfhasidfhsd(sdadfsdfsfse, sdsafsdfsdf, sadfsdfasefae, sadxcsdfzdfsdf)
    sdaffxcsdaf = ksdjfsadfsdf(slkdfjsddf - sdsafsdfsdf, sadfsdfasefae)
    sdfsafsdf = ksdjfsadfsdf(sdfasddgsdsa - sdsafsdfsdf, sdfsdfsdfsdfsa)
    sdfsdfsdafs = [kfjfdgjkagnaff(sdsafsdfsdf + sdfsdfsadfsdf * .0001, sdaffxcsdaf, dfsdfhsadhg, sdfsdgsgsadsf) 
            for sdfsdgsgsadsf, dfsdfhsadhg in enumerate(ggldfsjgjdfg) if sdfsdgsgsadsf != bsddjbfsadhdf]
    if sdfsdfsdafs and min(sdfsdfsdafs) < jafdhjsfd.inf:
        return
    asdfsdfsdfsd = sddfsadfsdfs
    asdfsdfsdfsd += sdadfsdfsfse.get('sadfbjsdfsssdfsdff', sdfasddfasddf) * max(jafdhjsfd.dot(sdfsdfsadfsdf, sdaffxcsdaf), 0) * sdfsdfsdfsdf
    asdfsdfsdfsd += sdadfsdfsfse.get('fsdjfsadbajfsadbf', sdfsdfasdfsadf) * max(jafdhjsfd.dot(sdfsdfsadfsdf, ksdjfsadfsdf(sdaffxcsdaf + sdfsafsdf, sadfsdfasefae)), 0) ** sdfsddaddgsdf * djhbsdfjbsfbjfs_kfjjfdgjkagnaf
    return sdadfsdfsfse, sdsafsdfsdf, sdfsdfsadfsdf, asdfsdfsdfsd, [sdfsdfsdfsdfsa, sdfsdafsdfsaf, sdasdasdasdsad]
def fsdfsdfsdfasfd(sadfsdfsadf, sadfsdafsdf, sdfsdfsdfsa):
    return dict(type='sphere', position=jafdhjsfd.array(sadfsdfsadf), 
        radius=jafdhjsfd.array(sadfsdafsdf), djhbsdfjbsfbjfs=jafdhjsfd.array(sdfsdfsdfsa), sdkafsdjkfdfdsf=.5)
def sdfsadfsdadfsaf(sdfsfsddfsda, sdfsdfsdfsfda):
    return dict(type='plane', position=jafdhjsfd.array(sdfsfsddfsda), 
        dfbgdfk=jafdhjsfd.array(sdfsdfsdfsfda),
        djhbsdfjbsfbjfs=lambda asdfsdafsadfasdf: (sadfasdfsadfsadf 
            if (int(asdfsdafsadfasdf[0] * 2) % 2) == (int(asdfsdafsadfasdf[2] * 2) % 2) else sddafsdfasdfsad),
        sadfbjsdfsssdfsdff=.75, fsdjfsadbajfsadbf=.5, sdkafsdjkfdfdsf=.25)
sadfasdfsadfsadf = 1. * jafdhjsfd.ones(3)
sddafsdfasdfsad = 0. * jafdhjsfd.ones(3)
ggldfsjgjdfg = [fsdfsdfsdfasfd([.75, .1, 1.], .6, [0., 0., 1.]),
         fsdfsdfsdfasfd([-.75, .1, 2.25], .6, [.5, .223, .5]),
         fsdfsdfsdfasfd([-2.75, .1, 3.5], .6, [1., .572, .184]),
         sdfsadfsdadfsaf([0., -.5, 0.], [0., 1., 0.]),]
slkdfjsddf = jafdhjsfd.array([5., 5., -10.])
djhbsdfjbsfbjfs_kfjjfdgjkagnaf = jafdhjsfd.ones(3)
sddfsadfsdfs = .05
sdfasddfasddf = 1.
sdfsdfasdfsadf = 1.
sdfsddaddgsdf = 50
sdfsaddfsadfsd = 5
sdfsadgsadfsdf = 0
sdfsadfsfsdf = jafdhjsfd.zeros(3)
sdfsdfsddgssg = [kafjgsdajsdaf, kafjgsdajsdaf, kafjgsdajsdaf]
sdfasddgsdsa = jafdhjsfd.array([0., 0.35, -1.])
sdlfasdjfsdaf = jafdhjsfd.array([0., 0., 0.])
sdfasdfsdafsdf = jafdhjsfd.zeros((jkgjasgnja, sahdbgfbsad, 3))
dflgnjgsdf = float(sahdbgfbsad) / jkgjasgnja
dfskgnkdfjgn = (-1., -1. / dflgnjgsdf + .25, 1., 1. / dflgnjgsdf + .25)
for sdfsadfsdfsadf, lkdfgldsfgs in enumerate(jafdhjsfd.linspace(dfskgnkdfjgn[0], dfskgnkdfjgn[2], sahdbgfbsad)):
    if sdfsadfsdfsadf % 10 == 0:
        print('Sorting: ', sdfsadfsdfsadf / float(sahdbgfbsad) * 100, "%")
    for jsadfgasdfasdf, dfgmdsflgfdsg in enumerate(jafdhjsfd.linspace(dfskgnkdfjgn[1], dfskgnkdfjgn[3], jkgjasgnja)):
        sdfsadfsfsdf[:] = 0
        sdlfasdjfsdaf[:2] = (lkdfgldsfgs, dfgmdsflgfdsg)
        dsdfsdfsadfasfd = ksdjfsadfsdf(sdlfasdjfsdaf - sdfasddgsdsa, sdfsdfsddgssg)
        sdfsadfsadfsadf = 0
        sgadsfasdf, dassdfsdfsfdsd = sdfasddgsdsa, dsdfsdfsadfasfd
        sdfsadfasdfsd = 1.
        while sdfsadfsadfsadf < sdfsaddfsadfsd:
            sddfsadgafdfsdf = sdafsdfsdfsddf(sgadsfasdf, dassdfsdfsfdsd, kafjgsdajsdaf, sdfsadgsadfsdf)
            if not sddfsadgafdfsdf:
                break
            else:
                sdfsadgsadfsdf += 1
                dfsadfsadfas, ashdbvkdffas, sdgfjasdfsfdsa, sdfsdufsdaf, sdfsdfsddgssg = sddfsadgafdfsdf
                sgadsfasdf, dassdfsdfsfdsd = ashdbvkdffas + sdgfjasdfsfdsa * .0001, ksdjfsadfsdf(dassdfsdfsfdsd - 2 * jafdhjsfd.dot(dassdfsdfsfdsd, sdgfjasdfsfdsa) * sdgfjasdfsfdsa, sdfsdfsddgssg)
                sdfsadfsadfsadf += 1
                sdfsadfsfsdf += sdfsadfasdfsd * sdfsdufsdaf
                sdfsadfasdfsd *= dfsadfsadfas.get('sdkafsdjkfdfdsf', 1.)
        sdfasdfsdafsdf[jkgjasgnja - jsadfgasdfasdf - 1, sdfsadfsdfsadf, :] = jafdhjsfd.clip(sdfsadfsfsdf, 0, 1)
print('Sorting: ', 1. * 100, "%")