''' page 384 - Python: The Complete Reference, Martin C. Brown - 2001
    just changed Tkinter - to - tkinter and added new scale(s) - work
    in progress'''


from tkinter import *

def main():
    main = Tk()
        
    global feetscale, metrescale, mphscale, kphscale, lbscale, kgscale
    lbscale = IntVar()
    kgscale = IntVar()
    mphscale = IntVar()
    kphscale = IntVar()
    feetscale = IntVar()
    metrescale = IntVar()
    
# =========================================================================================    
    lbframe = Frame(main)
    Scale(lbframe, command = update_lb, variable = lbscale,
          width = 20, length = 400, orient = 'vertical', from_ = 0, to = 1000,
          resolution = 1, tickinterval = 10,
          label = 'Lbs').pack(side = 'top')
    
    Label(lbframe,textvariable = lbscale).pack(side = 'bottom', pady = 5)
    lbframe.pack(side = 'left')
# =========================================================================================    
    mphframe = Frame(main)
    Scale(mphframe, command = update_mph, variable = mphscale,
          width = 20, length = 400, orient = 'vertical', from_ = 0, to = 200,
          resolution = 1, tickinterval = 10,
          label = 'Mph').pack(side = 'top')
    
    Label(mphframe,textvariable = mphscale).pack(side = 'bottom', pady = 5)
    mphframe.pack(side = 'left')
# =========================================================================================  
    kphframe = Frame(main)
    Scale(kphframe, command = update_kph, variable = kphscale,
          width = 20, length = 400, orient = 'vertical', from_ = 0, to = 328,
          resolution = 1, tickinterval = 20,
          label = 'Kph').pack(side = 'top')
           
    Label(kphframe,textvariable = kphscale).pack(side = 'bottom', pady = 5)
    kphframe.pack(side = 'left')    
# =========================================================================================     
    feetframe = Frame(main)
    Scale(feetframe, command = update_feet, variable = feetscale,
          width = 20, length = 400, orient = 'vertical', from_ = 0, to = 328,
          resolution = 1, tickinterval = 20,
          label = 'Feet').pack(side = 'top')
        
    Label(feetframe,textvariable = feetscale).pack(side = 'top', pady = 5)
    feetframe.pack(side = 'left')      
# =========================================================================================
    metreframe = Frame(main)
    Scale(metreframe,command = update_metre, variable = metrescale,
          width = 20, length = 400,
          orient = 'vertical', from_ = 0, to = 100,
          resolution = 1, tickinterval = 5,
          label = 'Metres').pack(side = 'top')
    
    Label(metreframe,textvariable = metrescale).pack(side = 'top', pady = 5)
    metreframe.pack(side = 'left') 
# =========================================================================================
 
    main.mainloop()

def update_lb(self):
    global lbscale, kgscale
    kgscale.set(int(lbscale.get()*2.5))
    

def update_feet(self):
    global metrescale, feetscale
    metrescale.set(int(feetscale.get()/3.280839895))
    
    
def update_metre(self):
    global metrescale, feetscale
    feetscale.set(int(metrescale.get()*3.280839895))
    
def update_mph(self):
    global mphscale, kphscale
    kphscale.set(int(mphscale.get()*1.609344))
    
def update_kph(self):
    global mphscale, kphscale
    mphscale.set(int(kphscale.get()/1.609344))
   
   
#The conversion from Celsius to Fahrenheit is:
#
#C = (F - 32)*(5/9)
#
#and the conversion from Fahrenheit to Celsius is:
#
#F = C*(9/5) + 32
     
                     
    
main()



                   
 
 
