import urllib.request
from PIL import Image

class main:
    def aspect_ratio(self, url):
        try:
            image = Image.open(urllib.request.urlopen(url))
            width, height = image.size
            aspect_ratio = self.rational_aspect_ratio(height / width)
            aspect_ratio_str = f"{aspect_ratio[0]}:{aspect_ratio[1]}"
            print(f"The aspect ratio is {aspect_ratio_str}")
        except:
            print("Unable to calculate the aspect ratio")
            raise

    def rational_aspect_ratio(self, aspect_ratio):
        precision = 1.0E-6
        x = aspect_ratio
        a = round(x)
        h1, k1, h, k = 1, 0, a, 1
        while x - a > precision * k * k:
            x = 1 / (x - a)
            a = round(x)
            h, k, h1, k1 = h1 + a * h, k1 + a * k, h, k
        return h, k

challenge = main()
challenge.aspect_ratio("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png")

