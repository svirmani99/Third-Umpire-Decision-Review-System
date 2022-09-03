import tkinter
import cv2
import PIL.Image, PIL.ImageTk


SET_WIDTH = 700
SET_HEIGHT = 400
window = tkinter.Tk()
window.title("Third Umpire Decision Review System")
cv_img = cv2.resize(cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB),(700,400))
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
window.mainloop()