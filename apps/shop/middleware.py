
class ShopMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
      self.num_requests = 0
      self.num_exceptions = 0
      self.context_response = {
         "msg": {"warning": "there is no more link in the printer"}
      }
      
   def __call__(self, request):
      # print(request.path)
      # print(request.headers['Host'])
      # print(request.headers['Accept-Language'])
      # print(request.META['REQUEST_METHOD'])
      # print(request.META['HTTP_USER_AGENT'])
      
      response = self.get_response(request)
      return response

   def stats(self, os_info):
      print(os_info)


   def process_view(self, request, view_func, view_args, view_kwargs):
      self.num_requests += 1
      # print(f"number of requests : {self.num_requests}")

   def process_exception(self, request, exception):
      self.num_exceptions += 1
      # print(f"number of exceptions : {self.num_exceptions}")

   def process_template_response(self, request, response):
      # response.context_data["new_data"] = self.context_response
      return response
   
   









