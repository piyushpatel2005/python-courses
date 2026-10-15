"""Editable source for the OOP conceptual diagrams (not UML).
Run with Python to regenerate the SVGs beside this file.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent
ASSETS = {}
INK = '#172c46'
MUTED = '#40566f'
BLUE = '#e8f1ff'
TEAL = '#ddf5ee'
PURPLE = '#eee8ff'
AMBER = '#fff1d7'

class Diagram:
    def __init__(self, name, title, desc, height=560):
        self.name, self.height = name, height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{height}" viewBox="0 0 600 {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 Z" fill="#40566f"/></marker></defs>', f'<rect width="600" height="{height}" rx="18" fill="#f8fafd"/>', '<rect x="24" y="24" width="552" height="5" rx="2" fill="#3974bd"/>']
        self.text(300, 62, title, 26, True)
        self.text(300, 91, 'CONCEPTUAL MODEL · ILLUSTRATIVE EXAMPLE', 14, color=MUTED)
    def text(self,x,y,s,size=19,bold=False,color=INK):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(s)}</text>')
    def box(self,x,y,w,h,title,lines=(),fill=BLUE):
        if isinstance(lines, str): lines = (lines,)
        self.parts.append(f'<g data-card="true"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#91a7bd" stroke-width="1.5"/>')
        count=1+len(lines)
        start=y+h/2-(count-1)*14+7
        self.text(x+w/2,start,title,21,True)
        for i,line in enumerate(lines): self.text(x+w/2,start+(i+1)*28,line)
        self.parts.append('</g>')
    def arrow(self,x1,y1,x2,y2):
        self.parts.append(f'<path data-connector="true" d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{MUTED}" stroke-width="2" marker-end="url(#arrow)"/>')
    def foot(self,*lines):
        y=self.height-24-(len(lines)-1)*25
        for i,line in enumerate(lines): self.text(300,y+i*25,line,18,color=MUTED)
    def finish(self):
        ASSETS[self.name+'.svg']='\n'.join(self.parts+['</svg>'])+'\n'

d=Diagram('class-and-instance-state','One Class, Separate Instance State','A shared QuestLog class supplies behavior. Two QuestLog objects have separate entries lists. Appending to a.entries does not change b.entries.',560)
d.box(100,120,400,98,'QuestLog Class',('Shared method: add_entry(self, text)',),PURPLE)
for x in (160,440):
    d.parts.append(f'<path data-connector="true" d="M300 218 L300 249 L{x} 249 L{x} 280" fill="none" stroke="{MUTED}" stroke-width="2" marker-end="url(#arrow)"/>')
d.box(40,280,240,122,'Instance a',('a.entries = ["Map"]','One list object'),TEAL)
d.box(320,280,240,122,'Instance b',('b.entries = []','A different list object'),BLUE)
d.box(70,433,460,62,'a.add_entry("Map") changes only a',(),AMBER)
d.foot('Initialize self.entries = [] inside __init__.'); d.finish()

d=Diagram('bound-method-self','A Bound Method Remembers self','For an ordinary instance method, item.record_use() calls GameItem.record_use(item). The bound method holds the original function and the receiving instance.',560)
d.box(110,120,380,72,'item.record_use()',(),BLUE)
d.arrow(300,192,300,229)
d.box(65,229,470,128,'Bound Method: item.record_use',('__self__ is item','__func__ is GameItem.record_use'),PURPLE)
d.arrow(300,357,300,394)
d.box(80,394,440,88,'GameItem.record_use(item)',('self receives item; no extra argument'),TEAL)
d.foot('Do not pass item again in item.record_use().'); d.finish()

d=Diagram('reflected-operator-dispatch','How Reflected Multiplication Works','For 3 * v where v is a Vector unrelated to int, int.__mul__ returns NotImplemented and Vector.__rmul__ receives v and 3. If neither supports the operation Python raises TypeError.',610)
d.box(140,118,320,60,'3 * v',(),BLUE)
d.arrow(300,178,300,210)
d.box(75,210,450,68,'int.__mul__(3, v)',('Cannot multiply this Vector'),PURPLE)
d.arrow(300,278,300,332); d.text(450,311,'NotImplemented',18)
d.box(75,332,450,68,'Vector.__rmul__(v, 3)',('Try the right-hand operand'),TEAL)
d.arrow(300,400,300,448)
d.box(75,448,450,68,'Return a New Vector',('Or TypeError if both decline'),AMBER)
d.foot('Example: Vector is not a subclass of int.','A right-hand subclass can change dispatch priority.'); d.finish()

d=Diagram('cooperative-mro-order','super() Follows the MRO','For A(object), B(A), C(A), and D(B, C), D has method resolution order D, B, C, A, object. Cooperative super calls follow that order, so super in B can call C on a D instance.',800)
d.box(40,120,520,92,'Example Base Declarations',('A(object) · B(A) · C(A) · D(B, C)',),PURPLE)
d.text(300,244,'D.__mro__: lookup and cooperative call order',18)
for i,(label,fill) in enumerate([('D',BLUE),('B',TEAL),('C',TEAL),('A',PURPLE),('object',AMBER)]):
    y=266+i*76
    d.box(210,y,180,60,label,(),fill)
    if i<4: d.arrow(300,y+60,300,y+76)
d.foot('On a D instance, super() inside B continues at C.','Each cooperative method calls super() once.','The shared A is visited once, not once per branch.'); d.finish()

d=Diagram('composed-service-delegation','A Service Uses Another Object','A local MatchService keeps an injected ScoreRule object and delegates score(points) to it. Standard and fake rules share the score method. This is local game logic, not a network service.',590)
d.box(65,120,470,92,'MatchService',('self.rule = rule',),BLUE)
d.arrow(300,212,300,282)
d.text(432,253,'Delegates score',18)
d.box(65,282,470,92,'Injected ScoreRule Object',('self.rule.score(points)',),TEAL)
d.text(300,413,'Choose the rule when constructing the match service',17)
d.box(35,438,250,76,'Standard Rule',('Local game scoring',),PURPLE)
d.box(315,438,250,76,'Fake Rule',('Used in tests',),AMBER)
d.foot('The service has a rule; it is not a rule.'); d.finish()

d=Diagram('enum-member-and-value','An Enum Member Is Not Its Value','For plain Enum QuestState with DONE equal to the string done, application code uses QuestState.DONE. The name is DONE and value is done. Persist the explicit value and reconstruct the member with QuestState("done").',590)
d.box(80,120,440,80,'Application: QuestState.DONE',('A member of a plain Enum',),PURPLE)
d.arrow(300,200,300,258)
d.text(434,236,'Read .value',18)
d.box(80,258,440,80,'Storage: "done"',('A string, not an enum member',),TEAL)
d.arrow(300,338,300,396)
d.text(430,374,'QuestState("done")',18)
d.box(80,396,440,80,'Application: QuestState.DONE',('Reconstruct the named member',),PURPLE)
d.foot('.name is "DONE"; .value is "done".','For plain Enum: QuestState.DONE != "done".'); d.finish()

d=Diagram('descriptor-lookup-precedence','Which Attribute Value Wins?','For ordinary obj.x lookup, first find a class candidate through the MRO. A readable data descriptor wins over the instance dictionary, which wins over a non-data descriptor or ordinary class attribute. Missing lookup can invoke __getattr__.',700)
d.text(300,125,'obj.x · ordinary instance attribute lookup',20,True)
d.text(300,153,'First find the class candidate using type(obj).__mro__.',17)
rows=[('1 · Readable Data Descriptor','__get__ plus __set__ or __delete__',PURPLE),('2 · Instance Dictionary','obj.__dict__["x"], if present',TEAL),('3 · Non-Data Descriptor','Class candidate has __get__ only',BLUE),('4 · Ordinary Class Attribute','Return the class candidate, if present',BLUE)]
for i,(title,line,fill) in enumerate(rows):
    y=177+i*100
    d.box(65,y,470,76,title,(line,),fill)
    if i<3: d.arrow(300,y+76,300,y+100)
d.text(300,592,'Stop at the first applicable result.',19,True)
d.foot('If missing: __getattr__ may provide a fallback.','Without a fallback value, AttributeError is raised.','Custom __getattribute__ can change this behavior.'); d.finish()

d=Diagram('cart-order-invoice-snapshot','Snapshot Once, Report From the Order','Checkout copies cart line values into independent order line records. Later cart edits do not change the order. The invoice uses order quantities and captured unit prices, not the live cart or catalog.',650)
d.box(65,120,470,94,'Editable Cart',('Tea · quantity 2 · unit price 500 cents','Live shopping state'),BLUE)
d.arrow(300,214,300,270)
d.text(444,248,'Copy line values',18)
d.box(65,270,470,94,'Order Snapshot',('Tea · quantity 2 · unit price 500 cents','Independent order line records'),TEAL)
d.arrow(300,364,300,420)
d.text(436,398,'Read order only',18)
d.box(65,420,470,94,'Invoice',('Tea: 2 × 500 = 1000 cents','Total derived from captured values'),PURPLE)
d.foot('Later cart or catalog edits must not alter this order.','Copy records, not just the outer list.','Invoice prices come from the snapshot.'); d.finish()

if __name__ == '__main__':
    for name,svg in ASSETS.items():
        (OUT/name).write_text(svg)
    print(f'Generated {len(ASSETS)} SVG diagrams in {OUT}')
