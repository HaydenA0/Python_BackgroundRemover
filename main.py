import argparse
def lazy_imports():
    global remove, Image
    from rembg import remove
    from PIL import Image



def help () :
    print("In house background remover")


def remove_background(source_image_path, output_image_path) :
    print("Lazy imports...")
    lazy_imports()
    print("Removing...")
    input = Image.open(source_image_path) 
    output = remove(input) 
    output.save(output_image_path) 


def main () -> None :
    parser = argparse.ArgumentParser()
    parser.add_argument("source_image")
    parser.add_argument("-o", "--output", default="genericOutput.png")
    args = parser.parse_args()
    source_image_path = args.source_image 
    output_image_path = args.output 
    remove_background(source_image_path, output_image_path)
    print("Done.")

    
if __name__ == "__main__" :
    main()
