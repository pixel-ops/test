from django.shortcuts import HttpResponse
#function based middlewares
# def Function_Middleware(get_response):
#     print("this is one time configuration code")

#     def middleware(request):
#         print("code executed before view is called")

#         response = get_response(request)

#         print("this code is executed after view is called")

#         return response

#     return middleware

#--------------------------------------------------------------------
#class based middlewares

# class ClassMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("here one time configuration code is executed")

#     def __call__(self, request):

#         print("This code is executed brefore view call")

#         response = self.get_response(request)

#         print("This code is executed after the view call")

#         return response

#-----------------------------------------------------------------
# Mulitple Middlewares

# class PrincipalMiddleware:
#     def __init__(self,get_response):

#         self.get_response = get_response
#         print("One time initialization from Principal")

#     def __call__(self, request):

#         print("this is from the Principal before view")

#         response = self.get_response(request)

#         print("this is from Principal after view")

#         return response
    
# class FacultyMiddleware:
#     def __init__(self,get_response):

#         self.get_response = get_response
#         print("One time initialization from Faculty")

#     def __call__(self, request):

#         print("this is from the Faculty before view")

#         response = self.get_response(request)

#         print("this is from Faculty after view")

#         return response
    
# class StudentMiddleware:
#     def __init__(self,get_response):

#         self.get_response = get_response
#         print("One time initialization from Student")

#     def __call__(self, request):

#         print("this is from the Student before view")

#         response = self.get_response(request)

#         print("this is from Student after view")

#         return response

#--------------------------------------------------------
# Middleware Hooks

class ProcessViewMiddleware:
    def __init__(self,get_response):

        self.get_response = get_response
        print("One time initialization from Process View")

    def __call__(self, request):

        print("this is from the Process View before view")

        response = self.get_response(request)

        print("this is from Process View after view")

        return response
    
    def process_view(request, *args, **kwargs):
        print("this is process view before view called")
        # return HttpResponse("This is from process view")
    # -----------------------OR-------------------------
        return None



class ExceptionMiddleware:
    def __init__(self,get_response):

        self.get_response = get_response
        print("One time initialization from Exception View")

    def __call__(self, request):

        print("this is from the Exception View before view")

        response = self.get_response(request)

        print("this is from Exception View after view")

        return response
    
    def process_exception(self, request,exception):
        msg = exception
        print("your exception --> ",msg)
        return HttpResponse(msg)
    # -----------------------OR-------------------------
        # return None