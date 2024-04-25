import json

def load_data(json_filepath):
    with open(json_filepath, 'r') as file:
        data = json.load(file)
    return data

def extract_captions(data, image_ids):
    # Dictionary to hold image_id and its list of captions
    captions_dict = {image_id: [] for image_id in image_ids}
    
    # Loop through each item in the data
    anns = data['annotations']
    for item in anns:
        if item['image_id'] in captions_dict:
            captions_dict[item['image_id']].append(item['caption'])
    
    return captions_dict

def save_captions(captions_dict, output_filepath):
    with open(output_filepath, 'w') as file:
        json.dump(captions_dict, file, indent=4)

def main():
    json_filepath = 'captions_val2017.json'
    output_filepath = 'extracted_captions.json'
    
    # Example image_ids to extract
    image_ids = [1503, 14473, 16502, 47112, 60449, 62025, 94336, 116206, 286994, 310072, 375430, 410612, 423229, 481404, 541634]
    
    # Load data from JSON
    data = load_data(json_filepath)
    
    # Extract captions for specified image IDs
    captions_dict = extract_captions(data, image_ids)
    
    # Save the extracted captions to a file
    save_captions(captions_dict, output_filepath)
    print(f"Captions extracted and saved to {output_filepath}")

if __name__ == "__main__":
    main()
