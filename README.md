# colaboratory_utils

Some useful (or not so much) Python stuff for Google Colab notebooks. 
Most of this stuff is taken from [this repository](https://github.com/ricardodeazambuja/colab_utils).
These collection of utilities in mainly used in [this repository](https://github.com/albertofernandezvillan/computer-vision-and-deep-learning-course).


## How to install it:
Click on a code cell and paste:
```
!pip install git+git://github.com/albertofernandezvillan/colaboratory-utils.git
```
Then `alt+enter` or `shift+enter` to execute. 

## Examples

Check [colaboratory_utils.ipynb](https://github.com/albertofernandezvillan/colaboratory-utils/blob/main/colaboratory_utils.ipynb) in order to see how this stuff can be used.

```
import colaboratory_utils as colab_utils

# 1. Show multiple image figures:
# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 7))
plt.suptitle("Testing visualization", fontsize=14, fontweight='bold')

colab_utils.show_img_plt(img, title='sample', n_rows=2, n_cols=3, pos=1)
# .....

# Show the created image:
plt.show()

# 2. Download an execute a file
colab_utils.download_and_execute_file(fname, url, params= "", execute=True, show_content=True)

# 3. Take image from webcam:
img = colab_utils.webcam2numpy()

# 4. Take video from webcam:
vid = colab_utils.videoGrabber(showVideo=False)
image_np = np.array(vid(0))

# 5. Show image (simple):
colab_utils.imshow(img)
```



