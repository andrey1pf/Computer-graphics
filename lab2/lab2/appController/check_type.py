

def check_type(folder):
    if folder[:-4:-1] == 'pmB':
        return 'Bmp'
    elif folder[:-4:-1] == 'fiG':
        return 'Gif'
    elif folder[:-4:-1] == 'gpJ':
        return 'Jpg'
    elif folder[:-4:-1] == '2ba':
        return 'Lab2'
    elif folder[:-4:-1] == 'xcP':
        return 'Pcx'
    elif folder[:-4:-1] == 'gnP':
        return 'Png'
    elif folder[:-4:-1] == 'fiT':
        return 'Tif'
