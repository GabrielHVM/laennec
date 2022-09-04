# $PH^2$ Dataset

**Select The Language:**
- [English](README.md)
- [Portuguese](README-pt.md)

$PH²$ is a dermoscopic image database acquired at the Dermatology Service of Hospital Pedro Hispano, Matosinhos, Portugal.

## Succinct Description
This image database contains a total of 200 dermoscopic images of melanocytic lesions, including 80 common nevi, 80 atypical nevi, and 40 melanomas. The PH² database includes medical annotation of all the images namely medical segmentation of the lesion, clinical and histological diagnosis and the assessment of several dermoscopic criteria (colors; pigment network; dots/globules; streaks; regression areas; blue-whitish veil).

## Dataset Contents
File organization
- ```PH2 Dataset images/```

    Insider this folder there is a dedicated folder for every image of the database, which contains the original dermoscopic image, the binary mask of the segmented lesion as well as the binary mask of the color classes presented in the skin lesion.
- ```PH2_dataset.txt```

    This file contains the classification of all imagens in a ".txt" file according to the dermoscopic criteria that evaluated in the $PH^2$ database.
- ```PH2_dataset.xlsx```

    This file contains the classification of all images in a ".xlsx" file according to the dermoscopic criteria that evaluated in the $PH^2$ database.


## Reference
1. Teresa Mendonça, Pedro M. Ferreira, Jorge Marques, Andre R. S. Marcal, Jorge Rozeira. PH² - A dermoscopic image database for research and benchmarking, 35th International Conference of the IEEE Engineering in Medicine and Biology Society, July 3-7, 2013, Osaka, Japan. 