import streamlit as st
import pickle
import pandas as pd

from encoding_config import custom_encoding

st.set_page_config(page_title="Downtime Predictor", layout='wide')

# Inject custom CSS/JS
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open("static/script.js") as f:
    st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)
# Optional HTML components (banners, messages, etc.)
# with open("components/html_snippets.html") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

st.title("⚙️ Supplier Downtime Prediction")
st.write("Predict the expected **Total Downtime Minutes** from defect-related incidents.")

# Sidebar input controls
st.sidebar.header("📝 Input Parameters")
category = st.sidebar.selectbox(
    "Category*", [
        "Mechanicals", "Logistics", "Packaging", "Materials & Components", "Goods & Services", "Electrical"
    ]
)
defect_type = st.sidebar.radio(
    "Defect Type*", ["No Impact", "Impact", "Rejected"]
)
defect_category = st.sidebar.selectbox(
    "Defect Category*", [
        "foreign_material", "misc_support", "defects_bad", "crease_warped",
        "incorrect_color", "defective_packaging", "print_defects", "labels_incorrect"
    ]
)
region = st.sidebar.selectbox(
    "Region*", ["Northeast", "Midwest", "South", "West"]
)
material_type = st.sidebar.selectbox(
    "Grouped Material Type*", [
        "Raw Materials", "Corrugate", "Electrical Components", "Glass/Composites", "Film",
        "Labels", "Carton", "Hardware", "Packaging Related", "Other"
    ]
)
defect_qty = st.sidebar.number_input(
    "Total Defect Quantity*", min_value=0, max_value=1_000_000, value=1000, step=100,
    help="Type any value (no slider)."
)

# Load model/scaler
with open("final_model_xgb.pkl", "rb") as f:
    encoders_dict, scaler, model = pickle.load(f)

input_dict = {
    'Category': [category],
    'Defect_Type': [defect_type],
    'Defect_Category': [defect_category],
    'Region': [region],
    'Grouped_Material_Type': [material_type],
    'Total_Defect_Qty': [defect_qty]
}
input_original_df = pd.DataFrame(input_dict)  # This will keep original labels for display

# Make a copy for encoding and modeling
input_df = input_original_df.copy()

# Apply custom encoding
for col in custom_encoding:
    if col in input_df.columns:
        input_df[col] = input_df[col].map(custom_encoding[col])


# Create a copy for model input that will use the scaled value
input_for_model = input_df.copy()

input_for_model['Total_Defect_Qty'] = scaler.transform(input_for_model[['Total_Defect_Qty']])

# input_encoded = pd.get_dummies(input_for_model)
input_encoded = input_for_model.copy()
model_columns = model.feature_names_in_
missing_cols = set(model_columns) - set(input_encoded.columns)
for col in missing_cols:
    input_encoded[col] = 0
input_encoded = input_encoded[model_columns]

low_threshold = 1904   # 25th percentile
mid_threshold = 3627   # 50th percentile (median)

if st.button("🔍 Predict Downtime"):
    prediction = model.predict(input_encoded)[0]
    prediction = int(round(prediction))
    if prediction < low_threshold:
        pred_class, pred_msg = "low", "🎉 Low downtime risk. Great job!"
        st.markdown('<script>confetti();</script>', unsafe_allow_html=True)
    elif prediction < mid_threshold:
        pred_class, pred_msg = "mid", "⚠️ Moderate downtime risk."
    else:
        pred_class, pred_msg = "high", "🚨 High downtime risk. Please review supplier process."

    # st.markdown(f'<div class="prediction-result {pred_class}">{round(prediction)} minutes<br><span>{pred_msg}</span></div>', unsafe_allow_html=True)
    hrs = prediction // 60
    mins = prediction % 60
    duration = f"{hrs} hr {mins} min"
    st.markdown(f'<div class="prediction-result {pred_class}">{duration}<br><span>{pred_msg}</span></div>', unsafe_allow_html=True)

    st.subheader("🧾 Input Summary")
    st.table(input_original_df.T)

    data = input_original_df.copy()
    data["Predicted_Downtime_Minutes"] = prediction

    st.download_button(
        label="⬇️ Download Prediction & Inputs (CSV)",
        data=data.to_csv(index=False),
        file_name="downtime_prediction.csv",
        mime="text/csv"
    )

st.markdown(
    "<div class='footer'>🛠 Built with Streamlit | 📊 Model: XGBoost | 🎨 UI: HTML/CSS/JS</div>",
    unsafe_allow_html=True
)
