from PIL import Image

def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return " "
    gary = (2126*r + 7152*g + 722*b)/10000
    ascii_char = list("$@B*oahkmZOJUzrjft]?-_+~<>i!I;:^`. ")    
    #定义示例ascii_char = list("$@B%&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!I;:^`. ")
    x = int( (gary / (alpha+1.0))*len(ascii_char) )
    return ascii_char[x]

def write_file(out_file_name, content):
    with open(out_file_name, "w") as f:
        f.write(content)

def main(file_name="图片文件地址路径", width=100, height=100, out_file_name="/home/watin/文档/2.txt"):
#定义示例def main(file_name="C:/Users/1/Desktop/1.jpg", width=80, height=80, out_file_name="C:/Users/1/Desktop/2.txt"):
    text = ""
    im = Image.open(file_name)
    im = im.resize((width,height), Image.NEAREST)
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j,i))
            text += get_char(*content)
        text += "\n"
    print(text)
    write_file(out_file_name, text)

if __name__ == '__main__':
    main(file_name="/home/watin/图片/sendpix0.jpg")
    #定义示例main(file_name="C:/Users/1/Desktop/1.jpg")

    

