import json
import os

PATH = "./SSLAD-2D/SSLAD-2d/train_annotations"
def converter(data, PATH):
    
    for idx, file in enumerate(data['images']):
    idx = idx+1
    
    #Darwin format
    info = {"dataset": "SODA10M"}
    info["annotations"] = []
    
    info["image"] = {
        "width": int(file['width']),
        "height": int(file['height']),
        "original_filename": file['file_name'],
        "filename": file['file_name'],
        "url": '',
        "thumbnail_url": '',
        "path": '/',
        "workview_url": '',
    }
    for seq,i in enumerate(data["annotations"]):
        if i["image_id"] == idx:
            info["annotations"].append(
                {"bounding_box": {"x": int(i['bbox'][0]), 
                                      "y": int(i['bbox'][1]), 
                                      "w": int(i['bbox'][2]), 
                                      "h": int(i['bbox'][3])},
                                      "name":data['categories'][i['category_id']-1]['name']

                    }
            )

    json_object = json.dumps(info, indent=4)
  
    # Writing to sample.json
    with open(f"{PATH}/{file['file_name'].split('.')[0]}.json", "w") as outfile:
        outfile.write(json_object)