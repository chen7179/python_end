from flask import Flask,render_template
from pyecharts.charts import Map
from pyecharts.charts import Bar, Page, Pie, Timeline
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__)



@app.route('/')
def timeline_map() -> Timeline:
    df = pd.read_csv("API_worldap2shijianzhou.csv")
    tl = Timeline()
    for i in range(2010, 2018):
        map0 = (
            Map()
                .add(
                "pm2.5浓度", list(zip(list(df.CountryName), list(df["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="2010-2017年世界空气污染程度".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=10,
                                                                                     font_style="italic")),

                visualmap_opts=opts.VisualMapOpts(series_index=0, max_=99.73437372),

            )
        )
        tl.add(map0, "{}".format(i))
        map0.render("./templates/world_airp.html")
        with open("./templates/world_airp.html", encoding="utf8", mode="r") as f:
            sym = "".join(f.readlines())
            return render_template('result.html',
                                   the_sym=sym,
                                   )

@app.route('/index2')
def geo_heatmap() -> Geo:
    df = pd.read_csv("chinafensheng.csv", encoding="ANSI")
    dfc = df.fillna(0)
    dfc
    d = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "二氧化硫排放量",
            [list(z) for z in zip(list(df.地区),list(df['2010']))],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1537818),
            title_opts=opts.TitleOpts(title="2010中国各省空气污染程度"),
        )
    )
    d.render("./templates/zhongaoduibi.html")
    with open("./templates/zhongaoduibi.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('result2.html',
                               the_sym=sym,
                               )

@app.route('/index3')
def geo_heatmap1() -> Geo:
    df = pd.read_csv("chinafensheng.csv", encoding="ANSI")
    dfc = df.fillna(0)
    dfc
    e = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "二氧化硫排放量",
            [list(z) for z in zip(list(df.地区),list(df['2017']))],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1537818),
            title_opts=opts.TitleOpts(title="2017中国各省空气污染程度"),
        )
    )
    e.render("./templates/zhongaoduibi.html")
    with open("./templates/zhongaoduibi.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('result3.html',
                               the_sym=sym,
                               )



@app.route('/index4')
def bar_base() -> Bar:
    df = pd.read_csv("API_worldap2shijianzhou.csv", index_col="CountryName")
    x轴 = [int(x) for x in df.columns.values[-8:]]
    中国 = list(df.loc['China'].values)[-8:]
    中国
    澳大利亚 = list(df.loc['Australia'].values)[-8:]
    澳大利亚
    za = (
        Bar()
        .add_xaxis(x轴)
        .add_yaxis("中", 中国)
        .add_yaxis("澳", 澳大利亚)
        .set_global_opts(title_opts=opts.TitleOpts(title="空气污染程度中澳对比", subtitle="pm2.5历年对比图"))
    )
    za.render("./templates/zhongaoduibi.html")
    with open("./templates/zhongaoduibi.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('result4.html',
                               the_sym=sym,
                               )

if __name__ == '__main__':
    app.run()

