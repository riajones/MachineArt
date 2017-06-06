import Image
import matplotlib.pyplot as plt
import random
import math
import os
import sys

def save(file):
    print ('Saving New Image')
    files = 0
    out_name = ''
    for c in range(4):
        out_name += str(file)[c]
    for f in os.listdir(r'.'):
        file_name = ''
        for c in range(4):
            file_name += str(f)[c]
        if file_name == out_name:
            files += 1
    if files == 0:
        im.save(out_name + '.png')
    else:
        im.save(out_name + '_' + str(files) + '.png')


def distance(x1, x2, y1, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def noise(pix, width, height):
    print ('Applying Noise')
    print ('Pixel Encoding: ', im.mode)

    for i in range(width - 1):
        for j in range(height - 1):
            coin = random.randint(0,100)
            if coin > 60:
                r = pix[i,j][0]
                g = pix[i,j][1]
                b = pix[i,j][2]
                a = 0
                if im.mode == 'RGBA':
                    a = pix[i,j][3]
                    coin = random.randint(0,10)
                    if coin < 5:
                        a += (random.randint(0, 255) % 255)
                    else:
                        a -= (random.randint(0, 255) % 255)
                coin = random.randint(0,10)
                if coin < 5:
                    r += (random.randint(0, random.randint(0,255)) % 255)
                else:
                    r -= (random.randint(0, 255) % 255)
                    
                coin = random.randint(0,10)
                if coin < 5:
                    g += (random.randint(0, 255) % 255)
                else:
                    g -= (random.randint(0, 255) % 255)
                    
                coin = random.randint(0,10)
                if coin < 5:
                    b += (random.randint(0, 255) % 255)
                else:
                    b -= (random.randint(0, 255) % 255)
                    
    
                if im.mode =='RGBA':
                    pix[i,j] = (r,g,b,a)
                else:
                    pix[i,j] = (r,g,b)
            
def random_color(mode):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	a = random.randint(0,255)
	if mode == 'RGBA':
		return (r,b,g,a)
	elif mode == 'RGB':
		return (r,g,b)

def dot(pix, x, y, radius, noise = False):
	
    if im.mode == 'RGBA':
        colour = random_color(im.mode)
    else:
        colour = random_color(im.mode)
    coin = random.randint(0,10)
    if coin > 5 or not noise:
        for i in range(x - radius, x + radius):
            for j in range(y - radius, y + radius):
                if i < width and i >= 0 and j < height and j >= 0:
                    if distance(i,x,j,y) < radius:
                        pix[i,j] = colour
    else:
        for i in range(x - radius, x + radius):
            for j in range(y - radius, y + radius):
                if i < width and i >= 0 and j < height and j >= 0:
                    if distance(i,x,j,y) < radius:
                        coin = random.randint(0,100)
                        if coin > 50:
                            pix[i,j] = colour


def make_dots(num_dots = 100):
    print('Creating Dots')
    dots = []
    for i in range(num_dots):
        tmp = (random.randint(0, width), random.randint(0, height))
        dots.append(tmp)
    for d in dots:
        die = random.randint(0,100)
        if die > 75:
            dot(pix, d[0], d[1], random.randint(3, 100), True)
        else:
            dot(pix, d[0], d[1], random.randint(3, 100))


def rect(pix, x, y, w, h, n = False):
    if x >= 0 and x + w < width and y >= 0 and y + h < height:
        colour = random_color(im.mode)
        for i in range(x, x + w):
            for j in range(y, y + h):
                if n:
                    die = random.randint(0,100)
                    if die > 70:
                        pix[i,j] = colour
                else: 
                    pix[i,j] = colour

def make_rects(number):
    print('Creating Rectangles')
    rects = []
    for i in range(number):
        x = random.randint(0,width)
        y = random.randint(0, height)
        tmp = (x, y, random.randint(0, width - x), random.randint(0, height - y))
        rects.append(tmp)
    for r in rects:
        die = random.randint(0,100)
        if die > 75:
            rect(pix, r[0], r[1], r[2], r[3], True)
        else:
            rect(pix, r[0], r[1], r[2], r[3])


def draw_line(pix, x1, y1, x2, y2, w):
    colour = random_color(im.mode)
    line = []
    line.append((x1,y1))

    x = x1
    y = y1
    dist = distance(x1,x2,y1,y2)
    count = 0
    if x <= x2 and y >= y2:
        while x <= x2 and y >= y2:
            count += 1
            if count > dist:
                break
            x += (x2 - x1) * 1.0 / dist
            y -= (y1 - y2) * 1.0 / dist
            line.append((x,y))
    elif x <= x2 and y <= y2:
        while x <= x2 and y <= y2:
            count += 1
            if count > dist:
                break
            x += (x2 - x1) * 1.0 / dist
            y += (y2 - y1) * 1.0 / dist
            line.append((x,y))
    elif x >= x2 and y <= y2:
        while x >= x2 and y <= y2:
            count += 1
            if count > dist:
                break
            x -= (x1 - x2) * 1.0 / dist
            y += (y2 - y1) * 1.0 / dist
            line.append((x,y))
    elif x >= x2 and y >= y2:
        while x >= x2 and y >= y2:
            count += 1
            if count > dist:
                break
            x -= (x1 - x2) * 1.0 / dist
            y -= (y1 - y2) * 1.0 / dist
            line.append((x,y))
    
    for x, y in line:
        for i in range(int(x) - w, int(x) + w):
            for j in range(int(y) - w, int(y)  + w):
                if i >= 0 and i < width and j >= 0 and j < height:
                    pix[i,j] = colour

def draw_lines(num_lines):
    print('Creating ' +str(num_lines) + ' lines')
    for i in range(num_lines):
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(0, width - 1)
        y2 = random.randint(0, height - 1)
        w = random.randint(0, 7)
        draw_line(pix, x1, y1, x2, y2, w)
    

def choose_features(number):
    while len(features) < number:
        coin = random.randint(0,10)
        if coin > 5:
            features.append(0)#Dots
        
        coin = random.randint(0,10)
        if coin > 3:
            features.append(1)#Lines
        
        coin = random.randint(0,10)
        if coin > 7:
            features.append(2)# Rects
        
        coin = random.randint(0,10)
        if coin > 8:
            features.append(3)# Noise

'''
Behaviors:
    Noise
        Varying levels of noise
        Toggle Color / Grey
    Dots
        Any number
        *Toggle Color / Grey
    Rectangles
        Any number
        *Toggle Color / Grey
    Lines
        *Any number
        *Toggle Color / Grey
    
'''


image_name = sys.argv[1]
print ('Image Name: ', image_name)
print ('Loading Image')
picture = Image.open(image_name)
width, height = picture.size

print ('Loading Pixels')
print ('Image Size: ', width, height)
im = Image.open(image_name)
pix = im.load()



print ('Modifying Image')

features = []
choose_features(random.randint(1,5))
#noise(pix, width, height)


random.shuffle(features)

for f in features:
    if f == 0:
        make_dots(random.randint(0, 15))
    elif f == 1:
        draw_lines(random.randint(0, 200))
    elif f == 2:
        make_rects(random.randint(0, 35))
    elif f == 3:
        noise(pix, width, height)



save(image_name);
print ('Complete')
