import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel数据
file_path = "test.xlsx"
sheet = pd.read_excel(file_path, sheet_name = "Sheet1") # sheet_name不指定时默认返回全表数据
col_name = sheet.columns

### 设置格式
# 设置坐标轴刻度向内
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.rcParams['font.sans-serif']=['Times New Roman']  # 设置全局字体，可选择需要的字体替换掉‘Times New Roman’
font1={'family': 'Times New Roman', 'weight': 'light', 'size': 12}  # 设置字体模板，
font2={'family': 'Times New Roman', 'weight': 'light', 'size': 16}  # 设置字体模板，

plt.title("Title",fontdict=font2)  # 标题

# # 设置坐标轴的取值范围
# plt.xlim((0.5, 6.5))
# plt.ylim((0, 36))

plt.title("Title")
plt.minorticks_on()   # 副刻度线
plt.xlabel('x - label',fontdict=font1)
plt.ylabel('y - label',fontdict=font1)

plt.ticklabel_format(axis='both',style='sci')  # 设置文章风格
plt.savefig("example.png",format="png",dpi=600)  # 自动保存图片
linestyle = ['r-+', 'g-o', 'b-*','y-^', 'c-v', 'm-x'] # 线条颜色及样式列表

for i in range(1,len(col_name)):
    plt.plot(sheet[col_name[0]], sheet[col_name[i]],linestyle[i%len(linestyle)],lw=1.5,label=col_name[i])#,marker = 'o')

plt.legend(loc="upper right",scatterpoints=1,prop=font1,shadow=False,frameon=True)  # 添加图例 loc控制图例位置，“best”为最佳位置，“bottom”,"top"，“topringt"等

plt.ticklabel_format(axis='both',style='sci')  # 设置文章风格
plt.savefig("example.png",format="png",dpi=600)  # 自动保存图片
plt.show()
