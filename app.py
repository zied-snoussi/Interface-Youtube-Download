from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)

link = input("Please enter the video URL : ")

video = YouTube(link)
print(f"The video title is :\n{video.title} \n----------------------")
print(f"The video description is :\n{video.description} \n----------------------")
print(f"The video views is :\n{video.views} \n----------------------")
print(f"The video rating is :\n{video.rating} \n----------------------")
print(f"The video duration is :\n{video.length} seconds \n----------------------")

#print(video.streams)

#for stream in video.streams:
 #   print(stream)

#for stream in video.streams.filter(progressive=True):
  #  print(stream)

#for stream in video.streams.filter(res="720"):
#    print(stream)

#for stream in video.streams.filter(subtype="mp4", res):
 #   print(stream)

# for stream in video.streams.filter(res="1080p"):
 #   print(stream)
 #print(video.streams.get_highest_resolution())
 #print(stream)
def finish():
    print("download done")

video.streams.get_highest_resolution().download(output_path="C:/Users/zieds/Videos")
video.register_on_complete_callback(finish())

@app.route('/postPaths' ,methods=['POST'])
def postPaths():
    #req= "tunisie"
    #if request.method == "POST":
    global req
    req = request.json["inputText"]
    return req
@app.route('/paths' ,methods=['GET'])
def paths():
    res = []
    global req
    return {"paths": res}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
