def rgb_vers_hsl(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    maxi = max(r, g, b)
    mini = min(r, g, b)
    d = maxi - mini
    l = (maxi + mini) * 50
    if d == 0:
        h = 0
        s = 0
    else:
        s = (100 * d) / (1 - abs(2 * l / 100 -1))
        c = 0
        if g < b:
            c = 6
        if maxi == r:
            h = 60 * (((g - b) / d) % 6)
        elif maxi == g:
            h = 60 * (((b - r) / d) + 2)    
        elif maxi == b:
            h = 60 * (((r - g) / d) + 4)
    return h, s, l

def hsl_vers_rgb(h, s, l):
    h = h % 360
    s = s / 100
    l = l / 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 -1))
    m = l - c / 2
    if h >= 0 and h < 60:
        r = c
        g = x
        b = 0
    elif h < 120:
        r = x
        g = c
        b = 0
    elif h < 180:
        r = 0
        g = c
        b = x
    elif h < 240:
        r = 0
        g = x
        b = c
    elif h < 300:
        r = x
        g = 0
        b = c
    elif h < 360:
        r = c
        g = 0
        b = x
    h = (r + m) * 255
    s = (g + m) * 255
    l = (b + m) * 255
    return h, s, l




#traitement pixelisation
def bruit_30(img):
    if img.mode != "RGB":
        img = img.convert("RGB")
    import random
    for j in range(img.height):
        for i in range(img.width):
            r, g, b = img.getpixel((i, j))
            img.putpixel((i, j), ((r + random.randint(-30, 30)), (g + random.randint(-30, 30)), (b + random.randint(-30, 30)))) 

    return img

#traitement embossage
def filtreEmbossage(img): 
    img_bis = img.copy()
    liste = []
    # on prend couleur pixel et on stocke dans liste
    for j in range(img.height):
        for i in range(img.width):
            r, g, b = img.getpixel((i, j))
            liste.append((r, g, b))
    
    # on n'inclue par bords image dans modif
    for j in range(1,img.height-1):
        for i in range(1,img.width-1):
            #on prend pixel milieu + ceux autours pour modifier celui-ci avec coeffs et valeurs des autres
            pix_0 = img.getpixel((i,j))
            pix_1 = img.getpixel((i-1,j-1))
            pix_2 = img.getpixel((i,j-1))
            pix_3 = img.getpixel((i+1,j-1))
            pix_4 = img.getpixel((i-1,j))
            pix_5 = img.getpixel((i+1,j))
            pix_6 = img.getpixel((i-1,j+1))
            pix_7 = img.getpixel((i,j+1))
            pix_8 = img.getpixel((i+1,j+1))

            # calcul nouvelle valeur rgb avec coeffs + autres pixels
            r_bis = (-2)*pix_1[0] + (-1)*pix_2[0] + 0*pix_3[0] + (-1)*pix_4[0] + 0*pix_5[0] + 1*pix_6[0] + 0*pix_7[0] + 1*pix_7[0] + 2*pix_8[0]
            g_bis = (-2)*pix_1[1] + (-1)*pix_2[1] + 0*pix_3[1] + (-1)*pix_4[1] + 0*pix_5[1] + 1*pix_6[1] + 0*pix_7[1] +  1*pix_7[1] + 2*pix_8[1]
            b_bis = (-2)*pix_1[2] + (-1)*pix_2[2] + 0*pix_3[2] + (-1)*pix_4[2] + 0*pix_5[2] + 1*pix_6[2] + 0*pix_7[2] +  1*pix_7[2] + 2*pix_8[2]

            # replace pixel avec nouvelle couleur
            img_bis.putpixel((i, j), (r_bis, g_bis, b_bis))

    
    return img_bis

#traitement réhausseur de contraste     
def filtreContraste(img): 
    img_bis = img.copy()
    liste = []
    # on prend couleur pixel et on stocke dans liste
    for j in range(img.height):
        for i in range(img.width):
            r, g, b = img.getpixel((i, j))
            liste.append((r, g, b))
    
    # on n'inclue par bords image dans modif
    for j in range(1,img.height-1):
        for i in range(1,img.width-1):
            #on prend pixel milieu + ceux autours pour modifier celui-ci avec coeffs et valeurs des autres
            pix_0 = img.getpixel((i,j))
            pix_1 = img.getpixel((i-1,j-1))
            pix_2 = img.getpixel((i,j-1))
            pix_3 = img.getpixel((i+1,j-1))
            pix_4 = img.getpixel((i-1,j))
            pix_5 = img.getpixel((i+1,j))
            pix_6 = img.getpixel((i-1,j+1))
            pix_7 = img.getpixel((i,j+1))
            pix_8 = img.getpixel((i+1,j+1))

            # calcul nouvelle valeur rgb avec coeffs + autres pixels
            r_bis = (-1)*pix_1[0] + (-1)*pix_2[0] + (-1)*pix_3[0] + (-1)*pix_4[0] + 9*pix_5[0] + (-1)*pix_6[0] + (-1)*pix_7[0] + (-1)*pix_7[0] + (-1)*pix_8[0]
            g_bis = (-1)*pix_1[1] + (-1)*pix_2[1] + (-1)*pix_3[1] + (-1)*pix_4[1] + 9*pix_5[1] + (-1)*pix_6[1] + (-1)*pix_7[1] +  (-1)*pix_7[1] + (-1)*pix_8[1]
            b_bis = (-1)*pix_1[2] + (-1)*pix_2[2] + (-1)*pix_3[2] + (-1)*pix_4[2] + 9*pix_5[2] + (-1)*pix_6[2] + (-1)*pix_7[2] +  (-1)*pix_7[2] + (-1)*pix_8[2]

            # replace pixel avec nouvelle couleur
            img_bis.putpixel((i, j), (r_bis, g_bis, b_bis))

    
    return img_bis

#symétrie verticale
def sym_axe_vertical(img):
  img_bis = img.copy()
  for j in range(img.height):
    for i in range(img.width):
        r, g, b = img.getpixel((i, j))
        img_bis.putpixel((img_bis.width-i-1, j), (r, g, b))
    
  return img_bis

#Saturation verts
def variation_s_g(img):
  for j in range(img.height):
      for i in range(img.width):
          r, g, b = img.getpixel((i, j)) # on prend couleur pixel image origine
              # on converti le pixel en hsk av le traitement pour modif la saturation
          h, s, l = rgb_vers_hsl(r, g, b) 
              
              # si le pixel est vert alors on multiplie la saturation par un coeff
          if h >= 60 and h <= 180: 
              s *= 50
              
              # reconversion en rgb pour remettre les pixels en place
          r, g, b = hsl_vers_rgb(h, s, l) 
              # arrondi à l'unité car les nombres rgb sont des entiers et il y a eu des divisions lors conv 
          r, g, b = int(r), int(g), int(b) 
              
          img.putpixel((i, j), (r, g, b)) # remise en place pixels

  return img  