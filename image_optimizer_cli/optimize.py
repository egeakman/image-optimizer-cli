import os
import sys
from PIL import Image
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument(
    "-p",
    "--path",
    help="Path to the image or folder to optimize.",
    required=False,
    default=os.getcwd(),
)
parser.add_argument(
    "-q",
    "--quality",
    help="Quality of optimized images",
    required=False,
    type=int,
    default=80,
)
parser.add_argument(
    "-n", "--number", help="Number of images to optimize", required=False, type=int
)
parser.add_argument(
    "-r",
    "--recursive",
    help="Recursively optimize images",
    required=False,
    action="store_true",
)

args = parser.parse_args()

number = 0


def main():
    global number
    print("Starting image optimizer...")

    if args.number and args.number <= 0:
        sys.exit("Number parameter must be a positive integer.")

    if os.path.isfile(args.path):
        img = Image.open(args.path)
        img.save(f"{args.path}/{os.path.basename(args.path)}", quality=args.quality)

    elif os.path.isdir(args.path):
        if args.recursive:
            number = recursive_optimize(number)
        else:
            number = optimize_path(number)

    else:
        sys.exit("Invalid path")

    print(f"Image optimizer finished. Optimized {number} image/s.")


def optimize_path(number):
    for image in os.listdir(args.path):
        if image.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(f"{args.path}/{image}")
            img.save(f"{args.path}/{image}", optimize=True, quality=args.quality),
            number += 1
            if args.number:
                args.number -= 1
                if args.number == 0:
                    break
    return number


def recursive_optimize(number):
    for dirpath, _, files in os.walk(args.path):
        for filename in files:
            image = os.path.join(dirpath, filename)
            if image.endswith((".jpg", ".jpeg", ".png")):
                img = Image.open(image)
                img.save(image, optimize=True, quality=args.quality)
                number += 1
                if args.number:
                    args.number -= 1
                    if args.number == 0:
                        break
    return number
