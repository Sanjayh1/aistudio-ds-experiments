## TensorBoard

> TensorBoard is a web-based tool provided by TensorFlow for visualizing and monitoring machine learning and deep learning experiments, track metrics, and visualize various aspects of model performance. 


This folder collects some experiments and scripts from the Machine Learning and Deep Learning folders that have been modified to use TensorBoard methods.

### How to use TensorBoard on Phoenix:
On the ``log_dir`` parameter place your TENSORBOARD_LOGIDIR variable using the ``os`` module as the following example:

``tf.keras.callbacks.TensorBoard(log_dir=os.environ["TENSORBOARD_LOGDIR"])``

To check the path inside this variable, run the following commands on your Jupyter Notebook:

``import os``

``os.environ``

You should be able to see your environment variables like this:

![](../images_readme/Tensorboard.png)

---

## Experiment details

### **scripts 1 to 4** 

Scripts that create random numbers to quickly test TensorBoard.

- **Required resources** 

    It can be run on the CPU.

- **Dataset details** 
    No dataset used.

---

### **[TB] Cancer classification with Keras** 

Sequential model for classifying breast cancer.

- **Required resources** 

    It can be run on the CPU, but we strongly recommend running it on a GPU to accelerate training.

- **Dataset details** 

    CSV file with 30 columns, 569 rows and no more than 144 KB.