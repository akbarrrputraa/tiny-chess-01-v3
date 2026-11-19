import json,os,random,sys,urllib.request
N=120000
S='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
V=(0,82,337,365,477,1025,0)
PW=(0,0,1,1,2,4,0)
PM=(b'\x40'*8,b'\x40\x40\x40\x40\x40\x40\x40\x40\x72\x72\x72\x72\x72\x72\x72\x72\x4a\x4a\x54\x5e\x5e\x54\x4a\x4a\x45\x45\x4a\x59\x59\x4a\x45\x45\x40\x40\x40\x54\x54\x40\x40\x40\x45\x3b\x36\x40\x40\x36\x3b\x45\x45\x4a\x4a\x2c\x2c\x4a\x4a\x45\x40\x40\x40\x40\x40\x40\x40\x40',b'\x0e\x18\x22\x22\x22\x22\x18\x0e\x18\x2c\x40\x40\x40\x40\x2c\x18\x22\x40\x4a\x4f\x4f\x4a\x40\x22\x22\x45\x4f\x54\x54\x4f\x45\x22\x22\x40\x4f\x54\x54\x4f\x40\x22\x22\x45\x4a\x4f\x4f\x4a\x45\x22\x18\x2c\x40\x45\x45\x40\x2c\x18\x0e\x18\x22\x22\x22\x22\x18\x0e',b'\x2c\x36\x36\x36\x36\x36\x36\x2c\x36\x40\x40\x40\x40\x40\x40\x36\x36\x40\x45\x4a\x4a\x45\x40\x36\x36\x45\x45\x4a\x4a\x45\x45\x36\x36\x40\x4a\x4a\x4a\x4a\x40\x36\x36\x4a\x4a\x4a\x4a\x4a\x4a\x36\x36\x45\x40\x40\x40\x40\x45\x36\x2c\x36\x36\x36\x36\x36\x36\x2c',b'\x40\x40\x40\x40\x40\x40\x40\x40\x45\x4a\x4a\x4a\x4a\x4a\x4a\x45\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x40\x40\x40\x45\x45\x40\x40\x40',b'\x2c\x36\x36\x3b\x3b\x36\x36\x2c\x36\x40\x40\x40\x40\x40\x40\x36\x36\x40\x45\x45\x45\x45\x40\x36\x3b\x40\x45\x45\x45\x45\x40\x3b\x40\x40\x45\x45\x45\x45\x40\x3b\x36\x45\x45\x45\x45\x45\x40\x36\x36\x40\x45\x40\x40\x40\x40\x36\x2c\x36\x36\x3b\x3b\x36\x36\x2c',b'\x22\x18\x18\x0e\x0e\x18\x18\x22\x22\x18\x18\x0e\x0e\x18\x18\x22\x22\x18\x18\x0e\x0e\x18\x18\x22\x22\x18\x18\x0e\x0e\x18\x18\x22\x2c\x22\x22\x18\x18\x22\x22\x2c\x36\x2c\x2c\x2c\x2c\x2c\x2c\x36\x54\x54\x40\x40\x40\x40\x54\x54\x54\x5e\x4a\x40\x40\x4a\x5e\x54')
PE=(b'\x40'*8,b'\x40\x40\x40\x40\x40\x40\x40\x40\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x72\x40\x40\x40\x40\x40\x40\x40\x40',b'\x0e\x18\x22\x22\x22\x22\x18\x0e\x18\x2c\x40\x40\x40\x40\x2c\x18\x22\x40\x4a\x4f\x4f\x4a\x40\x22\x22\x45\x4f\x54\x54\x4f\x45\x22\x22\x40\x4f\x54\x54\x4f\x40\x22\x22\x45\x4a\x4f\x4f\x4a\x45\x22\x18\x2c\x40\x45\x45\x40\x2c\x18\x0e\x18\x22\x22\x22\x22\x18\x0e',b'\x2c\x36\x36\x36\x36\x36\x36\x2c\x36\x40\x40\x40\x40\x40\x40\x36\x36\x40\x45\x4a\x4a\x45\x40\x36\x36\x45\x45\x4a\x4a\x45\x45\x36\x36\x40\x4a\x4a\x4a\x4a\x40\x36\x36\x4a\x4a\x4a\x4a\x4a\x4a\x36\x36\x45\x40\x40\x40\x40\x45\x36\x2c\x36\x36\x36\x36\x36\x36\x2c',b'\x40\x40\x40\x40\x40\x40\x40\x40\x45\x4a\x4a\x4a\x4a\x4a\x4a\x45\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x3b\x40\x40\x40\x40\x40\x40\x3b\x40\x40\x40\x45\x45\x40\x40\x40',b'\x2c\x36\x36\x3b\x3b\x36\x36\x2c\x36\x40\x40\x40\x40\x40\x40\x36\x36\x40\x45\x45\x45\x45\x40\x36\x3b\x40\x45\x45\x45\x45\x40\x3b\x40\x40\x45\x45\x45\x45\x40\x3b\x36\x45\x45\x45\x45\x45\x40\x36\x36\x40\x45\x40\x40\x40\x40\x36\x2c\x36\x36\x3b\x3b\x36\x36\x2c',b'\x0e\x18\x22\x2c\x2c\x22\x18\x0e\x22\x2c\x36\x40\x40\x36\x2c\x22\x22\x36\x54\x5e\x5e\x54\x36\x22\x22\x36\x5e\x68\x68\x5e\x36\x22\x22\x36\x5e\x68\x68\x5e\x36\x22\x22\x36\x54\x5e\x5e\x54\x36\x22\x22\x22\x40\x40\x40\x40\x22\x22\x0e\x22\x22\x22\x22\x22\x22\x0e')
SQ=tuple(r*16+f for r in range(8) for f in range(8))
def _mk(T):
 o=[]
 for p in range(-6,7):
  if p==0:o.append([0]*128)
  elif p>0:o.append([T[p][(7-(i>>4))*8+(i&7)]-64+V[p] for i in range(128)])
  else:o.append([-(T[-p][(i>>4)*8+(i&7)]-64+V[-p]) for i in range(128)])
 return o
SM=_mk(PM);SE=_mk(PE)
_R=random.Random(20261119)
Z=[[ _R.getrandbits(64) for _ in range(128)] for _ in range(13)]
ZS=_R.getrandbits(64);ZC=[_R.getrandbits(64) for _ in range(16)];ZE=[_R.getrandbits(64) for _ in range(8)]
J=(-33,-31,-18,-14,14,18,31,33)
G=(-17,-16,-15,-1,1,15,16,17)
I=(-17,-15,15,17)
O=(-16,-1,1,16)
class X(Exception):pass
class Engine:
 def __init__(self):
  self.b=[0]*128;self.s=1;self.c=0;self.e=-1;self.h=0;self.w=4;self.v=116
  self.mg=0;self.eg=0;self.ph=0;self.zh=0
  self.t={};self.kl=[0]*512;self.n=0;self.g=N;self.y=[];self.z=set()
  self.fen(S)
 def fen(self,f):
  b=[0]*128;z=f.split();mg=0;eg=0;ph=0;zh=0;w=4;v=116
  for r,row in enumerate(z[0].split('/')):
   x=0
   for ch in row:
    if ch.isdigit():x+=int(ch)
    else:
     k='PNBRQKpnbrqk'.find(ch);d=(k%6+1)*(1 if k<6 else -1)
     s=(7-r)*16+x;b[s]=d
     mg+=SM[d+6][s];eg+=SE[d+6][s];zh^=Z[d+6][s]
     if d==6:w=s
     elif d==-6:v=s
     if abs(d) not in (1,6):ph+=PW[abs(d)]
     x+=1
  self.b=b;self.w=w;self.v=v;self.mg=mg;self.eg=eg;self.ph=ph
  self.s=1 if z[1]=='w' else -1;self.c=0
  if len(z)>2:
   if 'K' in z[2]:self.c|=1
   if 'Q' in z[2]:self.c|=2
   if 'k' in z[2]:self.c|=4
   if 'q' in z[2]:self.c|=8
  zh^=ZC[self.c]
  self.e=-1
  if len(z)>3 and z[3]!='-':
   self.e=(int(z[3][1])-1)*16+(ord(z[3][0])-97);zh^=ZE[self.e&7]
  if self.s<0:zh^=ZS
  self.zh=zh
  self.h=int(z[4]) if len(z)>4 else 0
  self.y=[self.zh];self.z={self.zh}
 def ky(self):return self.zh
 def at(self,q,y,J=J,G=G,I=I,O=O):
  b=self.b
  for d in (-15,-17) if y>0 else (15,17):
   t=q+d
   if not t&0x88 and b[t]==y:return True
  for d in J:
   t=q+d
   if not t&0x88 and b[t]==2*y:return True
  for d in G:
   t=q+d
   if not t&0x88 and b[t]==6*y:return True
  for d in I:
   t=q+d
   while not t&0x88:
    p=b[t]
    if p:
     if p==3*y or p==5*y:return True
     break
    t+=d
  for d in O:
   t=q+d
   while not t&0x88:
    p=b[t]
    if p:
     if p==4*y or p==5*y:return True
     break
    t+=d
  return False
 def gn(self,o=False,v=None,y=0,J=J,G=G,I=I,O=O):
  b=self.b;s=self.s;e=self.e;m=[]
  pp=y if y<256 else 255;k0=self.kl[pp*2];k1=self.kl[pp*2+1]
  for q in SQ:
   p=b[q]
   if not p or (p>0)!=(s>0):continue
   a=p if p>0 else -p
   if a==1:
    d=16 if s>0 else -16;u=1 if s>0 else 6;w=7 if s>0 else 0;n=q+d
    if not o and not n&0x88 and b[n]==0:
     if (n>>4)==w:
      for z in (5,4,3,2):
       mv=q|(n<<7)|(z<<14);sc=(1<<14)+V[z]*10
       m.append((sc if mv!=v else 1<<20,mv))
     else:
      mv=q|(n<<7);sc=1<<13 if mv==k0 else (1<<13)-1 if mv==k1 else 0
      m.append((sc if mv!=v else 1<<20,mv))
      if (q>>4)==u:
       w2=q+2*d
       if b[w2]==0:
        mv=q|(w2<<7);sc=1<<13 if mv==k0 else (1<<13)-1 if mv==k1 else 0
        m.append((sc if mv!=v else 1<<20,mv))
    for ex in (d-1,d+1):
     t=q+ex
     if t&0x88:continue
     c=b[t]
     if c and (c>0)!=(s>0):
      if (t>>4)==w:
       for z in (5,4,3,2):
        mv=q|(t<<7)|(z<<14);sc=(V[abs(c)]*10-V[a]//10)+(1<<14)+V[z]*10
        m.append((sc if mv!=v else 1<<20,mv))
      else:
       mv=q|(t<<7);sc=(V[abs(c)]*10-V[a]//10)+(1<<14)
       m.append((sc if mv!=v else 1<<20,mv))
     elif t==e and not c:
      mv=q|(t<<7);sc=(V[1]*10-V[1]//10)+(1<<14)
      m.append((sc if mv!=v else 1<<20,mv))
   elif a==2 or a==6:
    for d in J if a==2 else G:
     t=q+d
     if t&0x88:continue
     c=b[t]
     if c==0:
      if not o:
       mv=q|(t<<7);sc=1<<13 if mv==k0 else (1<<13)-1 if mv==k1 else 0
       m.append((sc if mv!=v else 1<<20,mv))
     elif (c>0)!=(s>0):
      mv=q|(t<<7);sc=(V[abs(c)]*10-V[a]//10)+(1<<14)
      m.append((sc if mv!=v else 1<<20,mv))
   else:
    for d in I if a==3 else O if a==4 else I+O:
     t=q+d
     while not t&0x88:
      c=b[t]
      if c==0:
       if not o:
        mv=q|(t<<7);sc=1<<13 if mv==k0 else (1<<13)-1 if mv==k1 else 0
        m.append((sc if mv!=v else 1<<20,mv))
      else:
       if (c>0)!=(s>0):
        mv=q|(t<<7);sc=(V[abs(c)]*10-V[a]//10)+(1<<14)
        m.append((sc if mv!=v else 1<<20,mv))
       break
      t+=d
  if not o:
   for r,kf,kt,rf,em,pa in ((1,4,6,7,(5,6),(4,5,6)),(2,4,2,0,(3,2,1),(4,3,2)),(4,116,118,119,(117,118),(116,117,118)),(8,116,114,112,(115,114,113),(116,115,114))):
    if self.c&r and b[kf]==6*s and b[rf]==4*s and not any(b[x] for x in em) and not any(self.at(x,-s) for x in pa):
     mv=kf|(kt<<7);sc=1<<13 if mv==k0 else (1<<13)-1 if mv==k1 else 0
     m.append((sc if mv!=v else 1<<20,mv))
  m.sort(reverse=True)
  return m
 def lg(self,o=False):
  r=[]
  for _,m in self.gn(o):
   u=self.mk(m)
   if not self.at(self.w if self.s<0 else self.v,self.s):r.append(m)
   self.un(m,u)
  return r
 def mk(self,m,SM=SM,SE=SE,Z=Z,ZC=ZC,ZE=ZE,PW=PW):
  b=self.b;f=m&127;t=(m>>7)&127;z=m>>14;d=b[f];s=self.s;ad=d if d>0 else -d
  c=b[t];w=t
  if ad==1 and t==self.e and c==0:
   w=t-16 if s>0 else t+16;c=b[w]
  ci=-1;lw=-1
  u=(c,w,ci,lw,self.c,self.e,self.h,self.mg,self.eg,self.ph,self.zh)
  mg=self.mg;eg=self.eg;ph=self.ph;zh=self.zh
  mg-=SM[d+6][f];eg-=SE[d+6][f];zh^=Z[d+6][f]
  if c:
   ac=c if c>0 else -c
   mg-=SM[c+6][w];eg-=SE[c+6][w];zh^=Z[c+6][w]
   if ac!=1 and ac!=6:ph-=PW[ac]
  nd=(z if s>0 else -z) if z else d
  mg+=SM[nd+6][t];eg+=SE[nd+6][t];zh^=Z[nd+6][t]
  if z:
   ph+=PW[z]
  b[f]=0;b[t]=nd
  if d==6:self.w=t
  elif d==-6:self.v=t
  if w!=t:b[w]=0
  if ad==6 and (t-f==2 or f-t==2):
   if t>f:rf=f+3;rt=f+1
   else:rf=f-4;rt=f-1
   r=b[rf]
   mg-=SM[r+6][rf];eg-=SE[r+6][rf];zh^=Z[r+6][rf]
   mg+=SM[r+6][rt];eg+=SE[r+6][rt];zh^=Z[r+6][rt]
   b[rf]=0;b[rt]=r
  oc2=self.c
  if f==4 or t==4:self.c&=~3
  if f==0 or t==0:self.c&=~2
  if f==7 or t==7:self.c&=~1
  if f==116 or t==116:self.c&=~12
  if f==112 or t==112:self.c&=~8
  if f==119 or t==119:self.c&=~4
  if self.c!=oc2:zh^=ZC[oc2]^ZC[self.c]
  if self.e!=-1:zh^=ZE[self.e&7]
  self.e=-1
  if ad==1 and (t-f==32 or f-t==32):
   self.e=(f+t)//2;zh^=ZE[self.e&7]
  self.h=0 if (ad==1 or c!=0) else self.h+1
  zh^=ZS;self.s=-s
  self.mg=mg;self.eg=eg;self.ph=ph;self.zh=zh
  return u
 def un(self,m,u):
  b=self.b;f=m&127;t=(m>>7)&127;z=m>>14
  c,w,ci,lw,a,e,h,mg,eg,ph,zh=u
  self.s=-self.s;d=b[t]
  if z:d=1 if self.s>0 else -1
  if d==6 or d==-6:
   if d==6:self.w=f
   else:self.v=f
   if t-f==2 or f-t==2:
    if t>f:
     b[f+3]=4 if self.s>0 else -4;b[f+1]=0
    else:
     b[f-4]=4 if self.s>0 else -4;b[f-1]=0
  b[f]=d;b[t]=0
  if c:b[w]=c
  self.c,self.e,self.h=a,e,h
  self.mg,self.eg,self.ph,self.zh=mg,eg,ph,zh
 def ev(self):
  ph=self.ph
  s=(self.mg*ph+self.eg*(24-ph))//24
  return s if self.s>0 else -s
 def qs(self,a,b,p):
  self.n+=1
  if self.n>self.g:raise X
  if p>=100:return self.ev()
  c=self.at(self.w if self.s>0 else self.v,-self.s)
  if not c:
   sc=self.ev()
   if sc>=b:return b
   if sc>a:a=sc
   om=self.gn(True,None,0)
  else:
   om=self.gn(False,None,0)
  AT=self.at;MK=self.mk;UN=self.un
  legal=0
  for _,z in om:
   u=MK(z)
   if AT(self.w if self.s<0 else self.v,self.s):
    UN(z,u);continue
   legal+=1
   try:r=-self.qs(-b,-a,p+1)
   finally:UN(z,u)
   if r>=b:return b
   if r>a:a=r
  if c and legal==0:return -100000+p
  return a
 def sr(self,a,b,d,p):
  self.n+=1
  if self.n>self.g:raise X
  if self.h>=100:return 0
  k=self.zh
  if k in self.z:return 0
  if d<=0:return self.qs(a,b,p)
  T=self.t;t=T.get(k);v=None
  if t:
   td,tf,ts,tm=t
   if td>=d:
    sv=ts-p if ts>90000 else ts+p if ts<-90000 else ts
    if tf==0 or (tf==1 and sv>=b) or (tf==2 and sv<=a):return sv
   v=tm
  c=self.at(self.w if self.s>0 else self.v,-self.s)
  if c:d+=1
  om=self.gn(False,v,p)
  e=-10**9;y=None;f=2
  AT=self.at;MK=self.mk;UN=self.un;KL=self.kl;B=self.b
  legal=0
  for j,(_,z) in enumerate(om):
   f0=z&127;t0=(z>>7)&127;zz=z>>14
   cap=B[t0]!=0 or (t0==self.e and (B[f0]==1 or B[f0]==-1))
   u=MK(z)
   if AT(self.w if self.s<0 else self.v,self.s):
    UN(z,u);continue
   legal+=1
   try:
    if d>=3 and j>=3 and not cap and not zz and not c:
     sc=-self.sr(-b,-a,d-2,p+1)
     if sc>a:sc=-self.sr(-b,-a,d-1,p+1)
    else:sc=-self.sr(-b,-a,d-1,p+1)
   finally:UN(z,u)
   if sc>e:e=sc;y=z
   if sc>a:a=sc;f=0
   if a>=b:
    f=1
    if not cap and not zz:
     if KL[p*2]!=z:KL[p*2+1]=KL[p*2];KL[p*2]=z
    break
  if legal==0:
   return -100000+p if c else 0
  if e>-10**9:
   sv=e if f==0 else a
   ss=sv+p if sv>90000 else sv-p if sv<-90000 else sv
   T[k]=(d,f,ss,y)
  return e
 def bm(self,n=N):
  if len(self.t)>500000:self.t.clear()
  self.g=n;self.n=0;m=self.lg()
  if not m:return None
  if len(m)==1:return m[0]
  e=m[0]
  try:
   d=1
   while d<=64:
    o=e;a=-10**9;b=10**9
    for _,z in self.gn(False,o,0):
     u=self.mk(z)
     if self.at(self.w if self.s<0 else self.v,self.s):
      self.un(z,u);continue
     try:s=-self.sr(-b,-a,d-1,1)
     except X:self.un(z,u);raise
     self.un(z,u)
     if s>a:a=s;o=z
    e=o;d+=1
  except X:pass
  return e
def uc(m):
 f=m&127;t=(m>>7)&127;z=m>>14
 s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 if z:s+={2:'n',3:'b',4:'r',5:'q'}[z]
 return s
def pu(e,s):
 f=(ord(s[0])-97)+(int(s[1])-1)*16;t=(ord(s[2])-97)+(int(s[3])-1)*16;z=0
 if len(s)==5:z={'n':2,'b':3,'r':4,'q':5}[s[4]]
 for m in e.lg():
  if m&127==f and (m>>7)&127==t and (m>>14)==z:return m
 return None
U=os.environ.get('MAKEFUN_ENV_URL','').rstrip('/')
def po(h,b):
 r=urllib.request.Request(U+h,data=json.dumps(b).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(r,timeout=10) as x:return json.load(x)
def sh(e,g):
 t=Engine();t.fen(g.get('start_fen',S));k=[t.ky()]
 for u in g.get('moves',[]):
  m=pu(t,u)
  if m is None:return
  t.mk(m);k.append(t.ky())
 e.y=k;e.z=set(k)
def main():
 if not U:sys.exit(1)
 e=Engine()
 while True:
  g=po('/game',{})
  if g.get('status')=='done':break
  e.fen(g['fen']);sh(e,g)
  while g.get('status')=='your_move':
   m=e.bm()
   if m is None:po('/resign',{'game':g['game']});break
   g=po('/move',{'game':g['game'],'move':uc(m)})
   if g.get('status')=='your_move':e.fen(g['fen']);sh(e,g)
if __name__=='__main__':main()