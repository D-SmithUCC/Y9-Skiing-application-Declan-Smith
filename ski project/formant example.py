from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import webbrowser
root = Tk()


root.title("who's got snow")
root.geometry("730x900")

def callback(url):
    webbrowser.open_new(url)

def myfunction(event):
    scrollcan.configure(scrollregion=scrollcan.bbox("all"),width=730,height=680)

def airfares(event):
    root2= Tk()

def runcode(event):
        if (snowinf.get() ==""):
            print('This is not the data you are looking for')

def hotel_costs(event):
    root3 = Tk()


filein= open('whose_got_snow.csv', 'r')
snowinf= filein.readlines()
filein.close()

for line in snowinf:
    inf=line.split(',')
    if inf[0] == 'whistler':
        whistlerprox=inf[1]
        whistlerlifts= inf[2]
        whistlervert= inf[3]
    elif inf[0] == 'fernie':
        fernieprox= inf[1]
        fernielifts= inf[2]
        fernievert= inf[3]
    elif inf[0] == 'St.Anton':
        StAntonprox= inf[1]
        StAntonlifts= inf[2]
        StAntonvert= inf[3]
    elif inf[0] == 'WhiteFish':
        WhiteFishprox= inf[1]
        WhiteFishlifts= inf[2]
        WhiteFishvert= inf[3]
    elif inf[0] == 'MontTremblant':
        MontTremblantprox= inf[1]
        MontTremblantlifts= inf[2]
        MontTremblantvert= inf[3]
    elif inf[0] == 'BigWhite':
        BigWhiteprox= inf[1]
        BigWhitelifts= inf[2]
        BigWhitevert= inf[3]
    elif inf[0] == 'Revelstoke':
        Revelstokeprox= inf[1]
        Revelstokelifts= inf[2]
        Revelstokevert= inf[3]
    elif inf[0] == 'KickingHorse':
        KickingHorseprox= inf[1]
        KickingHorselifts= inf[2]
        KickingHorsevert= inf[3]
    
        
        
        

 
        
 

scrollframe=Frame(root)
scrollframe.pack(fill=X, side=BOTTOM)
scrollframe.pack(fill=Y)
scrollcan= Canvas(scrollframe,)
myscrollbar=Scrollbar(scrollframe,orient="vertical",command=scrollcan.yview)
scrollcan.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
scrollcan.pack(side='left')
bigframe= Frame(scrollcan, width=600)
bigframe.pack(fill=Y)
scrollcan.create_window((0,0),window=bigframe,anchor='nw')
scrollframe.bind("<Configure>",myfunction)

topframe = Frame(root,bg='#7126A2',height='125')
topframe.pack(fill=X)

fluff0= Label(topframe, text='                             ')
fluff2= Label(topframe, text='                                          ')
fluff0.grid(row= 0, column= 0)
fluff2.grid(row= 0,column= 2)
fluff0.config(bg='#7126A2')
fluff2.config(bg='#7126A2')



can1 = Canvas(topframe,height='125',bg="#7126A2",highlightthickness=0, width= '75')
myimage1 = Image.open('simple-plane (1).jpg')
myimage1 = myimage1.resize((75,75),Image.ANTIALIAS)
myimg1 = ImageTk.PhotoImage(myimage1)



can1.grid(row= 1, column=1)



can2 = Canvas(topframe,height='125',bg="#7126A2",highlightthickness=0, width= '75')
myimage2 = Image.open('hotel-building-icon-in-cartoon-style-vector-9293136.jpg')
myimage2 = myimage2.resize((75,75),Image.ANTIALIAS)
myimg2 = ImageTk.PhotoImage(myimage2)

can2.grid(row= 1, column=3)
           












snowrl= Label(topframe,font="Times 24 bold ", bg='#7126A2', text= 'Each card has information on a given resort\nand is linked to an online webpage\n with real-time iformation on snowfall')
snowrl.grid( row=0, column=1)



imgframe1 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=150)
imgframe1.grid(row=1, column=1)
bgcanvas4 = Canvas(imgframe1,height=150,width=200)
bgcanvas4.grid(row=0,column=0)
Bl1 = Label(imgframe1,text=" ----------------------Whistler-----------------------\nWhistler is " + whistlerprox + "km from Toronto \n Whistler features " + whistlerlifts + "ski lifts \n From peak to base, Whistler has " + whistlervert +"metres of vertical\n Whistler is a beatiful mountain resort\njust an hour's drive from the city of Vancouver.\n This is some of the best groomed\n skiing to be found in Canada!\n For more information about snowfall\n at Whistler, visit the linked 'on the snow' webpage.")
Bl1.grid(row=0,column=1)
Bl1.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/british-columbia/whistler-blackcomb/skireport.html"))
myimage7 = Image.open("2012_12_mikecrane_ja14_2012_027.jpg")
myimage7= myimage7.resize((200, 150), Image.ANTIALIAS)
myimg7 = ImageTk.PhotoImage(myimage7)
bgcanvas4.create_image(0, 0, image=myimg7, anchor = NW)

imgframe3 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=150)
imgframe3.grid(row=3, column=1)
bgcanvas6 = Canvas(imgframe3,height=150,width=200)
bgcanvas6.grid(row=0,column=0)
Bl2 = Label(imgframe3,text="-----------------------Fernie------------------------\n Fernie is " + fernieprox + "km from Toronto \n Fernie features " + fernielifts + "ski lifts \n From peak to base, Fernie has " + fernievert +"metres of vertical\n Fernie is a beautiful ski resort located within\n the interior of BC. This resort doesn't have\n the same cheery village as some others, but\n makes up for it with consistantly some\n of the best powder in Canada!\n For more information about snowfall\n at Fernie, visit the linked 'on the snow' webpage.")
Bl2.grid(row=0,column=1)
Bl2.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/british-columbia/fernie-alpine/skireport.html"))
myimage9 = Image.open("filename-p060089-101rr.jpg")
myimage9= myimage9.resize((200, 150), Image.ANTIALIAS)
myimg9 = ImageTk.PhotoImage(myimage9)
bgcanvas6.create_image(0, 0, image=myimg9, anchor = NW)

imgframe2 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=150)
imgframe2.grid(row=2, column=1)
bgcanvas5 = Canvas(imgframe2,height=150,width=200)
bgcanvas5.grid(row=0,column=0)
Bl3 = Label(imgframe2,text="----------------------St.Anton-----------------------\n St.Anton is " + StAntonprox + "km from Toronto \n St.Anton features " + StAntonlifts + "ski lifts \n From peak to base, St.Anton has " + StAntonvert +"metres of vertical\n St.Anton is one of the huge\n ski hills of the world.\nLocated in Austria, this bohemith\nof a restort has over 80 lifts!\n For more information about snowfall \n at St.Anton, visit the linked 'on the snow' webpage.")
Bl3.grid(row=0,column=1)
Bl3.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/tyrol/st-anton-am-arlberg/skireport.html"))
myimage8 = Image.open("download.jpg")
myimage8= myimage8.resize((200, 150), Image.ANTIALIAS)
myimg8 = ImageTk.PhotoImage(myimage8)
bgcanvas5.create_image(0, 0, image=myimg8, anchor = NW)

imgframe4 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=190)
imgframe4.grid(row=4, column=1)
bgcanvas6 = Canvas(imgframe4,height=150,width=200)
bgcanvas6.grid(row=0,column=0)
Bl4 = Label(imgframe4,text="---------------------White Fish----------------------\n White Fish is " + WhiteFishprox + "km from Toronto \n White Fish features " + WhiteFishlifts + "ski lifts From peak to base,\n White Fish has " + WhiteFishvert +"metres of vertical\n White Fish is a beautiful\n resort with stunning veiws, great\n skiing, and consistantly spectacular snow.\n Though not accessible through skiing\nin like at other resorts,\n the White Fish village is also spectacular.\nFor more information about snowfall\n at Whitefish, visit the linked 'on the snow' webpage.")
Bl4.grid(row=0,column=1)
Bl4.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/montana/whitefish-mountain-resort/skireport.html"))
myimage10 = Image.open("imageseseses.jpg")
myimage10= myimage10.resize((200, 150), Image.ANTIALIAS)
myimg10 = ImageTk.PhotoImage(myimage10)
bgcanvas6.create_image(0, 0, image=myimg10, anchor = NW)

imgframe5 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=190)
imgframe5.grid(row=5, column=1)
bgcanvas7 = Canvas(imgframe5,height=150,width=200)
bgcanvas7.grid(row=0,column=0)
Bl5 = Label(imgframe5,text="-------------------Mont Tremblant-------------------\n Mont Tremblant is " + MontTremblantprox + "km from Toronto \n MontTremblant features " + MontTremblantlifts + "\nski lifts From peak to base,\n MontTremblant has " + MontTremblantvert +"metres of vertical.\n Mont Tremblant is a small but charming\n resort in Quebec Canada.\n With great views and better snow, \n this is some of the best skiing in Eastern Canada.\nFor more information about snowfall\n at Mont Tremblant, visit the \nlinked 'on the snow' webpage. ")
Bl5.grid(row=0,column=1)
Bl5.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/quebec/tremblant/skireport.html"))
myimage11 = Image.open("ski-1.jpg")
myimage11= myimage11.resize((200, 150), Image.ANTIALIAS)
myimg11 = ImageTk.PhotoImage(myimage11)
bgcanvas7.create_image(0, 0, image=myimg11, anchor = NW)

imgframe6 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=190)
imgframe6.grid(row=6, column=1)
bgcanvas8 = Canvas(imgframe6,height=150,width=200)
bgcanvas8.grid(row=0,column=0)
Bl6 = Label(imgframe6,text="--------------------Big White-----------------------\n Big White is " + BigWhiteprox + "km from Toronto \n Big White features " + BigWhitelifts + "\nski lifts From peak to base,\n BigWhite has " + BigWhitevert +"metres of vertical.\n Big White is a beautiful resort for activities\n that include more than just skiing.\n The incredible accomadations,\n enticing restaurants and pleasant\n village are all cornerstones of this\n magnificant resort.\n For more information about snowfall\n at Big White, visit the linked 'on the snow' webpage. ")
Bl6.grid(row=0,column=1)
Bl6.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/british-columbia/big-white/skireport.html"))
myimage12 = Image.open("skiski.jpg")
myimage12= myimage12.resize((200, 150), Image.ANTIALIAS)
myimg12 = ImageTk.PhotoImage(myimage12)
bgcanvas8.create_image(0, 0, image=myimg12, anchor = NW)

imgframe7 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=190)
imgframe7.grid(row=7, column=1)
bgcanvas9 = Canvas(imgframe7,height=150,width=200)
bgcanvas9.grid(row=0,column=0)
Bl7 = Label(imgframe7,text="--------------------Revelstoke----------------------\n Revelstoke is " + Revelstokeprox + "km from Toronto \n Revelstoke features " + Revelstokelifts + "\nski lifts From peak to base,\n Revelstoke has " + Revelstokevert +"metres of vertical.\n Revelstoke is well known amongst the skiing\n community for its incredible cat\nskiing as more importantly\n powder. While not supportive to lower\nlevel skiers, this is\n truely one of the best resorts in North\n America for higher level skiers.\n For more information about snowfall\n at Revelstoke, visit the linked 'on the snow' webpage. ")
Bl7.grid(row=0,column=1)
Bl7.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/british-columbia/revelstoke-mountain/skireport.html"))
myimage13 = Image.open("freeride_world_tour_kicking_horse_teaser_header.jpg")
myimage13= myimage13.resize((200, 150), Image.ANTIALIAS)
myimg13 = ImageTk.PhotoImage(myimage13)
bgcanvas9.create_image(0, 0, image=myimg13, anchor = NW)

imgframe8 = Frame(bigframe,borderwidth = 1.5, relief=RAISED, width=300,height=190)
imgframe8.grid(row=8, column=1)
bgcanvas10 = Canvas(imgframe8,height=150,width=200)
bgcanvas10.grid(row=0,column=0)
Bl8 = Label(imgframe8,text="------------------Kicking Horse---------------------\n Kicking Horse is " + KickingHorseprox + "km from Toronto \n Kicking Horse features " + KickingHorselifts + "\nski lifts From peak to base,\n Kicking Horse has " + KickingHorsevert +"metres of vertical.\n Between the incredible variety in\n skiing and extrordinary snow and\n skiing conditions, Kicking Horse's reputation\n as one of the best ski resorts in Canada\n is well earned. From sweeping bowls to \n steep groomers, this resort has somthing\n for everyone. For more information about snowfall\n at Kicking Horse, visit the linked 'on the snow' webpage")
Bl8.grid(row=0,column=1)
Bl8.bind("<Button-1>", lambda e: callback("https://www.onthesnow.com/british-columbia/kicking-horse/skireport.html"))
myimage14 = Image.open("00-promo-image-revelstoke-british-columbia-canada.jpg")
myimage14= myimage14.resize((200, 150), Image.ANTIALIAS)
myimg14 = ImageTk.PhotoImage(myimage14)
bgcanvas10.create_image(0, 0, image=myimg14, anchor = NW)


bgcanvas1= Canvas(bigframe, height= 50, width=50)
myimage4 = Image.open("gold-medals-500x500.jpg")
myimage4 = myimage4.resize((50, 50), Image.ANTIALIAS)
myimg4 = ImageTk.PhotoImage(myimage4)
bgcanvas1.create_image(0, 0, image=myimg4, anchor = NW)
bgcanvas1.grid(row=1, column=0)

bgcanvas2= Canvas(bigframe,width=50, height= 60 )
myimage5 = Image.open("blank-silver-medal-12454422.jpg")
myimage5 = myimage5.resize((50, 60), Image.ANTIALIAS)
myimg5 = ImageTk.PhotoImage(myimage5)
bgcanvas2.create_image(0, 0, image=myimg5, anchor = NW)
bgcanvas2.grid(row=2, column=0)

bgcanvas3= Canvas(bigframe, width=60, height= 60 )
myimage6 = Image.open("blank-champion-bronze-medal-with-ribbon-vector-7591952.jpg")
myimage6 = myimage6.resize((60, 60), Image.ANTIALIAS)
myimg6 = ImageTk.PhotoImage(myimage6)
bgcanvas3.create_image(0, 0, image=myimg6, anchor = NW)
bgcanvas3.grid(row=3, column=0)




 



