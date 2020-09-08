from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import  pandas as pd
from termcolor import colored
from tqdm import tqdm_gui
import os 
from datetime import datetime
import shutil

file = pd.read_csv('event.csv')

print(colored('Before using please make sure your csv file has a "Name" Column to get names','red'))
university = input("Enter Your University Name: ")
acronym = input("Enter Your University Acronym: ")
eventname = input("Enter event name: ")
leadname = input("Your Name: ")
currentdate = datetime.date(datetime.now())

fname = 'certificates/'
if os.path.exists(fname):
    shutil.rmtree(fname)
os.mkdir(fname)

for names in tqdm_gui(file['Name']):
    image = Image.new('RGB',(1000,900),(255,255,255))

    draw = ImageDraw.Draw(image)
    font_path = './Almondita.ttf'
    fontdev = ImageFont.truetype('arial.ttf', size=35)
    fontcert = ImageFont.truetype('arial.ttf', size=55)
    fontname = ImageFont.truetype('arial.ttf', size=35)
    signature = ImageFont.truetype( 
                font_path, 150
            ) 

    colordev = 'rgb(128, 128, 128)'
    colorcert = 'rgb(89, 89, 89)'
    colorname = 'rgb(77, 148, 255)'

    dsc_logo = Image.open('logo.jpg')
    dsc_logo = dsc_logo.resize((75,75))

    image.paste(dsc_logo,(100,50))
    participation_message = f"is hereby awarded this Certificate of Participation on successfully attending \n{eventname} at {university} organized by DSC {acronym}"
    draw.text((190,70),'Developer Student Clubs',font=fontdev,fill=colordev)
    draw.text((100,150),'Certificate of Participation',font=fontcert,fill=colorcert)
    draw.text((100,240),names,font=fontcert,fill=colorname)
    draw.text((100,340),participation_message,font=ImageFont.truetype('arial.ttf', size=25),fill='rgb(102, 102, 102)')
    draw.line((150,600, 500,600), fill='rgb(0, 0, 0)')
    draw.text((150,460),leadname,font=signature,fill=colorname)

    draw.text((150,620),f'Developer Student Clubs {acronym} Lead',font=ImageFont.truetype('arial.ttf', size=20),fill=colorcert)
    draw.text((700,810),'#developerstudentclubs',font=ImageFont.truetype('arial.ttf', size=20),fill='rgb(179, 0, 0)')
    draw.text((700,740),'Certificate ID:',font=ImageFont.truetype('arial.ttf', size=20),fill=colorcert)
    draw.text((700,770),f'Issue Date: {currentdate}',font=ImageFont.truetype('arial.ttf', size=20),fill=colorcert)
    image.save('certificates/'+names+'.png')
