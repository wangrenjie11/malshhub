def calculateSimlaritems (prefs, n=10):
  result={}
     itemsPrefs=transformprefs(prefs)
	   c=0
	     for  items in  itemsPrefs:
		  c+=1
		  if c%100==0: print "%d/ %d"
		  socores=toMatches(itemprefs,items,n=n,similarity=sim_distance)
		  result[item]=scores
		  return result
		  
def getRecommendedItems(prefs,itemMatch,user):
	  userRatings=prefs[user]
	  socores={}
	  totalSim={}
	   for(item,rating) in userRatings.items():
	     for(similarity,item2)  in  itemMatch[item]:
		    if item2  in  userRatings:continue
			   socores.setdefault(item2,0)
			   scores[item2] +=similarity*rating
			    totalSim.setdefault(item2,0)
				 totalSim[item2]+=similarity
				 ratkings=[(socore/totalSim[item],item) for item,score in scores.item()]
				 ratings.sort()
				 ratkings.reverse()
				 return ratkings
def loadMovienlens(path-'/data/movielens')
	  movies{}
	     for  line in  open(path+'/u.item'):
		    (id,title)=line.split('|')[0:2]
			  movies[id]=title
	priefs={}
	  for line   open (path+'/u.data'):
	    (user,movieid, rating ,ts)=line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]]=float(ratings)
	          return prefs
	  