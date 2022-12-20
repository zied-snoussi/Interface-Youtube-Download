from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)
def download(link):
    list=[]
    video = YouTube(link)
    list.append(f"The video title is :\n{video.title} \n----------------------")
    list.append(f"The video description is :\n{video.description} \n----------------------")
    list.append(f"The video views is :\n{video.views} \n----------------------")
    list.append(f"The video rating is :\n{video.rating} \n----------------------")
    list.append(f"The video duration is :\n{video.length} seconds \n----------------------")
    video.streams.get_highest_resolution().download(output_path="C:/Users/zieds/Videos")
    video.register_on_complete_callback(finish())
    return list

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
    return "download done"


link=""
@app.route('/postLink' ,methods=['POST'])
def postLink():
    #req= "tunisie"
    #if request.method == "POST":
    global link
    link = request.json["inputText"]
    return link
@app.route('/getResult' ,methods=['GET'])
def getResult():
    global link
    return {"result": download(link)}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
