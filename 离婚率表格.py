#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf


app = Flask(__name__)


# 准备工作 
list1 = ["全国分省年度离婚率","华北","东北","华东","中南","西南","西北"]
data2 = pd.read_csv('分省年度数据，粗离婚率，年升序，分地区.csv',engine='python') #
df = data2.set_index("index")  #把数字变为index
#华北"
df5 = df.iloc[["0","1","2","3","4"]]
#df = data.set_index("地区")
regions_available_loaded = list1

@app.route('/',methods=['GET'])
def lihunlv():
    data_str = df.to_html()
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)   

@app.route('/lihunlv',methods=['POST'])
def lihunlv_select() -> 'html':
    plot_all = "华北地区离婚率"
    data_str = df5.to_html()
    regions_available =  regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

if __name__ == '__main__':
    app.run(debug=True,ort = 8009)   # debug=True, 在py使用, 在ipynb不使用
    


# In[ ]:




