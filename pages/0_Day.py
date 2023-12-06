# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

# import library

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

import streamlit as st
from streamlit.hello.utils import show_code


def days_df() -> None:

    days_df = pd.read_csv("https://raw.githubusercontent.com/HandivaPutri/submission/main/day.csv")
days_df.head() # untuk menampilkan 5 baris pertama

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    # st.button("Re-run")


st.set_page_config(page_title="Day", page_icon="📹")
st.markdown("# Day")
st.markdown("## Data Wrangling")
st.markdown("### Gathering Data")

st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)
st.sidebar.header("Day")

days_df()

show_code(days_df)
