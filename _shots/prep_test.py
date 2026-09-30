# -*- coding: utf-8 -*-
import io, os

src = u"C:\\Users\\96236\\Doubao\\chats\\2026-09-30\\new-chat\\mood-check\\心境自查.html"
outdir = u"C:\\Users\\96236\\Doubao\\chats\\2026-09-30\\new-chat\\mood-check\\_shots"
html = io.open(src, encoding='utf-8').read()

quiz_inject = u"""
<script>
(function(){
  var s={tier:20, qs:pickQuestions(20), answers:{}, idx:0, finished:false};
  s.answers[s.qs[0].id]=3;
  state=s;
  localStorage.setItem('moodCheck.v1', JSON.stringify({tier:s.tier, qs:s.qs.map(function(q){return q.id;}), answers:s.answers, idx:0, finished:false}));
  location.hash='#/quiz';
})();
</script>
"""

result_inject = u"""
<script>
(function(){
  var s={tier:50, qs:pickQuestions(50), answers:{}, idx:0, finished:true};
  var byDim={emotion:4,sleep:3,stress:2,social:4,self:3,life:4};
  s.qs.forEach(function(q){ s.answers[q.id]= byDim[q.dim]; });
  state=s;
  localStorage.setItem('moodCheck.v1', JSON.stringify({tier:s.tier, qs:s.qs.map(function(q){return q.id;}), answers:s.answers, idx:0, finished:true}));
  location.hash='#/result';
  setTimeout(function(){
    var a=document.getElementById('audio-result');
    if(a){ var p=a.play(); if(p&&p.catch) p.catch(function(){}); }
  }, 400);
})();
</script>
"""

io.open(os.path.join(outdir, u"tmp-quiz.html"), 'w', encoding='utf-8').write(html.replace(u'</body>', quiz_inject + u'</body>'))
io.open(os.path.join(outdir, u"tmp-result.html"), 'w', encoding='utf-8').write(html.replace(u'</body>', result_inject + u'</body>'))
print("prepared")
