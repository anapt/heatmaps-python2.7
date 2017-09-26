# Heatmaps in Python 2.7
**Python** script for generating **heatmaps** for any coordinate data using _jjguy/heatmap_ python module.

## Dependencies
If you want to create your own dataset from Mouse Movement data you need to install:
- pymouse
- time
- csv

If you just want to test the code you need to install:
- the _Heatmaps module_
- pandas
- Image

#### The generated heatmaps look like these
<img src="https://raw.githubusercontent.com/anapt/heatmaps-python2.7/master/outputs/blue-red/final_blue_red.png" width="250"  /><img src="https://raw.githubusercontent.com/anapt/heatmaps-python2.7/master/outputs/green-red/final_green-red.png" width="250"  />

## How to run the script

* **Before running the script, make sure you install the _HEATMAP MODULE_ following the instructions on http://jjguy.com/heatmap/**
  * You can also try `pip install heatmaps`


* **Then, make sure you have installed all the _Dependencies_**

* **Open the _calculator.py_ file and update the**
  1. screen_width
  2. screen_height

  **variables to those of your own system**

Once everything is setup correctly run
` $ python heatmaps_release.py` to try out the demo.

### Creating a dataset

If you want to create your own _dataset_ run `$ python .datafiles/create/csv_file_creator.py`. Your mouse movements will be logged on to a csv file in _datafiles_ folder.

### Genetating a heatmap from your custom dataset
In the **heatmaps_release.py** file in **init_list** _method_ change the **datafile** _variable_ to the **PATH** of your custom dataset. Then simply run the script.

### Adding a custom image
In the **heatmaps_release.py** file in the **merge_photos** _method_ change the **picture** _variable_ to the **PATH** of the image you want to use.

Open the _calculator.py_ file and update the
1. pic_width
2. pic_height

variables to those of your image.  

Then simply run the script.
