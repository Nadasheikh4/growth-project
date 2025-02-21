import streamlit as st

def main():
    st.set_page_config(page_title="growth mindset project", page_icon="★")

    st.title("🧠Growth Mindset Project")

    

    st.header("🚀Welcome to the Growth Mindset Project!")
    st.write("This is a project that aims to help you develop a growth mindset. A growth mindset is the belief that you can develop your abilities through hard work, dedication, and perseverance. It is the belief that you can learn and grow from your mistakes and failures. This project will provide you with resources, tools, and strategies to help you develop a growth mindset.")

    # Quote section
    st.subheader("💡What is a growth mindset?")
    st.write("A growth mindset is the belief that you can develop your abilities through hard work, dedication, and perseverance. It is the belief that you can learn and grow from your mistakes and failures. People with a growth mindset are more likely to take on challenges, persevere in the face of obstacles, and achieve their goals. They are more likely to view failure as an opportunity to learn and grow, rather than as a reflection of their abilities.")

    st.header("🔧 What's your challenge today?")
    user_input = st.text_input("Enter your challenge here you are facing:")

    # Condition
    if user_input:
        st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal!")
    else:
        st.warning("Please enter your challenge to move forward")

    # Initialize reflection variable
    reflection = ""

    # Reflection
    st.header("💪🏻Reflection on your learning journey")
    reflection = st.text_area("Enter your reflection here:")
    if reflection:
        st.success("Thank you for sharing your reflection! Keep up the good work!")
    else:
        st.warning("Please enter your reflection to move forward.")

    # Achievements
    st.header("🏆Achievements")
    achievements = st.text_area("Enter your achievements here:")
    if achievements:
        st.success("Congratulations on your achievements! Keep up the good work!")
    else:
        st.warning("Please enter your achievements to move forward.")

    # Footer
    st.markdown("---")
    st.write("Keep believing in yourself and keep pushing forward towards your goal!")
    st.write("© 2021 Growth Mindset Project. All rights reserved.")
    st.write("***📛Made with ❤️ by [Nada Sheikh]***")

if __name__ == "__main__":
    main()
