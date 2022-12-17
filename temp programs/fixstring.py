def allparspos(opt,pars,s):
    app=[s[:pars[0][0]]]
    for i in range(len(pars)-1):
        app.append(s[pars[i][1]+1:pars[i+1][0]])
    app.append(s[pars[-1][1]+1:])
    if len(app)==len(opt):
        app.append('')
    fr=[(app[0],0)]
    v=set()
    while len(fr)>0:
        l,n=fr.pop()
        if n<len(opt):
            if l+app[n+1] not in v:
                fr.append((l+app[n+1],n+1))
            for jjj in opt[n]:
                if l+jjj+app[n+1] not in v:
                    fr.append((l+jjj+app[n+1],n+1))
        else:
            v.add(l.replace('  ',' ').strip())
    return v
def allbracpos(opt,brac,s):
    app=[s[:brac[0][0]]]
    for i in range(len(brac)-1):
        app.append(s[brac[i][1]+1:brac[i+1][0]])
    app.append(s[brac[-1][1]+1:])
    if len(app)==len(opt):
        app.append('')
    fr=[(app[0],0)]
    v=set()
    while len(fr)>0:
        l,n=fr.pop()
        if n<len(opt):
            for jjj in opt[n]:
                if l+jjj+app[n+1] not in v:
                    fr.append((l+jjj+app[n+1],n+1))
        else:
            v.add(l.replace('  ',' ').strip())
    return v
def allmixpos(opt,mix,s):
    app=[(s[:mix[0][0]],s[mix[0][0]])]
    for i in range(len(mix)-1):
        app.append((s[mix[i][1]+1:mix[i+1][0]],s[mix[i+1][0]]))
    app.append((s[mix[-1][1]+1:],''))
    if len(app)==len(opt):
        app.append('')
    fr=[(app[0],0)]
    v=set()
    while len(fr)>0:
        l,n=fr.pop()
        if n<len(opt):
            if l[1]=='{':
                for jjj in opt[n]:
                    if jjj!='':
                        if l[0]+jjj+app[n+1][0] not in v:
                            fr.append(((l[0]+jjj+app[n+1][0],app[n+1][1]),n+1))
            elif l[1]=='(':
                fr.append(((l[0]+app[n+1][0],app[n+1][1]),n+1))
                for jjj in opt[n]:
                    if jjj!='':
                        if l[0]+jjj+app[n+1][0] not in v:
                            fr.append(((l[0]+jjj+app[n+1][0],app[n+1][1]),n+1))
        else:
            v.add(l[0].replace('  ',' ').strip())
    return v
def allposans(s):
    if s.find('{')==-1 and s.find('(')==-1 and s.find('/')==-1:
        return {s}
    pars=[]
    brac=[]
    lp=[]
    lb=[]
    p=0
    c=0
    slashes=[]
    for n,i in enumerate(s):
        if i=='{' and c==0:
            lb.append(n)
            c+=1
        elif i=='{':
            c+=1
        elif i=='}' and c==1:
            brac.append((lb.pop(),n))
            c-=1
        elif i=='}':
            c-=1
        elif i=='(' and p==0:
            lp.append(n)
            p+=1
        elif i=='(':
            p+=1
        elif i==')' and p==1:
            pars.append((lp.pop(),n))
            p-=1
        elif i==')':
            p-=1
        elif i=='/' and c==0:
            slashes.append(n)
    if len(slashes)>0:
        b=set()
        b.update(allposans(s[:slashes[0]].strip()))
        for i in range(len(slashes)-1):
            b.update(allposans(s[slashes[i]+1:slashes[i+1]].strip()))
        b.update(allposans(s[slashes[-1]+1:].strip()))
        return b
    if len(pars)>0 and len(brac)==0:
        opt=[]
        for i in pars:
            opt.append(allposans(s[i[0]+1:i[1]]))
        return allparspos(opt,pars,s)
    elif len(brac)>0 and len(pars)==0:
        opt=[]
        for i in brac:
            opt.append(allposans(s[i[0]+1:i[1]]))
        return allbracpos(opt,brac,s)
    elif len(brac)>0 and len(pars)>0:
        pp=brac.copy()
        pp.extend(pars)
        ppp=[]
        for i in pp:
            b=True
            for j in pp:
                if j!=i and j[0]<i[0] and i[1]<j[1]:
                    b=False
            if b:
                ppp.append(i)
        ppp=sorted(ppp)
        opt=[]
        for i in ppp:
            opt.append(allposans(s[i[0]+1:i[1]]))
        return allmixpos(opt,ppp,s)
def removesqb(s):
    lb=[]
    brac=[]
    b=0
    for n,i in enumerate(s):
        if i=='[' and b==0:
            lb.append(n)
            b+=1
        elif i==']' and b==1:
            brac.append((lb.pop(),n))
            b-=1
        elif i=='[':
            b+=1
        elif i==']':
            b-=1
    if len(brac)==0:
        return s.strip()
    else:
        fst=s[:brac[0][0]]
        for i in range(len(brac)-1):
            fst+=s[brac[i][1]+1:brac[i+1][0]]
        fst+=s[brac[-1][1]+1:]
        return fst.strip()
teststr=[
    "(AMUN-)RA / (P)RE",'ARRUNS (TARQUIN(IUS))',
    'STRUCK THE HEADS OFF (THE TALLEST) POPPIES (WITH HIS STAFF)',
    "CŪR FERS LIBRŌS {QUĪ {CIBUS / CIBĪ} FĪENT / {CIBUM / CIBŌS} FUTŪRŌS}?",
    'AGAMEMNON DELIBERATES (ON) WHETHER HE SHOULD SACRIFICE IPHIGENIA, WITH CALCHAS DENYING THAT IT IS RIGHT {(FOR IT) TO BE SAILED / TO SAIL} OTHERWISE',
    '{WOULD THAT / IF ONLY} THE GOOD MEN HAD NOT WON (IN) THE BATTLE!',
    '(ST.) JEROME / (SOPHRONIUS EUSEBIUS) HIERONYMUS',
    'YOU WILL TEACH THE LEADERS TO SPEAK {AGREEABLY / SWEETLY / CHARMINGLY}, {AS LONG AS / PROVIDED THAT} YOU {DEDICATE / DECLARE / ANNOUNCE} (AN) {HONOR / ADORNMENT} {TO/FOR} THE WORTHIEST SPEAKERS.',
    'WITH THE STRAITS HAVING BEEN FILLED WITH BROKEN {SPEARS / ASH TREES}, THE BROTHERS ENJOYED THEIR (GOOD) FORTUNES.',
    'ET MEĀ ET REĪ PŪBLICAE {INTEREST / RĒFERT} {CŌNSULĀTUM PETERE / UT CŌNSULĀTUM PETAM}',
    'OBSIDĒS {SERVĀ(TE) / CUSTŌDĪ(TE)} NĒ QUŌ (EF)FUGIANT',
    'YOU ARE {EARTH / DUST} AND YOU WILL {GO (BACK) / RETURN} TO {EARTH / DUST}',
    '{QUĀRTĀ / QUĀRTŌ} DIĒ {DISCESSIMUS / EXĪ(V)IMUS / ABĪ(V)IMUS}',
    'MARCUS {DID NOT WAGE / WAS NOT WAGING} MANY WARS, {DID / WAS} HE? / SURELY MARCUS {DID NOT WAGE / WAS NOT WAGING} MANY WARS?',
    'MAGNĀ CUM LAUDE and SUMMĀ CUM LAUDE [ACCEPT EITHER ORDER]',
    'ŌDĒRUNTNE TĒ VIRĪ QUŌS IN FORŌ {STANTĒS / STĀRE} VIDEŌ? [ACCEPT -NE ON ANY WORD]',
    '{WITH THE HEROES DEAD / NOW THAT THE HEROES HAVE DIED}, NOW IS THE TIME {FOR COMMITTING CRIMES AND BURNING HOUSES / TO COMMIT…}! [ACCEPT EQUIVS.]'
]
for s in teststr:
    print(s)
    s=removesqb(s)
    print(s)
    a=allposans(s)
    print('%s possible answers: '%len(a))
    for i in sorted(a):
        print('→ '+i)