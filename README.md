# FineTuningPrac
## Dataset
* 5 images per image file
* Each 1500 x 300 image file has 5 300 x 300 images grouped together
* Each trial folder contains **_augmented_traj_data.json(stores label information for each image) &  depth_images_panoramic, high_res_images_panoramic, instance_masks_panoramic folders_**
* Each trial folder holds the same images but with different operations done:
 ![image](https://github.com/layokii/FineTuningPrac/assets/147033274/ede87d18-3583-42c2-a864-7a840092d930)
  * depth_images_panoramic: depth estimation
  * high_res_images_panoramic: original images
  * instance_masks_panoramic: instance segmentation

* look_at_obj_in_light-BaseballBat-None-DeskLamp-303
  * _to be used as validation set_
  * 2 trial folders
    - trial_T20190907_060429_471715 - _45 png images in each folder_
    - trial_T20190907_060446_184846 - _39 png images in each folder_
      
* pick_and_place_simple-ToiletPaper-None-ToiletPaperHanger-417
  * _to be used as testing set_
  * 3 trial folders
    - trial_T20190908_043859_833063 - _22 png images in each folder_
    - trial_T20190908_043909_541721 - _20 png images in each folder_
    - trial_T20190908_185320_708158 - _40 png images in each folder_
        
* pick_heat_then_place_in_recept-BreadSliced-None-SideTable-3
  * _to be used as training set_
  * 3 trial folders
    - trial_T20190908_043859_833063 - _81 png images in each folder_
    - trial_T20190908_043909_541721 - _65 png images in each folder_
    - trial_T20190908_185320_708158 - _72 png images in each folder_
   
In the json files, "color_to_object_type" labels are specified using a dictionary. The keys are in BGR format while the values include the object id and class. 

**_Convert the BGR values to RGB before using_**

_The dataset doesn't include images in which semantic segmentation was performed, but adapt to this characteristic by treating the instance masks as one whole mask if the instances are of the same class_
