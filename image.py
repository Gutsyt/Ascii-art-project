
FILE_PATH = "bose.bmp"
WIDTH_OUT = 100

ASCII_CHARS = "$@%#*+=-:. "

def map_char(val):
    idx = int((val / 255) * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[idx]


def contrast_stretch(val, min_v, max_v):
    return int((val - min_v) * 255 / (max_v - min_v))


def gamma_correct(val, gamma=0.8):
    return int(255 * ((val / 255) ** gamma))


def main():
    with open(FILE_PATH, "rb") as f:
        f.seek(18)
        w_in = int.from_bytes(f.read(4), "little")
        h_in = int.from_bytes(f.read(4), "little")

        f.seek(10)
        offset = int.from_bytes(f.read(4), "little")
        f.seek(offset)

        padding = (4 - (w_in * 3) % 4) % 4
        pixels = []

        for _ in range(h_in):
            row = []
            for _ in range(w_in):
                b = int.from_bytes(f.read(1), "little")
                g = int.from_bytes(f.read(1), "little")
                r = int.from_bytes(f.read(1), "little")
                gray = int(0.299*r + 0.587*g + 0.114*b)
                row.append(gray)
            f.read(padding)
            pixels.append(row)

    pixels = pixels[::-1]  

    flat = [p for row in pixels for p in row]
    min_v, max_v = min(flat), max(flat)

    for y in range(h_in):
        for x in range(w_in):
            v = pixels[y][x]
            v = contrast_stretch(v, min_v, max_v)
            v = gamma_correct(v, 0.8)
            pixels[y][x] = v

    h_out = int(WIDTH_OUT * (h_in / w_in) * 0.55)

    for y in range(h_out):
        line = ""
        for x in range(WIDTH_OUT):
            src_x = int(x * w_in / WIDTH_OUT)
            src_y = int(y * h_in / h_out)
            line += map_char(pixels[src_y][src_x])
        print(line)

    with open("subhash_bose_ascii.txt", "w") as f:
        for y in range(h_out):
            line = ""
            for x in range(WIDTH_OUT):
                src_x = int(x * w_in / WIDTH_OUT)
                src_y = int(y * h_in / h_out)
                line += map_char(pixels[src_y][src_x])
            f.write(line + "\n")

if __name__ == "__main__":
    main()

