# File Name: gif_to_ascii.py
# Author: Zach Chaney
#
# Description: 
# Converts a gif or image file into an ascii representation. Call the script with the 
# name of the gif/image to convert, i.e.
#                   py gif_to_ascii.py <file_name>


from PIL import Image, ImageDraw, ImageFont
import argparse


def main():

    # Parses the input arguments. This script takes in a single positional argument, the name of the file to convert.
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "Specify the file name (e.g. 'gif_to_ascii.py nyan_cat.gif')")
    args = parser.parse_args()
    
    # Opens the given file and converts the gif to an array of image frames
    gif = Image.open(args.file)
    frames = gif_to_frames(gif)

    # Convert each frame to an ascii frame
    ascii_frames = []
    for im in frames:
        ascii_image = image_to_ascii(im)
        ascii_frames.append(ascii_image)
    
    # Save the ascii frames into either a gif or a single image
    if len(ascii_frames) > 1:
        ascii_frames[0].save("_ascii.".join(args.file.split(".")),save_all=True,append_images=ascii_frames[1:],loop=0, duration=gif.info['duration'])
    else:
        ascii_frames[0].save("_ascii.".join(args.file.split(".")))


# Converts a single image to an ascii image
def image_to_ascii(im):
    
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    orig_size = im.size
    
    # Convert Image to grayscale
    im = im.convert("L")
    
    # Scale image down to fit characters to pixels
    char_size = ImageFont.load_default().getsize(chr(32))
    spacing = 1 # Vertical spacing between the lines of text
    im = im.resize((int(im.size[0]/char_size[0]),int(im.size[1]/(char_size[1]+spacing))))
    
    # Convert pixels to characters and reassemble into image
    ascii_chars = "".join([ascii_chars[i//25] for i in im.getdata()])
    ascii_chars = "\n".join(ascii_chars[i:(i+im.size[0])] for i in range(0, len(ascii_chars), im.size[0]))
    
    ascii_image = Image.new("RGB",orig_size,(0,0,0))
    ImageDraw.Draw(ascii_image).text((0,0),ascii_chars,spacing=spacing)
    
    return ascii_image

# Converts a gif to an array of images
def gif_to_frames(gif):
    
    # Loops through each frame of the gif and extracts the image
    frames = []
    try:
        while True:
            new_frame = Image.new('RGBA',gif.size)
            new_frame.paste(gif,(0,0),gif.convert('RGBA'))
            frames.append(new_frame)
            gif.seek(gif.tell()+1)
    except EOFError:
        pass
    return frames

main()
