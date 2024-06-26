import streamlit as st
import pickle
import numpy as np
from itertools import islice
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plot

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: contents recommendation")
st.write("The second part is to find the book a specific customer will take interest in. We turn all the useful words in the book abstracts they read before with high ratings into vectors and integrate vectors into a profile vector for each reader, using glove. Then we do the matching step, finding the closest distance between book vectors and profile vectors. If we type user ID on the website, the system will recommend several books he would like to read according to his reading history.")
st.write("Moreover, we add multi-objective optimization to our recommendation system. We not only provide books with high similarity with user profiles, but also ensure the recommendation quality by choosing books with a high average history rating.")

#----------Reader Profile----------book profiles read before with high ratings aggregated
with open('/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/book_dic.pickle', 'rb') as f:
    book_dic = pickle.load(f)
with open('/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/profiles.pickle', 'rb') as f2:
    user_profile = pickle.load(f2)
# print(book_dic)
# print(user_profile)

# matching step
user = st.text_input('User_id: example 8842281e1d1347389f2ab93d60773d4d, 72fb0d0087d28c832f15776b0d936598, ab2923b738ea3082f5f3efcbbfacb218')
num = st.slider("How many books do you want?", 1, 20, 10)
st.write()
st.write("Here are the", num, "books recommended to you according to your reading history:")
st.markdown("<p style='font-family: Arial; font-size: 18px; color: orange;'>Here is the recommended list for you!</p>", unsafe_allow_html=True)

if user == '':
    st.write("Empty Search")
else:
    v = []
    profile_vector = user_profile[user]
    v.append(profile_vector)
    dic = {}
    for each in book_dic.values():
        if float(each[2]) >= 3.5:
            dic[each[0]] = [np.linalg.norm(profile_vector - each[1]), each[1], each[2]] # rating is larger than 3.5

    new = dict(sorted(dic.items(), key=lambda item: item[1][0])) # high similarity, multi-objective optimization
    first_num_items = dict(islice(new.items(), num))
    for key, value in first_num_items.items():
        st.write(key,": ",value[2])
        v.append(value[1])

    # Visualization
    from sklearn.decomposition import PCA
    vectors = np.array(v)
    # Perform PCA for dimensionality reduction to 2D or 3D
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(vectors)
    # Set the size of the plot
    plt.figure(figsize=(4, 3))  # Set width=8 inches and height=6 inches
    # Create a 3D scatter plot using Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot all points except the first one (colored in blue)
    ax.scatter(pca_result[1:, 0], pca_result[1:, 1], pca_result[1:, 2], color='blue', label='Recommended Books')

    # Plot the first point (colored in red)
    ax.scatter(pca_result[0, 0], pca_result[0, 1], pca_result[0, 2], color='red', label='Personal Profile')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    ax.set_title('PCA Result 3D Scatter Plot for Books')
    # Add legend to the plot
    ax.legend()
    # Display the plot using Streamlit
    st.pyplot(fig)

st.sidebar.text("Web Creator: Jialin Wang")
st.sidebar.image("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/mcj038257400001.jpeg", use_column_width=True)
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.form("my_form"):
   slider_val = st.slider("How much would you rate our website?", 1,10,8)
   feedback = st.text_input('Your suggestions')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
if submitted:
       st.write("You rate", slider_val)
       print(slider_val, feedback)