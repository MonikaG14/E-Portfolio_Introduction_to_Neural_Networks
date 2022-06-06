# E-Portfolio_Introduction_to_Neural_Networks

In this E-Portfolio I will introduce to you the basics of Neural Networks.

Presentation slides:
[Introduction to NN.pptx](https://github.com/MonikaG14/E-Portfolio_Introduction_to_Neural_Networks/files/8846386/Introduction.to.NN.pptx)

I am using:

- Python for coding
- Pycharm as an IDE
- Matplotlib to plot the error function while training the neural network
- NumPy for its great math functions
- TensorFlow and Keras for some more examples at the end of my demo

![grafik](https://user-images.githubusercontent.com/85937393/172236658-2788c635-7b2a-4498-9690-66bf7420db63.png)



## Neural Network
Neural networks, also known as artificial neural networks (ANN) or simulated neural networks (SNN), are a subset of machine learning and are at the heart of deep learning algorithms. Their name and structure are inspired by the human brain, mimicking the way biological neurons transmit signals to one another.

A neural network is a system that learns how to make predictions by following these steps:

 - Taking the input data
 - Making a prediction
 - Comparing the prediction to the desired output
 - Adjusting its internal state to correctly predict next time
    
![nn2](https://user-images.githubusercontent.com/85937393/172060537-c09a8b1d-9e1d-48e4-82d4-d43d35f6290c.png)


- Vectors: the data is stored in them
- Layers: transform the data from the previous layer. Each layer transforms the data from the previous layer by applying some mathematical operations

Simply put, the process of training the neural network consists of:

 - Starting with some random weights and bias vectors
 - Making a prediction
 - Adjusting the vectors to predict more accurately
 - Repeat until the difference between the prediction and the correct targets is minimal

## Parallels between biological and artificial neural networks

A biological neuron is composed of multiple dendrites, a nucleus, and an axon. When a stimulus is sent to the brain, it is received through the synapse located at the end of the dendrite.
When a stimulus arrives at the brain it is transmitted to the neuron via the synaptic receptors which adjust the strength of the signal sent to the nucleus. This message gets sent by the dendrites to the nucleus, where it is processed in combination with other signals coming from other receptors on the dendrites. Thus, the combination of all these signals takes place in the nucleus. After processing all these signals, the nucleus will emit an output signal through its single axon. The axon will then stream this signal to several other downstream neurons via its axon terminations. This way, a neuron analysis is pushed in the subsequent layers of neurons. 

On the other hand, artificial neural networks are built on the principle of biomimicry. External stimuli (the data), whose signal strength is adjusted by the neuronal weights (place where the mathematical calculation will happen) via the dendrites. The result of the calculation – called the output – is then re-transmitted (via the axon) to several other neurons and then subsequent layers are combined, and so on.

![NN](https://user-images.githubusercontent.com/85937393/172059553-f40b44c5-3467-424a-8e97-37c3d1a4cdd3.png)
