"""Minimal Java class file parser + bytecode disassembler (pure Python)."""
import struct, sys, os

CP_TAGS = {1:'Utf8',3:'Int',4:'Float',5:'Long',6:'Double',7:'Class',8:'String',
           9:'Fieldref',10:'Methodref',11:'InterfaceMethodref',12:'NameAndType',
           15:'MethodHandle',16:'MethodType',17:'Dynamic',18:'InvokeDynamic',
           19:'Module',20:'Package'}

class CP:
    def __init__(self):
        self.items = {}   # index -> (tag, payload)
    def utf8(self, i):
        t = self.items.get(i)
        if t and t[0] == 1:
            try: return t[1].decode('utf-8')
            except: return t[1].decode('latin-1')
        return None
    def cls(self, i):
        t = self.items.get(i)
        if t and t[0] == 7: return self.utf8(t[1])
        if t and t[0] == 1: return self.utf8(i)
        return None
    def nat(self, i):
        t = self.items.get(i)
        if t and t[0] == 12:
            a, b = t[1]
            return (self.utf8(a), self.utf8(b))
        return (None, None)
    def describe(self, i):
        """Human readable rendering of a constant pool entry reference."""
        t = self.items.get(i)
        if not t: return '<%d?>' % i
        tag, p = t
        if tag == 1: return self.utf8(i)
        if tag in (3,4,5,6): return repr(p)
        if tag == 7: return self.cls(i)
        if tag == 8: return '"%s"' % self.utf8(p)
        if tag in (9,10,11):
            c, nt = self.cls(p[0]), self.nat(p[1])
            kind = {9:'field',10:'method',11:'interface'}[tag]
            return '%s %s.%s%s' % (kind, c, nt[0], nt[1])
        if tag == 12:
            a, b = p
            return "%s%s" % (self.utf8(a), self.utf8(b))
        if tag == 15: return 'MethodHandle(kind=%d ref=%s)' % (p[0], self.describe(p[1]))
        if tag == 16: return 'MethodType(%s)' % self.utf8(p)
        if tag in (17,18): return 'InvokeDynamic(boot=%d nat=%s)' % (p[0], self.nat(p[1]))
        if tag == 19: return 'Module(%s)' % self.utf8(p)
        if tag == 20: return 'Package(%s)' % self.utf8(p)
        return str(t)

class ClassFile:
    def __init__(self, data):
        self.data = data
        self.cp = CP()
        self._parse_header()

    def _u1(self, o): return self.data[o]
    def _u2(self, o): return struct.unpack('>H', self.data[o:o+2])[0]
    def _u4(self, o): return struct.unpack('>I', self.data[o:o+4])[0]

    def _parse_header(self):
        d = self.data
        assert d[:4] == b'\xca\xfe\xba\xbe', 'not a class file'
        self.minor, self.major = struct.unpack('>HH', d[4:8])
        off = 8
        count = self._u2(off); off += 2
        i = 1
        while i < count:
            tag = d[off]; off += 1
            if tag == 1:
                ln = self._u2(off); off += 2
                self.cp.items[i] = (1, d[off:off+ln]); off += ln
            elif tag in (3,4):
                self.cp.items[i] = (tag, struct.unpack('>i' if tag==3 else '>f', d[off:off+4])[0]); off += 4
            elif tag in (5,6):
                v = struct.unpack('>q' if tag==5 else '>d', d[off:off+8])[0]
                self.cp.items[i] = (tag, v); off += 8; i += 1
            elif tag in (7,8,16,19,20):
                self.cp.items[i] = (tag, self._u2(off)); off += 2
            elif tag in (9,10,11,12,17,18):
                self.cp.items[i] = (tag, struct.unpack('>HH', d[off:off+4])); off += 4
            elif tag == 15:
                self.cp.items[i] = (15, (d[off], self._u2(off+1))); off += 3
            else:
                raise ValueError('bad cp tag %d at %d' % (tag, off))
            i += 1
        self.access, self.this_idx, self.super_idx = struct.unpack('>HHH', d[off:off+6]); off += 6
        ic = self._u2(off); off += 2 + 2*ic
        self.fields, off = self._members(off)
        self.methods, off = self._members(off)
        self.attrs = self._attributes(off)
        self.this_name = self.cp.cls(self.this_idx)

    def _members(self, off):
        d = self.data
        n = self._u2(off); off += 2
        out = []
        for _ in range(n):
            acc, ni, di = struct.unpack('>HHH', d[off:off+6]); off += 6
            attrs, off = self._attributes(off)
            out.append({'access':acc, 'name':self.cp.utf8(ni), 'desc':self.cp.utf8(di), 'attrs':attrs})
        return out, off

    def _attributes(self, off):
        d = self.data
        n = self._u2(off); off += 2
        out = []
        for _ in range(n):
            ni = self._u2(off); ln = self._u4(off+2); body = d[off+6:off+6+ln]
            out.append({'name': self.cp.utf8(ni), 'body': body})
            off += 6 + ln
        return out, off

    # ---- bytecode ----
    def code_of(self, m):
        for a in m['attrs']:
            if a['name'] == 'Code':
                b = a['body']
                mx, ml = struct.unpack('>HH', b[0:4])
                clen = struct.unpack('>I', b[4:8])[0]
                code = b[8:8+clen]
                p = 8 + clen
                etl = struct.unpack('>H', b[p:p+2])[0]; p += 2
                exc = [struct.unpack('>HHHH', b[p+8*k:p+8*k+8]) for k in range(etl)]
                return code, exc
        return None, None

OPS = {}
def _o(code, name, kind='none'):
    OPS[code] = (name, kind)

_o(0x00,'nop'); _o(0x01,'aconst_null'); _o(0x02,'iconst_m1'); _o(0x03,'iconst_0')
for i in range(8): _o(0x03+i, 'iconst_%d' % i)
_o(0x09,'lconst_0'); _o(0x0a,'lconst_1'); _o(0x0b,'fconst_0'); _o(0x0c,'fconst_1'); _o(0x0d,'fconst_2')
_o(0x0e,'dconst_0'); _o(0x0f,'dconst_1')
_o(0x10,'bipush','s1'); _o(0x11,'sipush','s2')
_o(0x12,'ldc','cp1'); _o(0x13,'ldc_w','cp2'); _o(0x14,'ldc2_w','cp2')
_o(0x15,'iload','u1'); _o(0x16,'lload','u1'); _o(0x17,'fload','u1'); _o(0x18,'dload','u1'); _o(0x19,'aload','u1')
for i in range(4): _o(0x1a+i,'iload_%d'%i)
for i in range(4): _o(0x1e+i,'lload_%d'%i)
for i in range(4): _o(0x22+i,'fload_%d'%i)
for i in range(4): _o(0x26+i,'dload_%d'%i)
for i in range(4): _o(0x2a+i,'aload_%d'%i)
for i, n in ((0x2e,'iaload'),(0x2f,'laload'),(0x30,'faload'),(0x31,'daload'),(0x32,'aaload'),(0x33,'baload'),(0x34,'caload'),(0x35,'saload')):
    _o(i,n)
_o(0x36,'istore','u1'); _o(0x37,'lstore','u1'); _o(0x38,'fstore','u1'); _o(0x39,'dstore','u1'); _o(0x3a,'astore','u1')
for i in range(4): _o(0x3b+i,'istore_%d'%i)
for i in range(4): _o(0x3f+i,'lstore_%d'%i)
for i in range(4): _o(0x43+i,'fstore_%d'%i)
for i in range(4): _o(0x47+i,'dstore_%d'%i)
for i in range(4): _o(0x4b+i,'astore_%d'%i)
for i, n in ((0x4f,'iastore'),(0x50,'lastore'),(0x51,'fastore'),(0x52,'dastore'),(0x53,'aastore'),(0x54,'bastore'),(0x55,'castore'),(0x56,'sastore')):
    _o(i,n)
for i, n in ((0x57,'pop'),(0x58,'pop2'),(0x59,'dup'),(0x5a,'dup_x1'),(0x5b,'dup_x2'),(0x5c,'dup2'),(0x5d,'dup2_x1'),(0x5e,'dup2_x2'),(0x5f,'swap')):
    _o(i,n)
for i in range(0x60, 0x84): _o(i, 'op_%02x' % i)
_o(0x84,'iinc','iinc')
for i, n in ((0x85,'i2l'),(0x86,'i2f'),(0x87,'i2d'),(0x88,'l2i'),(0x89,'l2f'),(0x8a,'l2d'),(0x8b,'f2i'),(0x8c,'f2l'),(0x8d,'f2d'),(0x8e,'d2i'),(0x8f,'d2l'),(0x90,'d2f'),(0x91,'i2b'),(0x92,'i2c'),(0x93,'i2s')):
    _o(i,n)
for i, n in ((0x94,'lcmp'),(0x95,'fcmpl'),(0x96,'fcmpg'),(0x97,'dcmpl'),(0x98,'dcmpg')):
    _o(i,n)
# branches
for i, n in ((0x99,'ifeq'),(0x9a,'ifne'),(0x9b,'iflt'),(0x9c,'ifge'),(0x9d,'ifgt'),(0x9e,'ifle')):
    _o(i,n,'br2')
for i, n in ((0x9f,'if_icmpeq'),(0xa0,'if_icmpne'),(0xa1,'if_icmplt'),(0xa2,'if_icmpge'),(0xa3,'if_icmpgt'),(0xa4,'if_icmple'),(0xa5,'if_acmpeq'),(0xa6,'if_acmpne')):
    _o(i,n,'br2')
_o(0xa7,'goto','br2'); _o(0xa8,'jsr','br2'); _o(0xa9,'ret','u1')
_o(0xaa,'tableswitch','tableswitch'); _o(0xab,'lookupswitch','lookupswitch')
for i, n in ((0xac,'ireturn'),(0xad,'lreturn'),(0xae,'freturn'),(0xaf,'dreturn'),(0xb0,'areturn'),(0xb1,'return')):
    _o(i,n)
_o(0xb2,'getstatic','cp2'); _o(0xb3,'putstatic','cp2'); _o(0xb4,'getfield','cp2'); _o(0xb5,'putfield','cp2')
_o(0xb6,'invokevirtual','cp2'); _o(0xb7,'invokespecial','cp2'); _o(0xb8,'invokestatic','cp2')
_o(0xb9,'invokeinterface','cp2u1'); _o(0xba,'invokedynamic','cp2pad'); _o(0xbb,'new','cp2')
_o(0xbc,'newarray','u1'); _o(0xbd,'anewarray','cp2'); _o(0xbe,'arraylength'); _o(0xbf,'athrow')
_o(0xc0,'checkcast','cp2'); _o(0xc1,'instanceof','cp2'); _o(0xc2,'monitorenter'); _o(0xc3,'monitorexit')
_o(0xc4,'wide','wide'); _o(0xc5,'multianewarray','cp2u1'); _o(0xc6,'ifnull','br2'); _o(0xc7,'ifnonnull','br2')
_o(0xc8,'goto_w','br4'); _o(0xc9,'jsr_w','br4')

ARITH = {0x60:'iadd',0x61:'ladd',0x62:'fadd',0x63:'dadd',0x64:'isub',0x65:'lsub',0x66:'fsub',0x67:'dsub',
         0x68:'imul',0x69:'lmul',0x6a:'fmul',0x6b:'dmul',0x6c:'idiv',0x6d:'ldiv',0x6e:'fdiv',0x6f:'ddiv',
         0x70:'irem',0x71:'lrem',0x72:'frem',0x73:'drem',0x74:'ineg',0x75:'lneg',0x76:'fneg',0x77:'dneg',
         0x78:'ishl',0x79:'lshl',0x7a:'ishr',0x7b:'lshr',0x7c:'iushr',0x7d:'lushr',0x7e:'iand',0x7f:'land',
         0x80:'ior',0x81:'lor',0x82:'ixor',0x83:'lxor'}
OPS.update({k:(v,'none') for k,v in ARITH.items()})

def disasm(cf, code, start_pc=0):
    out = []
    pc = 0
    n = len(code)
    while pc < n:
        op = code[pc]
        name, kind = OPS.get(op, ('<bad 0x%02x>' % op, 'none'))
        ln = 1
        arg = ''
        if kind == 'u1' or kind == 's1':
            v = code[pc+1]
            if kind == 's1' and v > 127: v -= 256
            arg = str(v); ln = 2
        elif kind == 's2':
            v = struct.unpack('>h', code[pc+1:pc+3])[0]; arg = str(v); ln = 3
        elif kind == 'u2':
            arg = str(struct.unpack('>H', code[pc+1:pc+3])[0]); ln = 3
        elif kind == 'cp1':
            i = code[pc+1]; arg = '#%d %s' % (i, cf.cp.describe(i)); ln = 2
        elif kind == 'cp2':
            i = struct.unpack('>H', code[pc+1:pc+3])[0]; arg = '#%d %s' % (i, cf.cp.describe(i)); ln = 3
        elif kind == 'cp2u1':
            i = struct.unpack('>H', code[pc+1:pc+3])[0]; arg = '#%d %s' % (i, cf.cp.describe(i)); ln = 4
        elif kind == 'cp2pad':
            i = struct.unpack('>H', code[pc+1:pc+3])[0]; arg = '#%d %s' % (i, cf.cp.describe(i)); ln = 5
        elif kind == 'br2':
            t = struct.unpack('>h', code[pc+1:pc+3])[0]; arg = '-> %d' % (pc + t); ln = 3
        elif kind == 'br4':
            t = struct.unpack('>i', code[pc+1:pc+5])[0]; arg = '-> %d' % (pc + t); ln = 5
        elif kind == 'iinc':
            a = code[pc+1]; b = code[pc+2]
            if b > 127: b -= 256
            arg = '%d, %d' % (a, b); ln = 3
        elif kind == 'tableswitch':
            pad = (4 - (pc+1) % 4) % 4
            p = pc + 1 + pad
            default = struct.unpack('>i', code[p:p+4])[0]
            lo = struct.unpack('>i', code[p+4:p+8])[0]
            hi = struct.unpack('>i', code[p+8:p+12])[0]
            arg = 'default->%d lo=%d hi=%d' % (pc+default, lo, hi)
            ln = 1 + pad + 12 + 4*max(0, hi-lo+1)
        elif kind == 'lookupswitch':
            pad = (4 - (pc+1) % 4) % 4
            p = pc + 1 + pad
            default = struct.unpack('>i', code[p:p+4])[0]
            npairs = struct.unpack('>i', code[p+4:p+8])[0]
            arg = 'default->%d npairs=%d' % (pc+default, npairs)
            ln = 1 + pad + 8 + 8*max(0, npairs)
        elif kind == 'wide':
            op2 = code[pc+1]
            if op2 == 0x84:
                arg = 'iinc %d, %d' % (struct.unpack('>H', code[pc+2:pc+4])[0], struct.unpack('>h', code[pc+4:pc+6])[0]); ln = 6
            else:
                arg = '%s %d' % (OPS.get(op2, ('?',))[0], struct.unpack('>H', code[pc+2:pc+4])[0]); ln = 4
        out.append((pc, name, arg))
        pc += ln
    return out

def load(path_or_bytes):
    if isinstance(path_or_bytes, (bytes, bytearray)):
        return ClassFile(bytes(path_or_bytes))
    with open(path_or_bytes, 'rb') as f:
        return ClassFile(f.read())
