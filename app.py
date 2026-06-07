import streamlit as st
import random
import time

st.set_page_config(page_title="ICPC Challenge Practice Arena", page_icon="🏆", layout="wide")
st.title("🏆 ICPC 2025 Online Winter Challenge Practice Arena")
st.markdown("Ready yourself for the real competition by solving curated algorithmic challenges.")

st.markdown("""
This competition rewards high-performance code. Your final score is determined by both:
*   **Correctness**: Your solution must pass a series of hidden test cases[reference:7].
*   **Efficiency**: The problem's large constraints mean you must design an optimal algorithm.

Use the space below to practice common ICPC problem types. Your real work will be done in your own development environment.
""")

st.divider()

st.header("🎲 Practice: Problem Solving & Code Execution")
st.markdown("**Problem Statement**: Implement a function that given an array of integers, returns the length of the longest increasing subsequence (LIS).")

col1, col2 = st.columns([2, 1])
with col1:
    user_input = st.text_input("Enter an array of integers (comma-separated):", "10,9,2,5,3,7,101,18")
    input_list = [int(x.strip()) for x in user_input.split(",") if x.strip()]

def solve_lis(nums):
    from bisect import bisect_left
    sub = []
    for x in nums:
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)

if st.button("Run Code", type="primary"):
    if not input_list:
        st.error("Please enter a valid list of integers.")
    else:
        with st.spinner("Executing..."):
            time.sleep(1)  # Simulate computation
            result = solve_lis(input_list)
        st.success(f"**Result**: The length of the longest increasing subsequence is **{result}**.")
        st.markdown("---")
        st.markdown("""
        **How to check for efficiency:**
        *   The algorithm above runs in **O(n log n)** time, which is optimal for large arrays (n up to 10⁵ or more).
        *   An **O(n²)** solution would fail on hidden test cases with large input sizes.
        """)

st.divider()

st.header("💡 Tips for ICPC Success")
st.markdown("""
1.  **Master Your Tools**: Practice with your chosen language (C++, Java, Python) using an IDE that supports large input files. **Codeforces** is the best place for this kind of practice.
2.  **Optimization is Key**: The problem will likely involve large numbers (up to \(10^{18}\)), so use 64-bit integers and efficient data structures[reference:8].
3.  **Submit Early, Submit Often**: The 16-day window allows you to refine your approach. Your last non-zero score submission will be used for final testing[reference:9]. Use this to your advantage and keep improving.
4.  **Read the Official Rules**: Familiarize yourself with the contest guidelines[reference:10][reference:11]. For any questions, contact the organizers at [manager@icpc.global](mailto:manager@icpc.global)[reference:12].
5.  **Compete as an Individual**: This challenge is an individual contest[reference:13], so your focus and preparation will be your key to victory.
""")

st.divider()
st.caption("Powered by GlobalInternet.py. Built by Gesner Deslandes.")
