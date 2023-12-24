import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

def app():


    st.title("店铺销售分析")

    # 文件上传
    uploaded_file = st.file_uploader("上传 'Store sales.csv' 文件", type=["csv"])

    if uploaded_file is not None:
        # 读取数据
        data = pd.read_csv(uploaded_file, encoding='GBK')

        # 设置 Matplotlib 的配置
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # 绘图
        plt.figure(figsize=(8, 4))  # 画布大小
        ls = ['-','--',':','-.']  # 线条样式
        for i in range(4):
            plt.plot(data['日期'], data.iloc[:, i+1], linestyle=ls[i])
        plt.xticks(data['日期'])
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(4))  # 设置坐标轴间隔
        plt.title('四个店铺订单量趋势')  # 标题
        plt.legend()

        # 使用 Streamlit 显示 Matplotlib 图表
        st.pyplot(plt)
