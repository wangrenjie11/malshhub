import feedparser
import  re
def  getwordcounts(url)；
  d=feedparser.parse(url)
   wc={}
  for e in d.entries:
     if 'summary' in  e: summary=e.summary
	  else :summary=e.description
	   words=getwords(e.title+''+summary)
	   for  word in word:
	     wc.setdefault(word,0)
		 wc[word] +=1
		 return d.feed.title,wc
  def getwords(html):
   txt=re.compile{r'<[^]+>').sub(''),html}
   words=re.compile(r'^A-z^a-z]+').split(txt)
     return [word.lower() for word in  word if word !='']
	 apcount={}
	 wordcounts={}
	 feedlist=[line for  line  in file('feedlist.txt')]
	   wordcounts[title]=wc
	   for word ,count in wc.items():
	   if  count>1
	    apcount[word] +=1
		wordlist=[]
		 for w,bc  in apcount.items():
		  frac=float(bc)/len(feedlist)
		     if frac>0.1 and frac<0.5:wordlist.append(w)
			 out=file('blogdat.txt','w')
			 out.write('Blog')
			 for blog,wc  in wordcounts.items():
			  out.write(blog)
			  for word in wordlist:
			    if word in wc:out.write('\t%d' % wc[word])
				else；out.write('\t0')
				out.write('\n')