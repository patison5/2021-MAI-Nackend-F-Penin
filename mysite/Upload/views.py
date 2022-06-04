from django.shortcuts import render
import magic


# Create your views here.

def check_memory_type(file):
    mime = magic.from_buffer(file.read(), mime=True)
    return mime

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        # fs = FileSystemStorage()
        # filename = fs.save(image_file.name, image_file)
        # image_url = fs.url(filename)
        # print(image_url)
        
        print(check_memory_type(image_file))
        
        # return render(request, "upload.html", {
        #     "image_url": image_url
        # })
    
    return render(request, "upload.html")