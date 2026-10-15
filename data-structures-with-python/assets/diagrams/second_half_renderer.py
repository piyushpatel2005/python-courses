"""Reusable SVG primitives: arrays, trees, parent pointers and captioned states."""
import html
BLUE='#dbeafe'; GREEN='#dcfce7'; ORANGE='#ffedd5'; RED='#fee2e2'; PURPLE='#ede9fe'; INK='#183153'
class Drawing:
    def __init__(self,title,subtitle,height=720):
        self.h=height; self.parts=[]
        self.parts.append(f'<rect x="0" y="0" width="600" height="{height}" fill="#ffffff"/>')
        self.text(300,37,title,27)
        self.text(300,69,subtitle,19)
    def text(self,x,y,s,size=23,color=INK):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" text-anchor="middle" fill="{color}">{html.escape(str(s))}</text>')
    def box(self,x,y,w,h,label,fill=BLUE,size=23):
        self.parts.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{INK}" stroke-width="1.5"/>')
        self.text(x+w/2,y+h/2+size*.35,label,size)
        self.parts.append('</g>')
    def edge(self,x1,y1,x2,y2,arrow=False,color=INK,via=None):
        pts=[(x1,y1)]+(via or [])+[(x2,y2)]
        path='M '+' L '.join(f'{x} {y}' for x,y in pts)
        self.parts.append(f'<path d="{path}" data-connector="true" data-arrow="{str(arrow).lower()}" fill="none" stroke="{color}" stroke-width="2"'+(' marker-end="url(#tip)"' if arrow else '')+'/>')
    def array(self,vals,y,x=30,w=None,colors=None,indices=False,start=0):
        w=w or 540/len(vals)
        for i,v in enumerate(vals):
            self.box(x+i*w,y,w-3,50,str(v),(colors or {}).get(i,BLUE),22)
            if indices:self.text(x+i*w+(w-3)/2,y+75,i+start,18)
    def node(self,x,y,label,fill=BLUE,w=66):self.box(x-w/2,y-25,w,50,label,fill)
    def tree(self,nodes,edges,colors=None,arrows=False,width=66):
        for a,b in edges:
            x,y,_=nodes[a]; X,Y,_=nodes[b]
            self.edge(x,y+25,X,Y-25,arrows)
        for k,(x,y,v) in nodes.items():self.node(x,y,v,(colors or {}).get(k,BLUE),width)
    def note(self,y,*lines):
        for i,line in enumerate(lines):self.text(300,y+30*i,line,21)
    def save(self,p,root,out):
        self.note(self.h-22,'Independent example • not an exercise fixture')
        content=f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{self.h}" viewBox="0 0 600 {self.h}" role="img"><title>{html.escape(p["brief"])}</title><defs><marker id="tip" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{INK}"/></marker></defs>'+''.join(self.parts)+'</svg>\n'
        (out/p['file']).write_text(content)
        local=root/p['lesson'];local.mkdir(parents=True,exist_ok=True)
        (local/p['file']).write_text(content)

