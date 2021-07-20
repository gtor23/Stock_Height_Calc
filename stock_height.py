import tkinter as tk
from tkinter import font

def stock_determine(entry):
     
    offset = 0.05

    sizes = {"a": [0.625, '1.5"'], "b":[0.75,'1.5"'] ,"c": [1.0,'1.0"'], "d": [1.25,'1.0"'], "e": [1.5,'1.0"'],

             "f":[1.75,'1.0"'], "g":[2.0, "None"],"h":[2.5,"None"], "i": [3.0, "None"] ,"j":[3.5, "None"]} 


    offset_dist = offset + entry

    if offset_dist <= sizes["j"][0]:
        
        if offset_dist <= sizes["a"][0]:
            s = sizes["a"][0]
            p = sizes["a"][1]

        elif offset_dist <= sizes["b"][0]:
            s = sizes["b"][0]
            p = sizes["b"][1]

        elif offset_dist <= sizes["c"][0]:
            s = sizes["c"][0]
            p = sizes["c"][1]

        elif offset_dist <= sizes["d"][0]:
            s = sizes["d"][0]
            p = sizes["d"][1]

        elif offset_dist <= sizes["e"][0]:
            s = sizes["e"][0]
            p = sizes["e"][1]

        elif offset_dist <= sizes["f"][0]:
            s = sizes["f"][0]
            p = sizes["f"][1]

        elif offset_dist <= sizes["g"][0]:
            s = sizes["g"][0]
            p = sizes["g"][1]

        elif offset_dist <= sizes["h"][0]:
            s = sizes["h"][0]
            p = sizes["h"][1]

        elif offset_dist <= sizes["i"][0]:
            s = sizes["i"][0]
            p = sizes["i"][1]

        else:
            offset_dist <= sizes["j"][0]
            s = sizes["j"][0]
            p = sizes["j"][1]

        final_str = 'Standard Offset: %s"\nPart Height: %s" \nStock Height: %s" \nParallels: %s' % (offset, entry, s,p)
        label['text'] = final_str
       
    else:
        label['text'] = 'Part Height: %s" \nPart is too big!' % (entry)
      
    return



def chk_enter(entry):
    
    if not entry:
        pass

    else:
        try:
            entry = float(entry)
            stock_determine(entry)

        except:

            pls = "Invalid input. Input must \nnot conatin any letters or \nspecial characters."  
            label['text'] = pls

    return


#################GUI WINDOW###############

H = 450
W = 400

root = tk.Tk()
root.title("Stock Height Config")

canvas = tk.Canvas(root, bg="#154360", height = H, width = W)
canvas.pack(fill = "both", expand = True)

frame_top = tk.Frame(root, bg="#154360")
frame_top.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="center")

top_label = tk.Label(frame_top, bg="#154360",text= "Stock Height and Parallel Calculator",font=(None,16,'bold'),fg='#d7dbdd')
top_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg='#990000', bd=10)
frame.place(relx= 0.5,rely=0.25,relwidth = 0.8, relheight=0.13, anchor = "center")

entry = tk.Entry(frame, bg='#d7dbdd', font = (None, 16), relief = 'sunken')
entry.place(relwidth=0.5, relheight=1)


button = tk.Button(frame, text = "Get Stock Height", bg='#d7dbdd', font = (None,10,'bold'), relief = "raised", command=lambda:chk_enter(entry.get()))
button.place(relx=0.6,relwidth=0.4, relheight=1)

entry.bind("<Return>", lambda e: chk_enter(entry.get()))

frame2 = tk.Frame(root, bg='#990000',bd=10)
frame2.place(relx= 0.5, rely = 0.65, relwidth=0.9, relheight=0.5, anchor = "center")

label = tk.Label(frame2, anchor='nw',justify = 'left',bg='#d7dbdd', font=(None, 23))
label.place(relwidth=1,relheight=1)

root.mainloop()
