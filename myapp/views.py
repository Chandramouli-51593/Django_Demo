from django.shortcuts import render,HttpResponse
import cv2
from django.http import StreamingHttpResponse
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        if username=='ram' and password=='123':
            return HttpResponse('Login Success')
        else:
            return HttpResponse('login Failed')
    return render(request,'login.html')

def video_stream():
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()

def camera_feed(request):
    return StreamingHttpResponse(video_stream(), content_type="multipart/x-mixed-replace; boundary=frame")