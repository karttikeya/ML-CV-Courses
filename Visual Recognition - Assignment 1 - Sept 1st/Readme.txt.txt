Name : Karttikeya MAngalam
Roll : 14311

I am the only ODD guy left in the course so, I have a single man team unfortunately. Kindly take that into account for grading :)

Format:

I have tuned both Resnet and VGG in the 1_1 part. The respective accuracies and observations are marked in the notebook under relevant blocks. 

For the custom Resnet I have acived ~93% accuracy. I have trained all my models on Titan X GPU. 

Observations:

One intereting thing, I observed is that the CIFAR-100 weights made a difference only in the first or second epochs. Gradually, as the weights converged to the custom data, the accuracied are similar with raw training even outperfoming the CIFAR weights in the end.

Secondly, I observed that resizing the images to 224,224 seemed an overkill for the images with actul sizes of 28,28 fo rfeedint into the Resnet18 or the VGG networks.

Another very interesting point is that, the training accuracy skyrokceted very fast to 90s and stayed there for many number of epochs while the validation/test accuracy was slowly picking up. So while the training accuracy went from 90 to 93, the validation accuracy almost tripled.

Th learning rate tuning for the Resnet was a bit frustrating. Because I could afford a 100 batch size on the 12GB GPU, even them I stuck to lower batch size due to lr tuning. But I guess, that's just deep learning. 

Thanks for the oppurtunity, It was a good learning experience! :) 
