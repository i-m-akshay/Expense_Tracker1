
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#st.set_option('deprecation.showPyplotGlobalUse', False)

try:
  excel_file_path = "data/expense.csv"

  def execution():
    dataframe = pd.read_csv(excel_file_path)
    if len(dataframe) != 0:
      max_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].max()]
      min_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].min()]
      st.subheader("You are spending the most here :cry:")
      st.dataframe(max_Amount.reset_index(drop=True))

      st.subheader("You are spending the least here :blush:")
      st.dataframe(min_Amount.reset_index(drop=True))

      st.subheader("You made the most number of transaction on :date:")
      st.dataframe(dataframe.groupby(by='Date').size().nlargest(1).index)

      st.subheader("You made the least number of transaction on :date:")
      st.dataframe(dataframe.groupby(by='Date').size().nsmallest(1).index)

      mode_Category = dataframe["Category"].mode()
      st.subheader("The categories for which you are spending the most :cry:")
      st.dataframe(mode_Category.reset_index(drop=True))
      st.subheader(
          "The categories for which you are spending the least :blush:")
      st.dataframe(
          dataframe[dataframe['Category'].value_counts().idxmin() ==
                    dataframe['Category']]["Category"].reset_index(drop=True))
      Description_data = ' '.join(list(dataframe['Description'].values))

      #function to generate and display word cloud
      def generate_wordcloud(text):
        wordcloud = WordCloud(width=400, height=400,
                              background_color=None).generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

      st.subheader("Description cloud :cloud:")
      generate_wordcloud(Description_data)

    else:
      st.header("Please add some expenses before analyzing it")

  execution()
except Exception as e:
  st.header("Please add some expenses before analyzing it")
  st.error(f"Error: {e}")
