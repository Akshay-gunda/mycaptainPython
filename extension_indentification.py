file=input("Enter the filename: ")
length = len(file)
for x in range(length):
    if(file[x]=="."):
        loc=x
y=file[loc+1:length]
extensions={"py":"python","txt":"text","cpp":"C++","c":"C language","js":"Javascript",".doc":"MS word","pdf":"PDF fiel","mp3":"audio file","mp4":"video file","zip":"zip compressed file","iso":"Disc image file"}
print("The extension of the file is : "+extensions[y])

