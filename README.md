# 🎨 Sketchify – Photo to Sketch & Cartoon Converter

Sketchify is a Python-based image processing application that transforms ordinary photographs into creative pencil sketches, cartoon-style images, and artistic effects. It uses OpenCV and computer vision techniques to provide multiple image transformation options through a simple and interactive web interface.

## ✨ Features

- **Pencil Sketch Effect:** Converts photos into realistic pencil drawings.
- **Cartoon Effect:** Transforms photographs into cartoon-style images.
- **Artistic Effect:** Applies artistic filters to create painting-like images.
- **Adjustable Intensity:** Customize the strength of image effects.
- **Compare Effects:** View different transformations of the same image.
- **Image Upload:** Upload your own JPG, JPEG, or PNG photographs.
- **Download Images:** Save transformed images in PNG format.
- **Interactive Interface:** Simple and user-friendly Streamlit interface.

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Streamlit
- Pillow

## ⚙️ Image Processing Techniques

Sketchify uses traditional computer vision techniques:

1. **Grayscale Conversion:** Converts the original image into grayscale.
2. **Image Inversion:** Inverts grayscale pixel values.
3. **Gaussian Blur:** Smooths the inverted image.
4. **Dodge Blending:** Combines grayscale and blurred images to generate the pencil sketch.
5. **Bilateral Filtering:** Reduces image noise while preserving edges for cartoon effects.
6. **Adaptive Thresholding:** Highlights edges and creates a cartoon-like appearance.
7. **Artistic Stylization:** Applies OpenCV artistic image filtering.

## 📂 Project Structure

```text
Sketchify/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/heatwaves0406/Sketchify.git
```

### 2. Navigate to the Project Folder

```bash
cd Sketchify
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 📸 How to Use

1. Open the Sketchify application.
2. Upload an image from your device.
3. Select your preferred transformation effect.
4. Adjust the intensity using the available slider.
5. Preview and compare the results.
6. Download your transformed image.

## 🎯 Project Objective

The objective of Sketchify is to demonstrate how computer vision and digital image processing can be used to transform everyday photographs into creative artistic outputs through an easy-to-use web application.

## 🔮 Future Enhancements

- AI-powered style transfer.
- More artistic filters and sketch styles.
- Real-time camera-based image transformation.
- Batch image processing.
- Mobile-friendly interface.

## 👩‍💻 Developed By

**Vaishnavi Malwade**

B.Tech – Computer Science and Engineering

GitHub: https://github.com/vaishnavimalwade

---

⭐ If you like this project, consider giving it a star on GitHub!

**Note:** This project currently uses traditional OpenCV-based computer vision algorithms rather than a trained deep learning model.
