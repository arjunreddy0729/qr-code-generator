import argparse
import qrcode
import os

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True)

args = parser.parse_args()

if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

img = qrcode.make(args.url)
img.save("qr_codes/qrcode.png")

print("QR code generated for:", args.url)