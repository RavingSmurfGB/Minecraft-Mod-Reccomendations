import yaml


mod_dict = {
    'Deep Origins Overlays': {
        'Catagory' : ' Resource Pack', 
        'Description': 'Grass, Dirt, Stone, Bricks & more get a overlay on to nearby blocks',
        'Rating': '10/10 ~ Amazing',
        'Link': 'https://modrinth.com/resourcepack/deep-origins-overlays/versions', 
        'Image-link' : 'https://cdn.modrinth.com/data/tOCRtfAR/f6cc525b2c8182da0eda51f94edf2915e5dc02a8.png',
    },
    'Deep Origins Overlays 2 ': {
        'Catagory' : ' Resource Pack', 
        'Description': 'Grass, Dirt, Stone, Bricks & more get a overlay on to nearby blocks',
        'Rating': '10/10 ~ Amazing',
        'Link': 'https://modrinth.com/resourcepack/deep-origins-overlays/versions', 
        'Image-link' : 'https://cdn.modrinth.com/data/tOCRtfAR/f6cc525b2c8182da0eda51f94edf2915e5dc02a8.png',
    },
}



with open('mod-reccomendations.yaml', 'w') as outfile:
    yaml.dump(mod_dict, outfile, default_flow_style=False)