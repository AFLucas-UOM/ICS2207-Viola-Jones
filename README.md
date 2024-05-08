# Viola-Jones Face Detection System

The Viola-Jones object detection framework, introduced in 2001 by Paul Viola and Michael Jones, represents a breakthrough in the field of Computer Vision (CV), particularly in the domain of real- time face detection.

## Overview

This Python script implements the Viola-Jones face detection algorithm using OpenCV for face, eye, and mouth detection. The program captures video from a webcam, processes each frame for face detection, and displays the live feed with bounding boxes around detected faces, eyes, and mouths.

## Requirements

- Python 3.x
- OpenCV (cv2)
- Tkinter (for GUI)
- macOS or Linux (for dynamic path handling)

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install OpenCV:
    ```bash
    pip install opencv-python
    ```
3. Install Tkinter (included in Python standard library).

## Usage
1. Clone or download the script to your local machine.
   ```bash
   git clone https://github.com/AFLucas-UOM/ICS2207-Viola-Jones
   ```
2. Run the script using Python:
    ```bash
    python Viola-Jones.py
    ```
3. Ensure that your webcam is connected and accessible.
4. The program will display the live webcam feed with face, eye, and mouth detection bounding boxes.
5. Press the 'q' key to exit the program.

## Features

- Utilizes the Viola-Jones algorithm for real-time face detection.
- Detects eyes and mouths within detected faces.
- Provides a simple GUI with an exit confirmation dialog.

## File Structure

- `Viola-Jones.py`: Main Python script implementing the Viola-Jones algorithm.
- `haarcascade_frontalface_default.xml`: Pre-trained Haar cascade XML file for face detection.
- `haarcascade_eye.xml`: Pre-trained Haar cascade XML file for eye detection.
- `haarcascade_mcs_mouth.xml`: Pre-trained Haar cascade XML file for mouth detection.
- `Icon.png`: Icon image used for the application window.

## Troubleshooting

- If the webcam is not accessible, ensure it is connected and not being used by other applications.
- Check for any warnings or errors displayed in the terminal while running the script.

## Contributions

Contributions to improve the functionality or add new features are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was developed as part of an academic assignment. Unit: `ICS2207` at the `University of Malta`.

## Contact

For any inquiries or feedback, please contact [Andrea Filiberto Lucas](mailto:andrealucasmalta@gmail.com).