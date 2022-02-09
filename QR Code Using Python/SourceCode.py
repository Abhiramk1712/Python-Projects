import pyqrcode
import png
link = "https://www.instagram.com/abhiram_k__/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)
link1 = "https://www.linkedin.com/in/abhiram-kattunga-821426204/"
qr_code1 = pyqrcode.create(link1)
qr_code1.png("LinkedIn.png", scale=5)