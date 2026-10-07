import sys, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from bank_week2 import WEEK2
from bank_week3 import WEEK3

LETTERS = "ABCD"

HEAD = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='14'%20fill='%231F6B57'/%3E%3Cpath%20d='M22%2024a10%2010%200%200%201%2020%200c0%206-7%207-9%2012'%20fill='none'%20stroke='%23fff'%20stroke-width='6'%20stroke-linecap='round'/%3E%3Ccircle%20cx='32'%20cy='48'%20r='4'%20fill='%23fff'/%3E%3C/svg%3E">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;1,6..72,400&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  :root{--paper:#EDEFEC;--surface:#F6F7F4;--sunk:#E3E6E1;--ink:#191D1A;--ink-soft:#414944;
    --muted:#6E766F;--rule:#D2D8D1;--rule-soft:#E1E5DF;--accent:#1F6B57;--accent-wash:#CFE3DA;
    --good:#1F6B57;--good-wash:#D6E9E0;--bad:#9B2C2C;--bad-wash:#F2DCDC;--hot:#8E6318;--hot-wash:#F0E4CB;
    --display:"Newsreader",Georgia,serif;--body:"Source Sans 3",-apple-system,"Segoe UI",sans-serif;
    --mono:"IBM Plex Mono","SF Mono",Menlo,monospace;color-scheme:light}
  @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
    --paper:#141815;--surface:#1B201D;--sunk:#10130F;--ink:#E4E8E3;--ink-soft:#B4BCB6;--muted:#8B948D;
    --rule:#2C332E;--rule-soft:#232925;--accent:#64BFA1;--accent-wash:#214136;--good:#64BFA1;
    --good-wash:#1E3A30;--bad:#E08080;--bad-wash:#3B2222;--hot:#D9A957;--hot-wash:#352C1C;color-scheme:dark}}
  :root[data-theme="dark"]{--paper:#141815;--surface:#1B201D;--sunk:#10130F;--ink:#E4E8E3;
    --ink-soft:#B4BCB6;--muted:#8B948D;--rule:#2C332E;--rule-soft:#232925;--accent:#64BFA1;
    --accent-wash:#214136;--good:#64BFA1;--good-wash:#1E3A30;--bad:#E08080;--bad-wash:#3B2222;
    --hot:#D9A957;--hot-wash:#352C1C;color-scheme:dark}
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;
       line-height:1.55;-webkit-font-smoothing:antialiased;padding-bottom:72px}
  .wrap{max-width:830px;margin:0 auto;padding:32px 24px 80px;display:flex;flex-direction:column;gap:28px}
  a{color:var(--accent)}
  .site{position:sticky;top:0;z-index:70;background:var(--paper);border-bottom:1px solid var(--rule)}
  .site .in{max-width:830px;margin:0 auto;padding:0 24px;height:50px;display:flex;align-items:center;
            justify-content:space-between;gap:14px}
  .site a,.site .cur{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase}
  .site a{text-decoration:none;color:var(--accent)}
  .site .cur{color:var(--muted)}
  .eyebrow{font-family:var(--mono);font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}
  h1{font-family:var(--display);font-weight:600;font-size:clamp(31px,5.2vw,44px);line-height:1.07;
     letter-spacing:-.015em;margin:10px 0 0;text-wrap:balance}
  .standfirst{font-family:var(--display);font-size:clamp(17px,2.3vw,19.5px);line-height:1.5;
              color:var(--ink-soft);max-width:60ch;margin:13px 0 0}
  p{margin:0;max-width:74ch}
  .how{background:var(--sunk);padding:15px 19px;display:flex;flex-direction:column;gap:7px;
       font-size:15.5px;color:var(--ink-soft)}
  .how b{color:var(--ink)}

  ol.quiz{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px;background:var(--rule)}
  li.q{background:var(--surface);padding:21px 22px 17px;display:flex;flex-direction:column;gap:13px;
       border-left:3px solid transparent}
  li.q.ok{border-left-color:var(--good)}
  li.q.no{border-left-color:var(--bad)}
  .topic{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .stem{font-size:18px;line-height:1.45;max-width:68ch}
  .stem .n{font-family:var(--mono);font-size:12px;color:var(--accent);margin-right:9px;font-weight:500}

  ol.opts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
  ol.opts>li{display:flex;flex-direction:column}
  button.opt{display:flex;gap:11px;width:100%;text-align:left;font:inherit;font-size:16px;color:var(--ink);
             background:var(--paper);border:1px solid var(--rule);padding:10px 13px;cursor:pointer;
             line-height:1.4;align-items:flex-start}
  button.opt:hover:not(:disabled){border-color:var(--accent)}
  button.opt .lt{font-family:var(--mono);font-size:13px;color:var(--muted);flex:none;padding-top:1px}
  button.opt.sel{background:var(--accent-wash);border-color:var(--accent)}
  button.opt.sel .lt{color:var(--accent)}
  li.q.checked button.opt{cursor:default}
  li.q.checked button.opt.pick-right{background:var(--good-wash);border-color:var(--good)}
  li.q.checked button.opt.pick-right .lt{color:var(--good)}
  li.q.checked button.opt.pick-wrong{background:var(--bad-wash);border-color:var(--bad)}
  li.q.checked button.opt.pick-wrong .lt{color:var(--bad)}
  .why{display:none;font-size:15px;color:var(--ink-soft);padding:7px 13px 2px 36px;max-width:66ch}
  li.q.checked .why,li.q.shown .why{display:block}
  .why b{color:var(--ink)}
  @media (max-width:560px){.why{padding-left:14px}}

  .tools{display:flex;gap:8px;flex-wrap:wrap}
  button.tool{display:inline-flex;align-items:center;gap:7px;font:inherit;font-family:var(--mono);
              font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);
              background:none;border:1px solid var(--rule);padding:6px 11px;cursor:pointer}
  button.tool:hover{color:var(--ink);border-color:var(--rule)}
  button.tool svg{width:14px;height:14px;flex:none}
  button.tool.on{color:var(--accent);border-color:var(--accent)}
  .panel{display:none;font-size:15.5px;line-height:1.5;padding:12px 15px;max-width:70ch}
  .panel.open{display:block}
  .hint{background:var(--hot-wash);color:var(--ink-soft);border-left:3px solid var(--hot)}
  .ans{background:var(--sunk);color:var(--ink-soft);border-left:3px solid var(--accent)}
  .ans .lt{font-family:var(--mono);color:var(--accent);font-weight:500}

  .finish{display:flex;flex-direction:column;gap:14px;align-items:flex-start}
  button.big{font:inherit;font-size:16px;color:var(--paper);background:var(--accent);border:none;
             padding:13px 26px;cursor:pointer;font-weight:600}
  button.big:hover{opacity:.9}
  .result{display:none;flex-direction:column;gap:9px;width:100%}
  .result.open{display:flex}
  .result .big-score{font-family:var(--display);font-size:38px;line-height:1.1;color:var(--ink)}
  .result .note{font-size:15.5px;color:var(--ink-soft)}
  .result .jump{display:flex;gap:8px;flex-wrap:wrap}
  .result .jump a{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-decoration:none;
                  color:var(--bad);border:1px solid var(--bad);padding:5px 9px}

  .bar{position:fixed;left:0;right:0;bottom:0;z-index:80;background:var(--surface);
       border-top:1px solid var(--rule);height:52px;display:flex;align-items:center}
  .bar .in{max-width:830px;margin:0 auto;padding:0 24px;width:100%;display:flex;align-items:center;
           justify-content:space-between;gap:16px}
  .bar .tick{font-family:var(--mono);font-size:13px;color:var(--ink)}
  .bar .tick i{font-style:normal;color:var(--muted)}
  .bar button{font:inherit;font-family:var(--mono);font-size:11px;letter-spacing:.08em;
              text-transform:uppercase;color:var(--accent);background:none;border:1px solid var(--rule);
              padding:7px 13px;cursor:pointer}
  .bar button:hover{border-color:var(--accent)}
  @media (max-width:560px){.wrap{padding:24px 15px 70px}li.q{padding:17px 15px 14px}}
</style>

<header class="site"><div class="in">
  <a href="./">All practice sets</a>
  <span class="cur">__CRUMB__</span>
</div></header>

<div class="wrap">
  <div>
    <div class="eyebrow">__EYEBROW__</div>
    <h1>__H1__</h1>
    <p class="standfirst">__STAND__</p>
  </div>

  <div class="how">
    <p><b>Answer every question before opening anything.</b> Guessing first and then being
      corrected beats reading the answer first. That is the pretesting effect, and it is the
      single largest free gain available tonight.</p>
    <p><b>The hint tells you where to look without telling you the answer.</b> Use it when you are
      stuck, and skip it when you are not.</p>
    <p><b>Then press check my answers at the bottom.</b> Every option gets its reasoning, including
      the ones you did not pick, because the wrong options are where the learning is.</p>
  </div>

  <ol class="quiz" id="quiz">
"""

Q_TMPL = """
  <li class="q" id="q__N__" data-a="__A__">
    <p class="topic">__TOPIC__</p>
    <p class="stem"><span class="n">__N__</span> __STEM__</p>
    <ol class="opts">
__OPTS__
    </ol>
    <div class="tools">
      <button type="button" class="tool t-hint"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/></svg>Hint</button>
      <button type="button" class="tool t-ans"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>Answer</button>
    </div>
    <div class="panel hint">__HINT__</div>
    <div class="panel ans"><span class="lt">__ALET__.</span> __AWHY__</div>
  </li>
"""

OPT_TMPL = """      <li><button type="button" class="opt"><span class="lt">__L__</span><span>__T__</span></button>
        <p class="why">__W__</p></li>"""

TAIL = """
  </ol>

  <div class="finish">
    <button type="button" class="big" id="check">Check my answers</button>
    <div class="result" id="result">
      <div class="big-score" id="bigscore"></div>
      <p class="note" id="resnote"></p>
      <div class="jump" id="jump"></div>
    </div>
  </div>
</div>

<div class="bar"><div class="in">
  <span class="tick" id="tick"></span>
  <button type="button" id="reset">Start over</button>
</div></div>

<script>
(function(){
  var KEY='__KEY__';
  var qs=[].slice.call(document.querySelectorAll('li.q'));
  var picked={},checked=false;
  try{picked=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){picked={};}

  function save(){try{localStorage.setItem(KEY,JSON.stringify(picked));}catch(e){}}

  function answered(){var n=0;qs.forEach(function(q,i){if(picked[i]!=null)n++;});return n;}
  function correct(){var n=0;qs.forEach(function(q,i){if(picked[i]===+q.dataset.a)n++;});return n;}

  function tick(){
    document.getElementById('tick').innerHTML=
      answered()+' of '+qs.length+' answered'+(checked?' <i>&middot; '+correct()+' right</i>':'');
  }

  function paint(q,i){
    var p=picked[i],a=+q.dataset.a;
    q.querySelectorAll('button.opt').forEach(function(b,k){
      b.classList.remove('sel','pick-right','pick-wrong');
      b.disabled=checked;
      if(!checked){ if(p===k+1) b.classList.add('sel'); return; }
      if(k+1===a) b.classList.add('pick-right');
      else if(k+1===p) b.classList.add('pick-wrong');
    });
    q.classList.toggle('checked',checked);
    q.classList.toggle('ok',checked&&p===a);
    q.classList.toggle('no',checked&&p!==a);
  }

  qs.forEach(function(q,i){
    q.querySelectorAll('button.opt').forEach(function(b,k){
      b.addEventListener('click',function(){
        if(checked)return;
        picked[i]=k+1;save();paint(q,i);tick();
      });
    });
    var h=q.querySelector('.hint'),an=q.querySelector('.ans');
    q.querySelector('.t-hint').addEventListener('click',function(){
      h.classList.toggle('open');this.classList.toggle('on',h.classList.contains('open'));
    });
    q.querySelector('.t-ans').addEventListener('click',function(){
      an.classList.toggle('open');this.classList.toggle('on',an.classList.contains('open'));
      q.classList.toggle('shown',an.classList.contains('open'));
    });
    paint(q,i);
  });
  tick();

  document.getElementById('check').addEventListener('click',function(){
    checked=true;
    qs.forEach(paint);tick();
    var n=correct(),un=qs.length-answered();
    document.getElementById('bigscore').textContent=n+' out of '+qs.length;
    var pct=Math.round(n/qs.length*100);
    var msg='That is '+pct+' per cent. ';
    if(un>0) msg+=un+' question'+(un===1?' was':'s were')+' left blank and counted as wrong. ';
    msg+=n===qs.length?'Nothing left to restudy here.'
        :'Read the reasoning under every red question, including why the option you picked is wrong.';
    document.getElementById('resnote').textContent=msg;
    var j=document.getElementById('jump');j.innerHTML='';
    qs.forEach(function(q,i){
      if(picked[i]===+q.dataset.a)return;
      var a=document.createElement('a');a.href='#q'+(i+1);a.textContent='Q'+(i+1);j.appendChild(a);
    });
    document.getElementById('result').classList.add('open');
    document.getElementById('result').scrollIntoView({behavior:'smooth',block:'center'});
  });

  document.getElementById('reset').addEventListener('click',function(){
    picked={};checked=false;save();
    qs.forEach(function(q,i){
      paint(q,i);
      q.classList.remove('shown');
      q.querySelectorAll('.panel').forEach(function(p){p.classList.remove('open');});
      q.querySelectorAll('.tool').forEach(function(t){t.classList.remove('on');});
    });
    document.getElementById('result').classList.remove('open');
    tick();window.scrollTo({top:0,behavior:'smooth'});
  });
})();
</script>
</html>
"""

def build(bank, out, title, crumb, eyebrow, h1, stand, key):
    body = []
    for n, (topic, stem, opts, a, hint) in enumerate(bank, 1):
        o = "\n".join(
            OPT_TMPL.replace("__L__", LETTERS[k]).replace("__T__", t).replace("__W__", w)
            for k, (t, w) in enumerate(opts))
        body.append(Q_TMPL
            .replace("__N__", str(n)).replace("__A__", str(a))
            .replace("__TOPIC__", topic).replace("__STEM__", stem)
            .replace("__OPTS__", o).replace("__HINT__", hint)
            .replace("__ALET__", LETTERS[a-1]).replace("__AWHY__", opts[a-1][1]))
    page = (HEAD.replace("__TITLE__", title).replace("__CRUMB__", crumb)
                .replace("__EYEBROW__", eyebrow).replace("__H1__", h1).replace("__STAND__", stand)
            + "".join(body) + TAIL.replace("__KEY__", key))
    p = os.path.join(REPO, out)
    open(p, "w", encoding="utf-8").write(page)
    return p, len(bank)

if __name__ == "__main__":
    for args in [
        (WEEK2, "exam-1/week-2.html", "PHI2394 Week 2 Practice",
         "Week 2", "PHI 2394 B00 &middot; exam 1 practice &middot; week 2",
         "Week 2: the Greeks, Bacon and the Middle Ages",
         "Twenty-five questions on Plato, Aristotle, Schadewaldt, Bacon, Lynn White and Rousseau. "
         "Multiple choice, one best answer each.", "phi2394-practice-w2-v1"),
        (WEEK3, "exam-1/week-3.html", "PHI2394 Week 3 Practice",
         "Week 3", "PHI 2394 B00 &middot; exam 1 practice &middot; week 3",
         "Week 3: Foucault and Kuhn",
         "Twenty-five questions on the panopticon, discipline and normalization, then paradigms, "
         "revolutions and incommensurability.", "phi2394-practice-w3-v1"),
    ]:
        p, n = build(*args)
        print("built", os.path.relpath(p, REPO), n, "questions,", os.path.getsize(p), "bytes")
