
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sketchify | Photo Art Studio",
    page_icon="🎨",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #202c40);
    color: white;
}
h1, h2, h3 {
    color: #ffffff;
}
.subtitle {
    color: #b8c5d9;
    font-size: 17px;
}
div.stButton > button {
    background: #8b5cf6;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 22px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- IMAGE PROCESSING ----------------

def pencil_sketch(image, strength):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    inverted = 255 - gray
    blur = cv2.GaussianBlur(
        inverted, (21, 21), 0
    )

    inverted_blur = 255 - blur

    sketch = cv2.divide(
        gray, inverted_blur, scale=256
    )

    # Adjust intensity
    strength = strength / 100
    result = cv2.addWeighted(
        gray, 1 - strength,
        sketch, strength, 0
    )

    return cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)


def cartoon_filter(image, strength):
    # Smooth image using bilateral filtering
    smooth = image.copy()

    # Strength controls smoothing
    iterations = max(1, int(strength / 20))

    for _ in range(iterations):
        smooth = cv2.bilateralFilter(
            smooth, 9, 100, 100
        )

    # Create edge mask
    gray = cv2.cvtColor(
        image, cv2.COLOR_RGB2GRAY
    )

    gray = cv2.medianBlur(gray, 7)

    edge = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # Combine smooth colors and edges
    edge_rgb = cv2.cvtColor(
        edge, cv2.COLOR_GRAY2RGB
    )

    cartoon = cv2.bitwise_and(
        smooth, edge_rgb
    )

    return cartoon


def stylization_filter(image, strength):
    # OpenCV edge-preserving artistic stylization.
    # This is algorithmic CV, NOT a trained AI model.
    sigma_s = int(10 + strength * 1.5)
    sigma_r = min(0.99, 0.1 + strength / 120)

    result = cv2.stylization(
        image,
        sigma_s=sigma_s,
        sigma_r=sigma_r
    )

    return result


# ---------------- HEADER ----------------

st.title("🎨 SKETCHIFY")
st.markdown(
    '<p class="subtitle">Transform your ordinary photos '
    'into beautiful pencil sketches and cartoon artwork.</p>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("⚙️ Studio Settings")

effect = st.sidebar.selectbox(
    "Choose Transformation",
    [
        "Pencil Sketch",
        "Cartoon Effect",
        "Artistic Stylization",
        "Compare All Effects"
    ]
)

strength = st.sidebar.slider(
    "Stylization Strength",
    min_value=10,
    max_value=100,
    value=70,
    step=5
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Upload a photo, choose an effect, "
    "adjust the strength and download your artwork."
)

# ---------------- IMAGE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📸 Upload your photograph",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    # Resize large images for faster processing
    h, w = image_np.shape[:2]
    if max(h, w) > 1400:
        scale = 1400 / max(h, w)
        image_np = cv2.resize(
            image_np,
            (int(w * scale), int(h * scale))
        )

    st.subheader("Your Photo")

    if effect == "Compare All Effects":

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image_np,
                caption="Original Image",
                use_container_width=True
            )

            sketch = pencil_sketch(
                image_np, strength
            )

            st.image(
                sketch,
                caption="Pencil Sketch",
                use_container_width=True
            )

        with col2:
            cartoon = cartoon_filter(
                image_np, strength
            )

            st.image(
                cartoon,
                caption="Cartoon Effect",
                use_container_width=True
            )

            artistic = stylization_filter(
                image_np, strength
            )

            st.image(
                artistic,
                caption="Artistic Stylization",
                use_container_width=True
            )

        results = [
            ("Pencil Sketch", sketch),
            ("Cartoon Effect", cartoon),
            ("Artistic Stylization", artistic)
        ]

        st.subheader("Download Your Artwork")

        download_cols = st.columns(3)

        for col, (name, result) in zip(
            download_cols, results
        ):
            with col:
                buffer = BytesIO()
                Image.fromarray(result).save(
                    buffer, format="PNG"
                )

                st.download_button(
                    f"⬇️ Download {name}",
                    data=buffer.getvalue(),
                    file_name=name.lower().replace(
                        " ", "_"
                    ) + ".png",
                    mime="image/png"
                )

    else:

        if effect == "Pencil Sketch":
            processed = pencil_sketch(
                image_np, strength
            )

        elif effect == "Cartoon Effect":
            processed = cartoon_filter(
                image_np, strength
            )

        else:
            processed = stylization_filter(
                image_np, strength
            )

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image_np,
                caption="Original Photo",
                use_container_width=True
            )

        with col2:
            st.image(
                processed,
                caption=effect,
                use_container_width=True
            )

        st.success("Your artwork is ready!")

        buffer = BytesIO()
        Image.fromarray(processed).save(
            buffer, format="PNG"
        )

        st.download_button(
            label="⬇️ Download Your Artwork",
            data=buffer.getvalue(),
            file_name="sketchify_artwork.png",
            mime="image/png"
        )

else:
    st.info(
        "👆 Upload an image to start creating your artwork."
    )

# ---------------- ABOUT SECTION ----------------

st.divider()

st.subheader("🔬 How Sketchify Works")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ✏️ Pencil Sketch")
    st.write(
        "Uses grayscale conversion, Gaussian blur, "
        "inversion and image division to create "
        "a pencil drawing effect."
    )

with c2:
    st.markdown("### 🎭 Cartoon Filter")
    st.write(
        "Uses bilateral filtering to smooth colors "
        "and adaptive thresholding to identify edges."
    )

with c3:
    st.markdown("### 🎨 Artistic Style")
    st.write(
        "Uses OpenCV's edge-preserving stylization "
        "to produce an artistic appearance."
    )

st.divider()

st.subheader("⚖️ Classic Computer Vision vs AI Models")

st.write("""
**Classic Computer Vision:** Uses predefined mathematical
operations and image-processing algorithms. It is fast,
lightweight and does not require model training.

**Deep Learning Models:** Use trained neural networks to
learn artistic styles from data. They can produce more
complex transformations but generally require more
computational resources and pretrained model weights.
""")

st.caption(
    "Sketchify currently implements classical OpenCV "
    "algorithms. Artistic Stylization is not a deep learning model."
)

st.markdown(
    "<center>Made with ❤️ using Python, OpenCV and Streamlit</center>",
    unsafe_allow_html=True
)
