# colaboratory_utils

Some useful (or not so much) Python stuff for Google Colab notebooks. 
Most of this stuff is taken from this repository: https://github.com/ricardodeazambuja/colab_utils

This stuff is mainly used in this repository: https://github.com/albertofernandezvillan/computer-vision-and-deep-learning-course

## How to install it:
Click on a code cell and paste:
```
!pip install git+git://github.com/albertofernandezvillan/colaboratory-utils.git
```
Then `alt+enter` or `shift+enter` to execute. 

## Examples

```
import colaboratory_utils as colab_utils
 
# Download an execute a file
colab_utils.download_and_execute_file(fname, url, params= "", execute=True, show_content=True)
 
# Take image from webcam:
img = colab_utils.webcam2numpy()

# Show image:
colab_utils.imshow(img)
 
# Take video from webcam:
vid = colab_utils.videoGrabber(showVideo=False)
image_np = np.array(vid(0))
```



