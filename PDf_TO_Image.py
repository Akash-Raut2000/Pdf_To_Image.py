from pdf2image import convert_from_path

old_pdf = convert_from_path(" PDF File Name OR PATH",Poppler_path = "Popppler file path")

for i in range(len(old_pdf)):
    old_pdf[i].save("New"+str(i)+".jpg","JPEG")