# Move and Control the Cursor with Eye Movements

In this project, our goal was to create a system that allows users to control a computer mouse cursor using only their eye movements — offering a hands-free, intuitive interface with significant accessibility potential.

The core idea was to collect visual data from the eyes at the moment of a mouse click. Each time the user clicked, we captured both an image of their eyes (using a standard webcam) and the corresponding screen coordinates of the mouse pointer. This dataset formed the foundation for training a deep learning model to predict gaze-based cursor positions. By correlating eye images with screen coordinates, we aimed to develop a model that could generalize across time and different users, enabling real-time gaze estimation. Once trained, the model would allow the system to predict where the user looks on the screen and move the cursor accordingly, effectively enabling mouse control through gaze alone.

Although this was a prototype built during a limited timeframe, the project demonstrated promising results and provided a proof of concept for gaze-based interaction.
