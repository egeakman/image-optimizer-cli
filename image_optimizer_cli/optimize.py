import os
from PIL import Image
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument(
    "-p", "--path", help="Path to source folder", required=False, default=os.getcwd()
)
parser.add_argument("-o", "--output", help="Path to output folder", required=False)
parser.add_argument(
    "-q",
    "--quality",
    help="Quality of optimized images",
    required=False,
    type=int,
    default=50,
)
parser.add_argument(
    "-n", "--number", help="Number of images to optimize", required=False, type=int
)

args = parser.parse_args()


def main():
    print("Starting image optimizer...")
    if not os.path.isdir(args.output):
        os.mkdir(args.output)

    if os.path.isfile(args.path):
        img = Image.open(args.path)
        img.save(args.output + "/" + os.path.basename(args.path), quality=args.quality)

    elif os.path.isdir(args.path):
        if not args.number:
            for image in os.listdir(args.path):
                if image.endswith((".jpg", ".jpeg", ".png")):
                    img = Image.open(f"{args.path}/{image}")
                    img.save(
                        f"{args.output}/{image}", optimize=True, quality=args.quality
                    )

        else:
            for image in os.listdir(args.path):
                if image.endswith((".jpg", ".jpeg", ".png")):
                    img = Image.open(f"{args.path}/{image}")
                    img.save(
                        f"{args.output}/{image}", optimize=True, quality=args.quality
                    )
                    args.number -= 1
                    if args.number == 0:
                        break
