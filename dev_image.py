from PIL import Image, ImageDraw
import os
import threading


def thread_func(tweet_texts, imagelist):

    iter = 0
    img_iter = 0
    for (x,y) in tweet_texts:
        
        filename = "img0" + str(iter) + ".png"
        f = open(filename, "w+")
        image = Image.new(mode = "RGB", size = (400,220), color = "red")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), x , fill=(200,200,0))
        image.save(filename)
        if(y == 1):
            new_name = "img0" + str(iter) + ".png"
            os.rename(imagelist[img_iter], new_name)
            img_iter +=1
    
        iter +=1
        filename = ''
        f.close()
    

def convert_text(tweet_texts, imagelist):
   
    #for tweet in tweet_texts:
    x = threading.Thread(target=thread_func, args=(tweet_texts, imagelist))
    x.start()
    
        
