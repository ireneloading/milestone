import streamlit as st

st.set_page_config(page_title="Milestone", layout="centered")

st.title("Milestone")
st.write("Turn your goal into a clear weekly plan — no overthinking, just progress.")

# --- Input Form ---
with st.form("roadmap_form"):
    goal_title = st.text_input("🎯 What do you want to call this goal?")
    motivation = st.text_area("📝 Why is this goal important to you?")
    duration = st.selectbox("⏳ How many weeks do you want to work on this?", [2, 4, 6])
    goal_type = st.radio("📌 What type of goal is this?", [
        "Build a Portfolio Website",
        "Learn a New Skill",
        "Launch a Side Project"
    ])

    submitted = st.form_submit_button("Generate My Plan")

# --- Plan Output ---
if submitted:
    st.success("🚀 Your Milestones are ready!")

    st.markdown(f"### 🎯 Goal: *{goal_title or goal_type}*")

    if motivation:
        st.markdown(f"📝 *\"{motivation.strip()}\"*")

    st.markdown(f"⏳ **Plan Duration: {duration} weeks**")
    st.markdown("---")

    # Predefined weekly plans
    plans = {
        "Build a Portfolio Website": {
            2: [
                ["Week 1", "- Choose platform\n- Sketch layout\n- Gather assets"],
                ["Week 2", "- Build basic sections\n- Test & launch\n- Share with a friend"]
            ],
            4: [
                ["Week 1", "- Pick platform\n- Sketch sections\n- Collect assets"],
                ["Week 2", "- Build homepage\n- Add social links\n- Style layout"],
                ["Week 3", "- Add a project page\n- Contact form\n- Test navigation"],
                ["Week 4", "- Polish\n- Publish\n- Ask for feedback"]
            ],
            6: [
                ["Week 1", "- Explore portfolio inspirations\n- Choose your stack\n- Draft layout"],
                ["Week 2", "- Set up platform\n- Build homepage\n- About section"],
                ["Week 3", "- Add projects\n- Write project blurbs\n- Collect feedback"],
                ["Week 4", "- Improve design\n- Add animations\n- Mobile check"],
                ["Week 5", "- Write blog/about\n- Add contact/socials\n- Test everything"],
                ["Week 6", "- Publish\n- Share it online\n- Reflect & next steps"]
            ]
        },
        "Learn a New Skill": {
            2: [
                ["Week 1", "- Pick topic\n- Do intro lesson\n- Set up tools"],
                ["Week 2", "- Do 2–3 lessons\n- Try a mini project\n- Reflect on progress"]
            ],
            4: [
                ["Week 1", "- Choose topic & course\n- Do intro module\n- Take notes"],
                ["Week 2", "- Finish 2 modules\n- Do small exercises"],
                ["Week 3", "- Apply skills\n- Do real-world task\n- Revisit tough parts"],
                ["Week 4", "- Wrap up course\n- Final project\n- Share or journal"]
            ],
            6: [
                ["Week 1", "- Pick topic & tools\n- Set realistic outcome"],
                ["Week 2", "- Finish basics\n- Quiz or test your understanding"],
                ["Week 3", "- Do mini project\n- Collect feedback"],
                ["Week 4", "- Practice edge cases\n- Join a forum or group"],
                ["Week 5", "- Do second mini project\n- Compare & reflect"],
                ["Week 6", "- Recap\n- Polish project\n- Plan next steps"]
            ]
        },
        "Launch a Side Project": {
            2: [
                ["Week 1", "- Pick idea\n- Write 1-line pitch\n- Design basic flow"],
                ["Week 2", "- Build MVP\n- Share with one person\n- Reflect & tweak"]
            ],
            4: [
                ["Week 1", "- Brainstorm & select idea\n- Sketch MVP"],
                ["Week 2", "- Start building\n- Fix blockers\n- Ask 1 person for feedback"],
                ["Week 3", "- Polish features\n- Create logo/homepage"],
                ["Week 4", "- Launch & share\n- Journal feedback\n- Celebrate!"]
            ],
            6: [
                ["Week 1", "- Explore ideas\n- Pick one & define scope"],
                ["Week 2", "- Map features\n- Create user flow\n- Start MVP"],
                ["Week 3", "- Build core function\n- Validate early"],
                ["Week 4", "- Improve UI\n- Fix bugs\n- Add onboarding"],
                ["Week 5", "- Create assets\n- Write launch post"],
                ["Week 6", "- Launch\n- Share on socials\n- Gather responses"]
            ]
        }
    }

    # Dynamically load selected plan
    selected_plan = plans[goal_type][duration]

    for week_title, tasks in selected_plan:
        st.markdown(f"#### {week_title}")
        st.markdown(tasks)
