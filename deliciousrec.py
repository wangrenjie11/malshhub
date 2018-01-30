from pydelicious import get_popular,get_userposts,get_urlposts
def initalizeuserDict(tag,count=5):
      user_dict={}
	  for p1 in get_popular(tag=tag)[0:count]；
	     for p2 in get_urlposts{['href']}:
		     user=p2['user']
			    user_dict[user]{}
				return user_dict
def fillitems(user_dict)
	 all_items={}
	  for  user  in user_dict:
	     for  i  in  range(3):
		  try:
		     post=get_urlposts(user)
			 break
			 except:
			 print"ffail user "+user",retrying"
			 time.sleep(4)
	for  post in  posts；
	  url=post['href']
	  user_dict[user][url]=1.0
	   all_items[url]=1.0
	   for range in  user_dict.values():
	     for item in all_items；
		   if item not in ratings:
		      ratings[item]=0.0
			  