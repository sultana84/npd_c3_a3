class MyRootModel(object):
   my_attrs = {'an_attr': int, 'another_attr': str}
   def __init__(self, **kwargs):
     for i, k in self.my_attrs.items:
         value_type = k(kwargs.get(i))
         setattr(self, i, value_type)

   
 
   #{'an_attr': 'I am an attr!',
   # 'another_attr': 6, 
   # 'a_third_attr': 'I should not exist'}
   #for each attr in my attrs, set
   #self.attr from kwargs


