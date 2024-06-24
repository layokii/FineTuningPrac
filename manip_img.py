from PIL import Image 
import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import json
import numpy as np

def json_handler(file_name):
    """
    json_handler

    file_name: name of the json file that needs to have labels extracted from
    function's purpose: open json file -> find relevant dictionary inside the larger dictionary -> return the dictionary containing the color_to_object_type dictionary
    return value: dictionary with colors(BGR codes) mapped to their respective object ids and types
    """
    opened_file = open(file_name) 

    #retrieve JSON object as dictionary
    data_dict = json.load(opened_file)

    objects_dict = {}

    #iterate through json list
    for categ in data_dict:
        if categ == "scene":
            objects_dict = data_dict[categ]
            break
    
    opened_file.close()
    return objects_dict



def instance_to_semantic(objects_dict):
    """
    instance_to_semantic

    objects_dict: dictionary that has dictionaries inside for each object with the bgr code as the key and the object ID and object types as the values
    function's purpose: group the masks in the instance segmentation dataset so that it can be used for semantic segmentation
    format of objects_dict: {"(__, __, __)": {"objectID": "___", "objectType": "___"}}
    return value: a dictionary with the object type as the key and the
    """
    
    classes_dict = {}
    for bgr_code in objects_dict: 
        objType = bgr_code["objectType"]
        if objType in classes_dict:
            classes_dict[].append(objects_dict[insObj])

            



def sep_image(file_name, folder_name):
    """
    sep_image

    file_name: name of the five view image file that is to be separated
    folder_name: name of the folder that the image file that is to be separated is a part of; needed to access image inside of directory
    function's purpose: define transformation -> access image -> open image and convert to rgb -> separate file with five views into separate views and store in list
    """
    width_height_one_view = 300 #width and height the same as each view is a square
    views = 5

    #weights are ImageNet statistics(mean and std dev vals for ImageNet) - change later to dataset specific mean and std dev later
    transform = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(), transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])])

    five_view_img_path = folder_name + "/" + file_name
    five_view_img = Image.open(five_view_img_path).convert('RGB')

    views_collec = []
    for view in range(views):
        #left and right as in coords
        left = i * width_height_one_view
        right = (i+1) * width_height_one_view
        #crop function params: left - x coord where view starts, top - y coord where view starts at top, right - x coord where view ends, bottom - y coord where view ends at the bottom
        indvl_view = five_view_img.crop((left, 0, right, width_height_one_view)) #top is always 0 as the five views are arranged horizontally
        indvl_view_tensor = transform(view)
        views[i] = indvl_view_tensor

#calculating mean and standard deviation for custom dataset

def calc_mean_and_std_dev_from_dataset():
    img_to_tensor = transforms.Compose([transforms.ToTensor()])
    dataset = datasets.ImageFolder(root = 'path_to_dataset', transform = img_to_tensor) #type in path to dataset later
    loader = DataLoader(dataset, batch_size = 64, shuffle = False, num_workers = 4) #4 is a common starting point for num_workers(determines number of subprocesses used for data loading); can be adjusted after experimentation
    mean = torch.zeros(3) #tensor to accumulate mean pixel vals for each channel, initialized to zeros
    std = torch.zeros(3) #tensor to accumulate standard deviation pixel vals for each channel, initialized to zeros
    sample_num= 0 #counter for number of samples processed

    for data, _ in loader: #_ is for ignoring the labels
        data = data.view(data.size(0), data.size(1), -1) #flattens height and width dims of images -> shape of (batch_size, channels, height * width)
        mean += data.mean(2).sum(0) #calculates mean of flattened dims for each channel and sums it up across all batches
        std += data.std(2).sum(0) #calculates standard deviation of the flattened dims for each channel and sums it up across all batches
        sample_num += data.size(0) #increment sample count by batch size

    mean /= sample_num #divide accumulated mean by total number of samples -> avg mean
    std /= sample_num #divide accumulated standard deviation by total number of samples -> avg standard deviation
    #TODO: FINISH THIS FUNCTION - NEEDS TO BE COMPLETED